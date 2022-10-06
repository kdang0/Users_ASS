from flask import redirect, request, render_template, session
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    users = User.get_all()
    return render_template("result.html", all_users = users)

@app.route('/add_user')
def result():
    return render_template("create.html")


@app.route('/edit', methods = ["POST"])
def edit():
    User.update(request.form)
    return redirect('/')

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        'fname' : request.form["fname"],
        'lname' : request.form["lname"],
        'email' : request.form["email"]
    }
    User.save(data)
    return redirect('/')

@app.route('/show/<int:id>')
def show_user(id):
    data = {
        "id" : id
    }
    return render_template("show.html", user=User.get_one(data))

@app.route('/delete/<int:id>')
def delete_user(id):
    data = {
        "id" : id
    }
    User.delete(data)
    return redirect('/')

@app.route('/edit_user/<int:id>')
def edit_user(id):
    data = {
        "id" : id
    }
    return render_template("edit.html", user=User.get_one(data))