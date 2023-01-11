import os

from setuptools import setup

CURRENT = os.path.abspath(os.path.dirname(__file__))


def _open(subpath):
    path = os.path.join(CURRENT, subpath)
    return open(path, encoding="utf-8", errors="ignore")


with _open("requirements.txt") as file:
    base_reqs = file.read().strip().split("\n")

with _open("requirements-dev.txt") as file:
    dev_reqs = file.read().strip().split("\n")

with _open("README.md") as f:
    readme = f.read()

setup(
    name="python-docparser",
    version="0.1.0",
    author="Hassane Abida",
    author_email="abidahass.uca@gmail.com",
    url="https://github.com/has-abi/docparser",
    description="Extract text from your docx document.",
    long_description=readme,
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    tests_require=base_reqs + dev_reqs,
    install_requires=base_reqs,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
