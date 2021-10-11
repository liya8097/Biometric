import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flaskr.db import get_db

bp = Blueprint('register', __name__, url_prefix='/')
@bp.route('/', methods=('GET', 'POST'))
def reg():
    if request.method == 'POST':
        username = request.form['username']
        registered = request.form['registered']
        error = None

        if not username:
            error = 'No user found'

        if error is None:
             with sql.connect("db.cpython-38.pyc") as con:
                 cur = con.cursor()
                 cur.execute("INSERT INTO Username (username) VALUES (?)"
                    "INSERT INTO Registered (registered) VALUES (?)") 
                
                 con.commit()
                 
    return render_template('/index.html')