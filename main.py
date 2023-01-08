from flask_mysqldb import MySQL
from flask import Flask, request,render_template,redirect,url_for


app = Flask(__name__)

# Configuration
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'Arohit621587'
MYSQL_DB = 'taskmng'

app.config['MYSQL_USER'] = MYSQL_USER
app.config['MYSQL_PASSWORD'] = MYSQL_PASSWORD
app.config['MYSQL_HOST'] = MYSQL_HOST
app.config['MYSQL_DB'] = MYSQL_DB
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL()
# Initialize the extension
mysql.init_app(app)

import routes.employee

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")
@app.route("/project",methods=["GET","POST"])
def project():
    cur = mysql.connection.cursor()
    if request.method == "POST":
        name = request.form.get("name")
        status = request.form.get("status")
        desc = request.form.get("desc")
        cur.execute("INSERT INTO project (p_name,p_status,p_desc) VALUES (%s,%s,%s)",(name,status,desc))
        mysql.connection.commit()
        return redirect(url_for("home"))
    return render_template("project.html")
@app.route("/admin",methods=["GET","POST"])
def admin():
    cur = mysql.connection.cursor()
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        a_status = request.form.get("status")
        cur.execute("INSERT INTO project (admin_name,admin_email,admin_status) VALUES (%s,%s,%s)",(name,email,a_status))
        mysql.connection.commit()
        return redirect(url_for("home"))
    return render_template("admin.html")


if __name__ == '__main__':
    app.run(debug=True)
