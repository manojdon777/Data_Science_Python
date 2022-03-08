from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the Flask class'

@app.route('/happy')
def happy():
    return 'I am happy to be a Data Scientist'

if __name__ == '__main__':
    app.run(debug= True)