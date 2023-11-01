#this is for finding emotion  from random phrase

from pymongo import MongoClient
import pygame
import os

def query1(text):
        
    # Initialize pygame mixer
    pygame.mixer.init()

    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017")
    db = client["Songs"]
    music_collection = db["Combined"]

    # Get user input for emotion
    # emotion = input("Enter the emotion: ")
    emotion = text
    query_result = music_collection.find({"Emotion": emotion}).limit(15)

    # Create a list to store song information
    songs = []

    # Retrieve song information and store in the list
    for song in query_result:
        title = song.get("Title", "Unknown Title")
        artist = song.get("Artist", "Unknown Artist")
        album = song.get("Album", "Unknown Album")
        path = song.get("Path", "")
        songs.append({"title": title, "artist": artist, "album": album, "path": path})

    # Display all song titles, artists, and albums
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print("Available songs:")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    
    for idx, song in enumerate(songs, start=1):
        print(f"{idx}. {song['title']}\n \t ({song['artist']}, {song['album']})")

    # Play the selected songs one by one
    for idx, song in enumerate(songs, start=1):
        print(f"\nPlaying {song['title']} ({idx}/{len(songs)})")
        print(f"\t ({song['artist']}, {song['album']})")
        pygame.mixer.music.load(song['path'])
        pygame.mixer.music.play()
        input("Press Enter to stop playback...")
        pygame.mixer.music.stop()

    # Close the connection
    client.close()
