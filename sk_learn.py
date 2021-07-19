from sklearn import datasets as ds
import numpy as np
from sklearn.model_selection import train_test_split as tt

iris = ds.load_iris()
x = iris.data
y = iris.target
print(x.shape, y.shape)

x_train, x_test, y_train, y_test = tt(x, y, test_size=0.2)
print(x_train.shape)
print(x_test.shape)

