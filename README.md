[![Lint](https://github.com/johanlundahl/pytils/actions/workflows/code-quality.yml/badge.svg)](https://github.com/johanlundahl/pytils/actions/workflows/code-quality.yml)
[![Tests](https://github.com/johanlundahl/pytils/actions/workflows/python-package.yml/badge.svg)](https://github.com/johanlundahl/pytils/actions/workflows/python-package.yml)

# pytils

A python package with various utility modules such as
* config
* date
* http
* key_generator?
* log
* logging
* method_chaining
* slack
* validator

## Installation

To modify the source code start by cloning the git repo
```
$ git clone https://github.com/johanlundahl/pytils
```

## Tests
Run the test of the module
```
$ make test

```

## Use in other projects

If you want to install the module to use with another python project
```
$ pip3 install git+https://github.com/johanlundahl/pytils.git
```

Or include the following in the requirements.txt
```
git+https://github.com/johanlundahl/pytils.git
```