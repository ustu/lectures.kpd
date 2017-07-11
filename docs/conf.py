#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

# standard library
import os
import sys

sys.path.insert(0, os.path.abspath('../_lectures/docs/'))

from config_sphinx import *  # noqa isort:skip


project = u'Каналы передачи данных'
html_title = project
epub_title = project

# Github
edit_on_github_project = 'ustu/lectures.kpd'
edit_on_github_branch = 'master'

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
    list(intersphinx_mapping.items())  # noqa
    + list(my_intersphinx.items())
)
