import os
from dotenv import load_dotenv
import requests

load_dotenv()

# Credenciales de Cloudflare
CLOUDFLARE_EMAIL = os.environ.get('CLOUDFLARE_EMAIL')
CLOUDFLARE_GLOBAL_API_KEY = os.environ.get('CLOUDFLARE_GLOBAL_API_KEY')
CLOUDFLARE_ACCOUNT_ID = os.environ.get('CLOUDFLARE_ACCOUNT_ID')

# Endpoint de la API de Cloudflare para consultar túneles
CLOUDFLARE_TUNNELS_ENDPOINT = f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/tunnels"

def get_tunnels_status():
    # Headers para la solicitud a la API
    headers = {
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'X-Auth-Key': CLOUDFLARE_GLOBAL_API_KEY,
        'Content-Type': 'application/json',
    }

    # Realizar la solicitud GET a la API
    response = requests.get(CLOUDFLARE_TUNNELS_ENDPOINT, headers=headers)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch tunnels - {response.status_code}")
        print(response.text)
        return None

# Obtener e imprimir el estado de los túneles
tunnels_status = get_tunnels_status()
if tunnels_status:
    print("Tunnels:")
    for tunnel in tunnels_status['result']:
        print(f"- {tunnel['name']} | ID: {tunnel['id']} | Status: {tunnel['status']}")
else:
    print("No se pudieron recuperar los estados de los túneles.")
