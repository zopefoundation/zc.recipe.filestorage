##############################################################################
#
# Copyright (c) 2006, 2007 Zope Corporation and Contributors.
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

        blob_dir = options.get('blob-dir', '')
        if not blob_dir:
            template = plain_template
        else:
            template = blob_template
            blob_dir = os.path.join(buildout['buildout']['directory'],
                                    blob_dir)
        options['blob-dir'] = blob_dir
        shared = options.get('shared-blob-dir', 'no')

        options['zconfig'] = template % dict(
            path=path,
            blob_dir=blob_dir,
            shared=shared)

    def install(self):
        if self.make_part:
            part = os.path.dirname(self.options['path'])
            if not os.path.exists(part):
                os.mkdir(part)
        return ()

    def update(self):
        self.install()

plain_template = """\
<zodb>
  <filestorage>
    path %(path)s
  </filestorage>
</zodb>
"""

blob_template = """\
<zodb>
  <blobstorage>
    blob-dir %(blob_dir)s
    shared-blob-dir %(shared)s
    <filestorage>
      path %(path)s
    </filestorage>
  </blobstorage>
</zodb>
"""
