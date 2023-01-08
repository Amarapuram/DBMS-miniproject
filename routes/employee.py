from __main__ import app,mysql
from flask import  request,render_template,redirect,url_for


@app.route("/employee",methods=["GET"])
def employee():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employee")
    employees = cur.fetchall()
    return render_template("employees.html",employees=employees)

    
@app.route("/employee/add",methods=["GET","POST"])
def add_emp():
    cur = mysql.connection.cursor()
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        dept = request.form.get("dept")
        cur.execute("INSERT INTO employee (Empname,Empage,EmpDept) VALUES (%s,%s,%s)",(name,age,dept))
        mysql.connection.commit()
        return redirect(url_for("employee"))
    return render_template("emp.html")

@app.route("/employee/delete/<id>",methods=["GET"])
def delete_emp(id):
    cur = mysql.connection.cursor()
    cur.execute(f"DELETE from employee where idemployee ={id}")
    mysql.connection.commit()
    return redirect(url_for("employee"))