import sys 
from heapq import heapify, heappush, heappop

def dijsktra(graph,src,dest):
    
    inf = sys.maxsize
    #Node data is to store the costs and the paths the model takes to reach the destination
    node_data = {'A':{'cost':inf,'pred':[]},
    'B':{'cost':inf,'pred':[]},
    'C':{'cost':inf,'pred':[]},
    'D':{'cost':inf,'pred':[]},
    'E':{'cost':inf,'pred':[]},
    'F':{'cost':inf,'pred':[]},
    'G':{'cost':inf,'pred':[]},
    'H':{'cost':inf,'pred':[]},
    'I':{'cost':inf,'pred':[]},
    'J':{'cost':inf,'pred':[]},
    'K':{'cost':inf,'pred':[]},
    'L':{'cost':inf,'pred':[]}
    }
    
    #The initial node cost and position is set to 0.
    node_data[src]['cost'] = 0
    visited = []
    temp = src
    for i in range(11):  # The range is set to the number of vertices -1.
        if temp not in visited: 
            visited.append(temp)
            min_heap = []
            for j in graph[temp]:
                if j not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['pred'] = node_data[temp]['pred'] + list(temp)
                    heappush(min_heap,(node_data[j]['cost'],j))
        heapify(min_heap)
        temp = min_heap[0][1]
    print("Shortest Distance: " + str(node_data[dest]['cost']))
    print("Shortest Path: " + str(node_data[dest]['pred'] + list(dest)))


if __name__ == "__main__":

    #Vertices and costs of two unit cubes that share a face. The image representation of this section is given in the .docx file.
    graph = {
        'A':{'B':2,'G':2, 'F':2},
        'B':{'A':2,'C':2,'H':2},
        'C':{'B':2,'D':2,'F':2,'I':2},
        'D':{'C':2,'E':2,'J':2},
        'E':{'D':2,'K':2,'F':2},
        'F':{'C':2,'L':2,'A':2,'E':2},
        'G':{'A':2,'H':2, 'L':2},
        'H':{'B':2,'G':2,'I':2},
        'I':{'C':2,'L':2,'H':2,'J':2},
        'J':{'D':2,'K':2,'I':2},
        'K':{'E':2,'L':2,'J':2},
        'L':{'G':2,'K':2,'F':2, 'I':2}
    }

    #Setting random source and destination vertices.
    sour = input("Enter Source Node: ").upper()
    dest = input("Enter Destination Node: ").upper()
    dijsktra(graph,sour,dest)