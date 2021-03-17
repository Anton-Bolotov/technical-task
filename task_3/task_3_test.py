import requests

data = {
    "lesson": [1594663200, 1594666800],
    "pupil": [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
    "tutor": [1594663290, 1594663430, 1594663443, 1594666473]
}

half_message = 'отправьте POST запрос с телом из body'


def method_post(json_data):
    r = requests.post('http://localhost:5000/', json=json_data)
    return r.json()


def method_get():
    r = requests.get('http://localhost:5000/')
    return r.json()


if __name__ == '__main__':
    assert method_post(json_data=data) == {'result': 3117}
    assert half_message in method_get()['message']
    print(method_post(json_data=data))
