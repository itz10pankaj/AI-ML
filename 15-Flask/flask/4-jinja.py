from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<h1>Home</h1>"


@app.route("/index",methods=['GET'])
def index_page():
    return render_template("index.html")

# I i donot write action in form then it will hit above form yroute on subm,it
@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        print(f"submit Name: {name}") 
        print(f"submit Email: {email}")
        print(f"submit Message: {message}")
        return f"{name}"
    else :
        render_template("form.js")



# Variable Rule
@app.route("/success/<score>")
def success(score):
    return f"The Marks is {score}"

# Variable Rule
# @app.route("/int-success/<int:score>")
# def Intsuccess(score):
#     return f"The Marks is"+str(score)

'''
Jinja2 Templates methods

{{}}----- For Variables
{%...%}-------condition for loops
{#...#}-------this is for comments

'''
@app.route("/int-success/<int:score>")
def Intsuccess(score):
    if score>50:
        res="Pass"
    else:
        res="Fail"
    return render_template("result.html",cate=res)


@app.route("/successres/<int:score>")
def successRes(score):
    if score>50:
        res="Pass"
    else:
        res="Fail"
    exp={'score':score,'res':res}
    return render_template("result2.html",exp=exp)

@app.route("/fail/<int:score>")
def fail(score):

    return render_template('result.html',result=score)

@app.route("/getresult",methods=['GET','POST'])
def getresult():
    if request.method=='POST':
        sub1=request.form.get('subject1')
        sub2=request.form.get('subject2')
        avg=(int(sub1)+int(sub2))/2
        return redirect(url_for('Intsuccess',score=int(avg)))
    else:
       return render_template('gteresult.html')



if __name__ == "__main__":
    app.run(debug=True)