from flask import Flask, render_template,url_for,request, make_response, session, abort, redirect
from session_interface import MySessionInterface

import os
os.environ["FLASK_DEBUG"] = "development"

app = Flask(__name__)
app.secret_key = b"sTroNgK**Ey1928"
app.session_interface = MySessionInterface()


def get_current_username(): #mevcut kullanıcı var ise emaili'ni ve login_auth boolean değişkenini true olarak, yok ise emaili null, login_auth'u ise false oalrak return eden metod
    email = ""
    login_auth = False
    if "email" in session:
        email = session['email']
        login_auth = True
    return email, login_auth

@app.route("/")
def index():
    email, login_auth = get_current_username()
    return render_template("index.html", email=email, login_auth=login_auth)

@app.route("/about")
def about():
    email, login_auth = get_current_username()
    return render_template("about.html", email=email, login_auth=login_auth)

@app.route("/gallery")
def gallery():
    email, login_auth = get_current_username()
    return render_template("gallery.html", email=email, login_auth=login_auth)

#       DENEME-gallery-single-post.html'i ayarla: galeride tıklanılan her foto detaylı bir şekilde gallerySingle/photoid? şeklinde açsın ve altında açıklama olsun
#       @@@@@@@@@@@@@@@@@@@@@@ Aynı işlemi blog için de ayarla @@@@@@@@@@@@@@@@@@@@@@
# @app.route("/gallery-single-post/<string:photo_id>")
# def gallerySingle(photo_id):
#     return render_template("DENEME-gallery-single-post.html", photo_id=photo_id)


@app.route("/blog")
def blog():
    email, login_auth = get_current_username()
    return render_template("DENEME-blog.html", email=email, login_auth=login_auth)

@app.route("/contact")
def contact():
    email, login_auth = get_current_username()
    return render_template("contact.html", email=email, login_auth=login_auth)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST': #Eğer kullanıcı login bilgileri ile bir form göndermiş ise
        if request.form: #gönderilen istekte form datası bulunuyor mu
            if 'email' in request.form and 'password' == request.form: #form'da email ve password bulunuyor mu
                email = request.form['email'].lower()
                password = request.form['password'] #formdan email ve password verileri alındı
                if email.lower() == 'admin@gmail.com' and password.lower() == 'admin':
                    session['email'] = email
                    return redirect(url_for('index')) #giriş işlemi başarılı ise index sayfasına
                else:
                    return redirect(url_for('login'))   #giriş işlemi başşarısız ise yeniden login sayfasına yönlendirilir.
        abort(400)
    email, login_auth = get_current_username()
    return render_template("login.html", email = email, login_auth = login_auth)

app.run()
