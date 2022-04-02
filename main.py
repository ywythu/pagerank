import time


def read_file(filepath):
    content = []
    with open(filepath) as f:
        for line in f:
            line = line.split(":")
            line[1] = line[1].strip("\n").split(",")
            if len(line[1]) < 1:
                print(line[1])
            content.append(line)
    return content


if __name__ == '__main__':
    read_start = time.time()
    graph = read_file('data/wiki.graph')
    read_end = time.time()
    # print(graph)
    print ('read data:', read_end - read_start)
