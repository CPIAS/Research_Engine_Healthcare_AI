from linkedin_scraper import Person, actions
from selenium import webdriver
from dotenv import load_dotenv
import pandas as pd
import os

df = pd.read_csv('LinkedIn_Profiles.csv')
linkedIn_list = df.LinkedIn
load_dotenv()
driver = webdriver.Chrome()

email = os.environ['LINKEDIN_EMAIL']
password = os.environ['LINKEDIN_PASSWORD']
actions.login(driver, email, password)  # if email and password isnt given, it'll prompt in terminal

linkedin_profiles = []

for link in linkedIn_list:
    try:
        person = Person(link, driver=driver, scrape=True, close_on_complete=False)
    except Exception as e:
        print(e)
        continue
    linkedin_profiles.append(person)
print(len(linkedin_profiles))

columns = ['LinkedIn URL', 'Name', 'About', 'Experiences', 'Interests', 'Accomplishments',
           'Company', 'Job Title', 'Contacts']


def profile_to_dict(profile):
    return {'url': profile.linkedin_url, 'Name': profile.name, 'About': profile.about,
            'Experiences': profile.experiences, 'Interests': profile.interests,
            'Accomplishments': profile.accomplishments, 'Company': profile.company,
            'Job Title': profile.job_title, 'Contacts': profile.contacts}


df = pd.DataFrame([profile_to_dict(x) for x in linkedin_profiles], columns=columns)
df.to_csv('all_extracted_profiles.csv', index=True, encoding='utf-8')
