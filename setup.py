from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='brawlstarswrapper',
    version='0.0.1',
    description='A wrapper for a brawl stars API.',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Muhammad Shafeeq',
    author_email='contactme@aspireyoung.me',
    license='MIT',
    classifiers=classifiers,
    keywords='wrapper',
    packages=find_packages(),
    install_requires=['requests==2.25.1']
)