from flask import Flask,render_template
'''
Create Instance of Flask Class which will
be your Web server Gateway interface application
'''
#WSGI APPLICTION
app=Flask(__name__)
@app.route("/")
def welcome():
    return "<html><h1>Pankaj</h1></html>"

@app.route("/contact")
def contact():
    return render_template("index.html")
# debug=True works like nodemon
if __name__ == "__main__":
    app.run(debug=True)