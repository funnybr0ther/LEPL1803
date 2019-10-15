from collections import defaultdict
from urllib.parse import unquote

def convert_to_adj(file_path):
    with open(file_path, "r") as file:
        lines = file.read().splitlines()
    unquotedLines = [unquote(item) for item in lines[4:]]
    dictDuCul = {k: [] for k, _ in map(lambda l: tuple(l.split("\t")), unquotedLines)}
    [dictDuCul[k].append(v) for k, v in map(lambda l: tuple(l.split("\t")), unquotedLines)]
    return dictDuCul

def dijkstra_shortest_path(graph, start, destination):
    unvisited = {i: True for i in list(graph.keys())}
    distances = {i: len(graph) + 1 for i in unvisited}
    distances[start] = 0
    previous = {i: None for i in list(graph.keys())}
    previous[start] = None

    def visitAndUpdate(key):
        for neighbour in graph[key]:
            if neighbour not in graph:
                distances[neighbour] = distances[key] + 1
                previous[neighbour] = key
            elif distances[neighbour] > distances[key] + 1:
                distances[neighbour] = distances[key] + 1
                previous[neighbour] = key
        unvisited.pop(key, None)

    while len(unvisited) != 0:
        nextItem =min(unvisited, key=lambda vtx: distances[vtx])
        visitAndUpdate(nextItem)
    path =[]
    prev = destination
    if previous[destination]==None:
        return path
    while prev!=None:
        path = [prev]+path
        prev = previous[prev]
    return path

print(dijkstra_shortest_path(convert_to_adj("links.tsv"),"Adolf_Hitler","Osteomalacia"))

