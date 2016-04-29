from collections import defaultdict
from operator import itemgetter
urls = open('all_github_urls.txt', 'r').read().split('\n')[:-1]
url_dict = defaultdict(int)

for url in urls:
    url_dict[url] += 1

sorted_list = sorted(url_dict.items(), key=itemgetter(1),reverse=True)
print(len(set(sorted_list)))
