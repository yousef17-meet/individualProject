from flask import Flask, render_template
from model import * 
from flask import Flask, url_for, flash, render_template, redirect, request, g, send_from_directory
from flask import session as login_session
from model import *
from werkzeug.utils import secure_filename
import locale, os




app = Flask(__name__)

@app.route('/')
def mainpage():
	allBands = session.query(Band).all()
	return render_template("mainpage.html", allBands = allBands)


@app.route('/newuser', methods = ['GET','POST'])
def signup():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		password = request.form['password']
		address = request.form['address']
		if name is None or email is None or password is None :
			flash("Your form is missing arguments")
			return redirect(url_for('newuser'))	

		if session.query(User).filter_by(email = email).first() is not None:
			flash("A user with this email address already exists")
			return redirect(url_for('newuser'))
		user = User(name = name, email=email, address = address)
		user.hash_password(password)
		session.add(user)
		session.commit()
		flash("User Created Successfully!")
		return redirect(url_for('mainpage'))

	else:
		return render_template('signup.html')	

	

@app.route("/Bands/<int:band_id>")
def ShowBandPage(band_id):
	myband = session.query(Band).filter_by(id=band_id).one()
	return render_template("band.html", myband=myband)

@app.route('/login', methods = ['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	elif request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		if email is None or password is None:
			flash('Missing Arguments')
			return redirect(url_for('login'))
		if verify_password(email, password):
			user = session.query(user).filter_by(email=email).one()
			flash('Login Successful, welcome, %s' % customer.name)
			login_session['name'] = user.name
			login_session['email'] = user.email
			login_session['id'] = customer.id
			return redirect(url_for('playlist'))
		else:
			flash('Incorrect username/password combination')
			return redirect(url_for('login'))

def verify_password(email, password):
	customer = session.query(customer).filter_by(email=email).first()
	if not customer or not customer.verify_password(password):
		return False
	return True

	
	

@app.route('/logout', methods = ['POST'])
def logout():
	if 'id' not in login_session:
		flash("You must be logged in order to log out")
		return redirect(url_for('login'))
	del login_session['name']
	del login_session['email']
	del login_session['id']
	flash("Logged Out Successfully")
	return redirect(url_for('mianpage'))


@app.route("/song/<int:song_id>/addtoplaylist", methods =['POST'])
def addtoplaylist(song_id):
	song = session.query(song).filter_by(id=song_id).one()
	Playlist = session.query(Playlist).filter_by(user_id=login_session['id']).one()
	if song not in Playlist.songs:
		a = SongPlaylistAssociation(song=song)
		Playlist.song.append(a)
		session.add_all([a, song, playlist])
		session.commit()
		flash("Successfully added to playlist")
		return redirect(url_for('playlist'))
	else:
		flash("This song is already in your playlist")
		return redirect(url_for('playlist'))

	return "To be implemented"

@app.route('/playlist')
def playlist():
	return "To be implemented"

@app.route("/removefromplaylist/<int:song_id>", methods = ['POST'])
def removefromplaylist(song_id):
	return "To be implemented"

@app.route('/makenewplaylist', methods = ['GET','POST'])
def makenewplaylist():
	if request.method == 'POST':
		newplaylist = Playlist(name= name, user= user_id, )
		session.add(newplaylist)
		session.commit()
	else:
		return render_template('playlist.html')	
		


if __name__ == '__main__':
    app.debug = True
    app.run(port=8080)







		


