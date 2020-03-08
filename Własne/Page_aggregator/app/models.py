from app import db

class Content(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    page = db.Column(db.String(64))
    link = db.Column(db.String(256))
    title = db.Column(db.String(256))
    time = db.Column(db.DateTime)
    type = db.Column(db.String(32))

    def __repr__(self):
        return f'Title = {self.title}'

    def delete():
        db.session.query(Content).delete()
        db.session.commit()

