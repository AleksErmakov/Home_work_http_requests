import requests
from pprint import pprint
from datetime import datetime, timedelta
import time

#Task 1

def most_smart_hero(heroes_group, URL):

    response = requests.get(URL).json()

    intelligence_heroes = {}
    for heroes in response:
        if heroes['name'] in heroes_group:
            powerstats = heroes['powerstats']
            intelligence_heroes[powerstats['intelligence']] = heroes['name']
            IQ_max = max(intelligence_heroes.keys())
    return print(f'Самый умный супергерой: {intelligence_heroes[IQ_max]}. Его интеллект = {IQ_max}')

heroes_list = ['Hulk', 'Captain America', 'Thanos']
URL_1 = "https://akabab.github.io/superhero-api/api//all.json"

# most_smart_hero(heroes_list, URL_1)

# Task 2

class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    token = '' #добавить токен на Полигоне
    new_file = YaUploader(token=token)
    # new_file.upload_file_to_disk('Home_work/new_file.txt', 'для примера.docx')


# Task 3

def links_for_question_for_two_days(URL, tags):
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    today_converted = int(time.mktime(today.timetuple()))
    yesterday_converted = int(time.mktime((yesterday.timetuple())))

    params = {
        'tagged': tags,
        'fromdate': yesterday_converted,
        'todate': today_converted
    }

    response = requests.get(URL_2, params=params).json()
    help_list = response['items']
    print('Ссылки на вопросы:')

    for links in help_list:
        print(links['link'])
    return

URL_2 = "https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow"
tag = 'python'
# links_for_question_for_two_days(URL_2, tag)
