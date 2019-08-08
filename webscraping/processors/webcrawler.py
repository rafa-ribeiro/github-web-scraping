import requests
import time
from bs4 import BeautifulSoup
from webscraping.processors.data import FileNode
from webscraping.processors.bytes_utils import get_multiplier

github_prefix = 'https://github.com/'

EXTENSIONS_BLACK_LIST = [".dat", ".png"]


def is_valid_extension(file_name):
    """
    Valida que o arquivo é de uma extensão válida para o cálculo das métricas.

    :param file_name: Nome ou path contendo a extensão do arquivo.
    :return: True se for uma extensão válida, caso contrário False.
    """

    for ext in EXTENSIONS_BLACK_LIST:
        if file_name.endswith(ext):
            return False
    return True


def execute_web_crawler(repository):
    """
    Executa o web scraping no repositório informado.

    TODO (rafael.ribeiro):
    - Refatorar de modo que as GET Requests que não possuem dependência entre sí possam ser feitas de forma assíncrona.
    Isso pode ser feito, por exemplo, para toda a listagem de arquivos/diretório que são filhos de um mesmo 'nó'
    na estrutura de pastas. *** Uma possibilidade é o uso da lib Scrapy (https://scrapy.org/)

    :param repository: Repositório que será efetuado o web scraping.
    :return: Nó raiz da estrutura de arquivos/diretórios em que foi iniciado o scraping.
    """

    start = time.time()
    print("Executing web crawler on page %s" % repository)
    html = request_html_page(repository)
    root = FileNode(repository)
    get_files(root, html)
    end = time.time()
    print("Web scraping execution time: %s seconds" % str(end-start))
    return root


def request_html_page(repository):
    """
    Executa uma GET request para obter as páginas HTML a partir do sufixo de URL do GitHub informada no parâmetro.

    :param repository: Sufixo do link de acesso ao GitHub.
    :return: Retorna a página HTML referente ao endereço informado.
    """
    url_repository = get_url(repository)
    try:
        req = requests.get(url_repository)
        if req.status_code == 200:
            return req.content
    except Exception as e:
        raise Exception("Erro. Não foi possível acessar a URL %s\n%s" % (url_repository, e))


def get_url(link_suffix):
    """
    Retorna o link completo para acessar as páginas do GitHub.

    :param link_suffix: Sufixo de acesso às páginas do GitHub.
    :return: URL completa.
    """
    return "%s%s" % (github_prefix, link_suffix)


def get_files(node_parent, html):
    """
    Efetua o web scraping na página coletando os dados necessários para acessar os diretórios e os arquivos do
    repositório.

    Esse método percorre os diretórios recursivamente e pára ao encontrar e processar um arquivo.

    :param node_parent: Nó a partir do qual a leitura por diretórios/arquivos será efetuada.
    :param html: Página HTML referente ao node_parent.
    """
    print("Processing on %s" % node_parent.name)
    soup = BeautifulSoup(html, 'html.parser')

    table_files_tag = extract_files(soup)

    if table_files_tag:
        table_rows = extract_rows(table_files_tag)

        for row in table_rows:
            dir_name, dir_link_suffix = extract_dir_info(row)
            if is_valid_extension(dir_link_suffix):
                next_html_page = request_html_page(dir_link_suffix)
                node_child = FileNode(dir_name, parent=node_parent)
                get_files(node_child, next_html_page)
    else:
        if is_valid_extension(node_parent.name):
            file_info_details_component = extract_file_info_component(soup)
            if file_info_details_component:
                lines_info, bytes_size, bytes_unity = extract_file_info_details(file_info_details_component)
                fill_file_node(node_parent, int(lines_info), convert_to_bytes(bytes_size, bytes_unity))


def extract_files(soup):
    """
    Extrai da página HTML o elemento tempo que contém a listagem de arquivos e diretórios.

    :param soup: Recurso do BeautifulSoup que parseou o arquivo HTML.
    :return: Componente <table> da página.
    """
    return soup.find('table', attrs={'class': 'files'})


