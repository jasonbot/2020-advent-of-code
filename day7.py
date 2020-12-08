import collections
import functools
import re


DESCRIPTION = re.compile("(?P<bag_name>.+)(?: bag[s]?) contain (?P<sentence>.+)[.]")


def build_graph():
    graph = collections.defaultdict(lambda: collections.defaultdict(int))

    with open('day7.input') as input:
        for line in input:
            line = line.strip()
            bag_groups = DESCRIPTION.match(line).groups()
            bag_name = bag_groups[0]
            bag_sentence = bag_groups[1].strip('.')
            parts = [s.strip() for s in bag_sentence.split(",")]
            print(bag_sentence, parts)
            for line in parts:
                ct = line.split(' ')[0]
                count = (int(ct) if ct.lower() != 'no' else 0)
                rest = ' '.join(line.split(' ')[1:-1])
                print("BNCR", bag_name, count, rest)
                graph[bag_name][rest] += count

    return graph


def traverse_graph(start_key, graph, traversal=None):    
    if start_key in graph:
        if traversal is None:
            traversal = set()
        else:
            if start_key in traversal:
                return traversal

            traversal.add(start_key)

        for key in graph[start_key]:
            traverse_graph(key, graph, traversal)
            pass

    return traversal


def traverse_total(start_key, graph, num=(), items=None):
    if items is None:
        items = [(start_key, num)]
    for subitem, total in graph[start_key].items():
        for item in traverse_total(subitem, graph, num + (total, )):
            items.append(item)
    return items

graph = build_graph()
for key in graph:
    traversal = traverse_graph(key, graph)


print(sum(1 if 'shiny gold' in traverse_graph(key, graph) else 0 for key in graph))
print('shiny gold')
print(graph['shiny gold'])
print('-----')
traversal = traverse_total('shiny gold', graph)


reduction = [functools.reduce(lambda x, y: x * y, i[1], 1) for i in traversal]
print(sum(reduction))
