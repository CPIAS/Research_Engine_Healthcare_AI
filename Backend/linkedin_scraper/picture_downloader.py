import requests
import json
import pandas as pd

df = pd.read_csv('LinkedIn_Profiles.csv')
linkedIn_list = df.LinkedIn

pfp_src_json = open('profile_pictures_src.json')
pfp_src = json.load(pfp_src_json)


def download_picture_from_src(url, file_path):
    data = requests.get(url).content
    f = open(file_path, 'wb')
    f.write(data)
    f.close()


j = 0
for i, element in enumerate(linkedIn_list):
    linkedin_url = element
    picture_src = pfp_src[j]
    # Using LinkedIn urls so that the jpg indices correspond to the user indices in the scraped data json
    if pd.isna(linkedin_url):
        continue
    if picture_src == '':
        j += 1
        continue
    path = f'pictures/user_picture_{i + 1}.jpg'
    download_picture_from_src(picture_src, path)
    j += 1

