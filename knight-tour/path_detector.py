from knights_tour import warnsdorff_knight_tour, is_closed_tour

closed_starts = []

for y in range(8):
    for x in range(8):
        board = warnsdorff_knight_tour(x, y)
        if board and is_closed_tour(board, x, y):
            closed_starts.append((x, y))

print("Starting points that give CLOSED TOUR:")
for pos in closed_starts:
    print(pos)

if not closed_starts:
    print("No closed tour found for this Warnsdorff implementation.")
