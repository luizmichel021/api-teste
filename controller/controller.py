from flask import request, jsonify
from enums.category import Category
from service.service import Service
from connection.database import db 
from flask import Response
import json

class TestController:
    def __init__(self, app):

        
        @app.route("/test/<string:category_name>", methods=["GET"])
        def get_questions(category_name):
            try:
                category = Category[category_name.upper()]  # Acessa pelo nome da Enum
            except KeyError:
                return {"error": "Categoria inválida"}, 400
            data = Service.get_question(category)
            
            json_response = json.dumps(data, indent=2, ensure_ascii=False)
            return Response(json_response, mimetype="application/json")
        
        
        @app.route("/test/<string:category_name>", methods=["POST"])
        def set_questions(category_name):
            try:
                category_name = Category[category_name.upper()]
            except KeyError:
                return {"error": "Categoria inválida"}, 400
                
            data = request.get_json()

            if not data:
                return jsonify({"error": "Corpo da requisição vazio ou inválido"}), 400

            text = data.get("text")
            answers_list = data.get("answers_list")
            correct_letter = data.get("correct_letter")

                
            if not all([text, answers_list, correct_letter]):
                return jsonify({"error": "Campos obrigatórios faltando"}), 400

                
            Service.set_total_question(text, category_name, answers_list, correct_letter)
            return jsonify({"status": "success", "message": "Questão registrada com sucesso!"}), 201
        
        @app.route("/test/corrector", methods=["POST"])
        def corrector():
            data = request.get_json()

            response = Service.test_corrector(data)
            return jsonify(response)