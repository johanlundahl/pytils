from setuptools import setup, find_packages

setup(
    name='pytils',
    version='0.3',
    packages=find_packages(include=['pytils', 'pytils.*']),
    scripts=['validator.py'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    long_description_content_typ='text/markdown',
    url='https://github.com/johanlundahl/pytils'
)
