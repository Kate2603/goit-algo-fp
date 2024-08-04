import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Якщо граф неорієнтований

    def dijkstra(self, start):
        # Відстані від початкової вершини
        distances = {vertex: float('infinity') for vertex in range(self.vertices)}
        distances[start] = 0
        
        # Пріоритетна черга для вершин
        priority_queue = [(0, start)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            if current_distance > distances[current_vertex]:
                continue
            
            # Перевірка сусідів
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                
                # Якщо знайдено коротший шлях
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances

def main():
    # Створення графа
    g = Graph(5)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 4, 3)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 4, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    
    start_vertex = 0
    distances = g.dijkstra(start_vertex)
    
    print(f"Найкоротші відстані від вершини {start_vertex}:")
    for vertex in distances:
        print(f"Вершина {vertex}: {distances[vertex]}")

if __name__ == "__main__":
    main()
