Workout Tracker
This Python script allows users to track their workouts and record them directly into a Google Sheet. The script uses the Nutritionix API to analyze exercise data and the Sheety API to post the data into a Google Sheet.

Features
Input Exercise Details: Users can input the type of exercise they did.
Calorie and Duration Calculation: The script uses the Nutritionix API to calculate the duration and calories burned for the specified exercise.
Automatic Logging to Google Sheets: The details of each workout, including date, time, exercise, duration, and calories burned, are automatically posted to a Google Sheet using the Sheety API.
Requirements
Python 3.x
requests library
You can install the requests library using pip if you haven't already:

bash
Copy code
pip install requests
Setup
Google Sheet: Create a new Google Sheet and set up Sheety to access it. Ensure you have the correct endpoint URL and authentication details.

Nutritionix API: Sign up for the Nutritionix API and get your APP_ID and APP_KEY.

Sheety API: Sign up for Sheety, set up your project, and obtain your API endpoint and authentication token.

Environment Variables (Optional): For security reasons, it's better to store sensitive information like API keys and authentication tokens as environment variables. Replace hard-coded values in the script with these environment variables.

Usage
Clone the repository or copy the script to your local machine.

Run the script:

bash
Copy code
python workout_tracker.py
When prompted, input the exercise you performed (e.g., "ran 3 miles").

The script will calculate the calories burned and duration using Nutritionix and then log the data into the Google Sheet using Sheety.

Code Explanation
API Configuration:

Set up API endpoints and authentication headers for Nutritionix and Sheety.
User Input:

The script takes user input for the exercise performed.
Nutritionix API Request:

Sends a POST request to Nutritionix with the user's exercise details to get the exercise information (calories burned, duration).
Data Formatting:

Formats the exercise data and gets the current date and time.
Sheety API Request:

Sends a POST request to the Sheety API with the formatted data to log it into Google Sheets.
Response Handling:

Prints the response from Sheety to confirm the data has been logged.
Example Output
arduino
Copy code
Which exercise did you do? ran 5 miles
{
  "workout": {
    "date": "04/09/24",
    "time": "10:30 AM",
    "exercise": "ran 5 miles",
    "duration": "45 min",
    "calories": 400
  }
}
Security Notice
Ensure you handle API keys and sensitive data securely. Avoid hardcoding them in your script if possible. Instead, use environment variables or a secure vault.
License
This project is open-source and available under the MIT License.
