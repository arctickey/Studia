from flask import render_template,request,redirect,url_for,flash
from app.actions import allowed_file,add,task

from app import app



@app.route('/',methods=["GET","POST"])
@app.route("/index",methods=["GET","POST"])
def index():
    if request.method =="GET":
        return render_template('index.html')
    file = request.files['data_file']
    if file and allowed_file(file.filename):
        add(file)
        file.filename = file.filename.split(".",maxsplit=1)[0] +".pdf"
    else:
        flash("Bad file")
        return redirect(url_for("index"))
    return task(file)


