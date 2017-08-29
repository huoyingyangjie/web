def avoid_duplication(O_array):
    ids = O_array
    news_ids = []
    for id in ids:
        if id not in news_ids:
            news_ids.append(id)
    return news_ids

import HTMLParser
class MyHTMLParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.links = []
    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        if tag == "li":
            if len(attrs) == 0:
                pass
            else:
                for (variable, value) in attrs:
                    if variable == "data-cityid":
                        self.links.append(value)