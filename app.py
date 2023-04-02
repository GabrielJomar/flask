from flask import Flask, request, render_template,redirect,url_for,session 
from sql_it import sqlsignup  
from sql_it import sqllogin  
from cartoonifier_it import model

from ml_it import ml
app=Flask(__name__)

#@app.route("/")
#def main():
#    return render_template("index.html")




@app.route('/', methods =["GET", "POST"])
def home():
    return render_template("index.html")

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       email = request.form.get("email")
       # getting input with name = lname in HTML form
       password = request.form.get("password")
       #print(email,password)
       if sqllogin(email,password)=='found':
           return redirect(url_for("inp"))  
       
        
      
       elif sqllogin(email,password)=='nouser':
           return redirect(url_for("invaliduser"))         
       elif sqllogin(email,password)=='wrongpass':
           return redirect(url_for("incorrect"))
           
       #return redirect(url_for("home"))
        
@app.route('/signup', methods=["GET","POST"])
def signup():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       username = request.form.get("username")
       email = request.form.get("email")
       # getting input with name = lname in HTML form
       password = request.form.get("password")
       print(username,email,password)
       sqlsignup(username,email,password)
           #return redirect(url_for("model"))
       return redirect(url_for("home"))




@app.route("/invalid",methods=['GET'])
def invaliduser():
    return "<h1>User doesnt exist.</h1>" 


@app.route("/incorrect",methods=['GET'])
def invalid():
    return "<h1>Incorrect Password.</h1>"


@app.route('/', methods =["GET", "POST"])
def res():
    return render_template("result.html")

@app.route('/action_page.php', methods =["GET", "POST"])
def inp():    
    if request.method == "POST":
       miles = request.form.get("mile")
       ml(miles)

    
'''@app.route("/model",methods=['GET'])
def modelpage():
    model()
 '''   
    

if __name__=='__main__':
    app.run()
