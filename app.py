from flask import Flask, render_template
import requests
import os

# Create a Flask app and specify the current directory as the template folder
app = Flask(__name__, template_folder=os.path.dirname(__file__))

# GNews API Key
API_KEY = "02f580555dca8fd65f692ea4012d9e4d"

# GNews API Endpoint
BASE_URL = "https://gnews.io/api/v4/top-headlines"

def fetch_news():
    # Parameters for the API request
    params = {
        "apikey": API_KEY,
        "lang": "en",  # Language of news
        "country": "us",  # Country code for news
        "max": 10  # Maximum number of results
    }
    try:
        # Make the API request
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Parse the JSON response
        data = response.json()

        # Extract articles
        articles = data.get("articles", [])
        return articles
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

@app.route("/")
def home():
    news_articles = fetch_news()
    return render_template("index.html", articles=news_articles)

if __name__ == "__main__":
    app.run(debug=True)
