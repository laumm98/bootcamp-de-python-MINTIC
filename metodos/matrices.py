chess_board = [
['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

print(chess_board)

chess_board[7][1] = 0 # Casilla original del caballo ahora está vacía
chess_board[5][2] = 'N' # Nueva posición del caballo
print(chess_board)

checkers_board = [
[0, 'b', 0, 'b', 0, 'b', 0, 'b'],
['b', 0, 'b', 0, 'b', 0, 'b', 0],
[0, 'b', 0, 'b', 0, 'b', 0, 'b'],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
['w', 0, 'w', 0, 'w', 0, 'w', 0],
[0, 'w', 0, 'w', 0, 'w', 0, 'w'],
['w', 0, 'w', 0, 'w', 0, 'w', 0]
]
print(checkers_board)

image = [
[255, 0, 0, 0, 255],
[0, 255, 0, 255, 0],
[0, 0, 255, 0, 0],
[0, 255, 0, 255, 0],
[255, 0, 0, 0, 255]
]
print(image)