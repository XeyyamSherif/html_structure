from bs4 import BeautifulSoup
import requests


def find_tags_count(link, *tags):

    try:
        page = requests.get(link)
    except:
        return {
            'status': 'cant find such website, make sure site URL  was entered correctly '
        }
    soup = BeautifulSoup(page.content, "html.parser")
    if tags:
        all = [tag.name for tag in soup.find_all() if tag.name in tags[0]]
        if len(all) == 0:
            return {
                'status': 'there are no such tags in this html code'
            }
    else:
        all = [tag.name for tag in soup.find_all()]

    counted_tags = []
    tags_count = {
    }
    for element in all:
        if element in tags_count:
            tags_count[element] += 1
        else:
            tags_count[element] = 1

    return tags_count


def find_difference(dicta, dictb):
    difference_tags = {}
    for key in dicta.keys():
        if key in dictb.keys():
            dif = dicta[key] - dictb[key]
            if dif != 0:
                difference_tags[key] = dif
        else:
            difference_tags[key] = dicta[key]

        for key in dictb.keys():
            if key not in dicta.keys():
                difference_tags[key] = -dictb[key]

    return difference_tags
