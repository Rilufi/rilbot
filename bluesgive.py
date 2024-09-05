from atproto import Client

BSKY_HANDLE = "seu_handle"  # Coloque seu handle aqui
BSKY_PASSWORD = "sua_senha"  # Coloque sua senha aqui
PDS_URL = "https://bsky.social"

client = Client(base_url=PDS_URL)
try:
    client.login(BSKY_HANDLE, BSKY_PASSWORD)
    print("Login bem-sucedido.")
except Exception as e:
    print(f"Erro ao autenticar: {e}")
