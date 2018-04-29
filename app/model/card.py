from app.database import db


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardname = db.Column(db.String)
    cmc = db.Column(db.Integer)
    colourIdentiy = db.Column(db.String)
    price = db.Column(db.Integer)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Card %r>' % self.cardname
