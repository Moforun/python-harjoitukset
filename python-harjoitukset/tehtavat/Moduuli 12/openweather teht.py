import requests

API_AVAIN = "72888b8c298bdafef9f2e2eaf212491f"
URL = "https://api.openweathermap.org/data/2.5/weather"

def kelvin_celsiukseksi(kelvin):
    return kelvin - 273.15

def hae_saa(paikkakunta):
    parametrit = {
        "q": paikkakunta,
        "appid": API_AVAIN,
        "lang": "fi",
    }
    vastaus = requests.get(URL, params=parametrit, timeout=10)
    if vastaus.status_code == 404:
        return None
    vastaus.raise_for_status()
    return vastaus.json()

if __name__ == "__main__":
    paikkakunta = input("Anna paikkakunnan nimi: ").strip()
    try:
        data = hae_saa(paikkakunta)
        if data is None:
            print("Paikkakuntaa ei löytynyt.")
        else:
            kuvaus = data["weather"][0]["description"]
            lampotila = kelvin_celsiukseksi(data["main"]["temp"])
            print(f"Sää paikkakunnalla {data['name']}: {kuvaus}")
            print(f"Lämpötila: {lampotila:.1f} °C")
    except requests.RequestException as virhe:
        print(f"Säätietojen haku epäonnistui: {virhe}")