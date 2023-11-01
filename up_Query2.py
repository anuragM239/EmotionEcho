from pymongo import MongoClient
import pygame
import os


def query2(text):
    
    # Initialize pygame mixer
    pygame.mixer.init()
    print(text)

    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Songs"]
    music_collection = db["Combined"]

    # Get user input for song name
    requested_song_title = text
    requested_song = music_collection.find_one({"Title": requested_song_title})
    print(requested_song)

    if requested_song:
        emotion = requested_song.get("Emotion", "Unknown Emotion")
        query2_result = music_collection.find({"Emotion": emotion, "Title": {"$ne": requested_song_title}}).limit(14)

        # Display and play the songs
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(f"Requested Song's Emotion: {emotion}")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")

        # Prepare a list to hold the titles, artists, albums, and paths of the songs
        songs = []

        # Display and store titles, artists, albums, and paths of all 15 songs
        for idx, song in enumerate([requested_song] + list(query2_result), start=1):
            title = song.get("Title", "Unknown Title")
            artist = song.get("Artist", "Unknown Artist")
            album = song.get("Album", "Unknown Album")
            path = song.get("Path", "")
            songs.append({"title": title, "artist": artist, "album": album, "path": path})
            print(f"{idx}. {title} \n \t ({artist}, {album})")

        # Play each song one by one
        for idx, song in enumerate(songs, start=1):
            print(f"\nPlaying {song['title']} ({idx}/{len(songs)})")
            print(f"\t ({song['artist']}, {song['album']})")
            pygame.mixer.music.load(song['path'])
            pygame.mixer.music.play()
            input("Press Enter to stop playback...")
            pygame.mixer.music.stop()

    # Close the connection
    client.close()

