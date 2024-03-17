# #Задание 1

# def is_valid_queen_move(start, end):
#     x1, y1 = start
#     x2, y2 = end
#     return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

# def is_valid_knight_move(start, end):
#     x1, y1 = start
#     x2, y2 = end
#     dx = abs(x1 - x2)
#     dy = abs(y1 - y2)
#     return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)

# def is_valid_chessboard_position(position):
#     x, y = position
#     return 1 <= x <= 8 and 1 <= y <= 8

# def parse_position(position_str):
#     try:
#         x, y = map(int, position_str.split())
#         return x, y
#     except ValueError:
#         return None

# def main():
#     start_str = input("Введите координаты начальной позиции (например, '2 3'): ")
#     start = parse_position(start_str)
#     if not start or not is_valid_chessboard_position(start):
#         print("Ошибка: введены некорректные координаты.")
#         return

#     end_str = input("Введите координаты конечной позиции (например, '5 7'): ")
#     end = parse_position(end_str)
#     if not end or not is_valid_chessboard_position(end):
#         print("Ошибка: введены некорректные координаты.")
#         return

#     if is_valid_queen_move(start, end):
#         print("Ферзь может попасть на эту клетку.")
#     elif is_valid_knight_move(start, end):
#         print("Конь может попасть на эту клетку.")
#     else:
#         print("Ферзь и конь не могут попасть на эту клетку.")

# main()












# # Задание 2

# def plus_two(number):
#     try:
#         result = int(number) + 2
#         print(f"Результат: {result}")
#     except ValueError:
#         print("Введено некорректное значение.")
        
# input_number = input("Введите число: ")
# plus_two(input_number)    
    





# # Задание 3
# def access_array_element(array, index):
#     try:
#         element = array[index]
#         print("Элемент с индексом", index, ":", element)
#     except IndexError:
#         print("Индекс за пределами массива.")
        
# arr = [1, 2, 3, 4, 5]
# access_array_element(arr, 10)
# access_array_element(arr, 3)












