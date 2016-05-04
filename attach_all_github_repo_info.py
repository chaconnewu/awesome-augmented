# import mistune
import markdown2
import re
import pymysql
import yaml
import iso8601
import pytz
import subprocess
import html.parser
import os

from bs4 import BeautifulSoup, Tag
from datetime import datetime, timedelta
from dateutil.parser import parse

input_dir = './original_awesomes/'
output_dir = './awesomes/'

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

def attach_github_info(filename, input_directory='./', output_directory='./'):
    print('processing ' + filename)
    file_path = input_directory + filename
    content = open(file_path, 'r').read()
    content = content.replace('] (http', '](http')
    markdown = markdown2.Markdown()
    soup = BeautifulSoup(markdown.convert(content), 'html.parser')
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
                tag.string = ' &#9733 %d, pushed %d days ago ' % (stars_count, updated_days_ago)
                if a[0] in visited:
                    continue
                else:
                    visited.add(a[0])
                    a[0].insert_after(tag)
                    # li.insert(len(li.contents), tag)

    output_filename = output_directory + filename
    f = open(output_filename, 'w')

    f.write(soup.prettify(formatter=None))
    del f

    # subprocess.check_call(
    # ['pandoc', filename + '.html', '-f', 'html', '-t', 'markdown_github', '-o', filename + '.md'])



def main():
    file_names = os.listdir(input_dir)

    for filename in file_names:
        if filename[-2:] != 'md':
            continue
        attach_github_info(filename, input_dir, output_dir)

if __name__ == '__main__':
    main()
