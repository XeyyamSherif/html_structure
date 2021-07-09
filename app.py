from functions import find_tags_count, find_difference
from flask import Flask, request

app = Flask(__name__)

auth_code = "QWDCR4"
number_phone = int(+71111111111)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        content = request.json
        try:
            code = content["code"]
            phone_code = int(content["number"])
        except:
            return {"status": "wrong input"}
        if code == auth_code and phone_code == number_phone:
            return {"status": "OK"}
        else:
            return {"status": "Fail"}
    else:
        number = request.args.get('phone')
        return {"authentication code": auth_code,
                "number": number_phone}


@app.route('/structure')
def structure_html():
    if 'link' in request.args:
        if 'tags' in request.args:
            tags = request.args.getlist('tags')
            link = request.args.getlist('link')
            counts = find_tags_count(link[0], tags[0])
        else:
            link = request.args.getlist('link')
            counts = find_tags_count(link[0])
    else:
        counts = find_tags_count("https://freestylo.ru/")
    return counts


@app.route('/check_structure', methods=['POST'])
def check_html_structure():
    try:
        content_link = request.json['link']
        content_structure = request.json['structure']
    except:
        return {
            'status': 'wrong input'
        }

    actual_structure = find_tags_count(content_link)
    print(actual_structure)
    print(content_structure)
    if actual_structure == content_structure:
        return {
            "is_correct": True
        }
    else:
        difference = find_difference(actual_structure, content_structure)
        return difference


if __name__ == '__main__':
    app.run(host='0.0.0.0')
