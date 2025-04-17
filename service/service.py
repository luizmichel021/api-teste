import logging
from enums.category import Category
from repository.repository import Repository

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Service:

    def set_total_question(text: str, category: Category, answers_list: list[dict], correct_letter: str):
        try:
            logging.info("incizalizando set question.")
            response_id = Repository.set_question(text,category)

            if(response_id):
                logging.debug("o metodo de inserir questão retornou o id corretamente")
                logging.debug("inciando inserção das respostas.")
                Repository.set_answers(response_id,answers_list)
                Repository.set_answerkey(response_id,correct_letter)
            else:
                logging.debug("o metodo de inserção de questão não retornou o id corretamente.")
        except Exception as e:
                print("Ocorreu um erro:", str(e))        
                


    def get_question(category: Category):
        try:
            logging.info("inicializando get question")
            data = Repository.get_random_questions_and_answers(category)
            return data
        except Exception as e:
            print("Ocorreu um erro:", str(e))        
                
    
    def test_corrector(answers_student: list[dict]):
        try:
            logging.info("inicializando answers_student")
            data = Repository.test_corrector(answers_student)
            return data
        except Exception as e:
            print("Ocorreu um erro:", str(e))
