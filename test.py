import speech_recognition as sr
from selenium import webdriver
import requests
import bs4
import os

browser = webdriver.Chrome('chromedriver.exe')
browser.get("https://soundcloud.com")

def call(recognizer, audio):
    track_url = "https://soundcloud.com/search/sounds?q="
    try:
        name = recognizer.recognize_google(audio)
        print(name)
        "%20".join(name.split(" "))
        browser.get(track_url + name)
        url = track_url + name
        request = requests.get(url)
        soup = bs4.BeautifulSoup(request.text, "lxml")
        # print(request.text)
        tracks = soup.select("h2")
        track_links = []
        track_names = []
        for index, track in enumerate(tracks):
            track_links.append(track.a.get("href"))
            track_names.append(track.text)
            print(str(index + 1) + ": " + track.text)
            print()
        while True:
            choice = input(">>> Your choice (x to re-select genre): ")
            print()

            if choice == 'x':
                break
            else:
                choice = int(choice) - 1

            print("Now playing: " + track_names[choice])
            print()
            def hello():
                browser.get("http://soundcloud.com" + track_links[choice])
            hello()
            x=0
            while x == 0:
                try:
                    browser.find_element_by_xpath("//*[@id='content']/div/div[2]/div/div[2]/div[2]/div/div/div[1]/a").click()
                    x = 1
                except:
                    x = 0
    except sr.UnknownValueError:
        print("Please say that again")

r = sr.Recognizer()
r.listen_in_background(sr.Microphone(),call)
print("Please say the name of the song you want to hear")
import time
while True:
    time.sleep(0.1)