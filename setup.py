import setuptools

with open("README.md", "r") as fh:
    long_describtion = fh.read()

setuptools.setup(
    name="test package to print text",
    version="0.0.1",
    author="Andrey Sivyakov",
    description="My test package to see how this works.",
    python_requires='>=3.6'
)