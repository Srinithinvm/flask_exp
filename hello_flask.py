from flask import Flask,render_template,redirect,request
import datetime,sqlite3
app = Flask(__name__)

insertQuery='INSERT INTO datas(name,password,gender) VALUES("%s","%s","%s")'
fetchQuery='SELECT * from datas'

@app.route("/")
def index():
    return "Flask Working fine -- Srinithin"
@app.route("/login")


def template():
    return render_template("index.html")
@app.route("/pageone")


def pageone():
    return render_template("firstpage.html")
@app.route("/pagetwo")


def pagetwo():
    return render_template("secondpage.html")
@app.route("/frontpage")


def frontpage():
    return render_template("frontpage.html")
@app.route("/resultpage")


def resultpage():
    return render_template("resultpage.html")
@app.route("/printtime")


def printtime():
    print()
    print(datetime.datetime.now())
    print()
    return redirect("/resultpage")
   
@app.route("/dashboard")
def dashboard():
    name="Srinithin"
    notification=5
    mail=8

@app.route("/inputpage")
def inputpage():
    return render_template("inputpage.html")
   
   
@app.route("/statuspage",methods=["post"])
def statuspage():
    status=request.form.get("textinput")
   
    return render_template("statuspage.html",status=status)
    
@app.route("/templateworks")
def templateworks():
    pythondata = ['anand','ruban','srinithin','prasanth']
    return render_template("templateworks.html",data = pythondata)
    

@app.route("/testpage")
def testpage():
    return render_template("testpage.html")
    
@app.route("/testpage2",methods=["post"])
def testpage2():
    name=request.form.get("textinput1")
    password=request.form.get("textinput2")
    gender=request.form.get("textinput3")
    con=sqlite3.connect("database.db")
    c=con.cursor()
    c.execute(insertQuery%(name,password,gender))
    con.commit()
    con.close()
    return render_template("testpage2.html",name=name,password=password,gender=gender)

  
def Create_table():
    createQuery="""
                    CREATE TABLE IF NOT EXISTS datas(
                        pid INTEGER PRIMARY KEY,
                        Name TEXT  NOT NULL,
                        Password TEXT NOT NULL,
                        Gender TEXT NOT NULL
                        )
                    """
    con=sqlite3.connect("database.db")
    c=con.cursor()
    c.execute(createQuery)
    con.commit()
    con.close()
@app.route("/view")
def Fetch_all():
    con=sqlite3.connect("database.db")
    c=con.cursor()
    c.execute(fetchQuery)
    receivedData=c.fetchall()
    return render_template("view.html",results=receivedData)

        

       
if __name__ == "__main__":

    Create_table()
    
    app.run(host="0.0.0.0",debug=True)