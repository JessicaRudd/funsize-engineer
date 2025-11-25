from setuptools import setup, find_packages

setup(
    name="funsize-engineer",
    version="0.1.0",
    author="Jessica Rudd",
    author_email="jessica.rudd@fanduel.com",
    description="A personal calling card for Jessica Rudd",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JessicaRudd/funsize-engineer",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "funsize-engineer=funsize_engineer.card:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
