import numpy as np
from sklearn.linear_model import Linear_regression
import matplotlib.piplot as plt

x = np.array([5, 10, 15, 25, 30]).reshape()
y = np.array([6, 12, 14, 23, 27, 32])
model = Linear_regression().fit(x, y)
y_pred = model.predict(x)

print('dados de teste', y, sep='\n')
print('dados da preddição', y_pred, sep='\n')
plt.scatter(x, y, c="blue")
plt.plot(x, y_pred, c="red")
pl.legend(['predição', 'Real'])

