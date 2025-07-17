import requests
import random
import string

def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = "gmail.com"
    email = f"{username}@{domain}"
    print(f"📧 Ton email temporaire : {email}")
    print("Tu peux consulter ta boîte ici :")
    print(f"https://www.gmail.com/?login={username}&domain={domain}")

if __name__ == "__main__":
    generate_email()
