from flask import Flask, render_template, request, jsonify, redirect, url_for, abort
from flaskext.mysql import MySQL

app = Flask(__name__)

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


@app.route('/login', methods=['POST'])
def login():
	if request.method == 'POST':
		login_data = request.form
		
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("select * from Users where username='{}'".format(login_data['user_name']))
		query_result = cursor.fetchone()
		if query_result is None:						
			# incorrect username but print incorrect username or passowor for security reasons
			return render_template('index.html',msg_code=3)
		elif query_result[3] == login_data['password']: # correct password
			return render_template('notes_page.html', user_info=query_result)




@app.route('/registration', methods=['POST'])
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
			cursor.execute("insert into Users(username, first_name, last_name, passwd) values ('{}','{}','{}','{}')".format(registration_data['user_name'],registration_data['first_name'],registration_data['last_name'], registration_data['password']))
			conn.commit()
			
			return render_template('index.html',msg_code=1)
		else:
			return render_template('index.html',msg_code=2)#"Username already taken.<br>Please try different one")


if __name__ == '__main__':
	app.run(debug=True)
