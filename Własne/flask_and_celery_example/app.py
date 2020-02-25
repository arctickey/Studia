from flask import Flask,render_template,request,session,flash
from flask_mail import Message
from celery import Celery
import os


app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = "chrzuszcz67@gmail.com"
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'flask@example.com'

celery = Celery(app.name,broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task
def send_async_email(email_data):
        msg = Message(subject=email_data['subject'], recipients=email_data['to'],
                      body=email_data['body'], sender=app.config['MAIL_DEFAULT_SENDER'])
        with app.app_context():
            msg.send()



@app.route("/",methods=['GET','POST'])
def index():
    if request.method == "GET":
        return render_template("index.html",email=session.get('email', ''))
    email = request.form['email']
    session['email'] = email
    email_data = {
        'subject': 'Hello from Flask',
        'to': email,
        'body': 'This is a test email sent from a background Celery task.'
    }
    if request.form['submit']=="Send":
        send_async_email.delay(email_data)
        flash(f"Sending emial to {email}")
    else:
        send_async_email.apply_async(args=[email_data],countdown=60)

if __name__ =="__main__":
    app.run()