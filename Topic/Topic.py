from flask import Blueprint, render_template, Request, redirect, url_for

topic_bp = Blueprint('topic_bp', __name__, template_folder='templates', static_folder='static')

@topic_bp.route('/')  
def show():
    return render_template('index.html')

@topic_bp.route('/Tech')
def Tech_page():
    return render_template('Tech.html')

@topic_bp.route('/CloudPlatforms')
def CP_page():
    return render_template('CloudPlatforms.html')

@topic_bp.route('/Travel')
def Teavel_page():
    return render_template('Travel.html')

@topic_bp.route('/Food')
def Food_page():
    return render_template('Food.html')

@topic_bp.route('/Clothing')
def Clothing_page():
    return render_template('Clothing.html')

@topic_bp.route('/Movies')
def Movies_page():
    return render_template('Movies.html')
