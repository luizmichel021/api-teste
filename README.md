📝 API de Questionário

Protótipo de API para gerenciamento de questionários, desenvolvido para um projeto social na comunidade da Rocinha - RJ.





🚀 Tecnologias Utilizadas
Python → Linguagem principal utilizada no desenvolvimento.

FastAPI → Framework web moderno e de alto desempenho.

Uvicorn → Servidor ASGI leve e rápido para rodar a aplicação.

📂 Estrutura do Projeto
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
(Opcional) Crie um ambiente virtual:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
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

Swagger UI

Redoc

✅ Funcionalidades
Criação de questionários → Permite criar novos questionários com perguntas e opções de resposta.

Gerenciamento → Edição e exclusão de questionários existentes.

Respostas → Submissão de respostas pelos usuários.

Visualização de resultados → Acesso às respostas coletadas para análise.

🤝 Contribuição
Contribuições são muito bem-vindas!
Sinta-se à vontade para abrir issues ou pull requests com sugestões de melhorias ou correções.

🎯 Sobre o projeto
Este projeto foi desenvolvido como parte das atividades de extensão universitária do curso de Engenharia de Software, com foco em aplicação prática para apoiar projetos sociais.
