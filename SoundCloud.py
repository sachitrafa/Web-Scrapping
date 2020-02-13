from selenium import webdriver
import requests
import bs4

top_url = "https://soundcloud.com/charts/top"
new_url = "https://soundcloud.com/charts/new"
track_url = "https://soundcloud.com/search/sounds?q="
artist_url = "https://soundcloud.com/search/people?q="
mix_url_end = "&filter.duration=epic"

browser = webdriver.Chrome('chromedriver.exe')
browser.get("https://soundcloud.com")

print()
print(">>> Welcome to the Python Soundcloud Scraper")
print(">>> Explore the Top / New & Hot Charts for all Genres")
print(">>> Search Soundcloud for Tracks, Artist, and Mixes")
print()

while True:
    print(">>> Menu")
    print(">>> 1 - Search for a track")
    print(">>> 0 - Exit")
    print()
    choice = int(input("Enter your choice:"))
    if choice == 0:
        browser.quit()
        break
    print()

    # search for a track
    if choice == 1:
        name = input("Name of the track: ")
        print()
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
            print(str(index+1) + ": " + track.text)
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
            x = 0
            while x==0:
                try:
                    elem=browser.find_element_by_xpath("//*[@id='content']/div/div[2]/div/div[2]/div[2]/div/div/div[1]/a").click()
                    x=1
                except:
                    x=0



        continue
