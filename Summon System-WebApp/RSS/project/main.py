# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from re import search
from flask import request, Flask, render_template, redirect   # Import these flask functions
import sqlite3
import os
from flask.helpers import flash, url_for

if  "mydb.db" not in os.listdir():
        conn = sqlite3.connect("mydb.db")
        db = conn.cursor()
        db.execute("CREATE TABLE datas (issue_date TEXT, no_plate TEXT, location TEXT, offence TEXT, status TEXT, reported_by TEXT, date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)")
        conn.commit()
        conn.close()

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/mainpage')
@login_required
def mainpage():
    return render_template('mainpage.html')



@main.route('/add', methods=["GET", "POST"]) # Allowing data requests
@login_required
def create_data():
    if request.method.upper() == "POST":
        issue_date = request.form.get("issue_date")
        no_plate = request.form.get("no_plate").upper()
        location = request.form.get("location")
        offence = request.form.get("offence")
        status = request.form.get("status")
        reported_by = request.form.get("reported_by")
        

        if issue_date.strip() == "" or no_plate.strip() == "" or location.strip() == "" or offence.strip()== "" or status.strip()== "" or reported_by.strip() == "":
            # flashes a message to tell the user to fill all the fields
            flash("Please fill all the fields or go back to main page")
            return render_template("add.html")

        conn = sqlite3.connect("mydb.db")
        cur = conn.cursor()
        # Adding the data to the database
        cur.execute("INSERT INTO datas (issue_date, no_plate, location, offence, status, reported_by) VALUES(?, ?, ?, ?, ?, ?)", (issue_date, no_plate, location, offence, status, reported_by))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('main.display_datas')) # redirect user
    return render_template("add.html")



@main.route("/datas")
@login_required
def display_datas():
    conn = sqlite3.connect("mydb.db")
    cur = conn.cursor()
    cur.execute("SELECT *, rowid FROM datas") # Getting all the datas from the sqlite3 database
    datas = cur.fetchall() # fetching all the datas from the database and assigning them to the datas variable
    cur.close()
    conn.close()
    return render_template("datas.html", datas=datas)  # Passing the datas variable ( which is a list ) to the front-end so that jinja2 can loop over it and display all the datas

@main.route("/datas/<int:data_id>")
@login_required
def display_data(data_id):
    conn = sqlite3.connect("mydb.db")
    cur = conn.cursor()
    data = cur.execute("SELECT * FROM datas WHERE rowid = ?", (str(data_id))).fetchone() # Notice the fetchone() fucntion

    return render_template("data.html", data=data, data_id=data_id)

@main.route("/datas/<int:data_id>/delete")
@login_required
def delete_data(data_id):
    conn = sqlite3.connect("mydb.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM datas WHERE rowid = ?", (str(data_id)))
    conn.commit()

    return redirect(url_for('main.display_datas'))

################################################################################################# 

@main.route("/datas/<int:data_id>/edit", methods=["POST", "GET"])
@login_required
def edit_data(data_id):
    conn = sqlite3.connect("mydb.db")
    cur = conn.cursor()
    data = cur.execute("SELECT * FROM datas WHERE rowid = ?", (str(data_id))).fetchone()

    if request.method.upper() == "POST":
        issue_date = request.form.get("issue_date")
        no_plate = request.form.get("no_plate").upper()
        location = request.form.get("location")
        offence = request.form.get("offence")
        status = request.form.get("status")
        reported_by = request.form.get("reported_by")

        if issue_date.strip() == "" or no_plate.strip() == "" or location.strip() == "" or offence.strip()== "" or status.strip()== "" or reported_by.strip() == "":
            flash("Please fill all the fields")
            return render_template("edit.html", data=data)

        cur.execute("UPDATE datas SET issue_date = ?, no_plate = ?, location = ?, offence = ?, status = ?, reported_by = ? WHERE rowid = ?", (issue_date, no_plate, location, offence, status, reported_by, data_id))
        conn.commit()

        return redirect(url_for('main.display_datas'))

    return render_template("edit.html", data=data)
