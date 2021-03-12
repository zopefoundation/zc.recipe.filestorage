##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

import os
import re
import doctest
from zope.testing import renormalizing


def test_suite():
    return doctest.DocFileSuite(
        "README.rst",
        checker=renormalizing.RENormalizing([
            (re.compile(r'\S+%(sep)s\w+%(sep)s\w+.fs'
                        % dict(sep=re.escape(os.path.sep))),
             r'/tmp/data/Data.fs'),
            (re.compile(r'\S+sample-(\w+)'), r'/sample-\1'),
        ]),
    )
