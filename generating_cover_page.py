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

    try:
        content = f.read()
        soup = generate_soup(content)
        github_count, all_count = generate_urls_ratio(soup)
        print('%s has %d github urls, %d all' % (urlparse(url).path.split('/')[-1], github_count, all_count))

        lis = soup.find_all('li');
        visited = set()

        for li in lis:
            a = li.find_all('a')

            if len(a) > 0 and re.search('^https://github.com/[^/]+/[^/]+/?$', a[0]['href']):
                repo_url = a[0]['href']
                query = "select stargazers_count, pushed_at from awesome_augmented where repo_url='%s'" % (repo_url)
                cur.execute(query)
                rows = cur.fetchall()
                if len(rows) == 1:
                    stars_count, updated_at = rows[0]
                    updated_at_datetime = parse(updated_at)

                    updated_days_ago = (datetime.now(pytz.utc)- updated_at_datetime).days
                    tag = soup.new_tag('sup')
                    tag.string = '%d GitHub links in total %d links, &#9733 %d, pushed %d days ago ' % (github_count, all_count, stars_count, updated_days_ago)
                    if a[0] in visited:
                        continue
                    else:
                        visited.add(a[0])
                        # a[0].insert_after(tag)
                        li.insert(len(li.contents), tag)
    except:
        traceback.print_exc()
    f = open(filename, 'w')

    f.write(soup.prettify(formatter=None))
    del f

def main():
    # awesome_url = 'https://raw.githubusercontent.com/sindresorhus/awesome/master/readme.md'
    # content = request_content(awesome_url)
    # f = open('awesome.md', 'w')
    # f.write(content)
    # del f

    soup = generate_soup(open('new.md', 'r').read())
    awesome_urls = generate_all_github_urls(soup)

    for url in awesome_urls:
        count_github_urls(url, input_dir)

    # attach_github_info('awesome.md')


if __name__ == '__main__':
    main()
