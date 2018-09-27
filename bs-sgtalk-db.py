import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from bs4 import BeautifulSoup
import dataset

db = dataset.connect('sqlite:///sgtalk.db')
sgtable = db['authors']
X = 9
page_list = []

for i in range(1,X):
    url='https://sgtalk.org/mybb/Forum-Market-Talk?page=' + str(i)
    page_list.append(url)


for list in page_list:
    page = requests.get(list, verify=False)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find_all('tr', class_='inline_row')
    for t in table:
        subject = t.find('span', class_="subject_new")
        subject_title = subject.find('a').get("href").replace('Thread-','')
        author = t.find('div', class_="author smalltext")
        author_name = author.find('a')
        author_name1=author_name.get('href').replace('https://sgtalk.org/mybb/User-','')
#        print(subject_title,",",author_name1)
        sgtable.insert(dict(name=author_name1, article=subject_title))
