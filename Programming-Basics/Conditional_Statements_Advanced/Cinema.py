movie_type = input()
rows = int(input())
columns = int(input())
cinema_area = rows * columns
income = 0
if movie_type == "Premiere":
    income = cinema_area * 12
elif movie_type == "Normal":
    income = cinema_area * 7.50
elif movie_type == "Discount":
    income = cinema_area * 5
print(f"{income:.2f} leva")