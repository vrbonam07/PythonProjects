from flask import Flask, render_template, request, redirect, Blueprint, url_for
from db_config import mydb
from datetime import datetime

login_bp = Blueprint('login_bp',__name__, template_folder='templates')

@login_bp.route("/")
def home():
    cur = mydb.cursor()
    cur.execute("select * from webappdata.projects")
    userdetails = cur.fetchall()
    if len(userdetails) > 0:
        return render_template('users.html', userdetails=userdetails)
    else:
        return render_template('users.html', userdetails='None')


@login_bp.route("/createprojects", methods = ["GET", "POST"])
def projects():
    if request.method == 'POST':            
            regdetails = request.form
            projectname = regdetails['Project_name']
            projectdesc = regdetails['Project_desc']
            prj_create_dt = datetime.now()
            cur = mydb.cursor()
            cur.execute("INSERT INTO webappdata.projects(PROJECT_NAME, PROJECT_DESC, PROJECT_CREATED_DATE) values(%s, %s, %s)",(projectname, projectdesc, prj_create_dt))
            mydb.commit()
            return redirect(url_for('login_bp.home'))
    return render_template('create_project.html')