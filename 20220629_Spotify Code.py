### The following section contains information about the authors and the creation of the code
"""
Course: Programming With Advanced Computer Languages
Created by: 1174
Submitted on the: 29th of June 2022
Readme and other documentation accessible through the following link:https://github.com/Coder0XYX/Spotify-Playlist-Generator
"""



### In the following section, relevant libraries are installed and imported
# Import more general libraries
import json
from random import randrange
# Import more specific libraries
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from spotipy_random import get_random



### In the following section, all functions are defined that are called in the core code later one
# Function to define how long the playlist should be
def length_function():
    # While statement is used to make sure that code runs until user has entered a valid input
    while True:
        # Try/except statement is used to make sure that code does not break if wrong input is entered
        try:
            # Ask user how long the playlist should be (we chose to limit the playlist length to max. 50 songs)
            number_songs = int(
                input("Please enter how many songs the new playlist should have, the maximum number of songs is 50: "))
        except ValueError:
            # Let user know that input was not valid because it is not an integer
            print("Error - This is not a valid input. Please try again and don't forget that the maximum is 50 songs: ")
            continue
        # If statement to check whether user has entered a number that is larger than the maximum playlist length
        if number_songs > 50:
            # Let user know that input integer was too big
            print("Error - The playlist is too long. Please try again and don't forget that the maximum is 50 songs: ")
            continue
        else:
            # If integer was valid, let user know how long his/her playlist will be
            print("Your playlist will contain %s songs." % number_songs)
            break
    return number_songs

# Function to define the year / time from which random songs should be chosen
def time_function():
    # While statement is used to make sure that code runs until user has entered a valid input
    while True: 
        # Try/except statement is used to make sure that code does not break if wrong input is entered
        try: 
            # Ask user for the year from which songs should be chosen (we chose to limit the timespan to 1970-2021)
            age_songs = int(input("Please enter a year between 1970 - 2021 from which songs should be chosen: "))
        except ValueError:
            # Let user know that input was not valid because it is not an integer
            print("Error - This is not a valid input. Please try again and don't forget that the year should be between 1970 - 2021: ")
            continue
        # If statement to check whether year is between 1970 - 2021
        if age_songs < 1970 or age_songs > 2021:
            # Let the user know that the inputted year is not valid
            print("Error - The year is not valid. Please try again and don't forget that the year should be between 1970 - 2021: ")
            continue
        else: 
            # If integer was valid, let user know from which year his/her playlist will be
            print("The songs in your playlist will be from the year %s." % age_songs)
            break
    return age_songs

# Function to define the music genre of the random songs that should be chosen
def genre_function():
    # While statement is used to make sure that code runs until user has entered a valid input
    while True: 
        # Try/except statement is used to make sure that code does not break if wrong input is entered
        try: 
            # Ask user to select a genre from those that are offered
            input_genre = int(input("Please choose a genre by entering the corresponding number - Pop = 1, Rock = 2, Rap = 3, House = 4, R&B = 5: "))
            # If statement to convert user input into the corresponding string that is used in the function
            if input_genre == 1:
                output_genre = "pop"
                break
            elif input_genre == 2:
                output_genre = "rock"
                break
            elif input_genre == 3:
                output_genre = "rap"
                break
            elif input_genre == 4:
                output_genre = "house"
                break
            elif input_genre == 5:
                output_genre = "r&b"
                break
            # If the user has entered a different number, an error statement will be returned
            else:
                print("Error - This is not a valid input. Please enter one of the integers that are listed.")
                continue
        except ValueError: 
            # Let user know that input was not valid
            print("Error - This is not a valid input. Please enter one of the integers that are listed.")
            continue
    # Let user know which genre his playlist will be
    print("Your playlist will have songs that are part of the %s genre." % output_genre)
    return output_genre

# Function to define the randomization, and how songs are chosen and added to the playlist
def Spotify_function():
    # User authentification using the defined clientID and clientSecret
    spotify_client = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=clientID,
        client_secret=clientSecret))
    # Choose a random song based on the defined criteria (e.g., genre)
    random_pop_song_json = str = get_random(spotify=spotify_client, type="track", year=playlist_age, genre=playlist_genre,
                                            limit=playlist_length, offset_min=offset, offset_max=(offset + 1))
    # Extract song URI from random song JSON (needed as input to add song back into the playlist)
    json_str = json.dumps(random_pop_song_json)
    resp = json.loads(json_str)
    track_uri = resp['uri']
    # Add selected random song to playlist on Spotify via the extracted URI
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientID, client_secret=clientSecret,
                                                   redirect_uri="http://localhost:8888/callback", scope=scope))
    sp.playlist_add_items(playlist_id=playlistID, items=[track_uri], position=None)



### In the following section, the core program is run
# Define key variables, which are needed to run the code
# Ask user for the Client ID and Client Secret which can be retrieved from https://developer.spotify.com
clientID = str(input("Please copy and paste your Client ID from the Spotify Developer Website:")) # This is personal and secret -> insert own client ID
clientSecret = str(input("Please copy and paste your Client Secret from the Spotify Developer Website:"))  # This is personal and secret -> insert own client secret
scope = "playlist-modify-public"

# Ask user for the playlist to which the songs should be added
playlistID = str(input("Please enter the playlist ID of the Spotify playlist where you want to add the songs: "))

# Set up the Loop
counter = int(1) # Used to count how many songs are already added to the playlist
playlist_length = length_function()
playlist_age = time_function()
playlist_genre = genre_function()

# Inform the user, that it will take a while until the songs are added to the playlist
print("Be aware, it may take a while until the songs are added to your playlist.")

# Loop through the function that selects and adds the random songs to the playlist 
while counter <= playlist_length:
    offset = randrange(1, 950) # Random offset is needed to improve randomisation of spotipy.random (otherwise more popular songs are preferred)
    # Let user know about the current progress of the code
    progress = (counter-1) / playlist_length * 100
    print("Current progress: %s percent." % progress)
    # Try/except statement to make sure that any HTTP errors stemming from the Spotify API do not break the code
    try: 
        Spotify_function()
        counter += 1
    except:
        pass

# Ask user to refresh their spotify playlist website to see the changes
print("Thanks for waiting, we are done! Please refresh the website and start listening. We hope you like the songs on your playlist!")



### This is the end of the code
