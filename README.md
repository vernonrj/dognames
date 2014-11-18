dognames
========

Randomly generates dog names, because why not?

To use, you'll first need to set up PyHyphen, which you can get at https://pypi.python.org/pypi/PyHyphen/

You'll probably need to install a hyphen language pack unless you've already done this (you'll probably need to run this as root)

```python
import hyphen.dictools
hyphen.dictools.install('en_US')
```

after that you can just run this script normally

```sh
python dognames.py
```
