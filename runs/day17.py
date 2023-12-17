import heapq


def find_shortest_paths(graph, start_point):
    visited = [[False for col in row] for row in graph]
    distance = [[float('inf') for col in row] for row in graph]
    distance[start_point[0]][start_point[1]] = 2
    prev_point = [[None for col in row] for row in graph]
    n, m = len(graph), len(graph[0])
    number_of_points, visited_count = n * m, 0
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    direction_counters = {direction: 0 for direction in directions}
    min_heap = []

    heapq.heappush(min_heap, (distance[start_point[0]][start_point[1]],
                              start_point[0], start_point[1]))

    while visited_count < number_of_points:
        current_point = heapq.heappop(min_heap)
        distance_from_start, row, col = current_point

        for direction in directions:
            new_row, new_col = row + direction[0], col + direction[1]
            if (
                -1 < new_row < n
                and -1 < new_col < m
                and not visited[new_row][new_col]
                and direction_counters[direction] < 3
            ):
                heat_loss = graph[new_row][new_col]
                dist_to_new_point = distance_from_start + heat_loss
                if dist_to_new_point < distance[new_row][new_col]:
                    distance[new_row][new_col] = dist_to_new_point
                    prev_point[new_row][new_col] = direction
                    direction_counters[direction] += 1
                    heapq.heappush(min_heap, (dist_to_new_point, new_row, new_col))
            direction_counters[direction] = 0

        visited[row][col] = True
        visited_count += 1

    return distance


puzzle = '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533'''

with open('runs/sources/puzzleinput_17.txt', 'r', encoding='utf-8') as puzzleinput:
    puzzle_1 = puzzleinput.read()

puzzle_matrix = [list(puzz) for puzz in puzzle_1.splitlines()]
for i in range(len(puzzle_matrix)):
    for j in range(len(puzzle_matrix[i])):
        puzzle_matrix[i][j] = int(puzzle_matrix[i][j])


distance = find_shortest_paths(puzzle_matrix, (0, 0))

print('----------')
print('INIT')
print('----------')
for p in puzzle_matrix:
    print(p)
print('----------')
print('RESULT')
print('----------')
for dist in distance:
    print(dist)
