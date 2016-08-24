#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

import os
import sys

sys.path.insert(0, os.path.abspath('../_lectures/docs/'))

from config_sphinx import *  # noqa

project = u'Каналы передачи данных'
epub_title = project
latex_documents = [
    ('index', 'lectures.tex',
     project,
     u'Свинцов Дмитрий', 'manual'),
]
my_intersphinx = {
    'http://docs.python.org/': None,
    'http://docs.sqlalchemy.org/en/latest/': None,
    'http://initd.org/psycopg/docs/': None,
}
intersphinx_mapping = dict(
    list(intersphinx_mapping.items())
    + list(my_intersphinx.items())
)
