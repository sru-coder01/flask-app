from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
import smtplib
import requests
import os

#
# app = Flask(__name__)
#
# # Route to render the HTML form
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# # Route to handle form submission
# @app.route('/summarize', methods=['POST'])
# def summarize():
#     video_link = request.form['videoLink']
#
#     # Send the video link to your Colab backend
#     colab_url = 'https://your-colab-notebook-url'
#     response = requests.post(colab_url, json={'videoLink': video_link})
#
#     if response.status_code == 200:
#         result = response.json()
#         return render_template('summary.html', summary=result['summary'])
#     else:
#         return "Error in processing the video."
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template
OWN_EMAIL = os.environ.get('OWN_EMAIL')
OWN_PASSWORD = os.environ.get('OWN_PASSWORD')
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_key')
ckeditor = CKEditor(app)
Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True)

