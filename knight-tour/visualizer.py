import matplotlib.pyplot as plt
from knights_tour import warnsdorff_knight_tour, BOARD_SIZE

def visualize_knight_tour(board, output_file="knights_tour.png"):
    fig, ax = plt.subplots(figsize=(8, 8))

    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            color = "#f0d9b5" if (x + y) % 2 == 0 else "#b58863"
            ax.add_patch(plt.Rectangle((x, BOARD_SIZE - 1 - y), 1, 1, color=color))

    positions = {}
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            step = board[y][x]
            positions[step] = (x, y)

    path_x = [positions[i][0] + 0.5 for i in range(64)]
    path_y = [(BOARD_SIZE - 1 - positions[i][1]) + 0.5 for i in range(64)]

    ax.plot(path_x, path_y, linewidth=2)

    for step, (x, y) in positions.items():
        ax.text(
            x + 0.5,
            (BOARD_SIZE - 1 - y) + 0.5,
            str(step),
            fontsize=8,
            ha="center",
            va="center",
            color="black"
        )

    ax.set_ylim(0, BOARD_SIZE)
    ax.set_xlim(0, BOARD_SIZE)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Knight's Tour Path", fontsize=16)

    plt.savefig(output_file, dpi=300)
    plt.close()
    print(f"Gambar disimpan sebagai {output_file}")


if __name__ == "__main__":
    print("Masukkan titik awal kuda (0–7).")
    start_x = int(input("Start X (column): "))
    start_y = int(input("Start Y (row): "))

    board = warnsdorff_knight_tour(start_x, start_y)

    if board:
        visualize_knight_tour(board, "knights_tour.png")
    else:
        print("Tidak ada solusi dari titik awal tersebut.")
