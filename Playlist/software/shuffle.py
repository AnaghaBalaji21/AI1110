import os
import random
import pygame

# Set the path to the directory containing the audio files
audio_directory = "Music"

# Initialize Pygame
pygame.mixer.init()

# Get a list of all audio files in the directory
audio_files = [file for file in os.listdir(audio_directory) if file.endswith(".mp3")]

# Function to shuffle the audio files list
def shuffle_audio_files():
    shuffled_files = []
    while audio_files:
        random_index = random.randint(0, len(audio_files)-1)
        shuffled_files.append(audio_files.pop(random_index))
    audio_files.extend(shuffled_files)

# Initialize the current song index
current_song_index = 0

# Function to load and play the current song
def play_current_song():
    global current_song_index

    # Get the current song
    current_song = audio_files[current_song_index]

    # Get the full path of the audio file
    audio_path = os.path.join(audio_directory, current_song)

    # Load and play the audio file
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    print("Now playing:", current_song)

# Shuffle the audio files initially
shuffle_audio_files()

# Play the first song
play_current_song()

# Main loop
while True:
    command = input("Enter command (pause/play/next/prev/shuffle/quit): ")

    if command == "pause":
        pygame.mixer.music.pause()
    elif command == "play":
        pygame.mixer.music.unpause()
    elif command == "next":
        # Increment the current song index
        current_song_index = (current_song_index + 1) % len(audio_files)
        pygame.mixer.music.stop()
        play_current_song()
    elif command == "prev":
        # Decrement the current song index
        current_song_index = (current_song_index - 1) % len(audio_files)
        pygame.mixer.music.stop()
        play_current_song()
    elif command == "shuffle":
        # Shuffle the audio files
        shuffle_audio_files()
        pygame.mixer.music.stop()
        current_song_index = 0
        play_current_song()
    elif command == "quit":
        pygame.mixer.music.stop()
        break
    else:
        print("Invalid command. Try again.")


