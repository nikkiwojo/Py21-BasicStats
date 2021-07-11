from typing import List
import math

def zcount(list: List[float]) -> float:
    
    return len(list)


def zmean(list: List[float]) -> float:
    
    return sum(list) / zcount(list)


def zmode(list: List[float]) -> float:

    return max(set(list), key = list.count)


def zmedian(list: List[float]) -> float:

    sortedList = sorted(list)
    n = len(list)
    index = (n -1) // 2

    if (n % 2 != 0):
        return sortedList[index]
    else:
        return (sortedList[index] + sortedList[index + 1]) / 2


def zvariance(list: List[float]) -> float:
    
    n = zcount(list) - 1
    mean = zmean(list)
    deviation = [abs(mean - xi) ** 2 for xi in list]
    variance = sum(deviation) / negative

    return variance

def zstddev(list: List[float]) -> float:

    var = zvariance(list)

    return math.sqrt(var)


def zstderr(list: List[float]) -> float:

    sd = zstddev(list)
    n = zcount(list)

    return sd / math.sqrt(n)


def zcov(listx: List[float], listy: List[float]) -> float:
    
    n = zcount(listx)
    sum_of_product = 0
    counter = 0
    
    while counter < len(listx):
        product = listx[counter] * listy[counter]
        sum_of_product += product
        counter += 1
    
    sums = (sum(listx) * sum(listy)) / n

    cov = (sum_of_product - sums) / (n - 1)
    return cov


def zcorr(listx: List[float], listy: List[float]) -> float:
    
    cov = zcov(listx, listy)
    sx = zstddev(listx)
    sy = zstddev(listy)

    return (cov) / (sx * sy)



def readDataSets(files):
#    print("in ReadDataSets...", files)
    data = {}
    for file in files:
        twoLists = readDataFile(file)
        data[file] = twoLists

    return data

def readDataFile(file):
    x, y = [], []
    with open(file) as f:
        first_line = f.readline() # consume headers
        for l in f:
            row = l.split(',')
            #  print(row, type(row))
            x.append(float[row[0]])
            y.append(float[row[1]])
    
    return (x,y)
