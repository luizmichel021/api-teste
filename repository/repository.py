from models import question, answers, answers_key
from connection import db
from sqlalchemy.exc import SQLAlchemyError
from enum import Enum

class Respository:

    def set_question(text: str, category: Enum):
        try:     
            new_question = question(text=text, category=category.value)

            db.session.add(new_question)
            db.session.commit()

            return{"status": "success" , "message" : "[Repository] - Pergunta Cadastrada."}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"status": "error" , "message": str(e)}
        
    