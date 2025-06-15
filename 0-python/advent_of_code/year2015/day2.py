def total_wrapping_paper(dimension: str) -> int:
    # try to extract information
    l, w, h = dimension.split("x")

    # BUG: bad practice
    l = int(l)
    w = int(w)
    h = int(h)

    sides = [l * w, w * h, h * l]
    area = 2 * l * w + 2 * w * h + 2 * h * l

    return area + min(sides)
