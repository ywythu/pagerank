import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_file():
    content = []
    se = set()
    turn = 0
    f = sys.stdin.readlines()
    for line in f:
        # if turn > 20:
        #     break
        line = line.split(":")
        line[0] = int(line[0])
        line[1] = line[1].strip("\n").split(",")
        se.add(line[0])
        if line[1][0] == '':
            continue
        line[1] = [int(x) for x in line[1]]
        for e in line[1]:
            se.add(e)
        # print(line)
        content.append(line)
        # turn += 1
    return content, se


def main():
    content, vec = read_file()
    vec = list(vec)
    vec.sort()
    n = len(vec)
    dic = {}
    for i in range(n):
        dic[vec[i]] = i
    indegree = []
    outdegree = []
    for i in range(n):
        indegree.append(0)
        outdegree.append(0)
    for i in range(len(content)):
        index_i = dic[content[i][0]]
        for j in content[i][1]:
            index_j = dic[j]
            indegree[index_j] += 1
            outdegree[index_i] += 1
    data = pd.DataFrame()
    data.insert(0, 'nodes', vec)
    data.insert(1, 'indegree', indegree)
    data.insert(2, 'outdegree', outdegree)
    data.sort_values(by='indegree', ascending=False).to_csv("indegree_nodes.csv")
    data.sort_values(by='outdegree', ascending=False).to_csv("outdegree_nodes.csv")
    # print(data['indegree'].value_counts().sort_index().tolist())
    # print(data['outdegree'].value_counts().sort_index().tolist())
    # data['indegree'].value_counts().sort_index().to_csv("indegree.csv")
    # data['outdegree'].value_counts().sort_index().to_csv("outdegree.csv")
    # ind = pd.read_csv("indegree.csv")
    # outd = pd.read_csv("outdegree.csv")
    # p1 = plt.plot(outd.values.tolist()[:200])
    # plt.ylabel('outdegree')
    # plt.title('plt of_first data')
    # plt.show()


if __name__ == "__main__":
    main()
