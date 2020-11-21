import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="corona_python",
    version="1.0.0",
    author="MakufonSkifto",
    author_email="emirsurmen@gmail.com",
    license="MIT",
    description="A Python 3 wrapper for the COVID-19 API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MakufonSkifto/corona-python",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)