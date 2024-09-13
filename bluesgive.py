from typing import Dict, List
import requests
from atproto import Client
import os
import subprocess
import time
import json
from datetime import datetime, timedelta, timezone

# Configurações do Bluesky
PDS_URL = "https://bsky.social"  # URL do Bluesky

# Limites diários e ações permitidas por hora
DAILY_LIMIT = 11666
HOURLY_LIMIT = DAILY_LIMIT // 24

def bsky_login_session(pds_url: str, handle: str, password: str) -> Client:
    """Logs in to Bluesky and returns the client instance."""
    print(f"Tentando autenticar no Bluesky para {handle}...")
    client = Client(base_url=pds_url)
    client.login(handle, password)
    print(f"Autenticação bem-sucedida para {handle}.")
    return client

def search_posts_by_hashtags(session: Client, hashtags: List[str]) -> Dict:
    """Searches for posts containing the given hashtags and returns them sorted by latest."""
    hashtag_query = " OR ".join(hashtags)
    url = "https://public.api.bsky.app/xrpc/app.bsky.feed.searchPosts"
    headers = {"Authorization": f"Bearer {session._access_jwt}"}
    params = {"q": hashtag_query, "limit": 100}

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    all_posts = response.json().get('posts', [])

    # Retorna todos os posts, ordenados por 'latest'
    return {"posts": all_posts}

def like_post(client: Client, uri: str, cid: str):
    """Likes a post given its URI and CID."""
    client.like(uri=uri, cid=cid)
    print(f"Post curtido: {uri}")

def repost_post(client: Client, uri: str, cid: str):
    """Reposts a post given its URI and CID."""
    client.repost(uri=uri, cid=cid)
    print(f"Post repostado: {uri}")

def follow_user(client: Client, did: str):
    """Follows a user given their DID."""
    client.follow(did)
    print(f"Seguindo usuário: {did}")

