from setuptools import setup, find_packages



setup(
    name = 'graphx',
    version = '0.0.4',
    keywords = 'graph',
    description = 'a library for Complex Network',
    license = 'MIT License',
    url = 'https://github.com/yorkchu1995/graphx/',
    author = 'York Chu',
    author_email = 'yorkchu1995@gmail.com',
    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = [],
    extras_require = {'all': ['copy', 'xlrd', 'matplotlib']}
)