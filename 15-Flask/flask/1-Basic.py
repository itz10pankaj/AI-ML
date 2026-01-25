from flask import Flask
'''
Create Instance of Flask Class which will
be your Web server Gateway interface application
'''
#WSGI APPLICTION
app=Flask(__name__)
@app.route("/")
def welcome():
    return "Welcome to home pagess. This should be trieal"

@app.route("/contact")
def contact():
    return "Welcome to contact pagess. This should be trieal"
# debug=True works like nodemon
if __name__ == "__main__":
    app.run(debug=True)