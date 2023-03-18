import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pandasgwas",
    version="0.99.12",
    author="Cao Tianze",
    author_email="hnrcao@qq.com",
    description="A Python package for easy retrieval of GWAS Catalog data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/caotianze/pandasgwas",
    project_urls={
        "Bug Tracker": "https://github.com/caotianze/pandasgwas/issues",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # package_dir={"": "pandasgwas"},
    packages=['pandasgwas'],
    python_requires=">=3.8",
    install_requires=['pandas>=1.4.3', 'requests>=2.28.1', 'progressbar2>=4.0.0'],
    license="MIT",
    keywords=['gwas', 'genomics', 'snp', 'bioinformatics','pandas'],
    package_data={
        "": ["*.csv","*.txt"]
    }
)
