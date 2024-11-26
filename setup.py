from setuptools import setup, find_packages

setup(
    name="CICD test",
    version="0.1.0",
    author="Jeahyuk Jeong",
    author_email="jeong_j1@denison.edu",
    description="A short description of your project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ban-thing/CICD_test.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=[
        # List your dependencies here
        "numpy",
        "requests",
        "scikit-learn",
        "torch",
        "sentence-transformers",
        "flask",
    ],
)
