##############################################################################
#
# Copyright (c) 2006 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

import logging, os


class Recipe:

    def __init__(self, buildout, name, options):
        self.name, self.options = name, options
        path = options.get('path')
        if path is None:
            path = os.path.join(buildout['buildout']['parts-directory'],
                                self.name, 'Data.fs')
            self.make_part = True
        else:
            path = os.path.join(buildout['buildout']['directory'], path)
            if not os.path.exists(path):
                logging.getLogger('zc.recipe.filestorage').error(
                    "%s does not exixt", path)
            self.make_part = False

        options['path'] = path
        options['zconfig'] = template % path

    def install(self):
        if self.make_part:
            part = os.path.dirname(self.options['path'])
            if not os.path.exists(part):
                os.mkdir(part)
        return ()

    def update(self):
        pass

template = """\
<zodb>
  <filestorage>
    path %s
  </filestorage>
</zodb>
"""
