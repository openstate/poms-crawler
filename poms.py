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

from pprint import pprint

import couchdb

def main():
    server = couchdb.Server('http://hackathon-api.omroep.nl/')
    db = server['poms']
    for row in db.view('media/broadcasts-by-channel-and-start', reduce=False, include_docs=True, limit=10):
        doc_id = row.id
        doc = db[doc_id]
        for key in doc:
            print "%s :" % (key,)
            pprint(doc[key])

if __name__ == '__main__':
    main()

