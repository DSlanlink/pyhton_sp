import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

jfxm_order = pd.read_csv('./jfmx_order.csv',header=None,names=['acct','num','ym','yue','shuruyue','acctyue','detail'],dtype={'acct':np.int64,'ym':np.int64})
print(jfxm_order.sort_values(by=['acct','ym']))
jfmx_order_out_2 = jfxm_order.sort_values(by = ['acct','ym']) # 按照用户账号和缴费时间进行排序
jfmx_order_out_2.to_csv('./jfmx_order_out_2.csv',index=False,header=False,encoding='GB2312')
jfmx_order_out_2.hist(figsize=(10,8))

plt.show()

sdl_new = pd.read_csv('./sdl_new.csv',header=None
                     ,names=['acct','degrees','bills','ym']
                     ,dtype={'acct':np.int64,'ym':np.int64}
                     )  # 各字段注释：acct:用户账号，degrees：售电量，电表显示用电度数，每条记录表示每次查电表时读取的电表读数
#，bills：本月应缴纳的电费金额，每条记录表示每次查电表时统计的应缴纳的电费金额，ym：每次缴纳电费的时间
sdl_new_out_1 = sdl_new.sort_values(by=['acct','ym']) # 按照用户账号和缴费时间进行排序
sdl_new_out_1.to_csv('./sdl_new_out_1.csv',index=False,header=False,encoding='GB2312')
sdl_new_out_1.hist(figsize=(10,8))
plt.show()

# 2.1 计算每个账户每个月的用电量和缴费量
fi = open('.\\sdl_new_out_1.csv', encoding='utf-8')
fo = open('.\\mr_out_3_1_mergedegree.csv','w')

temp_key = ''
linesgroup = {}

def process_degree(linesgroup, fo):
    if (not linesgroup):
        return

    for item in linesgroup:
        degree_sum = 0
        fee_sum = 0
        for ll in linesgroup[item]:
            acct, degree, fee, date = ll.split(',')
            try:
                degree_sum = degree_sum + float(degree)
            except:
                pass
            try:
                fee_sum += float(fee)
            except:
                pass

        fo.write(','.join([item, str(degree_sum), str(fee_sum)]) + '\n')
    fo.flush()  # 刷新

while True:
    line = fi.readline()  # 读取一条记录
    if not line:
        break
    acct, degree, fee, date = line.split(',')
    key = acct + date[:6]
    if (key != temp_key):
        process_degree(linesgroup, fo)
        temp_key = key
        linesgroup = {}

    if (key not in linesgroup):
        linesgroup[key] = []

    linesgroup[key].append(line)

    # 2.2 统计每个账户每个月各种账户活动发生的数量
fi = open('.\\jfmx_order_out_2.csv', encoding='utf-8')
fo = open('.\\mr_out_3_2_jfmx.csv', 'w',encoding='utf-8')

cntall = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def processjfmxbymonth(linesgroup, fo):
    if not linesgroup:
        return

    strs = ['转电费', '存入', '调整帐目', '账目余额调入', '退电费', '调整违约金', '补入银行收费', '账目余额调出',
            '坏票或贴息处理', '未达项未达处理', '帐务核销']

    for item in linesgroup:
        cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for ll in linesgroup[item]:
            acct, index, date, fee, payment, balance, note = ll.split(',')
            note = note.strip()
            try:
                idx = strs.index(note)
                cnt[idx] += 1
                cntall[idx] += 1
            except:
                pass
        fo.write(item + ',' + (','.join(str(x) for x in cnt)) + '\n')
    fo.flush()


temp_key = ''
linesgroup = {}

while True:
    line = fi.readline()
    if not line:
        break
    acct, index, date, fee, payment, balance, note = line.split(',')
    key = acct + date[:6]
    if (key != temp_key):
        processjfmxbymonth(linesgroup, fo)
        temp_key = key
        linesgroup = {}

    if (key not in linesgroup):
        linesgroup[key] = []

    linesgroup[key].append(line)

fo.close()
fi.close()

# 2.3 计算当月月底的账户余额
InvalidNum = 111000000000


