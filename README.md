### GitHub Web Scraping

Projeto para extração de dados de repositórios públicos contidos no GitHub.
O código se utiliza de técnicas de web scraping para efetuar a extração de dados de páginas html dos projetos do GitHub.

*Até o momento projeto efetua a extração dos seguintes dados:*
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

---

*Funcionalidades*
1. Extração de páginas de repositórios públicos do GitHub usando web scraping.
2. Extração e apresentação em arquivo da estrutura de pastas/arquivos do repositório.
3. Extração, compilação e apresentação de informações do repositório, como:
    * Quantidade de linhas dos arquivos consolidados por extensão de arquivo.
    * Percentual de linhas de arquivos por extensão de arquivo em relação ao repositório. 
    * Volume de bytes consolidados por extensão de arquivo.
    * Percentual de bytes de arquivos por extensão de arquivo em relação ao volume do repositório.

---

**Como executar/utilizar**

Repositório: https://github.com/rafa-ribeiro/github-web-scraping

* Para utilizar o projeto, é necessário efetuar o clone do projeto no link acima.
* Baixar as dependências do projeto listadas no arquivo Pipfile, para isso pode-se utilizar o comando:

    <code>
        $ pipenv install
    </code> 
    
* Com as dependências devidamentes instaladas, para execução do projeto, é necessário mover o arquivo de listagem dos repositórios para o seguinte diretório:
    
    <PATH_PROJETO>/webscraping/resources/repositories.txt

Obs: O nome do arquivo deve ser 'repositories.txt'

* Para execução, entrar na pasta do projeto e utilizar o comando:
    
    <code>
        $ python app.py
    </code>
    
* Após a execução finalizada, os arquivos gerados estarão armazenados em:

    <PATH_PROJETO>/webscraping/resources/<DONO_REPO>_<NOME_REPO>
   
   
* Na pasta <PATH_PROJETO>/webscraping/resources/, há exemplo do arquivo de entrada de repositórios e exemplos dos 
arquivos gerados pela aplicação. 
---

**Melhorias futuras**

1. Performance. 

    Otimizar as requisições HTTP às páginas do GitHub para que sejam executadas de forma assíncrona, sempre que possível. 
Para isso, uma possibilidade é a utilização da biblioteca Scrapy, acessível em https://scrapy.org/

2. Teste unitário.

    Desenvolvimento de testes de unidade para garantir a assertividade da aplicação na extração de informações do GitHub.