import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# -----------------------------
# Settings
# -----------------------------
np.random.seed(42)
random.seed(42)

NUM_USERS = 500
NUM_DAYS = 365

users = [f"U{str(i).zfill(4)}" for i in range(1, NUM_USERS + 1)]

cities = [
    "Chennai","Bangalore","Hyderabad","Mumbai","Delhi",
    "Pune","Kolkata","Ahmedabad","Coimbatore","Jaipur"
]

occupations = [
    "Student","Software Engineer","Teacher","Doctor",
    "Business","Designer","Analyst","Sales","Freelancer","Manager"
]

apps = {
    "Instagram":"Social Media",
    "WhatsApp":"Social Media",
    "Facebook":"Social Media",
    "YouTube":"Entertainment",
    "Netflix":"Entertainment",
    "Spotify":"Entertainment",
    "ChatGPT":"Productivity",
    "Gmail":"Productivity",
    "LinkedIn":"Productivity",
    "Google Docs":"Productivity",
    "Chrome":"Browser",
    "Maps":"Utility",
    "Camera":"Utility",
    "BGMI":"Gaming",
    "Free Fire":"Gaming"
}

start_date = datetime(2025,1,1)

rows = []

for day in range(NUM_DAYS):

    current_date = start_date + timedelta(days=day)

    day_type = "Weekend" if current_date.weekday()>=5 else "Weekday"

    for user in users:

        age = random.randint(18,45)

        gender = random.choice(["Male","Female"])

        city = random.choice(cities)

        occupation = random.choice(occupations)

        device = random.choice(["Android","iPhone"])

        sleep = round(np.random.uniform(4.5,9),1)

        steps = random.randint(2000,15000)

        apps_today = random.sample(list(apps.keys()), random.randint(4,8))

        for app in apps_today:

            usage = random.randint(5,180)

            unlock = random.randint(1,25)

            notification = random.randint(0,80)

            battery = random.randint(1,20)

            rows.append({

                "Date":current_date.date(),

                "User_ID":user,

                "Age":age,

                "Gender":gender,

                "City":city,

                "Occupation":occupation,

                "Device":device,

                "App_Name":app,

                "App_Category":apps[app],

                "Usage_Minutes":usage,

                "Unlock_Count":unlock,

                "Notifications":notification,

                "Battery_Usage":battery,

                "Sleep_Hours":sleep,

                "Steps":steps,

                "Day_Type":day_type

            })

df = pd.DataFrame(rows)

print(df.head())

print()

print("Total Rows :",len(df))

print("Total Columns :",len(df.columns))

df.to_csv("data/raw/digital_lifestyle_dataset.csv",index=False)

print()

print("Dataset Saved Successfully!")