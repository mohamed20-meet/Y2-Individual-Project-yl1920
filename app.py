from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


##### Code here ######

@app.route('/')
def home():
	return render_template("home.html")


@app.route('/Admin' , methods=['GET' , 'POST'])
def Admin():
    if request.method == 'GET':
        return render_template('Admin.html')
    else:
        name = request.form['uname']
        password = request.form['psw']
        if name == "shawrma12" and password == "1234":
        	return render_template('edit.html')
        	
        else:
        	return redirect('/')


@app.route('/Esports')
def Esports():
	if not 'right team' in login_session:
		login_session['right team'] = "Faze"
	if not 'left team' in login_session:
		login_session['left team'] = "liq"
	right = login_session['right team']
	left = login_session['left team']
	return render_template(
		"Esports.html", right =right , left=left)

@app.route("/edit" , methods =['GET' , 'POST'])
def Edit():
	if request.method == 'GET':
		return render_template("edit.html")
	else:
		login_session['left team'] = request.form["Team1"]
		login_session['right team'] = request.form["Team2"]
		print(login_session['right team'])
		return render_template("edit.html")



if __name__ == '__main__':
    app.run(debug=True)