import os
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from passlib.apps import custom_app_context as pwd_context
from tempfile import gettempdir
from datetime import datetime
from db import initialize_database

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = gettempdir()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

initialize_database()

db = SQL("sqlite:///database.db")


@app.route("/")
def landing():
    return redirect("/register")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("Please fill all fields")
            return redirect("/register")

        db.execute("INSERT INTO users (username, password, current_stamps, date_joined) VALUES (:username, :password, :current_stamps, :date_joined)",
                   username=username,
                   password=password,
                   current_stamps=1,
                   date_joined=datetime.now()
                   )
        user = db.execute(
            "SELECT * FROM users WHERE username = :username", username=username)
        session["user_id"] = user[0]["id"]

        return redirect("/card")


@app.route("/card")
def card():
    return render_template("card.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
