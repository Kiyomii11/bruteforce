import requests
import json

def get_profile_info(access_token):
    url = f"https://graph.facebook.com/v13.0/me?fields=id,name,picture&access_token={access_token}"
    response = requests.get(url)
    return response.json()

def main():
    access_token = input("Entrez votre token d'accès Facebook : ")
    try:
        profile_info = get_profile_info(access_token)
        print(json.dumps(profile_info, indent=4))
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    main()
