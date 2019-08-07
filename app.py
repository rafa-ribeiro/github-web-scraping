from webscraping.processors.files import open_file, get_repositories
from webscraping.processors.webcrawler import execute_web_crawler
from webscraping.processors.repos_analyzer import analyze_repo


def main():
    print("Running app.py...")
    repositories = get_repositories("/home/rafael/python-projects/vivadecora/webscraping/resources/repositories.txt")
    print("Repositories size = %s" % len(repositories))
    for repo in repositories:
        root = execute_web_crawler(repo)

        analyze_repo(root)

    pass


if __name__ == '__main__':
    main()
