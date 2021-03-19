import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="redditeasy",
    version="2.9.1",
    author="MakufonSkifto",
    description="RedditEasy is an API wrapper for the Reddit JSON API that supports "
                "both asynchronous and synchronous programs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MakufonSkifto/RedditEasy",
    packages=setuptools.find_packages(),
    install_requires=["requests", "python-dotenv", "aiohttp"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    keywords="reddit api async",
    python_requires='>=3.0',
)
