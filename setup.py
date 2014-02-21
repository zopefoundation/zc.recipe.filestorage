from setuptools import setup, find_packages
import os

name = "zc.recipe.filestorage"
setup(
    name=name,
    version='1.1.3.dev0',
    author="Jim Fulton",
    author_email="jim@zope.com",
    description="ZC Buildout recipe for defining a file-storage",
    long_description=(
        open(os.path.join("zc", "recipe", "filestorage", "README.rst")).read()
        + '\n\n' +
        open("CHANGES.rst").read()),
    license="ZPL 2.1",
    keywords=["zodb", "zc.buildout"],
    url="http://pypi.python.org/pypi/%s/" % name,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: ZODB",
        "Framework :: Buildout",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Zope Public License",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",

        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        ],
    packages=find_packages(),
    namespace_packages=["zc", "zc.recipe"],
    install_requires=["zc.buildout", "zope.testing", "setuptools", "six"],
    entry_points={"zc.buildout": ["default=%s:Recipe" % name]},
    include_package_data=True,
    zip_safe=True,
    )
