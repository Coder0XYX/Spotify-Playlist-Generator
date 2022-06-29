# Spotify-Playlist-Generator FS2022

Project language: Python

Group ID: 1174

## Table of contents

- Introduction
- Project Description
- Tutorial
- Repository
- Installations


## Introduction 

This project documentation is related to the group project assignment of the course 7,789| 8,789: Skills: Programming with Advanced Computer Languages taught by Dr. Mario Silic. This project at the University of St. Gallen was conducted by Valentin Back 20-620-985 (PythonCharmer), Michael Schnidrig 17-608-829 (MichaelX), Christina Cappelli 16-606-311 (chrima) and Fabio Bianchetti 16-605-149 (Coder_XYX).

## Project Description

With the raise of audio streaming services such as Spotify, users changed their music consumption habits radically. The new music streaming services allow one to listen to millions of songs without possessing hard copies of them and provide the user with huge flexibilty towards when, how and what to listen to. The swedish based company moreover operates a Developer Platform, where user can develop the platform over Spotify APIs and SDKs for JavaScript, iOS, and Android. With the increased functionality of the streaming service, end user benefit from improvements on a continuous basis,  which makes their music listening experience unique. With this opportunity set at hand, this project wants to demonstrate how such a streaming service improvement for end user can be designed and implemented.

With over 82 million songs on the platform user can get quite overwhelmed when they try to find a song or create a playlist. Here, Spotify already has running algorythms where user get suggestions based on their previous listening behaviour. With our playlist generator we want to contribute to this functionalities and give the user the opportunity to create and customize a randomized playlist with a simple program written in the program language python. The objective is to fill Spotify-playlists automatically and to ask the user for initial inputs to customize his playlist towards the number of songs, the genre, and the release year.

## Tutorial

To run the playlist generator the user needs to have an active spotify subscription and complete the outlined steps in this tutorial which are presented in the following sections:

### Spotify developer project

1. Loging to [spotify developer](https://developer.spotify.com/dashboard/login) or create a new account
2. Go to dashboard and start a new project by clicking on "create an app" 
3. Click on Edit Settings and redirect the URI to: http://localhost:8888/callback
4. Copy/Paste Client ID and Secret somewhere or let the spotify developer website open, while running the code you will be ask to insert the information to
      - Client ID
      - Client Secret
      
### Spotify playlist creation

5. Open [Web Spotify app](https://open.spotify.com/)
6. Create a new Playlist
6. Add the playlist to your profile to make it available for the public (necessary that the code can access the newly created playlist)
7. Copy/Paste Playlist ID, while running the code you will be ask to insert the Playlist ID
      - Copy Playlist URL
      - Delete the URL part until and including the last "/"
      - Paste only the Playlist ID behind

### Running the program in python

8. Download the project folder "Playlist Generator" containing the files 220627_Spotify Code.py and requirements 
9. Open the project folder in Visual Studio Code, PyCharm CE or a similar program
10. Install requirements.txt in your IDE terminal
   - `pip install -r requirements.txt`  
   - `pip3 install -r requirements.txt`  
   - `conda install -r requirements.txt` 
11. Make sure you have the information to Client ID, Client Secret and playlist ID ready (previous two sections in the tutorial)
12. After completion of steps 1-11 the program and the configuration is all set up and you can _run_ the program in your source-code editor

## Repository

The repository shows 3 files. The "README.md" file gives an overall introduction and project description with step-by-step instructions. "220220629_Spotify Code.py" contains the code. "requirements.txt" contains additional packages which are required to have running connections between the spotify developer platform, spotify and the source-code editor. Here is as well a google drive link where you can find a demo video of the Spotify Playlist Generator:


   
We hope that you find our Spotify Playlist Generator usefull and enjoy creating randomized playlists with our tool. Enjoy listening!


------------------------