def extract_rows(table_files_tag):
    """
    Extrai as linhas da <table> passada.

    :param table_files_tag: Componente <table> do HTML
    :return: Componente <tr> com os dados referentes ao diretório/arquivo.
    """
    content_table = table_files_tag.find('tbody')
    return content_table.find_all('tr', attrs={'class': 'js-navigation-item'})


def extract_dir_info(row_file):
    """
    Extrai o nome e o link de acesso do próximo diretório/arquivo a ser utilizado para extração.

    :param row_file: Componente <tr> da tabela de listagem de arquivos/diretórios.
    :return: dir_name com o nome do próximo recurso e dir_link_suffix contendo o link para acesso.
    """
    td_content = row_file.find('td', attrs={'class': 'content'})
    span_tag = td_content.find('span')
    a_tag = span_tag.find('a')
    dir_name = a_tag.text
    dir_link_suffix = a_tag.get('href')
    return dir_name, dir_link_suffix


def extract_file_info_component(soup):
    """
    Extrai o componente 'file-info-divider' que separa as informações referente ao tamanho e quantidade de linhas do
    arquivo.

    TODO (rafael.ribeiro): Alterar a maneira de obter as informações do 'file-info-divider':

    Estratégias:
    1. Extrair somente o último dos 'file-info-divider's e usar o método 'previous' para obter a quantidade de linhas
    e o '.next_sibling' para obter o tamanho e a unidade de medida. Warning: Arquivos de imagem continuam não sendo
    processados adequadamente.

    2. Mapear os tipos de extensão que possuem padrões de informações em template diferentes e criar extratores
    específicos por extensão.

    :param soup: Recurso do BeaultifulSoup que efetuou o parse do HTML.
    :return: Componente <span> próximo às informações do arquivo.
    """
    file_mode_span = soup.find('span', attrs={'class': 'file-mode'})
    if file_mode_span:
        file_mode_span.extract()
    return soup.find('span', attrs={'class': 'file-info-divider'})


def extract_file_info_details(file_info_details_component):
    """
    Extrai as informações referentes à quantidade de linhas e o tamanho dos arquivos do repositório.

    TODO (rafael.ribeiro): A forma como obter essas informações pode (deve) ser alterada para manter a extração
    dos dados mais padronizada, vide to do do método 'extract_file_info_component'

    :param file_info_details_component: Componente <span> contendo o identificador 'file-info-divider' para localização
    dos dados.
    :return: Respectivamente, a quantidade de linhas, tamanho e a unidade de medida do arquivo obtidos.
    """
    content_file_info_parent_container = file_info_details_component.find_previous().get_text()
    file_info = content_file_info_parent_container.replace("\n", "").strip()
    file_info = " ".join(file_info.split())
    file_info_list = file_info.split(" ")
    lines_info = file_info_list[0]
    bytes_size = file_info_list[4]
    bytes_unity = file_info_list[5]
    return lines_info, bytes_size, bytes_unity


def convert_to_bytes(any_bytes_size, bytes_unity):
    """
    Converte o valor informado para Bytes de acordo com a unidade de medida do mesmo.

    :param any_bytes_size: Valor a ser convertido
    :param bytes_unity: Unidade de Medida (Bytes, KB)
    :return: Valor em Bytes
    """
    unity_multiplier = get_multiplier(bytes_unity)
    return float(any_bytes_size) * unity_multiplier


def fill_file_node(file_node, lines_info, size_bytes):
    """
    Preenche o nó informado com os dados obtidos.

    :param file_node: Nó do arquivo que foi coletada as informações.
    :param lines_info: Quantidade de linhas do arquivo.
    :param size_bytes: Tamanho do arquivo em Bytes.
    """
    file_node.lines = lines_info
    file_node.size_bytes = size_bytes

