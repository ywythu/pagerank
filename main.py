

def read_file(filepath):
    content = []
    with open(filepath) as f:
        for line in f:
            content.append(line)
    return content


if __name__ == '__main__':
    graph = read_file('data/wiki.graph')
    print(len(graph))
