from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials


date_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date_input}/")
contents = response.text
soup = BeautifulSoup(contents, "html.parser")

titles = soup.select("li ul li h3")

CLIENT_ID = "35a7ca968fd04a01a2996fb0c620839d"
CLIENT_SECRET = "138a5aff8d044e15a9323aba14a0ed13"
USERNAME = "yadxhd87qeym7nesui6b8glzr"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=USERNAME,
    )
)
user_id = sp.current_user()["id"]

song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date_input.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    for track in result["tracks"]["items"]:
        print(track["name"] + ": " + result["tracks"]["items"][0]["href"])
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
