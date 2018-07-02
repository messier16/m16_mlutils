import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="m16_mlutils",
    version="0.0.1",
    author="Antonio Feregrino",
    author_email="antonio.feregrino@gmail.com",
    description="Some stuff that is probably better implemented somewhere else but I'm still a newbie to find out where...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/messier16/m16_mlutils",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)