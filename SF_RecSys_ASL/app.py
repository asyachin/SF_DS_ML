from flask import Flask, render_template, request, url_for
import os
import pandas as pd
import numpy as np


PATH = f'{os.getcwd()}/data/'
app = Flask(__name__)

data = pd.read_csv(PATH + 'submissions.csv')

# Read list of top_3 items from file:
with open(PATH + 'top_3_items.npy', 'rb') as f:
  top_3 = np.load(f)

@app.route('/')
@app.route('/index',  methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/predict',  methods=['POST', 'GET'])

def predict():
    start = request.form['action'] == 'Predict'
    userID= int(request.form['userID'])
    val_users = np.array(data.user_id)

    if start:
        if userID in val_users:

            predict = data[data.user_id == userID]['recommended_items'].apply(lambda x: x.split(',')).tolist()[0]

        else:
            predict = top_3

        val_1 = list(np.array(predict))[0]
        val_2 = list(np.array(predict))[1]
        val_3 = list(np.array(predict))[2]

    return render_template('predict.html', content = (val_1, val_2, val_3))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(debug=True, host='0.0.0.0', port=port)