from connection.database import db

class AnswerKey(db.Model):
    __tablename__ = "answers_key"

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, unique=True)
    correct_letter = db.Column(db.String(1), nullable=False)