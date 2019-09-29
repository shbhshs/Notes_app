from flask import Flask, render_template, request, jsonify
from flask import redirect, url_for, abort, session, g
from flaskext.mysql import MySQL
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

#database configuration
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'albanero'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		print('POST')
		login_data = request.form
		
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("select * from Users where username='{}'".format(login_data['user_name']))
		query_result = cursor.fetchone()

		if query_result is None or query_result[3] != login_data['password']:						
			# incorrect username but print incorrect username or passowor for security reasons
			return render_template('index.html',msg_code=3)
		elif query_result[3] == login_data['password']: # correct password
			session['user'] = login_data['user_name']
			return redirect(url_for('notes'))
	
	if request.method == 'GET':
		print('GET')
		if g.user:
			return redirect(url_for('notes'))
		else:
			return redirect(url_for('index'))



@app.route('/registration', methods=['GET','POST'])
def registration():
	if request.method == 'POST':
		registration_data = request.form

		conn = mysql.connect()
		cursor = conn.cursor()
		
		# check for duplicate username
		cursor.execute("select * from Users where username='{}'".format(registration_data['user_name']))
		query_result = cursor.fetchone()

		# insert data
		if query_result is None:
			cursor.execute("insert into Users(username, first_name, last_name, passwd) values ('{}','{}','{}','{}')"	\
							.format(registration_data['user_name'],				\
									registration_data['first_name'],			\
									registration_data['last_name'], 			\
									registration_data['password']))			
			conn.commit()
			
			return render_template('index.html',msg_code=1)
		else:
			return render_template('index.html',msg_code=2)
	
	return redirect(url_for('index'))


@app.before_request
def before_request():
	g.user = None
	if 'user' in session:
		g.user = session['user']
		print('before user:',g.user)


@app.route('/notes')
def notes():
	if g.user:
		conn = mysql.connect()
		cursor = conn.cursor()
		
		cursor.execute('select * from Notes where creator="{}"'.format(g.user))
		query_result = cursor.fetchall()

		return render_template('notes_page.html', notes_data = query_result)
	else:
		return redirect(url_for('index'))


@app.route('/note/create', methods=['POST'])
def note_create():
	if g.user:
		note_data = request.form

		conn = mysql.connect()
		cursor = conn.cursor()

		cursor.execute('INSERT INTO Notes (title, notes, creator, deleted) VALUES("{}", "{}", "{}","{}")'	\
						.format(note_data['note_title'], 		\
								note_data['note_text'], 		\
								g.user, 						\
								'0'))
		conn.commit()
		cursor.close()

		return redirect(url_for('notes'))
	
	else:
		return redirect(url_for('index'))


@app.route('/note/discard', methods=['POST'])
def note_discard():
	if g.user:
		return redirect(url_for('notes'))
	else:
		return redirect(url_for('index'))


@app.route('/note/save', methods=['POST'])
def note_save():
	if g.user:

		notes_data = request.form

		conn = mysql.connect()
		cursor = conn.cursor()
		
		cursor.execute('update Notes set notes = "{}" where id = "{}"'		\
						.format(notes_data['note_text'], 	\
								notes_data['Id']))
		conn.commit()
		
		return redirect(url_for('notes'))
	
	else:
		return redirect(url_for('index'))

@app.route('/note/delete', methods=['POST'])
def note_delete():
	if g.user:
		notes_data = request.form

		conn = mysql.connect()
		cursor = conn.cursor()

		cursor.execute('update Notes set deleted="{}" where id ="{}"'.format(1, notes_data['Id']))
		conn.commit()
		
		return redirect(url_for('notes'))

	else:
		return redirect(url_for('index'))



@app.route('/trash/restore', methods=['POST'])
def trash_restore():
	if g.user:
		notes_data = request.form
		conn =  mysql.connect()
		cursor = conn.cursor()

		cursor.execute('update Notes set deleted="{}" where id="{}"'.format(0, notes_data['Id']))
		conn.commit()

		return redirect(url_for('notes'))

	else:
		return redirect(url_for('index'))

@app.route('/trash/delete', methods=['POST'])
def trash_delete():
	if g.user:
		notes_data =  request.form
	
		conn =  mysql.connect()
		cursor = conn.cursor()

		cursor.execute('delete from Notes where id="{}"'.format(notes_data['Id']))
		conn.commit()
		
		cursor.close()
		return redirect(url_for('notes'))

	else:
		return redirect(url_for('index'))
	


@app.route('/logout')
def logout():
	if g.user:
		session.clear()
		print('logout:', g.user)
		return render_template('index.html', msg_code=4)
	else:
		return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)
