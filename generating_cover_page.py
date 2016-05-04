import html.parser
import requests
import markdown2
import json
import re
import queue
from urllib.parse import urlparse
import traceback

from multiprocessing import Process# Going parallel!
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# Own
from parse_awesome_lists import *
from attach_all_github_repo_info import *

input_dir = './original_awesomes/'

with open('config.yml', 'r') as config_file:
    config = yaml.load(config_file)

conn = pymysql.connect(
    host='127.0.0.1',
    charset='utf8',
    use_unicode=True,
    unix_socket='/tmp/mysql.sock',
    user=config['database']['user'],
    passwd=None,
    db=config['database']['db'],
    autocommit=True
    )

cur = conn.cursor()

def generate_urls_ratio(soup):
    lis = soup.find_all('li')

    github_urls = set()
    for li in lis:
        a = li.find_all('a')

        if has_valid_github_url(a):
            github_urls.add(a[0]['href'])

    return (len(github_urls), len(lis))

def count_github_urls(url, input_directory='.'):
    filename = input_directory + urlparse(url).path.split('/')[-1] + '.md'
    f = open(filename, 'r')

    content = f.read()
    soup = generate_soup(content)

    return generate_urls_ratio(soup)

def generate_awsome_project_info(url):
    query = "select stargazers_count, pushed_at from awesome_augmented where repo_url='%s'" % (url)
    cur.execute(query)
    rows = cur.fetchall()
    if len(rows) == 1:
        stars_count, updated_at = rows[0]
        updated_at_datetime = parse(updated_at)

        updated_days_ago = (datetime.now(pytz.utc)- updated_at_datetime).days
        return (stars_count, updated_days_ago)
    return (None, None)


def regenerate_hrefs(url):
    prefix = 'https://github.com/chaconnewu/awesome-augmented/blob/master/awesomes/'
    full_name = urlparse(url).path
    new_url = prefix + full_name.split('/')[-1] + '.md'

    return new_url

def main():
    # awesome_url = 'https://raw.githubusercontent.com/sindresorhus/awesome/master/readme.md'
    # content = request_content(awesome_url)
    # f = open('awesome.md', 'w')
    # f.write(content)
    # del f

    soup = generate_soup(open('README.md', 'r').read())
    lis = soup.find_all('li');
    visited = set()

    for li in lis:
        a = li.find_all('a')

        if len(a) > 0 and re.search('^https://github.com/[^/]+/[^/]+/?$', a[0]['href']):
            url = a[0]['href']
            print(url)
            github_count, all_count = count_github_urls(url, input_dir)
            stars_count, updated_days_ago = generate_awsome_project_info(url)
            if not stars_count or not updated_days_ago:
                continue

            tag = soup.new_tag('sup')
            tag.string = '%d GitHub Repo / %d Total, &#9733 %d, pushed %d days ago ' % (github_count, all_count, stars_count, updated_days_ago)
            if a[0] in visited:
                continue
            else:
                visited.add(a[0])
                a[0]['href'] = regenerate_hrefs(url)
                li.insert(len(li.contents), tag)


    f = open('README.md', 'w')
    f.write(soup.prettify(formatter=None))
    del f


if __name__ == '__main__':
    main()
