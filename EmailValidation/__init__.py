from flask import Flask
from flask_mail import Mail, Message


app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '0dd8f4003018cc'
app.config['MAIL_PASSWORD'] = 'fd0d2cdac10725'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app=app)
