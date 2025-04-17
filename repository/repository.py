from models.question import Question
from models.answers import Answer
from models.answers_key import AnswerKey
from connection.database import db
from sqlalchemy.exc import SQLAlchemyError
from enums.category import Category
from sqlalchemy import func

class Repository:

    def set_question(text: str, category: Category):
        try:     
            new_question = Question(text=text, category=category.value)

            db.session.add(new_question)
            db.session.commit()

            return {
                "status": "success",
                "message": "[Repository] - Pergunta cadastrada.",
                "id": new_question.id
            }
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"status": "error" , "message": str(e)}
        
    def set_answers(question_id: int, answers_list: list[dict]):
        try:
            for answers in answers_list:
                letter = answers["letter"].upper()
                text = answers["text"]

                new_response = Answer(
                    question_id=question_id,
                    letter=letter,
                    text=text
                )
                db.session.add(new_response)
            db.session.commit()
            return {"status": "success", "message": "[Repository] - Respostas adicionadas."}

        except SQLAlchemyError as e:
            db.session.rollback()
            return {"status": "error", "message": str(e)} 

    def set_answerkey(question_id: int, letter: str):
        try:
            new_key = AnswerKey(question_id=question_id,correct_letter=letter.upper())
            db.session.add(new_key)
            db.session.commit()

            return {"status" : "success" , "message": "[Repository] - Letra do Gabarito registrada."}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"status": "error", "message": str(e)} 

    def get_random_questions_and_answers(category: Category, limit: int = 5):
        try:
            questions = Question.query.filter_by(category=category.value).order_by(func.random()).limit(limit).all()
            result = []
            for question in questions:
                alternatives = Answer.query.filter_by(question_id=question.id).all()
                alternatives_format = {
                    alt.letter.upper(): alt.text for alt in alternatives
                }

                result.append({
                    "Question" : question.text,
                    "Alternatives": alternatives_format
                })
            return {"status" : "success", "dados" : result} 
        except SQLAlchemyError as e:
            return {"status": "error", "message": str(e)}     

    def test_corrector(answers_student: list[dict]):
        try:
            total = len(answers_student)
            hits = 0
            detailed_result = []

            for response in answers_student:
                question_id = response["question_id"]
                answer_student = response["response"].upper()

                answer_key = AnswerKey.query.filter_by(question_id=question_id).first()

                if answer_key:
                    correct = answer_key.correct_letter.upper()
                    hit = correct == answer_student

                    if hit:
                        hits += 1

                    detailed_result.append({
                        "question_id": question_id,
                        "answer_student": answer_student,
                        "answer_correct": correct,
                        "hit": hit
                    })
                else:
                    detailed_result.append({
                        "question_id": question_id,
                        "answer_student": answer_student,
                        "answer_correct": None,
                        "hit": False,
                        "error": "Answer key not found"
                    })

            return {
                "status": "success",
                "total_questions": total,
                "hits": hits,
                "percentage": round((hits / total) * 100, 2) if total > 0 else 0,
                "answers": detailed_result
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}    
                 
                