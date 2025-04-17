from flask import Flask
from connection.database import db
from repository.repository import Repository
from enums.category import Category

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:123@localhost:5432/testebd'  # ou sua URI do Postgres
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()  # Cria as tabelas se não existirem

    # resultado = Repository.set_question(
    #     "teste",
    #     Category.PYTHON
    # )

    # print(resultado)

    # respostas = [
    # {"letter": "A", "text": "Brasília"},
    # {"letter": "B", "text": "Rio de Janeiro"},
    # {"letter": "C", "text": "São Paulo"},
    # {"letter": "D", "text": "Salvador"}
    # ]

    # resultado = Repository.set_answers(13, respostas)
    # print(resultado)

    # letter = "A"

    # resultado = Repository.set_answerkey(13,letter)
    # print(resultado)

    # resposta = Repository.get_random_questions_and_answers(Category.PYTHON)

    # if resposta.get("status") == "success":
    #     for item in resposta["dados"]:
    #         print(f"Question: {item['Question']}")
    #         for letra, texto in item["Alternatives"].items():
    #             print(f"  {letra}: {texto}")
    # else:
    #     print("Erro:", resposta.get("message", "Erro desconhecido"))

    # answers = [
    # {"question_id": 1, "response": "B"},
    # {"question_id": 2, "response": "C"},
    # {"question_id": 3, "response": "A"}
    # ]

    # result = Repository.test_corrector(answers)

    # if result["status"] == "success":
    #     print("Hits:", result["hits"])
    #     print("Percentage:", result["percentage"], "%")

    #     for r in result["answers"]:
    #         print(f"Question {r['question_id']} - {'✅' if r['hit'] else '❌'} "
    #             f"(Correct: {r['answer_correct']}, Your answer: {r['answer_student']})")
    # else:
    #     print("Error:", result.get("message", "Unknown error"))