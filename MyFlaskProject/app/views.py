from flask import Flask, render_template, redirect, url_for, request, make_response, session, abort
from itsdangerous import Signer, BadSignature
from .session_interface import MySessionInterface

app = Flask(__name__)
app.secret_key = b"S003_123sRt4"


# app.session_interface = MySessionInterface() !!!!!!kontrol et!!!!!

# app.run() Çalıştırma seçeneği


def get_current_username():
    email = ""
    login_auth = False
    if 'email' in session:
        email= session['email']
        login_auth = True
    return email, login_auth







@app.route("/")
def index():
    email, login_auth = get_current_username()
    return render_template("index.html", email = email, login_auth = login_auth)


@app.route("/contact")
def Contact():
    email, login_auth = get_current_username()
    return render_template("contact.html", email = email, login_auth = login_auth)


@app.route("/contactlist")
def ContactList():
    email, login_auth = get_current_username()
    return render_template("contact_list.html", email = email, login_auth = login_auth)


@app.route("/login", methods=["GET", "POST"])
def Login():
    if request.method == "POST":
        if request.form:
            if "email" in request.form and "password" in request.form:
                email = request.form["email"]
                password = request.form["password"]
                print(email, password)
                if email == "admin@gmail.com" and password == "admin":
                    session["email"] = email
                    return redirect(url_for('index'))
                else:
                    return redirect(url_for('Login'))

        abort(400)
    email , login_auth = get_current_username()
    return render_template("Login.html", email = email, login_auth = login_auth)

    ###        Coockies For Index Page        ###

#     signer = Signer("secret key")
#     signed_name = request.cookies.get("name")
#     try:
#         name = signer.unsign(signed_name).decode()
#         print(name)
#     except BadSignature:
#         print("Bad Signature")
#     signed_name = signer.sign("Damla")
#     response = make_response("<html><body><h1> My first flask app </h1></body></html>")
#     response.set_cookie("name", signed_name)
#     return response


# @app.route("/hello")
# def Hello():
#     return render_template("hello.html")
#
#
# @app.route("/hello-admin")
# def HelloAdmin():
#     return render_template("hello_admin.html")
#
#
# @app.route("/hello-user/<name>")
# def HelloUser(name):
#     if name.lower() == "admin":
#         return redirect(url_for("HelloAdmin"))
#     return render_template("hello_user.html", username=name)
#
#
# @app.route("/add/<int:number1>/<int:number2>")
# def Add(number1, number2):
#     # number1 = request.args["number1"]
#     # number2 = request.args["number2"]
#     calculation_result = int(number1) + int(number2)
#     return render_template("add.html", number1=number1, number2=number2, result=calculation_result)
#
#
# @app.route("/sub/<int:num1>/<int:num2>")
# def sub(num1, num2):
#     res = num1 - num2
#     return render_template("sub.html", num1=num1, num2=num2, res=res)
#
#
# @app.route("/login", methods=["POST", 'GET'])
# def Login():
#     if request.method == "POST":
#         username = request.form["username"]
#         return redirect(url_for("HelloUser", name=username))
#     else:
#         return render_template("login.html")
#
#
# @app.route("/student")
# def Student():
#     return render_template("student.html")
#
#
# @app.route("/result", methods=["POST"])
# def Result():
#     ContexData = {
#         'name': request.form["name"],
#         'physic': request.form["physic"],
#         'math': request.form["math"],
#         'history': request.form["history"]
#     }
#     return render_template("student_result.html", **ContexData)
