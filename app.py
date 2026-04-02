
from flask import Flask,render_template,request,redirect,session,send_file
import os,json,pandas as pd

from modules.processing import DataProcessor
from modules.serialization import save_data
from modules.threading_tasks import thread_task
from modules.multiprocessing_tasks import process_task
from modules.validation import *

app=Flask(__name__)
app.secret_key="secret"

UPLOAD="uploads"
os.makedirs(UPLOAD,exist_ok=True)

def load_json(f):
    with open(f) as fp: return json.load(fp)
def save_json(f,d):
    with open(f,"w") as fp: json.dump(d,fp,indent=4)

@app.route("/")
def home(): return redirect("/login")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        email=request.form["email"]
        password=request.form["password"]

        if not validate_email(email): return "Invalid Email"
        if not validate_password(password): return "Weak Password"

        for u in load_json("data/users.json"):
            if u["email"]==email and u["password"]==password:
                session["user"]=email
                return redirect("/dashboard")
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":

        # ✅ GET ALL VALUES FIRST
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")

        # ✅ VALIDATION
        if not validate_name(name):
            return "Invalid Name"

        if not validate_email(email):
            return "Invalid Email"

        if not validate_phone(phone):
            return "Invalid Phone"

        if not validate_password(password):
            return "Weak Password"

        # ✅ SAVE USER
        users = load_json("data/users.json")

        users.append({
            "name": name,
            "email": email,
            "phone": phone,
            "password": password
        })

        save_json("data/users.json", users)

        return redirect("/login")

    return render_template("signup.html")

@app.route("/dashboard",methods=["GET","POST"])
def dashboard():
    if "user" not in session: return redirect("/login")

    stats=None; preview=None

    if request.method=="POST":
        f=request.files["dataset"]
        path=os.path.join(UPLOAD,f.filename)
        f.save(path)

        p=DataProcessor(path)

        thread_task(p.load_data)
        process_task(p.compute)
        stats=p.compute()

        save_data({"user":session["user"],"stats":stats})
        preview=p.df.head().to_dict(orient="records")

    return render_template("dashboard.html",stats=stats,preview=preview)

@app.route("/download")
def download():
    data=load_json("data/datasets.json")
    df=pd.DataFrame(data)
    file="report.csv"
    df.to_csv(file,index=False)
    return send_file(file,as_attachment=True)

@app.route("/logout")
def logout():
    session.clear(); return redirect("/login")

if __name__=="__main__":
    app.run(debug=True)
