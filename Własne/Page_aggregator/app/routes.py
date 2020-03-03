from app import app,db,fetcher
from flask import render_template
from app.models import Content




@app.route('/')
@app.route('/index')
def index():
    db.session.query(Content).delete()
    fetcher.helper()
    content = Content.query.all()
    return render_template('index.html',content = content)

