from webscraping.data.files import open_file, get_repositories
from webscraping.data.webcrawler import execute_web_crawler


def main():
    print("Running app.py...")
    repositories = get_repositories("/home/rafael/python-projects/vivadecora/webscraping/resources/repositories.txt")
    print("Repositories size = %s" % len(repositories))
    for repo in repositories:
        url_repository = execute_web_crawler(repo)
    pass


if __name__ == '__main__':
    main()
