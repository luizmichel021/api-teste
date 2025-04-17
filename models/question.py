from connection.database import db

class Question(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    category = db.Column(db.Text, nullable=False)

    answers = db.relationship("models.answers.Answer", backref="question", cascade="all, delete-orphan", lazy=True)
    answer_key = db.relationship("models.answers_key.AnswerKey", backref="question", uselist=False, cascade="all, delete-orphan", lazy=True)
