from flask import Blueprint, render_template
import glob

note_bp = Blueprint('note_bp', __name__,template_folder='templates')


def fetch_notes():
    final_notes=[]
    notes=glob.glob('bugtracker/noteapp/SavedNotes/*.note')
    for note in notes:
        with open(note) as _file:
            final_notes.append(_file.read())
        _file.close()
    
    return final_notes

@note_bp.route('/')
def show():
    return render_template('note_index.html', notes=fetch_notes())

