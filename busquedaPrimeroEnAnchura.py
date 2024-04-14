from collections import deque

def bfs(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    
    visited = set()  # Conjunto para almacenar las celdas visitadas
    queue = deque([(start, [])])  # Cola para mantener las celdas a visitar junto con el camino tomado
    
    while queue:
        cell, path = queue.popleft()  # Sacamos la primera celda de la cola junto con el camino tomado
        
        # Si la celda es la salida, retornamos el camino tomado
        if cell == end:
            return path + [cell]
        
        # Si la celda no ha sido visitada y no es una pared
        if cell not in visited and maze[cell[0]][cell[1]] == 0:
            visited.add(cell)  # Marcamos la celda como visitada
            
            # Agregamos los vecinos no visitados a la cola junto con el camino tomado
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_cell = (cell[0] + dx, cell[1] + dy)
                if 0 <= next_cell[0] < rows and 0 <= next_cell[1] < cols:
                    queue.append((next_cell, path + [cell]))
    
    # Si no se encuentra una solución, retornamos None
    return None

# otros laberintos
laberinto_simple = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]
entrada_simple = (0, 0)
salida_simple = (4, 4)

laberinto_mas_grande = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
entrada_mas_grande = (0, 0)
salida_mas_grande = (8, 8)

laberinto_con_obstaculos = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]
entrada_con_obstaculos = (0, 0)
salida_con_obstaculos = (4, 4)

laberinto_con_caminos_alternativos = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
entrada_con_caminos_alternativos = (0, 0)
salida_con_caminos_alternativos = (4, 4)


# Ejemplo de uso
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)  # Punto de inicio
end = (4, 4)  # Punto de salida

path = bfs(maze, start, end)
if path:
    print("Camino encontrado:")
    for row, col in path:
        print(f"({row}, {col})")
else:
    print("No se encontró un camino.")
