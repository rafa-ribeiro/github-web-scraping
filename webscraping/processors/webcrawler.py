import requests
import time
from bs4 import BeautifulSoup
from anytree import Node, RenderTree
from webscraping.processors.data import MyNode
from webscraping.processors.bytes_utils import BytesUnity, get_multiplier

github_prefix = 'https://github.com/'


def execute_web_crawler(repository):
    start = time.time()
    print("Executing web crawler on page %s" % repository)
    html = get_html_page(repository)

    root = MyNode(repository)

    get_files(root, html)

    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.__str__()))

    end = time.time()
    print("Time execution %s seconds" % str(end-start))
    return root


def get_html_page(repository):
    url_repository = get_url(repository)
    try:
        req = requests.get(url_repository)
        if req.status_code == 200:
            return req.content
    except Exception as e:
        raise Exception("Erro. Não foi possível acessar a URL %s" % url_repository)


def get_url(link_suffix):
    return "%s%s" % (github_prefix, link_suffix)


def get_files(node_parent, html):
    # print("Processing %s" % node_parent.name)

    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', attrs={'class': 'files'})
    if table:
        tbody_tag = table.find('tbody')
        trs = tbody_tag.find_all('tr', attrs={'class': 'js-navigation-item'})

        for tr in trs:
            td_content = tr.find('td', attrs={'class': 'content'})
            span_tag = td_content.find('span')
            a_tag = span_tag.find('a')

            directory_name = a_tag.text
            link_suffix = a_tag.get('href')

            directory_html = get_html_page(link_suffix)

            node_child = MyNode(directory_name, parent=node_parent)

            get_files(node_child, directory_html)
    else:
        span_file_info = soup.find('span', attrs={'class': 'file-info-divider'})
        if span_file_info:
            div_container = span_file_info.find_previous().get_text()
            file_info = div_container.replace("\n", "").strip()
            file_info = " ".join(file_info.split())
            print(file_info)
            file_info_list = file_info.split(" ")
            lines_info = file_info_list[0]
            bytes_size = file_info_list[4]
            bytes_unity = file_info_list[5]

            print("%s %s %s" % (lines_info, bytes_size, bytes_unity))
            multiplier = get_multiplier(bytes_unity)
            print(multiplier)

            node_parent.lines = int(lines_info)
            node_parent.size_bytes = float(bytes_size) * multiplier
            print(node_parent.__str__())
