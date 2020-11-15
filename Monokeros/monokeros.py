def search_node(nodes, value):
    for node in nodes:
        if node[0][0] < value <= node[0][1]:
            result = node
            nodes.remove(result)
            return result


def monokeros(numbers):
    nodes = [((float('-Inf'), float('Inf')), 1)]

    for element in numbers:
        node = search_node(nodes, element)
        ((left, right), level) = node
        nodes.insert(0, ((left, element), level + 1))
        nodes.insert(1, ((element, right), level + 1))
        print(level, end=' ')


if __name__ == '__main__':
    number_of_elements = int(input())
    elements = map(int, input().split())
    monokeros(elements)