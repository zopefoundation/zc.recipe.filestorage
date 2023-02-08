=======
CHANGES
=======

2.0 (unreleased)
----------------

- Add support for Python 3.10, 3.11.

- Drop support for Python 2.7, 3.5, 3.6.

- Drop support for Python 2.6, 3.2, 3.3.

- Add support for Python 3.5, 3.6, 3.7, 3.8, 3.9, PyPy, PyPy3.


1.1.2 (2014-02-21)
------------------

- Fixed: packaging bug that caused 'pip install zc.recipe.filestorage' to fail
  with an error about missing README.txt

1.1.1 (2014-02-16)
------------------

- Fixed: packaging bug that caused a test failure in
  a test runner that didn't use buildout to run setup.py.

1.1.0 (2014-02-14)
------------------

- Python 3 compatibility

- Using Python's ``doctest`` module instead of deprecated
  ``zope.testing.doctest``.

- Removed 'shared-blob-dir' from blobstorage section.


1.0.0 (2007-11-03)
------------------

- Initial release.
