import pytest
import requests
import yaml

with open('config.yaml') as file:
    my_dict = yaml.safe_load(file)

url = my_dict['url']
url1 = my_dict['url1']
username = my_dict['username']
password = my_dict['password']

@pytest.fixture()
def login():
    obj_data = requests.post(url=url, data={'username': username, 'password': password})
    token = obj_data.json()['token']
    return token

def test_step2(login):
    new_post_data = {
        'title': 'заголовок поста',
        'description': 'описание поста',
        'content': 'cодержание'
    }
    headers = {'X-Auth-Token': login}
    response = requests.post(url=url1, json=new_post_data, headers=headers)
    assert response.status_code == 201

    #список постов и проверка наличия нового поста по описанию
    response = requests.get(url=url1, headers=headers, params={'owner': username})
    content_var = [item['description'] for item in response.json()['data']]
    assert new_post_data['description'] in content_var

    #проверка по полю content
    assert new_post_data['content'] in content_var
