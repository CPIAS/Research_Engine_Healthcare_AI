from selenium import webdriver
from dotenv import load_dotenv
import pandas as pd
import os
from linkedin_scraper import Person, actions
from profile_formatter import profile_to_dict
import json

df = pd.read_csv('LinkedIn_Profiles_short_ver.csv')
linkedIn_list = df.LinkedIn
load_dotenv()
driver = webdriver.Chrome()

email = os.environ['LINKEDIN_EMAIL']
password = os.environ['LINKEDIN_PASSWORD']
actions.login(driver, email, password)  # if email and password isnt given, it'll prompt in terminal

linkedin_profiles = []
json_profiles = {
    "profiles": {}
}
unique_id = 0
for link in linkedIn_list:
    unique_id += 1
    try:
        person = Person(link, driver=driver, scrape=True, close_on_complete=False)
        print(person.experiences[0])
    except Exception as e:
        print(e)
        continue
    json_profiles['profiles'][unique_id] = profile_to_dict(person)
    linkedin_profiles.append(person)
print(len(linkedin_profiles))
print(json_profiles)
with open("bug_fixing.json", "w") as outfile:
    json.dump(json_profiles, outfile, indent=4, default=lambda o: '<not serializable>')


