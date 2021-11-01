import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
datain = pd.read_csv('..\\finaldata.csv', header = None)
# 单独指定DateFrame的索引名
datain.columns = ["0.账户","1.日期","2.degrees","3.bills","4.zhuanru",
                    "5.cunru","6.tiaozheng","7.yuetiaoru","8.tuidianfei","9.weiyuejin",
                    "10.buruyinhang","11.yuetiaochu","12.huaizhang","13.weidabiao","14.acctcancel",
                    "15.balance1","16.balance2"]

# 将2.degrees到14.acctcancel字段为空的填0
datain[datain.iloc[:,2:15].isna()] = 0
datain.head()

# 将2.degrees到14.acctcancel字段为空的填0
datain[datain.iloc[:,2:15].isna()] = 0
datain.head()

# 统计余额为空的记录数
temp = datain
print(temp.shape)
cnt = temp.loc[temp.loc[:,"15.balance1"].isna()].shape[0]
cntold = 0
print(cnt, cntold)

# 当月余额数据缺失时，使用上个月的数据进行循环补充
while (cntold != cnt) and (0 != cnt):
    i = 0
    # 将余额列整体下移一位，拼接到源数据表的最右列
    ss = temp.iloc[:, 15]
    ns = np.r_[[None], ss.loc[:]]
    ns = pd.DataFrame(ns)
    temp = pd.concat([temp, ns[0:-1]], axis=1)

    # 将帐户列整体下移一位，拼接到源数据表的最右列
    tt = temp.iloc[:, 0]
    nt = np.r_[[None], tt.loc[:]]
    temp = pd.concat([temp, pd.DataFrame(nt)[0:-1]], axis=1)
    # print("columns is ", temp.columns[17])

    # 如果当前余额为空， 且当前账户和拼接账户一样
    # 则使用拼接的（上个月）余额赋值给当前月。
    tempIndex = (temp.iloc[:, 0] == temp.iloc[:, 18]) & (temp.iloc[:, 15].isna())
    temp.loc[tempIndex, '15.balance1'] = temp[tempIndex].iloc[:, 17]
    # 赋值填充后，再删除这两列
    temp = temp.iloc[:, 0:-2]

    # 重新计算余额为空剩余的记录数
    cntold = cnt
    cnt = temp.loc[temp.iloc[:, 15].isna()].shape[0]
    # print(cnt,cntold)

temp.head()

# 删除第15列余额任为空的行
datain = temp
print("before delete",datain.shape)
datain = temp[-temp.iloc[:,15].isna()]
datain = datain.reset_index(drop = True)   # 删除行后，行号要重新index下，不然后面concat会按行号拼接
print("after delete",datain.shape)

# 将16列中NA值，用15列进行覆盖
dataIndex = datain.iloc[:,16].isna()
datain.loc[dataIndex,'16.balance2'] = datain.loc[dataIndex,'15.balance1']
datain.head()

#以类似于当月余额拼接的方法，拼接下月10号前余额的数据
#取出16列，在16列的第一行加上一个NA，并去除16列最后一行
temp = datain
ss = temp.iloc[:,16]
ns = np.r_[[None], ss.iloc[:]]
ns = pd.DataFrame({'ns':ns})
temp = pd.concat([temp, ns[0:-1]], axis=1)

#取出1列，在1列的第一行加上一个NA，并去除1列最后一行
tt = temp.iloc[:,0]
nt = np.r_[[None], tt.iloc[:]]
nt = pd.DataFrame({'nt':nt})
temp = pd.concat([temp, nt[0:-1]], axis=1)

#将第一行用初始值进行填充
temp.iloc[0,17] = 0
temp.iloc[0,18] = 10000000442
temp.head(10)

#当月新消费=帐户下个月10号之前余额-(帐户这个月10号之前余额-当月总电费)，并追加在总表后面
pay = temp.iloc[:,16] - (temp.iloc[:,17] - temp.iloc[:,3])
pay = pd.DataFrame({'17.pay':pay})
temp = pd.concat([temp, pay], axis=1)
tempIndex = temp.iloc[:,18] != temp.iloc[:,0]
temp.loc[tempIndex, '17.pay'] = 0
temp = temp.drop(['ns','nt'], axis=1)
print(temp.shape)
temp.head()

#计算消费与当月总费用比重，并写入到最后一列
pratio = temp.iloc[:,17] / (temp.iloc[:,3] + 0.1)
pratio[pratio<=0] = 0
pratio[temp.iloc[:,3] <= 100] = 1
pratio = pd.DataFrame(pratio.values, columns=['18.ratio'])
temp = pd.concat([temp, pratio], axis=1)
temp.head()

#将消费小于0的全部重置为0
datain = temp
datain.loc[datain.iloc[:,17] < 0, '17.pay'] = 0
datain.head(20)

#将欠费的客户记flag为1
#当月下个月10号之前余额小于当月应缴电费，则判定为欠费
flag = pd.DataFrame(np.zeros((datain.shape[0], 1), dtype=int), columns=['19.flag'])
flag.loc[datain.iloc[:, 16] < datain.iloc[:, 3]] = 1
datain = pd.concat([datain, flag], axis=1)
datain.head()

#flag

#选取有用的列
datain = datain.iloc[:, [0, 1, 2, 3, 4, 5, 7, 9, 16, 17, 18, 19]]
datain.head()

#计算每度电所用的费用
uprice = abs(datain.iloc[:, 3] / (datain.iloc[:, 2] + 0.01))
uprice.loc[datain.iloc[:, 2] == 0] = 1
uprice[uprice>100] = 100
uprice = pd.DataFrame(uprice.values, columns=['20.price'])
datain = pd.concat([datain, uprice], axis=1)
datain.head()