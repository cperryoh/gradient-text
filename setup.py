# setup.py
from setuptools import setup

setup(
    name="gradient_text",
    version="1.0",
    description="A tool to print text with a gradient between two colors.",
    author="Your Name",
    author_email="your.email@example.com",
    py_modules=["gradient_text"],  # The name of your script file (without .py)
    install_requires=["rich"],  # List of dependencies
    entry_points={
        "console_scripts": [
            "gradient-text=gradient_text:main",  # Command name and function to call
        ],
    },
)
