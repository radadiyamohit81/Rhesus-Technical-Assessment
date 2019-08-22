from flask import Flask, render_template, request
from flask import MySQL
import yaml

app = Flask(__name__)

db=yaml.load(open('db.yaml'))
app.configure['MYSQL_HOST'] = db['mysql_host']
app.configure['MYSQL_USER'] = db['mysql_user']
app.configure['MYSQL_PASSWORD'] = db['mysql_password']
app.configure['MYSQL_DB'] = db['mysql_db']

mysql =MySQL(app)

@app.route('/', method=['GET','POST'])
def hello_world():
	if request.method == 'POST':
		detail = request.form
		comment = detail['comment']
		cur =mysql.connection.cursor()
		cur.execute("INSERT INTO user(comment) VALUES(%s)",(comment))
		mysql.connection.commit()
		cur.close()
		return 'success'
	return render_template('hello_world.html')
if __name__ == '__main__':
   app.run(debug = True)