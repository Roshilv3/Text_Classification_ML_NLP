from setuptools import setup, Require, find_packages

with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()


setup(
    name = "Text Classification ML Project",
    version = "0.0.1",
    description = "This is the full ML Classification Project",
    long_description=long_description,
    author = "Roshil Verma",
    author_email = "roshil.verma.3@gmail.com",
    url = "https://github.com/Roshilv3/Text_Classification_ML_NLP",
    packages = find_packages("requirements.txt")
)

