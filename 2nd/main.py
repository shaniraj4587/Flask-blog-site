from flask import Flask, render_template, request, redirect, session, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import os
import math
from werkzeug.utils import secure_filename
from flask_mail import Mail

with open("config.json", "r") as c:
    params = json.load(c)['params']


app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config.update(
    MAIL_SERVER = 'smtp.hostinger.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    # MAIL_USE_TLS=True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD = params['gmail-pass']
)
mail = Mail(app)

app.config['UPLOAD_FOLDER'] = params['upload_location']

if (params['local_server'] == 'True'):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCEMY_DATABASE_URL'] = params['prod_uri']
db = SQLAlchemy(app)


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    img_file = db.Column(db.String(12), nullable=True)

@app.route("/")
def index():
    posts = Posts.query.filter_by().all()  #[0:params['no_of_post']]
    last = math.ceil(len(posts)/int(params["no_of_post"]))
    page = request.args.get("page")
    if (not str(page).isnumeric()):
        page =1
    page = int(page)
    posts = posts[(page-1)*params['no_of_post'] : (page-1)*params['no_of_post'] + params['no_of_post']]
    if page == 1:
        prev = "#"
        next = "/?page=" + str(page+1)
    elif page == last:
        prev = "/?page=" + str(page-1)
        next = "#"
    else:
        prev = "/?page=" + str(page-1)
        next = "/?page=" + str(page+1)
    return render_template("index.html", params=params, posts = posts, next=next, prev = prev)


@app.route("/about")
def about():
    return render_template('about.html', params=params)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if(request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('msg')

        entry = Contacts(name=name, phone_number=phone, msg=message, date=datetime.now(), email=email,)
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from ' + name,
                          sender= params['gmail-user'],
                          recipients = [params['gmail-user'], email],# this will message on both
                                                  
                          body = message + "\n mobile number is:" + phone
                          )
        flash("thankyou for filling the form we will get back to you soon", "success") #here second args take as categories

    return render_template('contact.html', params=params)

@app.route("/post/<post_slug>")
def post_route(post_slug):

    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template("post.html", params = params, post=post)
    
@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    if "user" in session and session['user']==params['admin_user']:
        posts = Posts.query.all()
        return render_template("dashboard.html", params=params, posts = posts)
    
    if request.method == 'POST':
        username = request.form.get('uname')
        password = request.form.get('pass')
        if username == params['admin_user'] and password == params['admin_pass']:
            session['user'] = username
            posts = Posts.query.all()
            return render_template("dashboard.html", params=params, posts = posts)

    else:
        return render_template("login.html", params=params)

@app.route("/logout")
def logout():
    session.pop("user")
    return redirect("/")

@app.route('/delete/<sno>', methods=['GET', 'POST'])
def delete(sno):
    if "user" in session and session['user']==params['admin_user']:
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
        return redirect("/dashboard")

@app.route('/edit/<sno>', methods=['GET', 'POST'])
def edit(sno):
    if "user" in session and session['user']==params['admin_user']:
        if request.method == 'POST':
            box_title = request.form.get("title")
            slug = request.form.get("slug")
            content = request.form.get("content")
            image_file = request.form.get("image_file")
            date = datetime.now()

            if sno == "0":
                post = Posts(title=box_title, slug=slug, content=content, img_file=image_file, date=date)
                db.session.add(post)
                db.session.commit()
                flash("Post added !!")
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title = box_title
                post.slug = slug
                post.content = content
                post.img_file = image_file
                post.date = date
                flash("Post edited successful! ")
                db.session.commit()
                return redirect("/edit/"+sno)
            
        post = Posts.query.filter_by(sno=sno).first()

        upload_dir = app.config['UPLOAD_FOLDER']
        try:
            files = os.listdir(upload_dir)
            files = [f for f in files if os.path.isfile(os.path.join(upload_dir, f))]
        except FileNotFoundError:
            files = []
        return render_template("edit.html", params = params, post=post, sno=sno, files=files)


@app.route("/uploader", methods=['GET', 'POST'])
def uploader():
    if "user" in session and session['user'] == params["admin_user"]:
        if request.method == "POST":
            f = request.files['file1']
            custom_name = request.form.get('new_filename', '')

            if f and custom_name:
                # Get and secure the extension and filename
                original_filename = secure_filename(f.filename)
                file_ext = os.path.splitext(original_filename)[1]
                safe_custom_name = secure_filename(custom_name)

                # Combine custom name with original extension
                new_filename = safe_custom_name + file_ext

                # Save the file
                save_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
                f.save(save_path)
                flash(f"File uploaded successfully as {new_filename}")
                return  redirect("/dashboard")
            else:
                return "Missing file or filename input."

    return "Unauthorized", 403

@app.route("/uploads")
def list_uploads():
    if "user" in session and session['user'] == params["admin_user"]:
        upload_dir = app.config['UPLOAD_FOLDER']
        try:
            files = os.listdir(upload_dir)
            files = [f for f in files if os.path.isfile(os.path.join(upload_dir, f))]
        except FileNotFoundError:
            files = []

        return render_template("uploads.html", files=files)

    return "Unauthorized", 403


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

app.run(debug=True)