from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the Flask class'

@app.route('/happy')
def happy():
    return 'I am happy to be a Data Scientist'

@app.route('/person/<name>')
def person(name):
    return 'Name of the person is ' + name

@app.route('/success/<int:score>')
def success(score):
    return 'The person has passed and marks are ' + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'The person has failed and marks are ' + str(score)

#RESULT CHECKER
@app.route('/result/<int:marks>')
def result(marks):
    result=''
    if marks < 40:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result, score=marks))

if __name__ == '__main__':
    app.run(debug= True)