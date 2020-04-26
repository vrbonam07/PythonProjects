from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# Database configuration:
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mysqlroot123'
app.config['MYSQL_DB'] = 'webappdata'

mysql = MySQL(app) # this mysql object will be used in the code to refer to a mysql table.

from Login.login import login_bp as login_bp
from registry.register import register_bp as register_bp
from Topic.Topic import topic_bp as topic_bp
from noteapp.noteindex import note_bp as note_bp
from noteapp.createnote import createnotes as createnotes
from DymPrjc.dynamicProjects import dyprj_bp as dyprj_bp 

app.register_blueprint(login_bp, url_prefix="/home")
app.register_blueprint(register_bp, url_prefix="/register")
app.register_blueprint(topic_bp, url_prefix="/topic")
app.register_blueprint(note_bp, url_prefix="/notes")
app.register_blueprint(createnotes, url_prefix="/notes")
app.register_blueprint(dyprj_bp, url_prefix="/project")
    
@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Fetch the form data from login_page.html
        logindetails = request.form
        username = logindetails['username']
        password = logindetails['password']
        cur = mysql.connection.cursor()
        while len(username) == 0 or len(password) == 0:
            return "Username or password not provied"
            break
        else:    
            cur.execute("select distinct password from webappdata.users where username in (%s)",(username,))
            pw_fromdb = cur.fetchone()
            if pw_fromdb is not None:
                for i in pw_fromdb:
                    if password == i:
                        return redirect('/home')
            else:
                return render_template('invalid_credentials.html')        
        cur.close()
    return render_template('login_page.html')


if __name__ == "__main__":
    app.run(debug=True)