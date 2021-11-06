def fill_the_box(*args):
    box_size = (args[:3])
    size = 1
    cubs = 0
    for el in (box_size):
        size *= el
    for el in args[3:]:
        if el == 'Finish':
            break
        cubs += el
    if size > cubs:
        return f"There is free space in the box. You could put {size-cubs} more cubes."
    return f"No more free space! You have {cubs-size} more cubes."
# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))