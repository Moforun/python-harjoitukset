import requests

def hae_vitsi():
    vastaus = requests.get("https://api.chucknorris.io/jokes/random", timeout=10)
    vastaus.raise_for_status()
    return vastaus.json()["value"]

if __name__ == "__main__":
    try:
        print(hae_vitsi())
    except requests.RequestException as virhe:
        print(f"Vitsin haku epäonnistui: {virhe}")