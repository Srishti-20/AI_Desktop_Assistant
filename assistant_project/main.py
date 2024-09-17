from threading import Thread
from spotify_module import play_song, pause_song, resume_song, stop_song, initialize_spotify
from speech_module import say, takeCommand
from ai_module import get_weather
# from wake_word_detection import wake_word_detection 
# from face_recognition_module import face_recognition
# from recommender_module import recommend_song, song_data
import datetime
import os
import webbrowser

def main():
    print('Starting Jarvis A.I')
    say("Jarvis A.I")

    initialize_spotify()

    listening = False 

    while True:
        if listening:
            print("Listening...")
            query = takeCommand()

            sites = [["youtube", "https://www.youtube.com"], ["google", "https://www.google.com"],
                     ["wikipedia", "https://www.wikipedia.com"], ["pinterest", "https://www.pinterest.com"]]

            apps = [["facetime", "/System/Applications/FaceTime.app"],
                    ["apple music", "/System/Applications/Music.app"],
                    ["notes", "/System/Applications/Notes.app"],
                    ["calculator", "/System/Applications/Calculator.app"],
                    ["chat gpt", "/Applications/ChatGPT.app"],
                    ["camera", "/System/Applications/Photo\\ Booth.app"]]

            musics = [["radha rani", "spotify:track:3ZziJElZDohG9ufvtgeAWq"],
                      ["darshan raval", "spotify:track:0rMeOAvbQZ2RTG4B6L1M4p"],
                      ["taylor swift", "spotify:track:1D4PL9B8gOg78jiHg3FvBb"],
                      ["selena gomez", "spotify:track:4l0Mvzj72xxOpRrp6h8nHi"],
                      ["eminem", "spotify:track:6or1bKJiZ06IlK0vFvY75k"],
                      ["justin bieber", "spotify:track:6epn3r7S14KUqlReYr77hA"]]

            processed = False  

            for site in sites:
                if f"open {site[0]}" in query.lower():
                    say(f"Opening {site[0]}...")
                    webbrowser.open(site[1])
                    processed = True
                    break

            for app in apps:
                if f"open {app[0]}" in query.lower():
                    say(f"Opening {app[0]}...")
                    os.system(f"open {app[1]}")
                    processed = True
                    break

            for music in musics:
                if f"play {music[0]}" in query.lower():
                    say(f"Playing your favorite song by {music[0]}...")
                    play_song(music[1])
                    processed = True
                    break

            if "pause" in query.lower():
                say("Pausing the song")
                pause_song()
                processed = True

            if "resume" in query.lower():
                say("Resuming the song")
                resume_song()
                processed = True

            if "stop" in query.lower():
                say("Stopping the song")
                stop_song()
                processed = True

            if "play system music" in query.lower():
                musicPath = "/Users/2003s/Downloads/better-day-186374.mp3"
                say("Playing the system music")
                os.system(f"open {musicPath}")
                processed = True

            if "the current time and weather" in query.lower():
                hour = datetime.datetime.now().strftime("%H")
                min_ = datetime.datetime.now().strftime("%M")
                city_name = "Hyderabad"
                weather_info = get_weather(city_name)
                say(f"The current time is {hour} hours and {min_} minutes, and the weather is: {weather_info}")
                processed = True

            if "thanks jarvis" in query.lower():
                say("You're welcome. Have a good day ahead.")
                processed = True

            if "goodbye jarvis" in query.lower():
                say("Goodbye!")
                listening = False
                processed = True

            if not processed:
                say("I'm sorry, I didn't understand that command.")

        else:
            query = takeCommand()
            if "hello jarvis" in query.lower():
                say("Hello! How can I assist you?")
                listening = True

if __name__ == '__main__':
    main()
