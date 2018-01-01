from flask import Flask, render_template, request
from flaskext.mysql import MySQL
 
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'redhat'
app.config['MYSQL_DATABASE_DB'] = 'dbv1'
app.config['MYSQL_DATABASE_HOST'] = '192.168.124.140:3306'
mysql.init_app(app)
app = Flask(__name__)

@app.route('/')
def render():
	return render_template('index.html')

if __name__=='__main__':
	app.run(host='0.0.0.0', debug=True, port=8080)
