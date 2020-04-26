from flask import Flask, render_template, request, redirect, Blueprint, url_for
from db_config import mydb
from datetime import datetime
register_bp = Blueprint('register_bp',__name__, template_folder='templates')


@register_bp.route("/", methods=['GET','POST'])
def register():
        if request.method == 'POST':            
            regdetails = request.form
            fname = regdetails['firstname']
            lname = regdetails['lastname']
            email = regdetails['email']
            username = regdetails['username']
            password = regdetails['password'] 
            ins_date = datetime.now()
            cur = mydb.cursor()
            cur.execute("INSERT INTO webappdata.users(FNAME, LNAME, EMAIL, USERNAME, PASSWORD, INSERT_DATE, UPDATE_DATE) values(%s, %s, %s, %s, %s, %s, %s)",(fname, lname, email, username, password, ins_date, ins_date))
            mydb.commit()
            return redirect(url_for("login_bp.home"))
        return render_template('register.html')