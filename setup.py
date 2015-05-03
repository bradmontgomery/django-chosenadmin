from setuptools import setup
from chosenadmin import __version__


url = "https://github.com/bradmontgomery/django-chosenadmin/archive/v{0}.tar.gz".format(__version__)

setup(
    name="django-chosenadmin",
    version=__version__,
    author="Brad Montgomery",
    author_email="brad@bradmontgomery.net",
    description=("Adds Chosen.js to the Django Admin app"),
    install_requires=[],
    license="MIT",
    keywords="django chosen admin",
    url=url,
    packages=[
        "chosenadmin",
    ],
    long_description="Adds the Chosen.js plugin to Select and Multi-select elements in Django's admin.",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        "Topic :: Utilities",
    ],
)
