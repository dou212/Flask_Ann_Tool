from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user
from att import bcrypt
from att.models import User
from att.users.forms import LoginForm
from att.static.root_path import Config
import os

main = Blueprint('main', __name__)

@main.route("/", methods=['GET','POST'])
@main.route("/home", methods=['GET','POST'])
def home():
    extracted_path = Config.extracted_path
    
    dir_list = []
    files = os.listdir(extracted_path)
    for dir in files:
        if os.path.isdir(os.path.join(extracted_path,dir)):
            dir_list.append(dir)
    dir_list.sort()
    
    date_list = []
    date_dict = {}
    for dir in dir_list:
        month,day,_ = dir.split('-')
        date = month+"-"+day
        if date not in date_list:
            date_list.append(date)
        if date not in date_dict:
            date_dict[date]=[dir]
        else:
            date_dict[date].append(dir)
    date_list.sort()

    if not current_user.is_authenticated:
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password,form.password.data):
                login_user(user,remember=form.remember.data)
                return render_template('home.html',date_list=date_list,date_dict=date_dict)
            else:
                flash('Login Unsuccessful, Please check email and password','danger')
        return render_template('login.html', title='Login', form = form)
    
    
    return render_template('home.html', date_list = date_list,date_dict=date_dict)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
