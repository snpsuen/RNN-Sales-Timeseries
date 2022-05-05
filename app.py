import tensorflow as tf
from tensorflow import keras
from numpy import asarray
from flask import Flask, render_template, request

app = Flask(__name__)
model = tf.keras.models.load_model("./rnn_sales_timeseries_model")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
  if request.method == 'POST':
    month01 = float(request.form.get('month01'))
    month02 = float(request.form.get('month02'))
    month03 = float(request.form.get('month03'))
    month04 = float(request.form.get('month04'))
    month05 = float(request.form.get('month05'))	
 
    n_steps = 5
    row = asarray([month01, month02, month03, month04, month05]).reshape((1, n_steps, 1))
    yhat = model.predict(row)
    return render_template('result.html', result=yhat)
