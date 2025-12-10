BOARD_SIZE = 8

moves = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def inside_board(x, y):
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE

def count_onward_moves(board, x, y):
    count = 0
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if inside_board(nx, ny) and board[ny][nx] == -1:
            count += 1
    return count

def warnsdorff_knight_tour(start_x, start_y):
    board = [[-1 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    x, y = start_x, start_y
    board[y][x] = 0

    for step in range(1, BOARD_SIZE * BOARD_SIZE):
        min_degree = 99
        next_x, next_y = -1, -1

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if inside_board(nx, ny) and board[ny][nx] == -1:
                degree = count_onward_moves(board, nx, ny)
                if degree < min_degree:
                    min_degree = degree
                    next_x, next_y = nx, ny

        if next_x == -1:
            return None

        x, y = next_x, next_y
        board[y][x] = step

    return board

def print_board(board):
    for row in board:
        print(" ".join(f"{x:2}" for x in row))

def is_closed_tour(board, start_x, start_y):
    end_x = end_y = None
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            if board[y][x] == BOARD_SIZE * BOARD_SIZE - 1:
                end_x, end_y = x, y

    for dx, dy in moves:
        if end_x + dx == start_x and end_y + dy == start_y:
            return True
    return False


if __name__ == "__main__":
    print("Masukkan titik awal kuda (0–7).")
    start_x = int(input("Start X (column): "))
    start_y = int(input("Start Y (row): "))

    board = warnsdorff_knight_tour(start_x, start_y)
    
    if board is None:
        print("Tidak ada solusi untuk titik awal tersebut.")
    else:
        print("\nSolusi Knight's Tour:")
        print_board(board)

        if is_closed_tour(board, start_x, start_y):
            print("\nTour ini adalah CLOSED TOUR.")
        else:
            print("\nTour ini adalah OPEN TOUR.")
