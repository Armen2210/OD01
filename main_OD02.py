# Стек (Stack) — это структура данных, работающая по принципу "последний пришел, первый ушел" (Last In, First Out, LIFO).
# push — добавление элемента в стек,
# pop — удаление верхнего элемента,
# peek — получение верхнего элемента без удаления,
# is_empty — проверка, пуст ли стек

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

stack = Stack() # Создаем объект класса

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.is_empty())
print(stack.peek())

#Очередь (Queue) — это структура данных, работающая по принципу "первый пришел — первый ушел" (First In, First Out).

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

queue = Queue()

print(queue.is_empty())

queue.enqueue('номер 1')
queue.enqueue('номер 2')
queue.enqueue('номер 3')
queue.enqueue('номер 4')

print(queue.is_empty())
print(queue.size())
print(queue.dequeue())
print(queue.size())

# Дерево (Tree) — это иерархическая структура данных, состоящая из узлов (node),
# где один узел является корнем (root node), а остальные узлы — его потомками (children).
# Каждый узел может иметь несколько дочерних узлов, подобно семейному дереву, где у каждого человека могут быть дети.

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.value < key: # если значение больше, значит уходим в правую ветку
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

root = Node(70)

root = insert(root, 30)
root = insert(root, 56)
root = insert(root, 89)
root = insert(root, 45)
root = insert(root, 60)
root = insert(root, 73)
root = insert(root, 98)
root = insert(root, 84)



# Граф — это структура данных, состоящая из множества узлов, то есть вершин, и множества рёбер, которые соединяют пары узлов.
# Графы похожи на карту дорог: у нас есть города, которые представляют собой узлы, точки, вершины, а дороги между ними — это рёбра.

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v): # Добавим метод для добавления ребра от одной точки к другой
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
# Этот метод принимает два параметра (две точки): u и v, которые представляют собой узлы.
# С помощью условия (if) мы проверяем, есть ли точка u в нашем графе.
# Если её нет, то создаём для неё пустой список связей.
# На следующей строке мы для этого списка связей, используя функцию append, добавляем узел v в список связей для узла u.

    def print_graph(self):
# {0: [1, 4], 1: [2, 3, 4], 2: [3], 3: [4]}
        for node in self.graph:
            print(node, "->", " -> ".join(map(str, self.graph[node])))
# С помощью цикла for мы работаем с каждой точкой по отдельности, перебирая список точек.
# Чтобы выводилась эта точка, мы прописали print.
# Рассмотрим эту строку кода подробнее: с ее помощью у нас будет выводиться каждый элемент из списка связей для определённой точки.
# То есть, у нас будет точка, от которой идёт стрелочка к следующей точке;
# после этого, если есть дополнительные связи, они также будут присоединены через стрелочки.
# Все точки будут преобразованы в строковый тип данных — для этого преобразования и нужен метод map.

g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_graph()
