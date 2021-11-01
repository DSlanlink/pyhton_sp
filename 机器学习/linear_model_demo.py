from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def linear_model1():
    boston = load_boston()

    x_train,x_test,y_train,y_test  = train_test_split(boston.data,boston.target,test_size=0.2)

    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)

    estimator = LinearRegression()
    estimator.fit(x_train,y_train)

    y_pre = estimator.predict(x_test)
    print('预测值是：',y_pre)

    score = estimator.score(x_test,y_test)
    print('准确率是：',score)

    ret = mean_squared_error(y_test,y_pre)
    print('均方误差是：',ret)



if __name__ == '__main__':
    linear_model1()