from setuptools import setup, find_packages

name = "zc.recipe.filestorage"
setup(
    name=name,
    version="1.1.0dev",
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
        ],
    packages=find_packages(),
    data_files=[(".", ["README.txt"])],
    namespace_packages=["zc", "zc.recipe"],
    install_requires=["zc.buildout", "zope.testing", "setuptools"],
    entry_points={"zc.buildout": ["default=%s:Recipe" % name]},
    include_package_data=True,
    zip_safe=True,
    )
