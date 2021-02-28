import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "CHANGES.txt")) as f:
    CHANGES = f.read()

requires = [
    "spleeter",
    "plaster_pastedeploy",
    "pyramid",
    "pyramid_mako",
    "pyramid_debugtoolbar",
    "waitress",
]

tests_require = ["WebTest >= 1.3.1", "pytest >= 3.7.4", "pytest-cov"]  # py3 compat

setup(
    name="drumio",
    version="0.0",
    description="drumio",
    long_description=CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
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
    extras_require={"testing": tests_require},
    install_requires=requires,
    entry_points={"paste.app_factory": ["main = drumio:main"]},
)
