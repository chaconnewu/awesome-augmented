import requests
import pymysql
import json
import traceback
from urllib.parse import urlparse
from datetime import datetime
import pymysql
import yaml

with open('config.yml', 'r') as config_file:
    config = yaml.load(config_file)

def get_all_repo_urls():
    return set(open('all_github_urls.txt', 'r').read().split('\n')[:-1])

def db_cursor():
    conn = pymysql.connect(
        host='127.0.0.1',
        charset='utf8',
        use_unicode=True,
        unix_socket='/tmp/mysql.sock',
        user=config['database']['user'],
        # passwd=str(config['database']['password']),
        passwd=None,
        db=config['database']['db'],
        autocommit=True
    )

    return conn.cursor()

def already_in_db():
    query = "select repo_url from awesome_augmented";
    cur = db_cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return set([x[0] for x in rows])

def insert_into_db(url_list):
    cur = db_cursor()
    repo_table_name = 'awesome_augmented'
    missed = []
    urls_already_in_db = already_in_db()
    count = 0
    for idx, item_url in enumerate(url_list):
        if item_url in urls_already_in_db:
            continue
        if count == 4800:
            break
        repo_url = 'https://api.github.com/repos' + urlparse(item_url).path
        count += 1
        try:
            r = requests.get(repo_url, auth=(config['github_credential']['username'], config['github_credential']['password']))
            content = r.json()

            created_at = content.get('created_at', 'None')
            description = content.get('description', 'None')
            if description != None:
                description = description.replace("'", "\\'")
            fork = content['fork']
            forks_count = content['forks_count']
            full_name = content['full_name']
            homepage = content.get('homepage', 'None')
            id = content['id']
            language = content['language']
            name = content['name']
            open_issues_count = content['open_issues_count']
            owner_login = content['owner']['login']
            owner_url = content['owner']['url']
            pushed_at = content['pushed_at']
            repo_url = content['html_url']
            size = content['size']
            stargazers_count = content['stargazers_count']
            subscribers_count = content['subscribers_count']
            updated_at = content['updated_at']
            url = content['url']
            watchers_count = content['watchers_count']

            values = "('%s', '%s', '%i', '%d', '%s', '%s', '%d', '%s', '%s', '%d', '%s', '%s', '%s', '%s', '%d', '%d', '%d', '%s', '%s', '%d');" % (created_at, description, fork, forks_count, full_name, homepage, id, language, name, open_issues_count, owner_login, owner_url, pushed_at, repo_url, size, stargazers_count, subscribers_count, updated_at, url, watchers_count)
            insert_query = 'insert into ' + repo_table_name + ' values ' + values
            cur.execute(insert_query)
            print('success at: ', idx)
        except:
            traceback.print_exc()
            missed.append(item_url)
            if content.get('message') == 'Not Found':
                continue
            else:
                print('failed at: %d, %s' % (idx, repo_url))
                print(insert_query)
                # break

def main():
    insert_into_db(get_all_repo_urls())

if __name__ == '__main__':
    main()
