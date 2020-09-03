# U3S1 - [Proof it works](https://colab.research.google.com/drive/1onnzNbt6q7j-_Iy6Wgwt5w_9Nb4b0VpH?usp=sharing)

A collection of data science utility functions.

## [How to update](https://youtu.be/-Ijbaf6LkJ0?t=6963)

1. Change/add/remove/edit code
2. Update version number in `setup.py` file
3. Delete (3 grey) folders `build`, `dist` & `*.egg-info`
4. Update version number in the README.md instructions
5. Save everything!!!
6. Run `python setup.py sdist bdist_wheel`  
7. Run `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`
8. **Push to github**

## Installation

```python
pip install -i https://test.pypi.org/simple/ My-Cool-Functions==0.0.5
```

## Usages

### ten_x

```python
from my_data.ds_utilities import enlarge

print(ten_x(5))
```

### replace_spaces_with_underscore_in_column_names_and_make_lowercasee

```python
from my_data.ds_utilities import replace_spaces_with_underscore_in_column_names_and_make_lowercase
```

```python
import pandas as pd

cols = ['fixed acidity','volatile acidity','citric acid','residual sugar',
         'chlorides','free sulfur dioxide','total sulfur dioxide','density',
         'pH','sulphates','alcohol','quality']

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
df = pd.read_csv(url, sep=';', header=None, names=cols, skiprows=1)

df = replace_spaces_with_underscore_in_column_names_and_make_lowercase(df)

df.head()
```
