import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Yellowstone_National_Park'


def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    candidates = soup.find_all('span', text='citation needed')
    return len(candidates)


print(get_citations_needed_count(url))


def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    candidates = soup.find_all('span', text='citation needed')
    parents = []
    report_lines = []
    for tag in candidates:
        parents.append(tag.findParent('p'))

    report = 'Citations are needed for the following passages:\n\n'

    for tag in parents:
        report += f'{tag.text}\n'
        report_lines.append(tag.text.strip())

    return report, report_lines


print(get_citations_needed_report(url))
