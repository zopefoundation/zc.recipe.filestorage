import os

from setuptools import find_packages
from setuptools import setup


name = "zc.recipe.filestorage"
setup(
    name=name,
    version='2.0',
    author="Jim Fulton",
    author_email="zope-dev@zope.dev",
    description="ZC Buildout recipe for defining a file-storage",
    long_description=(
        open(os.path.join(
            "src", "zc", "recipe", "filestorage", "README.rst")).read()
        + '\n\n' +
        open("CHANGES.rst").read()),
    license="ZPL 2.1",
    keywords=["zodb", "zc.buildout"],
    url="https://pypi.org/project/%s/" % name,
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
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=["zc", "zc.recipe"],
    python_requires='>=3.7',
    install_requires=["zc.buildout", "zope.testing", "setuptools"],
    entry_points={"zc.buildout": ["default=%s:Recipe" % name]},
    include_package_data=True,
    zip_safe=True,
)
