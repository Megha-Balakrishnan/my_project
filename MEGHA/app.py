from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    """Grabs the input values and uses them to make prediction"""
    fruits = int(request.form['fruits'])
    stress = int(request.form['stress'])
    places = int(request.form['places'])
    others = int(request.form['others'])
    social = int(request.form['social'])
    achievment = int(request.form['achievment'])
    BMI = int(request.form['BMI'])
    todolist = int(request.form['todolist'])
    walk = int(request.form['walk'])
    vision = int(request.form['vision'])
    sleep = int(request.form['sleep'])
    shout = int(request.form['shout'])
    income = int(request.form['income'])
    passion = int(request.form['passion'])
    meditation = int(request.form['meditation'])
    age = int(request.form['age'])
    gender = int(request.form['gender'])
    print(" result is ",fruits,stress,places,others,social,achievment,BMI,todolist,walk,vision,sleep,shout,income,passion,meditation,age,gender)
    
    prediction = model.predict([[fruits,stress,places,others,social,achievment,BMI,todolist,walk,vision,sleep,shout,income,passion,meditation,age,gender]])  # this returns a list e.g. [127.20488798], so pick first element [0]
    
    output = round(prediction[0],2) 

    return render_template('prediction.html',title='Success',prediction_text= f'Your Life style score is ${output}')

if __name__ == "__main__":
    app.run(debug =True)
