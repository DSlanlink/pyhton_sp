from sklearn.linear_model import LinearRegression

x = [[80,86],
      [82,80],
      [85,78],
      [90,90],
     [86,82],
     [82,90],
     [78,80],
     [92,94]]

y = [84.2,80.6,80.1,90,83.2,87.6,79.4,93.4]

estimator = LinearRegression()

estimator.fit(x,y)

coef = estimator.coef_
print('系数：',coef)
print("预测值是：",estimator.predict([[80,100]]))