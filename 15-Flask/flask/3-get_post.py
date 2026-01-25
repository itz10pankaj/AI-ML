from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<h1>Home</h1>"


@app.route("/index",methods=['GET'])
def index_page():
    return render_template("index.html")

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        print(f"Name: {name}") 
        print(f"Email: {email}")
        print(f"Message: {message}")
    return render_template('form.html')
# I i donot write action in form then it will hit above form yroute on subm,it
@app.route("/submit",methods=['POST'])
def submit():
    if request.method=='POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        print(f"submit Name: {name}") 
        print(f"submit Email: {email}")
        print(f"submit Message: {message}")
        return f"{name}"



if __name__ == "__main__":
    app.run(debug=True)