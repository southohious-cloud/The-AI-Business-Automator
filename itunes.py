import sys

# Try to import requests, and give a helpful message if it's missing
try:
    import requests
except ModuleNotFoundError:
    print("The 'requests' library is not installed.")
    print("Install it by running: pip install requests")
    sys.exit()

import json

# Ask the user for a search term instead of using sys.argv
term = input("Artist or song to search: ").strip()

if not term:
    print("No search term provided.")
    sys.exit()

# Build the URL exactly like your original version
response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=50&term=" + term
)

o = response.json()

for result in o["results"]:
    print(result["trackName"])
