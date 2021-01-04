
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="redditeasy",
    version="2.5.0",
    author="MakufonSkifto",
    author_email="emirsurmen@gmail.com",
    description="RedditEasy is an API wrapper for the Reddit JSON API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MakufonSkifto/RedditEasy",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    python_requires='>=3.6',
)
