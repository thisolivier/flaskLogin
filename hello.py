import os
from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

@app.route("/")
def home():
  if not session.get('logged_in'):
    print('++++++++    let us log you in')
    return render_template('login.html')
  else:
    print('++++++++   about to return')
    return "Woo, hello!"

@app.route('/login', methods=['POST'])
def login_admin():
  if request.form['password'] == 'test' and request.form["username"] == 'admin':
    session['logged_in'] = True
  else:
    flash('wrong_password')
  return home()

@app.route('/logout')
def logout():
  session['logged_in'] = False
  return home()

if __name__ == "__main__":
  app.secret_key = os.urandom(12)
  app.run(host='0.0.0.0', port=4000, debug=True)