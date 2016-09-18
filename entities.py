import json

ls = [{u'salience': 1, u'mentions': [{u'text': {u'content': u'Statue of Liberty', u'beginOffset': 4}}], u'type': u'LOCATION', u'name': u'Statue of Liberty'},{u'salience': 1, u'mentions': [{u'text': {u'content': u'Statue of Liberty', u'beginOffset': 4}}], u'type': u'LOCATION', u'name': u'Statue of Liberty', u'metadata': {u'wikipedia_url': u'http://en.wikipedia.org/wiki/Statue_of_Liberty'}}]

def scrape(entities):
    str_res = []
    for i in entities:
        try:
            loc_name = i["name"]
            url = i["metadata"]["wikipedia_url"]
        except KeyError:
            continue
        loc_name = loc_name.encode('ascii','ignore')
        url = url.encode('ascii','ignore')
        s = '<a href="'+url+'">'+loc_name+'</a>'
        str_res.append(s)
    final = ','.join(str_res)
    return final
