import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='bdc2df_win',  
    version='0.1',
    author="SilasMouraDev",
    author_email="silas_moura_5@hotmail.com",
    description="Utility for loading dbc files into Pandas DataFrames",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SilasMouraDev/bdc2df_win",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ]
)