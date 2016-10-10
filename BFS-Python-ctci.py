'''Consider an undirected graph consisting of  nodes where each node is labeled from  to  and the edge between any two nodes is always of length . We define node  to be the starting position for a BFS.

Given  queries in the form of a graph and some starting node, , perform each query by calculating the shortest distance from starting 
node  to all the other nodes in the graph. Then print a single line of  space-separated integers listing node 's shortest distance to each of the  other nodes (ordered sequentially by node number); if  is disconnected from a node, print  as the distance to that node.
Input Format
The first line contains an integer, , denoting the number of queries. The subsequent lines describe each query in the following format:

The first line contains two space-separated integers describing the respective values of  (the number of nodes) and  (the number of edges) in the graph.
Each line  of the  subsequent lines contains two space-separated integers,  and , describing an edge connecting node  to node .
The last line contains a single integer, , denoting the index of the starting node.'''
#https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach

class Nodes:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.children = []
        self.isVisited = False
        self.weight = 0
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        return self.head == None
    
    def enqueue(self,node):
        if self.isEmpty():
            self.head = node  # H-> N1 -> N2 -> N3 <- T
            self.tail = node
        else:
            temp = self.tail
            temp.next = node
            self.tail = node
    def dequeue(self):
        node = None
        if not self.isEmpty():
            node = self.head
            self.head = node.next
        return node
        
class Graph(object):
    def __init__(self, n):
        self.nodes = [Nodes(x + 1) for x in range(n)]
        self.n = n
        
    def connect(self,x,y):
        nodeX = self.getNode(x)
        nodeY = self.getNode(y)
        nodeX.children.append(nodeY)
        nodeY.children.append(nodeX)
        
    def getNode(self,x):
        return self.nodes[x]
    
    def find_all_distances(self,s):
        result = [-1 for x in range(n)]
        nodeS = self.getNode(s)
        q = Queue()
        q.enqueue(nodeS)
        while not q.isEmpty():
            deq_node = q.dequeue()
            for child in deq_node.children:
                if not child.isVisited:
                    child.weight = deq_node.weight + 6
                    result[ child.data - 1 ] = child.weight
                    q.enqueue(child)
                    child.isVisited = True
        result = [x for k,x in enumerate(result) if k != s ]
        return " ".join(map(str,result))
        


t = input()
for i in range(t):
    n,m = [int(x) for x in raw_input().split()]
    graph = Graph(n)
    for i in xrange(m):
        x,y = [int(x) for x in raw_input().split()]
        graph.connect(x-1,y-1) 
    s = input()
    print graph.find_all_distances(s-1)
    
