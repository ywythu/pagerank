import sys

import numpy as np
import sys


def read_file():
    content = []
    se = set()
    turn = 0
    f = sys.stdin.readlines()
    for line in f:
        line = line.split(":")
        line[0] = int(line[0])
        line[1] = line[1].strip("\n").split(",")
        se.add(line[0])
        if line[1][0] == '':
            continue
        line[1] = [int(x) for x in line[1]]
        for e in line[1]:
            se.add(e)
        content.append(line)
    return content, se


def pagerank(content, vec):
    n = len(vec)
    alpha = 0.85
    outdegree = []
    dic = {}
    for i in range(n):
        dic[vec[i]] = i
    for i in range(n):
        outdegree.append(0)
    for i in range(len(content)):
        index_i = dic[content[i][0]]
        outdegree[index_i] += len(content[i][1])
    pr = []
    temp_i = []
    s = 0
    for i in range(n):
        pr.append(1 / n)
        temp_i.append((1 - alpha) / n)
        if outdegree[i] == 0:
            s += pr[i]
    for k in range(1, 51):
        for i in range(len(content)):
            index_i = dic[content[i][0]]
            for j in content[i][1]:
                index_j = dic[j]
                temp_i[index_j] += alpha * pr[index_i] / outdegree[index_i]

        for i in range(n):
            pr[i] = temp_i[i] + alpha * s / n
            temp_i[i] = (1 - alpha) / n
        s = 0
        for i in range(n):
            if outdegree[i] == 0:
                s += pr[i]

        if k == 2:
            for i in range(n):
                sys.stdout.write("{} {:.10f}\n".format(vec[i], pr[i]))
            return


def main():
    content, vec = read_file()
    vec = list(vec)
    vec.sort()
    pagerank(content, vec)


if __name__ == '__main__':
    main()

