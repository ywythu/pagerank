import sys
<<<<<<< HEAD


# import time
=======
# import time
import numpy as np
>>>>>>> 8dda32929c9eb2a50732c4b5a8296fee2394e1be


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


<<<<<<< HEAD
def comp(pr):
    with open("data/wiki.pagerank") as f:
        ite = 0
        dis = 0
        for line in f:
            line = line.strip('\n').split(" ")
            dis += (pr[ite] - float(line[1])) ** 2
            if ite == 1 or ite == 100 or ite == 300 or ite == 500:
                print('{:.8f}'.format(pr[ite]), f" : {line[1]}")
            ite += 1
        print(f"dis:{dis ** 0.5}")
        return


def pagerank(content, vec):
    n = len(vec)
    alpha = 0.8
=======
def pagerank(content, vec):
    # print("pagerank start")
    n = len(vec)
    alpha = 0.85
>>>>>>> 8dda32929c9eb2a50732c4b5a8296fee2394e1be
    outdegree = []
    dic = {}
    for i in range(n):
        dic[vec[i]] = i
    for i in range(n):
        outdegree.append(0)
    for i in range(len(content)):
        # print(i)
        index_i = dic[content[i][0]]
        outdegree[index_i] += len(content[i][1])
<<<<<<< HEAD
=======
    outdegree = np.array(outdegree)
>>>>>>> 8dda32929c9eb2a50732c4b5a8296fee2394e1be
    pr = []
    temp_i = []
    s = 0
    for i in range(n):
        pr.append(1 / n)
        temp_i.append((1 - alpha) / n)
        if outdegree[i] == 0:
            s += pr[i]
<<<<<<< HEAD
    for k in range(1, 2000):
=======
    pr = np.array(pr)
    temp_i = np.array(temp_i)
    for k in range(1, 201):
        pr_old = pr.copy()
>>>>>>> 8dda32929c9eb2a50732c4b5a8296fee2394e1be
        for i in range(len(content)):
            index_i = dic[content[i][0]]
            for j in content[i][1]:
                index_j = dic[j]
                temp_i[index_j] += alpha * pr[index_i] / outdegree[index_i]
<<<<<<< HEAD

        for i in range(n):
            pr[i] = temp_i[i] + alpha * s / n
            temp_i[i] = (1 - alpha) / n
=======
        pr = temp_i + alpha * s / n
        temp_i = np.ones(temp_i.shape) * ((1 - alpha) / n)
>>>>>>> 8dda32929c9eb2a50732c4b5a8296fee2394e1be
        s = 0
        for i in range(n):
            if outdegree[i] == 0:
                s += pr[i]
<<<<<<< HEAD
        print(f"{k}turn:")
        comp(pr)

        if k == 20:
            for i in range(n):
                sys.stdout.write(str(vec[i]) + ' ' + '{:.8f}'.format(pr[i]) + '\n')
                sys.stdout.write("{} {:.10f}\n".format(item[0], item[1]))
=======

        dis = np.linalg.norm(pr_old - pr)
        if dis < 1e-8:
            for i in range(n):
                sys.stdout.write(str(vec[i]) + ' ' + str(pr[i]) + '\n')
>>>>>>> 8dda32929c9eb2a50732c4b5a8296fee2394e1be
            break


def main():
<<<<<<< HEAD
    content, vec = read_file()
    vec = list(vec)
    vec.sort()
    pagerank(content, vec)
=======
    # time1 = time.time()
    content, vec = read_file()
    vec = list(vec)
    vec.sort()
    # time2 = time.time()
    # print(len(content), len(vec))
    # print(time2 - time1)
    # print(vec)
    pagerank(content, vec)
    # time3 = time.time()
    # print(time3 - time2)
>>>>>>> 8dda32929c9eb2a50732c4b5a8296fee2394e1be


if __name__ == '__main__':
    main()