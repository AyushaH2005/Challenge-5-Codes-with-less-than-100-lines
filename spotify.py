import requests
import base64

# Replace with your Spotify API credentials
CLIENT_ID = "cc19130f62b54f34b8c4ed3cd1df8fd4"
CLIENT_SECRET = "cae8c1725b1d47f1b08bd6f6236b6529"

# Step 1: Get access token
def get_token():
    auth = f"{CLIENT_ID}:{CLIENT_SECRET}"
    b64_auth = base64.b64encode(auth.encode()).decode()
    headers = {
        "Authorization": f"Basic {b64_auth}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    r = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
    return r.json()["access_token"]

# Step 2: Search for tracks based on mood
def search_tracks(mood, token):
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "q": mood,
        "type": "track",
        "limit": 10
    }
    r = requests.get("https://api.spotify.com/v1/search", headers=headers, params=params)
    return r.json()["tracks"]["items"]

# Step 3: Display results
def show_tracks(tracks):
    print("\n🎵 Recommended Tracks:\n")
    for t in tracks:
        name = t["name"]
        artist = t["artists"][0]["name"]
        url = t["external_urls"]["spotify"]
        print(f"🎧 {name} by {artist}\n🔗 {url}\n")

# Run the recommender
if __name__ == "__main__":
    mood = input("Enter your mood (e.g., happy, sad, chill): ")
    token = get_token()
    tracks = search_tracks(mood, token)
    show_tracks(tracks)
