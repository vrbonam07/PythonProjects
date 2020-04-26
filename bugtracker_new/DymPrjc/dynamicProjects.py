from flask import Flask, Blueprint, render_template,request, redirect, url_for
from db_config import mydb
from datetime import datetime

dyprj_bp = Blueprint('dyprj_bp',__name__,template_folder="templates")

@dyprj_bp.route("/<project_name>")
def dynamicprj(project_name):
    cur = mydb.cursor()
    cur.execute("select Distinct Task_Type from webappdata.Task_Type order by Task_Type")
    tasktypes = cur.fetchall()
    cur.execute("select ID, PROJECT_NAME, TASK_TYPE, TASK_TITTLE, TASK_DESC, TASK_PROGRESS from webappdata.Task where project_name = %s",(project_name,))
    task_list = cur.fetchall()
    if request.method == 'POST':
        status = request.form['taskprogerss']
        cur = mydb.cursor()
        cur.execute("INSERT INTO WEBAPPDATA.TASK(TASK_PROGRESS) VALUES(%s)",(status))
        mydb.commit()
    return render_template('dynamic_project.html', projectname=project_name,tasktypes=tasktypes, tasklist=task_list)

@dyprj_bp.route("/<project_name>/<task_name>", methods=['GET','POST'])
def dynamictask(project_name,task_name):
    if request.method == 'POST':
        regdetails = request.form
        tittle = regdetails['Tittle']
        desc = regdetails['Desc']
        ins_dt = datetime.now()
        cur = mydb.cursor()
        cur.execute("INSERT INTO WEBAPPDATA.TASK(PROJECT_NAME, TASK_TYPE, TASK_TITTLE, TASK_DESC, TASK_CREATED_DT, TASK_UPDATED_DT) VALUES(%s,%s,%s,%s,%s,%s)",(project_name, task_name, tittle, desc, ins_dt, ins_dt))
        mydb.commit()
        return redirect(url_for("dyprj_bp.dynamicprj",project_name=project_name))
    return render_template('Create_task.html', projectname=project_name,taskname=task_name)
