API de Questionário
Este projeto é um protótipo de uma API de questionário, desenvolvido como parte de um projeto social na comunidade da Rocinha, no Rio de Janeiro. A API foi criada com o objetivo de facilitar a criação, gerenciamento e resposta a questionários, auxiliando iniciativas sociais na coleta de informações de forma estruturada.

🚀 Tecnologias Utilizadas
Python: Linguagem de programação principal utilizada no desenvolvimento da API.

FastAPI: Framework web moderno e de alto desempenho para a construção da API.

Uvicorn: Servidor ASGI leve e rápido para rodar a aplicação FastAPI.

📂 Estrutura do Projeto
O projeto está organizado da seguinte forma:

bash
Copiar
Editar
api-teste/
├── app.py                 # Arquivo principal que inicia a aplicação
├── config/                # Configurações da aplicação
├── connection/            # Configuração de conexão com o banco de dados
├── enums/                 # Definições de enums utilizados na aplicação
├── models/                # Modelos de dados (ORM)
├── repository/            # Lógica de acesso aos dados
├── test-manual.py         # Script para testes manuais da API
├── requirements.txt       # Lista de dependências do projeto
└── .gitignore             # Arquivos e pastas ignorados pelo Git
⚙️ Como Executar
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/luizmichel021/api-teste.git
cd api-teste
Crie um ambiente virtual (opcional, mas recomendado):

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # No Linux/Mac
venv\Scripts\activate     # No Windows
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Execute a aplicação:

bash
Copiar
Editar
uvicorn app:app --reload
Acesse a documentação interativa:

Swagger UI: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc

📝 Funcionalidades
Criação de questionários: Permite a criação de novos questionários com perguntas e opções de resposta.

Gerenciamento de questionários: Edição e exclusão de questionários existentes.

Respostas aos questionários: Submissão de respostas pelos usuários.

Visualização de resultados: Acesso às respostas coletadas para análise.

🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com sugestões de melhorias ou correções.

📄 Licença
Este projeto está licenciado sob a licença MIT.
