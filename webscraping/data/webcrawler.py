import requests
from bs4 import BeautifulSoup
from anytree import Node, RenderTree

github_prefix = 'https://github.com/'


def execute_web_crawler(repository):
    print("Executing web crawler on page %s" % repository)
    html = get_html_page(repository)
    print("Executing for %s" % repository)
    root = Node(repository)
    get_files(root, html)

    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))


def get_html_page(repository):
    url_repository = get_url(repository)
    print("URl: %s" % url_repository)

    try:
        req = requests.get(url_repository)
        if req.status_code == 200:
            return req.content
    except Exception as e:
        raise Exception("Erro. Não foi possível acessar a URL %s" % url_repository)


def get_url(link_suffix):
    return "%s%s" % (github_prefix, link_suffix)


def get_files(node_parent, html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', attrs={'class': 'files'})
    if table:
        tbody_tag = table.find('tbody')
        trs = tbody_tag.find_all('tr', attrs={'class': 'js-navigation-item'})
        x = 0
        for tr in trs:
            x = x + 1
            print("tr %s" % x)
            td_content = tr.find('td', attrs={'class': 'content'})
            span_tag = td_content.find('span')
            a_tag = span_tag.find('a')

            title_directory = a_tag.get('title')
            link_directory = a_tag.get('href')

            print("Title: %s" % title_directory)
            print("href: %s" % link_directory)

            directory_html = get_html_page(link_directory)

            node_child = Node(title_directory, parent=node_parent)
            get_files(node_child, directory_html)
