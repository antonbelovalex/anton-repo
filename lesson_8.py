#1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
n = int(input("Сколько друзей встретилось: "))

g = [[1 for _ in range(n)] for _ in range(n)]
sum_fr = 0

for i in range(n):
    g[i][i] = 0
    sum_fr += sum(g[i])

print(f'Встретилось {n} друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Всего было {sum_fr} рукопожатий')







#2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
import random

n = int(input("Введите количество вершин для создания графа для теста алгоритма: "))

g = [[random.randint(0, 3) for _ in range(n)] for _ in range(n)]

for i in range(n):
    g[i][i] = 0

def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float("inf")] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0

    while min_cost < float("inf"):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float("inf")
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    return f'Необходимо обойти {parent} вершины, кратчайшие пути займут {cost}'


print(g)
m = int(input("Из какой вершины просчитать путь: "))

print(dijkstra(g, m))


#3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).

# Примечания:
#
# a. граф должен храниться в виде списка смежности;
#
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
def graf_generation(n):
    g = [[i for i in range(n)] for _ in range(n)]

    for i in range(n):
        g[i].pop(i)

    return g


n = int(input("Введите количество вершин для создания графа: "))
inc = graf_generation(n)

visited = set()


def dfs(v):
    if v in visited:
        return
    visited.add(v)
    for i in inc[v]:
        if not i in visited:
            dfs(i)


start = int(input("Из какой вершины просчитать путь: "))
dfs(start)
print(visited)

