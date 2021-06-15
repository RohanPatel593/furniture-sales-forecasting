from flask import Flask, render_template, request
import pickle
import numpy as numpy

app = Flask(__name__)
model=pickle.load(open('models.pkl','rb'))
file = open('models.pkl', 'rb')
pred_ci = pickle.load(file)


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict', methods=['POST'])
def predict():
    date = request.form['date']
    x=pred_ci.loc[date,'lower price']
    y=pred_ci.loc[date,'upper price']
    return render_template('index.html',date='The prediction for month {}'.format(date),lower_price='Lower price is {}'.format(x),upper_price='Upper price is {}'.format(y))

if __name__=="__main__":
   app.run(debug=True)
