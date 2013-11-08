#!/usr/bin/env python
# encoding: utf-8
"""
poms.py

Created by Breyten Ernsting on 2013-11-05.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import re
import json
import codecs

from pprint import pprint

import couchdb

def main():
    server = couchdb.Server('http://hackathon-api.omroep.nl/')
    db = server['media']
    if not os.path.exists('info'):
        os.makedirs('info')
    skip = 0
    step = 1000
    should_continue = True
    while should_continue:
        results = db.view(
            'media/broadcasts-by-channel-and-start', reduce=False, include_docs=True, limit=step, skip=skip
        )
        print len(results)
        for row in results:
            doc = row #db[row.id]
            file_name = "info/%s.json" % (row.id,)
            if os.path.exists(file_name):
                continue

            print row.id
            with codecs.open(file_name, 'w', 'utf-8') as out_file:
                out_file.write(json.dumps(doc))
        should_continue = (len(results) > 0)
        #should_continue = False
        skip += step

if __name__ == '__main__':
    main()

