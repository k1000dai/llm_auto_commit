from setuptools import setup
import setuptools

setup(
    name="gitautocommit",
    version="0.1.0",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "gitac = app.autocommit:main"
        ]
    },
)