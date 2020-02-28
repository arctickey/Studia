from app import app,celery,db
from app.database import FileContent
from flask_weasyprint import render_pdf,HTML

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']




def task(file):
    pdf = render_pdf(HTML(string=file))
    return pdf


def add(file):
    file_content = FileContent(name=file.filename, content=file)
    db.session.add(file_content)
    db.session.commit()





