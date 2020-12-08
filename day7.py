import collections
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
            traversal = {start_key}
        else:
            if start_key in traversal:
                return traversal

            traversal.add(start_key)

        for key in graph[start_key]:
            traverse_graph(key, graph, traversal)
            pass

    return traversal

graph = build_graph()
for key in graph:
    print(traverse_graph(key, graph))

print(sum(1 if 'shiny gold' in traverse_graph(key, graph) else 0 for key in graph))
