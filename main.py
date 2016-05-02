import html.parser
import requests
import markdown2
import json
import re
import queue
from urllib.parse import urlparse

from multiprocessing import Process# Going parallel!
from urllib.parse import urlparse
from bs4 import BeautifulSoup

number_of_processes = 3

def examine_each_awesome(awesome_urls):
    prefix = 'https://raw.githubusercontent.com'
    postfix = '/master/'

    def worker(process_id, urls):
        for url in urls:
            full_name = urlparse(url).path
            filename = './awesomes/' + full_name.split('/')[-1] + '.md'
            readme_url = prefix + full_name + postfix

            # print('Process ' + str(process_id) + ' Requesting: ' + readme_url)
            try:
                contents = request_content(readme_url + 'README.md')
                if contents == 'Not Found':
                    contents = request_content(readme_url + 'readme.md')

                soup = generate_soup(contents)
                all_github_urls = generate_all_github_urls(soup)
                for url in all_github_urls:
                    print(url)

                f = open(filename, 'w')
                f.write(contents)
                del f
            except:
                pass

    unit_size = int(len(awesome_urls) / number_of_processes)
    start = 0
    procs = []
    for i in range(number_of_processes):
        if start+unit_size < len(awesome_urls):
            items = awesome_urls[start:start+unit_size]
        else:
            items = awesome_urls[start:]

        start += unit_size

        p = Process(target=worker, args=(i, items))
        procs.append(p)
        p.start()

    # Finish all the processes
    for p in procs:
        p.join()

    # def worker(thread_id, urls, out_q):
    #     for url in urls:
    #         content = request_content(url)
    #         soup = generate_soup(content)
    #         all_github_urls = generate_all_github_urls(soup)
    #         out_q.put(all_github_urls)
    #         print('Thread ' + str(thread_id) + ': ' + url + ': ' + str(len(all_github_urls)))
    #
    # unit_size = int(len(awesome_urls) / 20)
    # start = 0
    # out_q = queue.Queue()
    # procs = []
    # for i in range(20):
    #     if start+unit_size < len(awesome_urls):
    #         items = awesome_urls[start:start+unit_size]
    #     else:
    #         items = awesome_urls[start:]
    #
    #     start += unit_size
    #
    #     p = Process(target=worker, args=(i, items, out_q))
    #     procs.append(p)
    #     p.start()
    #
    # for p in procs:
    #     p.join()
    #
    # for i in range(20):
    #     print(len(out_q.get()))

def has_valid_github_url(a):
    return len(a) > 0 and a[0].get('href') and re.search('^https://github.com/[^/]+/[^/]+/?$', a[0]['href'])

def generate_all_github_urls(soup):
    lis = soup.find_all('li')

    github_urls = set()
    for li in lis:
        a = li.find_all('a')

        if has_valid_github_url(a):
            github_urls.add(a[0]['href'])

    return list(github_urls)

def generate_soup(content):
    content = content.replace('] (http', '](http')
    markdown = markdown2.Markdown()
    return BeautifulSoup(markdown.convert(content), 'html.parser')

def request_content(url):
    return requests.get(url).content.decode('utf-8')

def regenerate_hrefs(soup):
    prefix = 'https://github.com/chaconnewu/awesome-augmented/blob/master/awesomes/'
    lis = soup.find_all('li')

    github_urls = set()
    for li in lis:
        a = li.find_all('a')
        if has_valid_github_url(a):
            full_name = urlparse(a[0]['href']).path
            a[0]['href'] = prefix + full_name.split('/')[-1] + '.md'

    f = open('new.md', 'w')
    f.write(soup.prettify())
    del f

def main():
    awesome_url = 'https://raw.githubusercontent.com/sindresorhus/awesome/master/readme.md'
    content = request_content(awesome_url)

    soup = generate_soup(content)
    awesome_urls = generate_all_github_urls(soup)
    examine_each_awesome(awesome_urls)
    regenerate_hrefs(soup)

if __name__ == '__main__':
    main()
