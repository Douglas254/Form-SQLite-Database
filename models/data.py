from app import db

class userdata(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    Username = db.Column(db.String(32),nullable=True)
    Password = db.Column(db.String(32),nullable=True)

    def saveinfo(self):
        db.session.add(self)
        db.session.commit()