def process_yue(linesgroup, fo):
    if not linesgroup:
        return

    balance1 = InvalidNum  # 记录当月10号前的余额
    balance2 = 0  # 记录当月月底的余额

    for item in linesgroup:
        for ll in linesgroup[item]:
            acct, index, date, fee, payment, balance, note = ll.split(',')
            day = date[6:]
            b1 = 0
            day = int(day)

            try:
                b1 = float(balance)
            except:
                pass

            if (day < 10):
                balance1 = b1
            balance2 = b1
        fo.write(item + ',' + (','.join([str(balance1), str(balance2)]) + '\n'))
    fo.flush()

# 2.3 计算当月月底的账户余额
fi = open('.\\jfmx_order_out_2.csv', encoding='gbk')
fo = open('.\\mr_out_3_3_jfmxyue.csv', 'w', encoding='gbk')

temp_key = ''
linesgroup = {}

while True:
    line = fi.readline()
    if not line:
        break

    acct, index, date, fee, payment, balance, note = line.split(',')
    key = acct + date[:6]
    if (key != temp_key):
        process_yue(linesgroup, fo)
        temp_key = key
        linesgroup = {}
    if (key not in linesgroup):
        linesgroup[key] = []
    linesgroup[key].append(line)

fi.close()
fo.close()

# 2.4 计算下月10日前的账户余额
fi = open('.\\mr_out_3_3_jfmxyue.csv', encoding='gbk')
fo = open('.\\mr_out_3_4_jfmxyue', 'w')

InvalidNum = 111000000000


def processyuenextmonth(lastline, line, fo):
    key1, balance1, balance2 = lastline.split(',')
    date = key1[-6:]
    month = int(date[-2:])
    b2 = ''
    if (line):
        key2, balance12, balance22 = line.split(',')
        date2 = key2[-6:]
        month2 = int(date2[-2:])
        if (month2 - month == 1 and balance12 != str(InvalidNum)):
            b2 = balance12
        if ((month2 - month == -11) and (balance12 != str(InvalidNum))):
            b2 = balance12
    fo.write(','.join([key1, balance2.strip(), b2]) + '\n')
    fo.flush()


lastline = fi.readline()
key1, balance1, balance2 = lastline.split(',')
acc1 = key1[:-6]

while True:
    line = fi.readline()
    if not line:
        break
    key2, balance12, balance22 = line.split(',')
    acc2 = key2[:-6]
    if (acc2 != acc1):
        processyuenextmonth(lastline, None, fo)
    else:
        processyuenextmonth(lastline, line, fo)

    lastline = line

fi.close()
fo.close()

# 将上述步骤中得出的表，合并整理为新的用户缴费明细和用电量明细表
fi1 = open('.\\mr_out_3_1_mergedegree.csv', encoding='utf-8')
fi2 = open('.\\mr_out_3_2_jfmx.csv', encoding='utf-8')
fi3 = open('.\\mr_out_3_4_jfmxyue', encoding='utf-8')
fo = open('.\\finaldata.csv', 'w')

line1 = fi1.readline()
line2 = fi2.readline()
line3 = fi3.readline()

while True:
    if not line1 and not line2 and not line3:
        break
    pp1 = None
    key = "aaaaaaaaaaa"
    if line1:
        pp1 = line1.split(',')
        if (pp1[0] < key):
            key = pp1[0]

    pp2 = None
    if line2:
        pp2 = line2.split(',')
        if (pp2[0] < key):
            key = pp2[0]

    pp3 = None
    if line3:
        pp3 = line3.split(',')
        if (pp3[0] < key):
            key = pp3[0]

    acct = key[:-6]
    date = key[-6:]
    res = [acct, date, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

    if pp1:
        if (key == pp1[0]):
            res[2] = pp1[1].strip()
            res[3] = pp1[2].strip()
            line1 = fi1.readline()

    if pp2:
        if (key == pp2[0]):
            res[4] = pp2[1].strip()
            res[5] = pp2[2].strip()
            res[6] = pp2[3].strip()
            res[7] = pp2[4].strip()
            res[8] = pp2[5].strip()
            res[9] = pp2[6].strip()
            res[10] = pp2[7].strip()
            res[11] = pp2[8].strip()
            res[12] = pp2[9].strip()
            res[13] = pp2[10].strip()
            res[14] = pp2[11].strip()
            line2 = fi2.readline()

    if pp3:
        if (key == pp3[0]):
            res[15] = pp3[1].strip()
            res[16] = pp3[2].strip()
            line3 = fi3.readline()

    fo.write(','.join(res) + '\n')

fi1.close()
fi2.close()
fi3.close()
fo.close()