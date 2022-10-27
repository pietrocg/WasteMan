from flask import Flask, request, render_template, session, redirect, jsonify
import DBcalls as DB
from base64 import b64encode
from flask_login import LoginManager
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])

def display_report():
    return render_template('Submit-a-Report.html')


@app.route("/submit", methods=['POST', 'GET'])

def report_submission():
    #if not session.get('logged_in'):
    #    return render_template('login.html')

    if request.method == 'POST':
        #image_1 = request.files.get('camera--output') this was for the piece of code that opened the HTML camera, but it is redundant for mobile devices
        #if image_1 == None:
        user_ID = '2435'
        image = request.files.get('camera_upload')
        message = request.form.get('report_text')
        longitude = request.form.get('longitude')
        latitude = request.form.get('latitude')
        image = b64encode(image.read())
        report = {'user_id': user_ID, 'latitude' : latitude,'longitude': longitude,'image': image, 'text': message, 'collected': False}
        config = DB.fetch_config()
        DB.write_report(report, config)
        return render_template('Report_Submission.html')

@app.route("/Account", methods=['GET'])

def account():
    return render_template('Account.html')

@app.route("/Reports", methods=['GET'])

def reports():
    config = DB.fetch_config()
    reports = DB.fetch_reports(config)
    r = []
    for i in reports:
        b = []
        b.append(i[0])
        b.append(i[2])
        b.append(float(i[3]))
        b.append(float(i[4]))
        b.append("No" if i[7]==0 else "Yes")
        r.append(b)
    return render_template('Reports.html', data=r)

@app.route("/Login", methods=['POST', 'GET'])

def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        Flask.flash('wrong password!')
    return report_submission()
    return render_template('Login.html')

@app.route("/Login_Success")

def success():
    return render_template('Login_Success.html')

@app.route('/login', methods=['POST'])


@app.route("/Logout")
def logout():
    session['logged_in'] = False
    return report_submission()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))