from music_main import db, login_manager
from flask_login import UserMixin

# database settings

# reload information to get user who just registered
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# User table
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    input = db.relationship("Input", backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username}')"


# User input texts table
class Input(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # User was auto set to lowercase, so user.id
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    text_sum = db.Column(db.JSON, nullable=False)
    lyrics_id = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return f"Input('{self.title}')"


## music lyrics table
class Lyrics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song = db.Column(db.String(100), nullable=False)
    song_author = db.Column(db.String(100), nullable=False)
    song_lyrics = db.Column(db.Text, nullable=False)
    lyrics_sum = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return f"Lyrics('{self.song}','{self.song_author}')"
