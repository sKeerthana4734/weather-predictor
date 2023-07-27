from flask import Flask, render_template, redirect, url_for, request
import pickle

app = Flask(__name__)

model = pickle.load(open("weather.pkl", "rb"))


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/predict.html")
def pred():
    return render_template('predict.html')


@app.route("/predict", methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        outlook = int(request.form.get('Outlook'))
        temp = int(request.form.get('Temperature'))
        humidity = int(request.form.get('Humidity'))
        wind = int(request.form.get('Wind'))
        values = [outlook, temp, humidity, wind]
        result = model.predict_proba([values])
        prediction = result[0][1]
        print(prediction)
        if prediction > 0.5:
            return render_template('predict.html', pred="The weather is not so good to step out today. Have a great day at your home.")
        else:
            return render_template('predict.html', pred="The weather is good to step out today. Have a great day.")


if __name__ == "__main__":
    app.run()
