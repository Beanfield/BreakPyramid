import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.txt")).read()
CHANGES = open(os.path.join(here, "CHANGES.txt")).read()

requires = [
    "Akhet",
    "pyramid>=1.0a10",
    "pyramid_beaker",
    "pyramid_handlers",
    "pyramid_tm",
    "SQLAHelper",
    "SQLAlchemy",
    "transaction",
    "WebError",
    "zope.sqlalchemy",
]

if sys.version_info[:3] < (2,5,0):
   requires.append("pysqlite")
    

entry_points = """\
    [paste.app_factory]
    main = testapp:main

    [paste.app_install]
    main = paste.script.appinstall:Installer
"""

setup(name="TestApp",
      version="0.0",
      description="TestApp",
      long_description=README + "\n\n" +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author="",
      author_email="",
      url="",
      keywords="web pyramid pylons",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="testapp",
      entry_points=entry_points,
      paster_plugins=["pyramid"],
      )

