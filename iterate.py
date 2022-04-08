import sys


# import time


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
    pr = []
    temp_i = []
    s = 0
    for i in range(n):
        pr.append(1 / n)
        temp_i.append((1 - alpha) / n)
        if outdegree[i] == 0:
            s += pr[i]
    for k in range(1, 2000):
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
        print(f"{k}turn:")
        comp(pr)

        if k == 20:
            for i in range(n):
                sys.stdout.write(str(vec[i]) + ' ' + '{:.8f}'.format(pr[i]) + '\n')
                sys.stdout.write("{} {:.10f}\n".format(item[0], item[1]))
            break


def main():
    content, vec = read_file()
    vec = list(vec)
    vec.sort()
    pagerank(content, vec)


if __name__ == '__main__':
    main()