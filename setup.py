#!/usr/bin/env python3
from setuptools import setup
from brill_games import __version__

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="brill_games",
    version=__version__,
    description="The brillest of games.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="MiguelX413, chrisphamm521",
    author_email="lbpgaming27@gmail.com, chris.pham2003@rocketmail.com",
    license="AGPL-3.0",
    python_requires=">=3.7",
    project_urls={
        "GitHub": "https://github.com/BrillGames/brill_games",
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: GNU Affero General Public License v3",
    ],
)
