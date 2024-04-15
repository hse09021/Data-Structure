from quickSort import *
from mergeSort import *

def do_sort(input_file):
    data_file = open(input_file)
    dic = dict()
    val = []

    for line in data_file.readlines():
        lpn = line.split()[0]
        if lpn in dic:
            dic[lpn] += 1
        else:
            dic[lpn] = 1

    for i in dic:
        val.append(dic[i])

    mergeSort(val, 0, len(val) - 1)
    val.reverse()

    for i in range(10):
        for j in dic:
            if dic[j] == val[i]:
                print(j, val[i])
                del dic[j]
                break

if __name__=="__main__":
    do_sort("linkbench_short.trc")