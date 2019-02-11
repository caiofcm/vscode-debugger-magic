import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="vscode-debugger-magic",
    version="1.2.0",
    description="A Ipython (Jupyter) magic for attaching a debugging session on VSCode ",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/caiofcm/vscode-debugger-magic",
    author='Caio Marcellos',
    author_email='caiocuritiba@gmail.com',
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    # packages=["vscode_debugger_magic"],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["ipython", "ptvsd"],
)
