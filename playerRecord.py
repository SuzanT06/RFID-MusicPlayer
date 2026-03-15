#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

# --- CONFIGURATION ---
DEVICE_ID = "DEVICE_ID"
CLIENT_ID = "CLIENT_ID"
CLIENT_SECRET = "CLIENT_SECRET"
REDIRECT_URI = "http://127.0.0.1:8080" 
SCOPE = "user-read-playback-state user-modify-playback-state"

# 1. AUTHENTICATE ONCE (Outside the loop)
auth_manager = SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI,
                            scope=SCOPE)
sp = spotipy.Spotify(auth_manager=auth_manager)
reader = SimpleMFRC522()

print("Jukebox Ready! Scan a card...")

try:
    while True:
        # 2. WAIT FOR SCAN
        # This will pause the script here until a card touches the reader
        card_id, text = reader.read()
        print(f"Detected Card ID: {card_id}")

        try:
            # 3. WAKE UP THE PI (With a slight delay for the 3B)
            sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
            sleep(1) 

            # 4. CARD LOGIC (Note: No quotes around the numbers)
            if card_id == 1234567890: # Replace with the actual ID number
                print("Playing Track...")
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:"REPLACE-WITH-SONG-ID"'])
            
            elif card_id == 9876543210:
                print("Playing Album...")
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:"REPLACE-WITH-ALBUM-ID"')

            # Anti-duplicate: wait 3 seconds so it doesn't scan the same card twice
            sleep(3)
            print("Ready for next scan...")

        except Exception as spotify_err:
            print(f"Spotify Error: {spotify_err}")

except KeyboardInterrupt:
    print("Stopping Jukebox...")
finally:
    GPIO.cleanup()
