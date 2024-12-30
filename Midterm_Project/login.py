from flask import Flask, render_template

login = Flask(__name__)

@login.route("/")
def login_function():
    return render_template("login.html")

if __name__ == "__main__":
    login.run(debug=True)