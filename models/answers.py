from connection.database import db

class Answer(db.Model):
    __tablename__ = "answers"

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id", ondelete="CASCADE"), nullable=False)
    letter = db.Column(db.String(1), nullable=False)
    text = db.Column(db.Text, nullable=False)
