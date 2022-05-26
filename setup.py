import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ran-quote-ovaixe",
    version="0.0.1",
    author="Bhat Owais",
    author_email="owaisbhat996@outlook.com",
    description="A simple package which gets a random quote",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ovaixe/random-quote",
    project_urls={
        "Bug Tracker": "https://github.com/ovaixe/random-quote/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=['requests'],
)

