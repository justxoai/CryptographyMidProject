from flask import Flask, render_template, request

from Midterm_Project.otp import check_otp, show_qr

login = Flask(__name__)

@login.route("/")
def login_function():
    return render_template("login.html")

@login.route('/verify', methods = ['POST'])
def verify_otp():
    otp = request.form.get('password')
    if check_otp(otp):
        print('ok')
        return render_template('index.html')
    else:
        print('no')
        return 'no'

if __name__ == "__main__":
    show_qr()
    login.run(debug=True)