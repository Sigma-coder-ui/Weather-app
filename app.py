from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "fa2c4c95154bd3c0ea61a4fa32e0cc45"

@app.route('/', methods=['GET', 'POST'])
def home():
    weather = None

    if request.method == 'POST':
        city = request.form['city']

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        #print(response.status_code)
        #print(response.text)

        if response.status_code == 200:
            data = response.json()

            weather = {
                'city': city,
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description'],
                'wind': data['wind']['speed']
            }

    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)