import requests
import time
from bs4 import BeautifulSoup
from webscraping.processors.data import FileNode
from webscraping.processors.bytes_utils import get_multiplier

github_prefix = 'https://github.com/'


def execute_web_crawler(repository):
    start = time.time()
    print("Executing web crawler on page %s" % repository)
    html = request_html_page(repository)
    root = FileNode(repository)
    get_files(root, html)
    end = time.time()
    print("Execution time: %s seconds" % str(end-start))
    return root


def request_html_page(repository):
    url_repository = get_url(repository)
    try:
        req = requests.get(url_repository)
        if req.status_code == 200:
            return req.content
    except Exception as e:
        raise Exception("Erro. Não foi possível acessar a URL %s\n%s" % (url_repository, e))


def get_url(link_suffix):
    return "%s%s" % (github_prefix, link_suffix)


def get_files(node_parent, html):
    print("Processing on %s" % node_parent.name)
    soup = BeautifulSoup(html, 'html.parser')

    table_files_tag = extract_files(soup)

    if table_files_tag:
        table_rows = extract_rows(table_files_tag)

        for row in table_rows:
            dir_name, dir_link_suffix = extract_dir_info(row)
            next_html_page = request_html_page(dir_link_suffix)

            node_child = FileNode(dir_name, parent=node_parent)
            get_files(node_child, next_html_page)
    else:
        file_info_details_component = extract_file_info_component(soup)
        if file_info_details_component:
            lines_info, bytes_size, bytes_unity = extract_file_info_details(file_info_details_component)

            fill_file_node(node_parent, int(lines_info), convert_to_bytes(bytes_size, bytes_unity))


def extract_files(soup):
    return soup.find('table', attrs={'class': 'files'})


def extract_rows(table_files_tag):
    content_table = table_files_tag.find('tbody')
    return content_table.find_all('tr', attrs={'class': 'js-navigation-item'})


def extract_dir_info(row_file):
    td_content = row_file.find('td', attrs={'class': 'content'})
    span_tag = td_content.find('span')
    a_tag = span_tag.find('a')
    dir_name = a_tag.text
    dir_link_suffix = a_tag.get('href')
    return dir_name, dir_link_suffix


def extract_file_info_component(soup):
    return soup.find('span', attrs={'class': 'file-info-divider'})


def extract_file_info_details(file_info_details_component):
    content_file_info_parent_container = file_info_details_component.find_previous().get_text()
    file_info = content_file_info_parent_container.replace("\n", "").strip()
    file_info = " ".join(file_info.split())
    file_info_list = file_info.split(" ")
    lines_info = file_info_list[0]
    bytes_size = file_info_list[4]
    bytes_unity = file_info_list[5]
    return lines_info, bytes_size, bytes_unity


def convert_to_bytes(bytes_size, bytes_unity):
    unity_multiplier = get_multiplier(bytes_unity)
    return float(bytes_size) * unity_multiplier


def fill_file_node(file_node, lines_info, size_bytes):
    file_node.lines = lines_info
    file_node.size_bytes = size_bytes

