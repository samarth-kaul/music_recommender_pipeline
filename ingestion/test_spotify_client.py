from spotify_client import SpotifyClient

spotify = SpotifyClient()

# Search for artist
artist = spotify.search_artist("Taylor Swift")
if not artist:
    print("Artist not found.")
else:
    artist_id = artist["id"]
    print("✅ Artist:", artist["name"])

    # Get full artist info
    genres = spotify.get_artist_genres(artist_id)
    print("✅ Genres:", genres)

    # Get top tracks
    print("\n🎵 Top Tracks:")
    tracks = spotify.get_artist_top_tracks(artist_id)
    for t in tracks[:5]:
        print(f"   - {t['name']} (Popularity: {t['popularity']})")
