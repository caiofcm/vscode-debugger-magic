from setuptools import setup
from codecs import open
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vscode_debugger_magic',
    version='0.1',
    description='Magic for Vscode debugging from Jupyter notebook',
    long_description=long_description,
    author='Caio Marcellos',
    author_email='caiocuritiba@gmail.com',
    packages=['vscode_debugger_magic'],
    install_requires=['ipython'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: OS Independent',

        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords = 'vscode code jupyter notebook debugging',
    project_urls={
        # 'Source': 'https://github.com/MiniZinc/iminizinc/',
        # 'Tracker': 'https://github.com/MiniZinc/iminizinc/issues',
    },
)
