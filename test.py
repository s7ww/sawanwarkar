# app.py
from flask import Flask, render_template
from etc import get_weather

app = Flask(__name__)

@app.route('/')
def home():
    temperature, description = get_weather()
    return render_template('index.html', temperature=temperature, description=description)


@app.route('/about')
def about():
    return "Computer Engineer"

if __name__ == '__main__':
    app.run()

