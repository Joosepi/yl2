total_area = 0
for box in data:

    l, w, h = sorted(map(int. box.split('x')))
    area = (2 * 1 * w) * (2 * l * h ) * (2 * w * h)
    extra = 1 * w
    total_area += (area * extra)