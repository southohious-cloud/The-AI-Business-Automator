import requests

def main():
    print("Search iTunes!")
    artist = input("Artist: ")

    try:
        response = requests.get(
            "https://itunes.apple.com/search",
            params={"term": artist, "entity": "song", "limit": 20}
        )
        response.raise_for_status()

        data = response.json()
        results = data.get("results", [])

        if not results:
            print("No songs found.")
            return

        print(f"\nSongs found for '{artist}':\n")
        for song in results:
            print(f"- {song.get('trackName', 'Unknown Title')}")

    except requests.HTTPError:
        print("Couldn't complete request!")

main()
