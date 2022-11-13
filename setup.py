from setuptools import setup


setup(
    name='pytils',
    version='1.0.2',
    packages=['pytils'],
    include_package_data=True,
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    url='https://github.com/johanlundahl/pytils',
    install_requires=[
        'argparse',
        'python-box',
        'pyyaml',
        'requests',
        'flask'
    ]
)