def load_interactions(account_name: str) -> Dict:
    """Loads interactions from a JSON file specific to the account."""
    interactions_file = f'alts/{account_name}_interactions.json'
    if os.path.exists(interactions_file):
        with open(interactions_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print(f"O arquivo {interactions_file} está vazio ou corrompido. Inicializando com valores padrão.")
                return {"likes": [], "reposts": [], "follows": []}
    return {"likes": [], "reposts": [], "follows": []}

def save_interactions(account_name: str, interactions: Dict):
    """Saves interactions to a JSON file specific to the account."""
    interactions_file = f'alts/{account_name}_interactions.json'
    with open(interactions_file, 'w') as file:
        json.dump(interactions, file)

def perform_actions_for_account(handle: str, password: str, account_name: str):
    """Performs like, repost, and follow actions for a given account."""
    if not handle or not password:
        print(f"Credenciais faltando para a conta: {{'handle': '{handle}', 'password': '***'}}")
        return

    # Carregar interações passadas para evitar duplicatas
    interactions = load_interactions(account_name)

    # Login to Bluesky
    try:
        client = bsky_login_session(PDS_URL, handle, password)
    except Exception as e:
        print(f"Erro ao autenticar {handle}: {e}")
        return

    # Define the hashtags to search for
    giveaway_hashtags = [
        "#giveaway",
        "#sorteio",
        "#contest",
        "#raffle",
        "#freebie"
    ]

    # Define the number of actions to perform per hour
    actions_per_hour = HOURLY_LIMIT
    action_counter = 0

    # Search for posts
    for hashtag in giveaway_hashtags:
        try:
            search_results = search_posts_by_hashtags(client, [hashtag])
        except Exception as e:
            print(f"Erro ao buscar posts para {hashtag}: {e}")
            continue
        
        print(f"Resultados da pesquisa para {hashtag}:")
        if not search_results.get('posts'):
            print("Nenhum resultado encontrado.")
        else:
            for post in search_results["posts"]:
                uri = post.get('uri')
                cid = post.get('cid')
                author_did = post.get('author', {}).get('did', '')

                # Curtir, repostar e seguir o autor do post
                if action_counter < actions_per_hour:
                    try:
                        like_post(client, uri, cid)
                        interactions["likes"].append(uri)
                        action_counter += 1
                    except Exception as e:
                        print(f"Erro ao curtir o post: {e}")
                        if "RateLimitExceeded" in str(e):
                            print("Limite de taxa atingido ao curtir, aguardando antes de continuar...")
                            time.sleep(60)  # Espera por 60 segundos antes de tentar novamente
                        continue

                if action_counter < actions_per_hour:
                    try:
                        repost_post(client, uri, cid)
                        interactions["reposts"].append(uri)
                        action_counter += 1
                    except Exception as e:
                        print(f"Erro ao repostar: {e}")
                        if "RateLimitExceeded" in str(e):
                            print("Limite de taxa atingido ao repostar, aguardando antes de continuar...")
                            time.sleep(60)  # Espera por 60 segundos antes de tentar novamente
                        continue

                if action_counter < actions_per_hour:
                    try:
                        follow_user(client, author_did)
                        interactions["follows"].append(author_did)
                        action_counter += 1
                    except Exception as e:
                        print(f"Erro ao seguir: {e}")
                        if "RateLimitExceeded" in str(e):
                            print("Limite de taxa atingido ao seguir, aguardando antes de continuar...")
                            time.sleep(60)  # Espera por 60 segundos antes de tentar novamente
                        continue

                # Verifica se o limite de ações foi atingido
                if action_counter >= actions_per_hour:
                    print("Limite de ações por hora atingido.")
                    break

            if action_counter >= actions_per_hour:
                break

    # Post a fortune message
    try:
        fortune_text = subprocess.run(["fortune", "alts/fortunes"], capture_output=True, text=True).stdout.strip()
        if len(fortune_text) <= 300:
            client.send_post(fortune_text)
            print(f"Fortune postada: {fortune_text}")
        else:
            print("Fortune muito longa, não postada.")
    except Exception as e:
        print(f"Erro ao postar fortune: {e}")

    # Salva as interações para a próxima execução
    save_interactions(account_name, interactions)

    print(f"Concluído para a conta: {handle}")

if __name__ == "__main__":
    # Cria a pasta alts se não existir
    if not os.path.exists('alts'):
        os.makedirs('alts')

    # Lista de contas para execução
    accounts = [
        {"acc": "Rilufi" ,"handle": os.environ.get("BSKY_HANDLE"), "password": os.environ.get("BSKY_PASSWORD")},
        {"acc": "Luffzar" ,"handle": os.environ.get("BSKY_HANDLE_LUFF"), "password": os.environ.get("BSKY_PASSWORD_LUFF")},
        {"acc": "Rilufix" ,"handle": os.environ.get("BSKY_HANDLE_RIL"), "password": os.environ.get("BSKY_PASSWORD_RIL")},
        {"acc": "Jameson" ,"handle": os.environ.get("BSKY_HANDLE_JAM"), "password": os.environ.get("BSKY_PASSWORD_JAM")},
        {"acc": "Xame" ,"handle": os.environ.get("BSKY_HANDLE_XAM"), "password": os.environ.get("BSKY_PASSWORD_XAM")},
        {"acc": "Zark" ,"handle": os.environ.get("BSKY_HANDLE_ZARK"), "password": os.environ.get("BSKY_PASSWORD_ZARK")},
        {"acc": "Uva" ,"handle": os.environ.get("BSKY_HANDLE_UVA"), "password": os.environ.get("BSKY_PASSWORD_UVA")},
        {"acc": "Lufi" ,"handle": os.environ.get("BSKY_HANDLE_LUFI"), "password": os.environ.get("BSKY_PASSWORD_LUFI")},
        {"acc": "Woba" ,"handle": os.environ.get("BSKY_HANDLE_WOBA"), "password": os.environ.get("BSKY_PASSWORD_WOBA")},
        {"acc": "Majin" ,"handle": os.environ.get("BSKY_HANDLE_MAJ"), "password": os.environ.get("BSKY_PASSWORD_MAJ")},
        {"acc": "Zelda" ,"handle": os.environ.get("BSKY_HANDLE_ZELD"), "password": os.environ.get("BSKY_PASSWORD_ZELD")},
        {"acc": "Mevu" ,"handle": os.environ.get("BSKY_HANDLE_MEV"), "password": os.environ.get("BSKY_PASSWORD_MEV")},
        {"acc": "Ifulir" ,"handle": os.environ.get("BSKY_HANDLE_IFU"), "password": os.environ.get("BSKY_PASSWORD_IFU")}
    ]

    # Executar para cada conta
    for account in accounts:
        if account["handle"] and account["password"]:
            print(f"Começando para a conta {account['acc']} \n-------------------------\n")
            perform_actions_for_account(account["handle"], account["password"], account["acc"])
        else:
            print(f"Credenciais faltando para a conta: {account}")
