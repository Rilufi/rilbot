import os
from typing import Dict, List
import requests
from atproto import Client
from datetime import datetime
import fortune


# Configurações do Bluesky
BSKY_HANDLE = os.environ.get("BSKY_HANDLE")  # Handle do Bluesky
BSKY_PASSWORD = os.environ.get("BSKY_PASSWORD")  # Senha do Bluesky
PDS_URL = "https://bsky.social"  # URL do Bluesky
BOT_NAME = "Johnata"  # Nome do bot para evitar interagir com os próprios posts

# Limites diários e ações permitidas por hora
DAILY_LIMIT = 11666
HOURLY_LIMIT = DAILY_LIMIT // 24

def bsky_login_session(pds_url: str, handle: str, password: str) -> Client:
    """Logs in to Bluesky and returns the client instance."""
    print("Tentando autenticar no Bluesky...")
    client = Client(base_url=pds_url)
    client.login(handle, password)
    print("Autenticação bem-sucedida.")
    return client

def search_posts_by_hashtags(session: Client, hashtags: List[str]) -> Dict:
    """Searches for posts containing the given hashtags."""
    hashtag_query = " OR ".join(hashtags)
    url = "https://public.api.bsky.app/xrpc/app.bsky.feed.searchPosts"
    headers = {"Authorization": f"Bearer {session._access_jwt}"}  # Usando _access_jwt obtido do client
    params = {"q": hashtag_query, "limit": 5}  # Ajuste o limite conforme necessário

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

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

if __name__ == "__main__":
    # Login to Bluesky
    client = bsky_login_session(PDS_URL, BSKY_HANDLE, BSKY_PASSWORD)

    # Define the hashtags to search for (without #)
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
        search_results = search_posts_by_hashtags(client, [hashtag])
        
        # Print detailed information about the search results
        print(f"Resultados da pesquisa para {hashtag}:")
        if not search_results.get('posts'):
            print("Nenhum resultado encontrado.")
        else:
            for post in search_results["posts"]:
                uri = post.get('uri')
                cid = post.get('cid')
                author = post.get('author', {})
                author_name = author.get('displayName', 'Unknown')
                author_did = author.get('did', '')

                # Evitar interagir com posts do próprio bot
                if author_name == BOT_NAME:
                    continue

                # Curtir, repostar e seguir o autor do post
                if action_counter < actions_per_hour:
                    like_post(client, uri, cid)
                    action_counter += 1
                if action_counter < actions_per_hour:
                    repost_post(client, uri, cid)
                    action_counter += 1
                if action_counter < actions_per_hour:
                    follow_user(client, author_did)
                    action_counter += 1

                # Verifica se o limite de ações foi atingido
                if action_counter >= actions_per_hour:
                    print("Limite de ações por hora atingido.")
                    break

            # Verifica se o limite de ações foi atingido
            if action_counter >= actions_per_hour:
                break

    # For fortunes
    if len(fortune_text) <= 300:
        fortune_text = os.popen("fortune alts/fortunes").read()
        post = client.send_post(fortune_text)
    else:
        print("Non rolaste la fortuna.")
        pass
    print("Concluído.")
