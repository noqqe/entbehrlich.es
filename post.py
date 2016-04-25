#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
import re
import json
import commands
import urlparse
import wikipedia
from datetime import datetime
from dateutil.parser import parse

cmd = 'rvo export -c entbehrliches --to json'
md_dest = "/home/noqqe/Code/entbehrlich.es/content/post/"
head = "---\n"
n = "\n"

(status, output) = commands.getstatusoutput(cmd)
posts = json.loads(output)

for post in posts:

    # fetch rvo document results
    title = post["title"]
    filename = title.replace(" ","-") + ".md"
    title = post["title"]
    content = '\n'.join(post["content"].split('\n')[1:])

    # build markdown compatible timestamp
    t = post["created"]["$date"]
    t = datetime.fromtimestamp(t/1000)
    t = t.replace(microsecond=0)
    postdate = t.isoformat()

    # find wikipedia link
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)[0]
    url = urlparse.urlparse(url)
    wikilang = url.netloc.split('.')[0]
    wikititle = url.path.split('/')[2]

    # set lang and title, fetch wikipedia article
    wikipedia.set_lang(wikilang)
    wiki = wikipedia.summary(wikititle)

    # first sentence of the article and quote it for markdown
    if len(wiki) >= 250:
        wiki = nltk.tokenize.sent_tokenize(wiki)[0]
    wiki = "> " + wiki

    # generate markdown document
    text = head + "title: " + title + n + "date: " + postdate + n + head + content + n + wiki

    # write markdown to the document
    with open(md_dest + filename, "w") as f:
        f.write(text.encode("utf-8"))
        f.close()

    print("Generated: %s" % title)
