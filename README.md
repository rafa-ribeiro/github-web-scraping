**GitHub Web Scraping**

Projeto para extração de dados de repositórios públicos contidos no GitHub.
O código se utiliza de técnicas de web scraping para efetuar a extração de dados de páginas html dos projetos do GitHub.

*Até o momentoo projeto efetua a extração dos seguintes dados:*
1. Estrutura de pastas e arquivos.
2. Quantidade de linhas dos arquivos.
3. Volume em Bytes dos arquivos.


*Autor: Rafael Ribeiro*

---

**Principais tecnologias e bibliotecas utilizadas**

1. Python 3.7 - (3.7.0)
2. Pipenv (version 2018.05.18)
3. Virtualenv (16.7.2)
4. Beautifulsoup4 (4.8.0)
5. Anytree (2.6.0)
6. 

---

**Funcionalidades**

1. Cadastro de tarefas;
2. Atualização de nome e descriçao das tarefas;
3. Atualização de status (pending/completed) das tarefas;
4. Exclusão de tarefas;
5. Consulta de todas as tarefas e suas respectivas informações;
6. Consulta do estado da API e suas dependências;
7. Consulta de métricas da API.

---

**Como executar/utilizar**

Repositório: git@github.com:wrmaga/todolist.git ou https://github.com/wrmaga/todolist.git

1. Gerando e executando jar file (a partir do diretório raiz do projeto):
    - Executar o comando "mvn clean install -DskipTests";
    - Executar o comando "java -jar target/todolist.artifact-1.0.0.jar".
2. Gerando e executando docker container (a partir do diretório raiz do projeto):
    - Executar o comando "mvn clean install -DskipTests -Pdocker";
    - A imagem será gerada com repository williamrmagalhaes/todolist e tag 1.0.0;
    - Executar o comando "docker run -it -p8787:8787 <ID_DA_IMAGEM_GERADA>".
3. Executando docker container:
    - Executar o comando "docker pull williamrmagalhaes/todolist:1.0.0";
    - Executar o comando "docker run -it -p8787:8787 <ID_DA_IMAGEM_BAIXADA>".
    
---

**Endpoints**

1. Para cadastrar uma tarefa (/todo/create):
    - Exemplo de model a ser utilizado no body da requisição:
        - *{
              "name":"Name",
              "description":"Description"
           }*
    - Exemplo de requisição via curl:
        - curl -d '{"name":"Name Curl","description":"Description Curl"}' -H "Content-Type: application/json" -X POST http://localhost:8787/todo/create

2. Para atualizar uma tarefa (/todo/update):
    - Exemplo de model a ser utilizado no body da requisição:
        - *{
             "id":"1",
             "name":"Novo Nome",
             "description":"Nova Descrição"
           }*
    - Exemplo de requisição via curl:
        - curl -d '{"id":"1","name":"Name Curl","description":"Description Curl"}' -H "Content-Type: application/json" -X POST http://localhost:8787/todo/update

3. Para finalizar uma tarefa (/todo/complete):
    - Exemplo de requisição:
        - *http://localhost:8787/todo/complete?taskID=1*
    - Exemplo de requisição via curl:
        - curl -X POST http://localhost:8787/todo/complete?taskID=1

4. Para excluir uma tarefa (/todo/delete):
    - Exemplo de requisição:
        - *http://localhost:8787/todo/delete?taskID=1*
    - Exemplo de requisição via curl:
        - curl -X DELETE http://localhost:8787/todo/delete?taskID=1

5. Para listar todas as tarefas (/todo/todo):
    - Exemplo de requisição:
        - *http://localhost:8787/todo/todo*
    - Exemplo de requisição via curl:
        - curl -X GET http://localhost:8787/todo/todo

6. Para validar o funcionamento da API e seus componentes (/todo/healthcheck):
    - Exemplo de requisição:
        - *http://localhost:8787/todo/healthcheck*
    - Exemplo de requisição via curl:
        - curl -X GET http://localhost:8787/todo/healthcheck

7. Para obter as métricas da API (/todo/metrics):
    - Exemplo de requisição:
        - *http://localhost:8787/todo/metrics*
    - Exemplo de requisição via curl:
        - curl -X GET http://localhost:8787/todo/metrics

---

**Observações**

Ao executar a aplicação, a base inicial com alguns registros já é carregada em memória.