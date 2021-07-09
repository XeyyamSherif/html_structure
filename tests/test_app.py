import json
import pytest

from werkzeug.datastructures import Headers


def test_index(client):
    res = client.get('/structure')
    assert res.status_code == 200
    expected = {
        'body': 1,
        'div': 1,
        'head': 1,
        'html': 1,
        'img': 1,
        'link': 18,
        'meta': 5,
        'noscript': 2,
        'script': 23,
        'style': 1,
    }
    assert expected == json.loads(res.get_data(as_text=True))


def test_login(client):
    mimetype = 'application/json'
    res = client.get('/login')

    assert res.status_code == 200

    excepted = {"authentication code": 'QWDCR4',
                "number": +71111111111}
    assert excepted == json.loads(res.get_data(as_text=True))

    send_post = {
        "code": 'QWDCR4',
        "number": +71111111111
    }
    responso_post = client.post('/login', data=json.dumps(send_post))
    assert responso_post.content_type == mimetype
