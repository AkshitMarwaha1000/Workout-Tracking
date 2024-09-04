import datetime
import os

import requests

GOOGLE_SHEET = 'https://docs.google.com/spreadsheets/d/1tuq87d77HDXg89f9Dabf4dw0X7gPCYN2vu5qrtTtRnU/edit?usp=sharing'
APP_ID = '7f188408'
APP_KEY = '67f1ed3807ca155ce04434d9664eda9a'
API_END_POINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_API_ENDPOINT_POST = 'https://api.sheety.co/3bcb0bccb622c2d049d4b30e0c15494a/workoutTrackingData/workouts'
AUTHENTICATION_HEADER = 'Authorization: Basic YWtzaGl0X3dvcmtvdXQ6YWtzaGl0QDEyMw=='


header_nurix = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
}

query = input("Which exercise did you do? ")

params = {
    'query': query,
    'gender': 'male',
    'weight_kg': 82,
    'height_cm': 174,
    'age': 20
}

response = requests.post(url=API_END_POINT, json=params, headers=header_nurix)
ex = response.json()['exercises']

for exercise in ex:
    exercise_name = exercise['user_input']
    duration = exercise['duration_min']
    calories = exercise['nf_calories']

    date_now = datetime.datetime.now().strftime("%d/%m/%y")
    time_now = datetime.datetime.now().strftime("%I:%M %p")

    formatted_duration = f"{int(duration):02d} min"
    sheet_data = {
        'workout': {
            'date': date_now,
            'time': time_now,
            'exercise': exercise_name,
            'duration': formatted_duration,
            'calories': calories,
        }
    }

    header_sheety = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic YWtzaGl0X3dvcmtvdXQ6YWtzaGl0QDEyMw=='
    }

    sheet_response = requests.post(url=SHEETY_API_ENDPOINT_POST, json=sheet_data, headers=header_sheety)
    print(sheet_response.json())

