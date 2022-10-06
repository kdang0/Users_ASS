from flask import Flask, redirect, request, render_template, session
from user import User
app = Flask(__name__)
app.secret_key = "MAKE IT MAKE SENSE"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result')
def result():
    users = User.get_all()
    return render_template("create.html", all_users = users)

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        'fname' : request.form["fname"],
        'lname' : request.form["lname"],
        'email' : request.form["email"]
    }
    User.save(data)
    return redirect('/result')

if __name__ == "__main__":
    app.run(debug=True)