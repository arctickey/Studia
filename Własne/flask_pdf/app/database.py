from app import db



class FileContent(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    content = db.Column(db.LargeBinary)

    def __repr__(self):
        return '<User {}>'.format(self.name)