#!/usr/bin/env python
"""
Download battle summaries from Kennedy

This saves local copies of the webpages to the ./html folder, along with
metadata about the pages (url headers) in ./html/METADATA.json
"""
import urllib2
import urlparse
from os import path
import os
import re
import json

from lxml import html


BASE_URL = "http://www.bibliobase.com/history/readerscomp/civwar/html/"
INDEX_URL = urlparse.urljoin(BASE_URL, "cw_000108_app_the384pr.htm")

def _metdata(url):
    return {'headers' : url.info().dict(),
            'url' : url.geturl()}

def add_url(url, dst, metadata):
    filename = path.basename(url)
    dstfile = path.join(dst, filename)
    try: 
        req = urllib2.urlopen(url)
        metadata.update({filename : {'headers' : req.info().dict,
                                     'url' : req.geturl()}})
        page = req.read()
        with open(dstfile, 'w') as f:
            f.write(page)
            return page
    except urllib2.HTTPError:
        print("add_url ERROR: could not download %s" % url)

def save_webpages(dst):
    _METAFN = path.join(dst, 'METADATA.json')
    CODEC = 'latin-1'

    # Generate destination if it doesn't exist
    if not path.isdir(dst):
        print("making %s" % dst)
        os.makedirs(dst)

    # metadata about each webpage
    filelist = {}

    # Battles by state
    battleidx = add_url(INDEX_URL, dst, filelist)
    battle_html = html.fromstring(battleidx)

    def _isbattle(x):
        if x[0].text:
            if re.match("^[A-Z]{2}[0-9]{3}[a-z]?$", x[0].text):
               if not x[2].startswith("#"):
                   return True

    battlelinks = dict((x[0].text, urlparse.urljoin(BASE_URL, x[2])) for x
                       in battle_html.iterlinks()
                       if _isbattle(x))

    # Two battles share the same link (VA075)
    for k, link in battlelinks.iteritems():
        add_url(link, dst, filelist)

    metadata = {'files' : filelist,
                'battles' : battlelinks}
    with open(_METAFN, 'w') as f:
        json.dump(metadata, f)

def main():
    dst = 'html'
    save_webpages(dst)

if __name__ == '__main__':
    main()

