
import numpy as np
import sys


def read_file(filepath):
    content = []
    se = set()
    np.set_printoptions(precision=10)
    turn = 0
    f = sys.stdin.readlines()
    for line in f:
        if turn > 40:
            break
        line = line.split(":")
        line[0] = int(line[0])
        line[1] = line[1].strip("\n").split(",")
        if line[1][0] != '':
            line[1] = [int(x) for x in line[1]]
        se.add(line[0])
        for e in line[1]:
            if e != '':
                se.add(e)
        content.append(line)
        turn += 1
    return content, se


def create_matrix(g, v):
    num = len(v)
    matrix = np.zeros((num, num))
    dic = {}
    for i in range(len(v)):
        dic[v[i]] = i
    for i in range(len(g)):
        i_index = dic[g[i][0]]
        for j in g[i][1]:
            matrix[i_index][dic[j]] = 1

    col_num = matrix.shape[1]
    row_num = 0
    for row in matrix:
        if sum(row) == 0:
            for col in range(col_num):
                matrix[row_num][col] = 1
        row_num += 1

    row_num = 0
    for row in matrix:
        n = sum(row)
        col_num = 0
        for col in row:
            matrix[row_num][col_num] = col / n
            col_num += 1
        row_num += 1

    return matrix


def create_pr(g, v):
    pr = []
    num = len(v)
    for i in range(num):
        pr.append(1 / num)
    pr = np.array(pr)
    return pr


def pagerank(mat, pr, v):
    num = mat.shape[1]
    alpha = 0.85
    divide = (1 - alpha) / num
    divide_vec = divide * np.ones(num)

    for i in range(1, 201):
        pr_new = alpha * np.dot(pr, mat) + divide_vec

        print(f"第{i}次迭代pr:{pr_new}")
        print(f"正确性{np.sum(pr_new)}")
        if np.linalg.norm(pr_new - pr) < 1e-7:
            break

        pr = pr_new
    # for i in range(num):
    #     sys.stdout.write(str(v[i]) + ' ' + str(pr[i]) + '\n')


if __name__ == '__main__':
    graph, se = read_file('data/wiki.graph')
    vec = list(se)
    vec.sort()

    mat = create_matrix(graph, vec)

    pr = create_pr(graph, vec)

    pagerank(mat, pr, vec)

