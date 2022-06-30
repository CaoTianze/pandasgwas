import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pandasgwas",
    version="0.99.6",
    author="Cao Tianze",
    author_email="hnrcao@qq.com",
    description="A Python package to query, download and wrangle GWAS catalog data",
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
    install_requires=['pandas>=1.4.2', 'requests>=2.27.1', 'progressbar2>=4.0.0'],
    license="MIT",
    keywords="GWAS pandas",
    package_data={
        "": ["*.csv"]
    }
)
