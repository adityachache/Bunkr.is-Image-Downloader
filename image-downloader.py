from bs4 import BeautifulSoup
import requests
import os

BUNKR_URL = "https://bunkr.is/a/lMFjwdoN"

FOLDER_PATH = "C:/Users/User/Desktop/New folder"

headers = {
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=BUNKR_URL, headers=headers)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")


pictures = soup.find_all(name='a', class_='image')
print(len(pictures))

picture_links = [link.get("href") for link in pictures]
print(picture_links)


os.chdir(FOLDER_PATH)
print(os.getcwd())

counter = 0
for image in picture_links:
    r = requests.get(image)

    print(f"Downloading image {counter}...")
    with open(f"image{counter}.jpg", 'wb') as f:
        f.write(r.content)
    counter += 1

print("Download Completed")