import os
import binascii
import time
import csv
import statistics
from ex_euclid import ex_euclid
from exEuclidExp import exEuclidExp
from exEuclidTime import exEuclidTime


def main():
    #(1)1024ビットの数 g を 10^4 個生成
    print('(1)1024ビットの数 g を 10^4 個生成。生成数はtable1.csvに出力')
    a=[]
    for i in range(10000):
        a.append(int(binascii.hexlify(os.urandom(1024)), 16))

    #ファイルに出力
    filename ='table1.csv'
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(a)

    #(2)平均時間と標準偏差
    print('(2)平均時間と標準偏差')
    p1 = 179769313486231590770839156793787453197860296048756011706444423684197180216158519368947833795864925541502180565485980503646440548199239100050792877003355816639229553136239076508735759914822574862575007425302077447712589550957937778424442426617334727629299387668709205606050270810842907692932019128194467627007
    sample = []
    taketime0 = time.perf_counter()
    for g in a:
        takingtime = exEuclidTime(g, p1)
        sample.append(takingtime)
        taketime1 = time.perf_counter() - taketime0
    print(f'it takes {taketime1} seconds for 10^4 iteratings')
    print(f'mean is {taketime1/10000} seconds')
    std = statistics.pstdev(sample)
    print(f'std is {std}')

    #(3)ステップ数の平均回数と標準偏差
    print('(3)ステップ数の平均回数と標準偏差')
    sample = []
    for g in a:
        steps = exEuclidExp(g, p1)[3]
        sample.append(steps)
    wholeSteps = sum(sample)
    print(f'it takes {wholeSteps} steps for 10^4 iteratings')
    print(f'mean is {wholeSteps/10000} steps')
    std2 = statistics.pstdev(sample)
    print(f'std is {std2}')

    #(4)512ビットの数 g を 10^4 個生成
    print('(4)512ビットの数 g を 10^4 個生成。生成数はtable2.csvに出力')
    b=[]
    for i in range(10000):
        b.append(int(binascii.hexlify(os.urandom(512)), 16))

    #ファイルに出力
    filename ='table2.csv'
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(b)

    #(5)平均時間と標準偏差
    print('(5)平均時間と標準偏差')
    p1 = 179769313486231590770839156793787453197860296048756011706444423684197180216158519368947833795864925541502180565485980503646440548199239100050792877003355816639229553136239076508735759914822574862575007425302077447712589550957937778424442426617334727629299387668709205606050270810842907692932019128194467627007
    sample = []
    taketime2 = time.perf_counter()
    for g in b:
        takingtime = exEuclidTime(g, p1)
        sample.append(takingtime)
    taketime3 = time.perf_counter() - taketime0
    print(f'it takes {taketime3} seconds for 10^4 iteratings')
    print(f'mean is {taketime3/10000} seconds')
    std3 = statistics.pstdev(sample)
    print(f'std is {std3}')

    #(6)ステップ数の平均回数と標準偏差
    print('(6)ステップ数の平均回数と標準偏差')
    sample = []
    for g in b:
        steps = exEuclidExp(g, p1)[3]
        sample.append(steps)
    wholeSteps2 = sum(sample)
    print(f'it takes {wholeSteps2} steps for 10^4 iteratings')
    print(f'mean is {wholeSteps2/10000} steps')
    std4 = statistics.pstdev(sample)
    print(f'std is {std4}')

if __name__ == '__main__':
    main()