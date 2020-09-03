import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="My Cool Functions",  # Replace with your own username
    version="0.0.5",
    author="Jacob Padgett",
    author_email="jacobpad@gmail.com",
    description="A short description... no, I'm actually tall.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jacobpad/My-Library-DSPT7",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
