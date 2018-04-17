
from gtts import gTTS
from time import sleep
import datetime
import os
import pyglet
import random
import webbrowser

# Keurig start function for a fresh Cup-o-Joe
def keurig_start():
    # This will be completed with RaspPi Servo if possible 
    pass

# Open blinds/lights function
def open_blinds():
    # This will be completed with RaspPi Servo if possible
    pass

# Voiced time using google_test_to_speech (gTTS) 
def voice_activation():
    time = datetime.datetime.now().strftime("%c") 
    morning_greeting = "Good morning Christian. The date is " + str(time)

    tts = gTTS(text=morning_greeting, lang='en')
    filename = '/tmp/temp.mp3'
    tts.save(filename)

    music = pyglet.media.load(filename, streaming=False)
    music.play()

    sleep(music.duration) #prevent from killing
    os.remove(filename) #remove temperory file

def weather_summary():
    api_key = "e82e91429d97385172aa7303e5f2f4c8"
    zip = str(75002)
    country_code = "us"
    weather = "api.openweathermap.org/data/2.5/weather?zip=" + zip + "," + country_code + "&" + api_key
    print(weather)

# Youtube playlist to play random selection
def playlist_func():

    random_youtube_selection_list = [
        "https://www.youtube.com/watch?v=MF2GsvelF7c",
        "https://www.youtube.com/watch?v=7YJLPeIK8yQ",
        "https://www.youtube.com/watch?v=Qh1GZUff6kw",
        "https://www.youtube.com/watch?v=LcFvO6vGTX4",
        "https://www.youtube.com/watch?v=0CmZtTxgGyk",
        "https://www.youtube.com/watch?v=wbgInLJ81eY"
    ]

    to_play = webbrowser.get()
    to_play.open(random.choice(random_youtube_selection_list))

# Main function to call associated parts
def main():
    keurig_start()
    open_blinds()
    # voice_activation()
    sleep(1)
    weather_summary()
    sleep(1)
    # playlist_func()
    
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()