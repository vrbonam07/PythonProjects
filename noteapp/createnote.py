from flask import Blueprint, render_template, request, redirect
import random

createnotes = Blueprint('createnotes', __name__,template_folder='templates')


def random_gen(length=16):
    final_str =''
    chars='abcdefghijklmnopqrstuvwxyz0123456789'

    for x in range(0, length):
        final_str += chars[random.randint(0, len(chars)-1)]
        
    return final_str

@createnotes.route('/createnote', methods=['POST', 'GET'] )
def show():

    if request.method =='POST':
        if request.form.get('createnote'):
            text = request.form.get('notetext')
            
            with open('noteapp/savednotes/{}.note'.format(random_gen()),'w+') as newfile:
                newfile.write(text)
            
            newfile.close()
            return redirect('/notes')
    return render_template('createnote.html')