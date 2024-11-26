from setuptools import setup, find_packages

setup(
    name="your_project_name",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description of your project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/wjdwpgur23/banthig/CICD_test",
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