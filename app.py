import os
from webscraping.processors.files import get_repositories_list, write_file
from webscraping.processors.webcrawler import execute_web_crawler
from webscraping.processors.repos_analyzer import analyze_repo
from webscraping.processors.report_creator import create_report


def main():
    resources_path = "%s%s" % (os.getcwd(), "/webscraping/resources/")
    repositories_path = "%s%s" % (resources_path, "repositories.txt")
    repositories = get_repositories_list(repositories_path)

    for repo in repositories:
        repo = repo.strip()
        root = execute_web_crawler(repo)
        repo_metrics = analyze_repo(root)
        report = create_report(repo, root, repo_metrics)
        report_file_name = "{}".format(repo.replace("/", "_"))
        export_path = "{}{}.txt".format(resources_path, report_file_name)
        write_file(export_path, report)


if __name__ == '__main__':
    main()
