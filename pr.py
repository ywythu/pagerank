import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    data = pd.DataFrame()
    node = []
    pr = []
    with open("data/wiki.pagerank", "r") as f:
        for line in f:
            line = line.strip("\n").split()
            node.append(line[0])
            pr.append(line[1])
        data['node'] = node
        data['pr'] = pr
        data2 = pd.read_csv("indegree_nodes.csv").sort_values(by='nodes')
        data['indegree'] = data2['indegree'].tolist()
        data['outdegree'] = data2['outdegree'].tolist()
        data = data.sort_values(by='pr')
        # print(data2)
        print(data[:20])
        print(data.sort_values(by='pr', ascending=False)[:20])
        # data = data.sort_values(by='pr', ascending=True).to_csv("pr_rank_low.csv")
        # pr_ = data['pr'].value_counts().sort_index().to_csv("pr_sort.csv")
        # p1 = plt.plot(pr_.values.tolist()[:200])
        # plt.ylabel('pr')
        # plt.title('plt of_first data')
        # plt.show()


if __name__ == "__main__":
    main()
