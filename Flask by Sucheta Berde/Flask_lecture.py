from flask import Flask, jsonify, request, redirect, url_for
app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Hello World and Data Science"

@app.route('/hello')
def hello_world():
    return "Welcome"

@app.route('/hellodatascience')
def hellodatascience():
    return "Welcome To DS world"

####add_url_rule####

# def hello_world():
#     return "Hello World"
# app.add_url_rule('/hello','hello',hello_world)

####Variables####

@app.route('/hello/<name>')
def hello_name(name):
    return "Welcome %s!" % name

@app.route('/blog/<int:postId>')
def blog(postId):
    return "Blog Number %d!" % postId

@app.route('/rev/<float:revNo>')
def rev(revNo):
    return "Revision Number %f!" % revNo


#####redirect(url_for)
@app.route('/admin')
def hello_admin():
    return "Hello Admin"

@app.route("/guest/<guest>")
def hello_guest(guest):
    return " Hello %s as guest" % guest

@app.route('/user/<name>')
def hello_user(name):
    if name == "admin":
       return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest",guest=name))


####HTTP methods#####
@app.route('/welcome/<name>')
def welcome(name):
    return "Welcome to home page %s" % name

@app.route('/login', methods = ["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("welcome", name=user))

    else:
        user = request.args.get("nm")
        return redirect(url_for("welcome", name=user))

#####get_json###

@app.route("/welcomeapi", methods = ["POST"])
def welcomeapi():
    data = request.get_json()
    name = data["name"]
    print(name)
    return jsonify({"Species" : name})

if __name__ == "__main__":
    app.run(debug = True)
