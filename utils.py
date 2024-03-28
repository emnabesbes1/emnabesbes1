import requests
from requests.auth import HTTPBasicAuth

def test_nessus_connection():
    access_key = 'ab73bd41c94fad3a6d8beb6dc27008dc5ee4c1664504a92d02ec977251734f28'
    secret_key = '5706ffbedfc18e1c110947a7f31a9be8455e00591973189810c89d54ab29f148'
    url = 'https://maryem-virtual-machine:8834'
    # Endpoint de test, vous pouvez le remplacer par n'importe quel endpoint de l'API Nessus que vous souhaitez tester
    test_endpoint = '/server/status'
    headers = {
        'Content-Type': 'application/json',
        'X-ApiKeys': f'accessKey={access_key}; secretKey={secret_key}'
    }
    try:
        response = requests.get(url + test_endpoint, headers=headers, verify=False)
        response.raise_for_status()  # Vérifie si la réponse a un code de statut 2xx, sinon lance une exception
        print("Connexion à l'API Nessus réussie !")
        print("Réponse de l'API Nessus :", response.json())
    except requests.exceptions.RequestException as e:
        print("Une erreur s'est produite lors de la connexion à l'API Nessus :", e)

# Appel de la fonction de test
test_nessus_connection()
