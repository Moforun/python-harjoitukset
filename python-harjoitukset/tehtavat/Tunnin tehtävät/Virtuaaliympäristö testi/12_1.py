import requests

nimi = input("Anna pokemonin nimi: ").strip().lower()

try:
    vastaus = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nimi}", timeout=10)
    if vastaus.status_code == 200:
        data = vastaus.json()
        tyypit = [t["type"]["name"] for t in data["types"]]
        print("Pokemonin tyypit:", ", ".join(tyypit))
    elif vastaus.status_code == 404:
        print("Pokemonia ei löytynyt.")
    else:
        print("Virhe, statuskoodi:", vastaus.status_code)
except requests.exceptions.RequestException as e:
    print("Yhteysvirhe:", e)
