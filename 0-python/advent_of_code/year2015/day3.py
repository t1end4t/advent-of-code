def visited_houses(moves: str):
    x, y = 0, 0
    visited_houses = set()
    visited_houses.add((x, y))
    for move in moves:
        if move == "^":
            y += 1
        if move == "v":
            y += -1
        if move == ">":
            x += 1
        if move == "<":
            x += -1
        visited_houses.add((x, y))

    return len(visited_houses)
