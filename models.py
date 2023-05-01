class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    display_name = db.Column(db.String(20), nullable=False)
    avatar = db.Column(db.String(50), nullable=False, default='default.png')
    wins = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"User('{self.username}', '{self.display_name}', '{self.avatar}', '{self.wins}')"
