===================================
Recipe for setting up a filestorage
===================================

This recipe can be used to define a file-storage.  It creates a ZConfig
file-storage database specification that can be used by other recipes to
generate ZConfig configuration files.

This recipe takes an optional path option.  If none is given, it creates and
uses a subdirectory of the buildout parts directory with the same name as the
part.

The recipe records a zconfig option for use by other recipes.

We'll show a couple of examples, using a dictionary as a simulated buildout
object:

    >>> import zc.recipe.filestorage
    >>> buildout = dict(
    ...   buildout = {
    ...      'directory': '/buildout',
    ...      },
    ...   db = {
    ...      'path': 'foo/Main.fs',
    ...      },
    ...   )
    >>> recipe = zc.recipe.filestorage.Recipe(
    ...                   buildout, 'db', buildout['db'])

    >>> print(buildout['db']['path'])
    /buildout/foo/Main.fs

    >>> from six import print_
    >>> print_(buildout['db']['zconfig'], end='')
    <zodb>
      <filestorage>
        path /buildout/foo/Main.fs
      </filestorage>
    </zodb>

    >>> recipe.install()
    ()

    >>> import tempfile
    >>> d = tempfile.mkdtemp()
    >>> buildout = dict(
    ...   buildout = {
    ...      'parts-directory': d,
    ...      },
    ...   db = {},
    ...   )

    >>> recipe = zc.recipe.filestorage.Recipe(
    ...                   buildout, 'db', buildout['db'])

    >>> print(buildout['db']['path'])
    /tmp/tmpQo0DTB/db/Data.fs

    >>> print_(buildout['db']['zconfig'], end='')
    <zodb>
      <filestorage>
        path /tmp/tmpQo0DTB/db/Data.fs
      </filestorage>
    </zodb>

    >>> recipe.install()
    ()

    >>> import os
    >>> os.listdir(d)
    ['db']

The update method doesn't do much, as the database part's directory
already exists, but it is present, so buildout doesn't complain and doesn't
accidentally run install() again:

    >>> recipe.update()

If the storage's directory is removed, is it re-added by the update method:

    >>> os.rmdir(os.path.join(d, 'db'))
    >>> os.listdir(d)
    []
    >>> recipe.update()
    >>> os.listdir(d)
    ['db']

This is useful in development when the directory containing the database is
removed in order to start the database from scratch.
