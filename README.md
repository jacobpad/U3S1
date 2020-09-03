# U3S1

A collection of data science utility functions.

## [How to update](https://youtu.be/-Ijbaf6LkJ0?t=6963)

1. Change code
2. Update version number in `setup.py` file
3. Delete (3 grey) folders `build`, `dist` & `*.egg-info`
4. Run `python setup.py sdist bdist_wheel` & **Push to github** 
5. Run `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`

## Installation

```python
pip install -i https://test.pypi.org/simple/ My-Cool-Functions==0.0.1
```

## Usages

### ten_x

```python
from my_lambdata.ds_utilities import enlarge

print(ten_x(5))
```
