import os
from atproto import Client

# Configurações do Bluesky
BSKY_HANDLE = os.getenv("BSKY_HANDLE")
BSKY_PASSWORD = os.getenv("BSKY_PASSWORD")
PDS_URL = "https://bsky.social"

def bsky_login_session(pds_url: str, handle: str, password: str) -> Client:
    """Logs in to Bluesky and returns the Client instance."""
    print("Tentando autenticar no Bluesky...")
    client = Client(pds_url)
    try:
        client.login(handle, password)
        print("Autenticação bem-sucedida.")
        return client
    except Exception as e:
        print(f"Erro ao autenticar: {e}")
        raise

if __name__ == "__main__":
    client = bsky_login_session(PDS_URL, BSKY_HANDLE, BSKY_PASSWORD)
