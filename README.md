# Spotify-Playlist-Generator FS2022

Project language: Python

Group ID: _TBD_

## Table of contents

- Introduction
- Project Description
- Tutorial
- Repository
- Installations


## Introduction 

This project documentation is related to the group project assignment of the course 7,789| 8,789: Skills: Programming with Advanced Computer Languages taught by Dr. Mario Silic. This project at the University of St. Gallen was conducted by Valentin Back (_CodingXCamp User: TBD_), Michael Schnidrig (_MichaelX_), Christina Cappelli (_chrima_) and Fabio Bianchetti (_Coder_XYX_).

## Project Description

With the raise of audio streaming services such as Spotify, users changed their music consumption habits radically. The new music streaming services allow one to listen to millions of songs without possessing hard copies of them and provide the user with huge flexibilty towards when, how and what to listen to. The swedish based company moreover operates a Developer Platform, where user can develop the platform over Spotify APIs and SDKs for JavaScript, iOS, and Android. With the increased functionality of the streaming service, end user benefit from improvements on a continuous basis and make their music listening experience unique. With this opportunity set at hand, this project wants to demonstrate how such a streaming service improvement for end user can be designed and implemented.

With over 82 million songs on the platform user can get quite overwhelmed when they try to find a song or create a playlist. Here, Spotify already has running algorythms where user get suggestions based on their previous listening behaviour. With our playlist generator we want to contribute to this functionalities and give the user the opportunity to create and customize a randomized playlist with a simple program written in the program language python. The objective is to fill Spotify-playlists automatically and to ask the user for initial inputs to customize his playlist towards the number of songs, the release year or multi-year periods. 

## Tutorial

To run the playlist generator the user needs to have an active spotify subscription and complete the outlined steps in this tutorial which are presented in the following sections:

### Spotify developer project

1. Loging to [spotify developer](https://developer.spotify.com/dashboard/login) or create a new account
2. Start a new project on the spotify developer platform
3. Click on Edit Settings and redirect the URI to: http://localhost:8888/callback
4. Copy/Paste Spotify ID
      - ClientID
      - playlistID
      
### Spotify playlist creation

4. Open [Web Spotify app](https://open.spotify.com/)
5. Create a new Playlist
6. Add the playlist to your profile to make it available for the public (necessary that the code can access the newly created playlist)
7. Copy/Paste Playlist ID
      - Copy Playlist URL
      - Delete the URL part until and including the last "/"
      - Paste only the Playlist ID behind

### Running the program in python

8. Download the project folder "Playlist Generator" containing the files 10k non-hits.py and requirements 
9. Open the project folder in Visual Studio Code, PyCharm CE or a similar program
10. Install requirements.txt
11. Add the key variables which where extracted from the developer project website and the newly generated playlist (previous two sections in the tutorial)
      - clientID = "_Your clientID_"
      - clientSecret = "_Your clientSecret_"
      - playlistID = "_Your playlistID_"
      - scope = "playlist-modify-public"
12. After completion of steps 1-11 the program and the configuration is all set up and you can _run_ the program in your source-code editor.

## Repository

The repository shows 3 files. The "X" file gives an overall introduction and project description with step-by-step instructions. "10k non-hits.py" contains the code. "requirements.txt" contains X which are required to have running connections between the spotify developer platform, spotify and the source-code editor.

## Installations

The following programs were used to analyse and test the code:

   - [Python 3.10.5](https://www.python.org/downloads/)
   - [PyCharm CE 2022.1.2](https://www.jetbrains.com/pycharm/download/#section=mac)
 
The following packages and modules are moreover required to run the code:

   - TBD
   
The following libraries are relevant to run the code:

   - TBD

Info: In case these packages are not installed yet, you need to write the following commands on your command prompt. If pip is not installed yet, please rund "pyhton get-pip.py" first: 

Reihenfolge anpassen und Ergänzungen vornehmen!!!

   - `pip install spotipy` or `pip3 install spotipy`  
   - `-m pip install --upgrade pip` 
   - `pip3 install spotipy --upgrade`  
   - `pip3 install spotipy_random` 
   - `python3 -m ensurepip` 
   
   

We hope that you find our Spotify Playlist Generator usefull and enjoy creating randomized playlists with our tool. Enjoy listening!


-------------------------

Notes to delete at the end of project:
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
