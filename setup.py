import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="redditeasy",
    version="3.6.2",
    author="MakufonSkifto",
    description="RedditEasy is an API wrapper for getting posts using the Reddit JSON API with both sync and"
                " async options",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://redditeasy.readthedocs.io/en/latest/",
    project_urls={
        "Documentation": "https://redditeasy.readthedocs.io/en/latest/",
        "Issue tracker": "https://github.com/MakufonSkifto/RedditEasy/issues",
        "Source": "https://github.com/MakufonSkifto/RedditEasy"
    },
    packages=setuptools.find_packages(),
    install_requires=["requests", "python-dotenv", "aiohttp"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux"
    ],
    keywords="reddit api async meme redditapi redditbot asyncreddit redditposts praw discord.py bot",
    python_requires='>=3.6',
)
