import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from bs4 import BeautifulSoup

page_list = ["https://sgtalk.org/mybb/Forum-Market-Talk",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=2",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=3",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=4",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=5",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=6",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=7",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=8",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=9",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=10",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=11",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=12",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=13",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=14",
            "https://sgtalk.org/mybb/Forum-Market-Talk?page=15"
]

#page_list = ["https://sgtalk.org/mybb/Forum-Market-Talk"]

for list in page_list:
    page = requests.get(list, verify=False)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find_all('tr', class_='inline_row')
    for t in table:
        subject = t.find('span', class_="subject_new")
        subject_title = subject.find('a')
        author = t.find('div', class_="author smalltext")
        author_name = author.find('a')
        print(subject_title.get('href'),",",author_name.get('href').replace('https://sgtalk.org/mybb/',''))

