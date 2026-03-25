from setuptools import setup, find_packages

setup(
    name="kali", 
    version="1.0.2",
    author="Aditya Rai",
    author_email="adityarai0133@gmail.com", 
    description="A lightweight RAM optimizer for legacy systems",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tera-username/rai-ram", # Apni GitHub repo ka link
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
