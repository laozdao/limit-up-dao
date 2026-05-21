from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="limit-up-dao",
    version="2.0.0",
    author="老子道",
    author_email="laozdao@126.com",
    description="A股涨停股批量归因分析工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/laozdao/limit-up-dao",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Office/Business :: Financial :: Investment",
    ],
    python_requires=">=3.8",
    install_requires=[
        "akshare>=1.10.0",
        "pandas>=1.5.0",
        "requests>=2.28.0",
    ],
    entry_points={
        "console_scripts": [
            "limit-up-dao=src.cli:main",
        ],
    },
)
