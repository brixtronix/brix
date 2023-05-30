from flask import render_template, redirect, request, flash, session
from flask_app.__innit__ import app
from flask_app.models.parcel import Parcel
from flask_app.models.user import User

#login render and method
@app.route('/index')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user:
        flash("Emai not found")
        return redirect('/index')
    if not user.password == request.form['password']:
        flash("Invalid Password", "login")
        return redirect('/index')
    session['user_id']=user.id
    return redirect('/home')

"""
# home
@app.route('/home')
def me():
    return render_template("home.html")
"""

# layout preview
@app.route('/layout')
def layout():
    return render_template("layout.html")

# new parcel render and post method
@app.route('/home')
def new_parcel():
    if 'user_id'not in session:
        return redirect('/logout')
    data={
        "id": id
    }
    parcels = Parcel.get_all_parcels()
    print(parcels)
    return render_template("home.html", current_user=User.get_by_id(data), all_parcels=parcels)

@app.route('/parcel/new', methods=['POST'])
def parcel_new():
    if "user_id" not in session:
        return redirect('/logout')
    data={
        "parcel": request.form['parcel'],
        "user_id": session['user_id']
    }
    Parcel.save_parcel(data)
    return redirect('/home')

"""
# get all parcels for home feed
@app.route('/')
def all_parcels():
    if "user_id" not in session:
        return redirect('/logout')
    data={
        'id': session['user_id']
    }
    
    return render_template("home.html", current_user=User.get_by_id(data))
"""

#delete 
@app.route('/delete/parcel/<int:id>')
def delete_parcel(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': id
    }
    Parcel.delete_parcel(data)
    return redirect('/home')

# work stuff
@app.route('/work')
def resume():
    return render_template("work.html")

# logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/index')

