# Copyright (c) 2012 Paul Tagliamonte <paultag@debian.org>
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import os
import sys
import json
from pymongo import Connection


_db_default = "monomoy"


CONFIG = {}

cfil = 'config/monomoy.json'
if os.path.exists(cfil):
    CONFIG = json.load(open(cfil, 'r'))

if 'mongo_db' in CONFIG:
    _db_default = CONFIG['mongo_db']

_db_name = os.environ.get('MONOMOY_DB', _db_default)
if _db_name.strip() == "":
    _db_name = _db_default

connection = Connection('localhost', 27017)
db = getattr(connection, _db_name)


def mangle_sys():
    pth = "./scripts"
    pth = os.path.abspath(pth)
    if pth not in sys.path:
        sys.path.insert(0, pth)

mangle_sys()
