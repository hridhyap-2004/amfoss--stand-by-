import os
import requests
from bs4 import BeautifulSoup

def check_update_and_download(comic_url, download_path):
    response = requests.get(comic_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        comic_img = soup.find("img", {"alt": "Comic"})["src"]
        comic_img_url = f"{comic_url}/{comic_img}"
        img_response = requests.get(comic_img_url)
        if img_response.status_code == 200:
            with open(os.path.join(download_path, "comic.png"), "wb") as f:
                f.write(img_response.content)
                print(f"Comic image saved to {download_path}.")
        else:
            print("Could not download comic image.")
    else:
        print("Website returned a non-200 status code.")
comic_url = "https://example.com/webcomic"
download_path = os.path.expanduser("~/Desktop")
check_update_and_download(comic_url, download_path)
