from app import mail,app
from flask_mail import Message
from app.modules import User
from flask import render_template
from threading import Thread

def send_async_mail(app,msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject,sender,recipient,body,html_body):
    msg = Message(subject,recipient,body,sender=sender,html = html_body)
    Thread(target=send_async_mail,args=(app,msg)).start()

def send_password_request_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
               sender=app.config['ADMINS'][0],
               recipient=[user.email],
               body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))