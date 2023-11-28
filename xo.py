from typing import List
from colorama import init, Fore
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

init(autoreset=True)

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Point(self.x * other, self.y * other)
        elif isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        elif isinstance(other, (tuple, list, set)):
            return Point(self.x * other[0], self.y * other[1])
        
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, (tuple, list, set)):
            return Point(self.x + other[0], self.y + other[1])
    
    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        elif isinstance(other, (tuple, list, set)):
            return Point(self.x - other[0], self.y - other[1])
        
    def __str__(self):
        return f"x = {self.x}, y = {self.y}"

class Matrix:
    def __init__(self, matrix: List[List[str]]):
        self.matrix = matrix
        
    def get_point(self, point: Point):
        try:
            return self.matrix[point.y][point.x]
        except Exception as e:
            return None
        
    def change_point(self, point: Point, data):
        self.matrix[point.y][point.x] = data
        
    def __len__(self):
        return (len(self.matrix[0]), len(self.matrix))
        

class Game:
    def __init__(self, size: tuple | list | set, streak: int):
        matrix = [[] for _ in range(size[1])]
        c = 0
        for i in range(1, size[0]*size[1]+1):
            matrix[c].append(str(i))
            if len(matrix[c]) == size[0]:
                c += 1
        self.matrix = Matrix(matrix)
        self.size = size
        self.streak = streak
        
    def change_point(self, user_input: str, xo: str):
        point = self.check_user_input(user_input)
        if isinstance(point, Point):
            self.matrix.change_point(point, xo)
            
        return point
        
    def get_point(self, point: Point):
        return self.matrix.get_point(point)
        
    def is_end(self):
        for point in [Point(i, j) for i in range(self.size[0]) for j in range(self.size[1])]:
            for direction in [Point(i, j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
                
                valid = True
                for offset in range(self.streak):
                    new_point = point + direction * offset
                    if not (0 <= new_point.x < self.size[0] and 0 <= new_point.y < self.size[1]):
                        valid = False
                        break
                    if self.get_point(point) != self.get_point(new_point):
                        valid = False
                        break
            
                if valid:
                    return True

        return False

    def is_end_draw(self):
        return bool(sum([row.count('x')+row.count('o') for row in self.matrix.matrix]) == sum([len(row) for row in self.matrix.matrix]))

    

                
    def check_user_input(self, user_input: str):
        try:
            user_input = int(user_input) - 1
        except Exception as e:
            return Fore.RED + 'Введите число!' + Fore.RESET
        
        if user_input >= self.size[0]*self.size[1]:
            return Fore.RED + 'Слишком большое число!' + Fore.RESET
        
        point = Point(user_input % self.size[0], user_input // self.size[0])
        if self.matrix.get_point(point) in ['x', 'o']:
            return Fore.RED + 'Вы уже ввели значение!' + Fore.RESET
        
        return point
                
    def __str__(self):
        # Находим максимальную длину элемента в матрице
        max_width = max(len(str(item)) for row in self.matrix.matrix for item in row)
        
        # Формируем матрицу, учитывая выравнивание и цвет
        formatted_matrix = [
            [' '.join([
                Fore.RED + str(item).ljust(max_width) + Fore.RESET if item == 'x' 
                else (Fore.BLUE + str(item).ljust(max_width) + Fore.RESET if item == 'o' 
                    else str(item).ljust(max_width)) 
            ]) for item in row] 
            for row in self.matrix.matrix
        ]
        
        return '\n\n' + '\n\n'.join([' '.join(row) for row in formatted_matrix]) + '\n\n'

        
xo = 'o'
change_xo = False

while True:
    try:
        game_size = int(input('Введите размер игры: '))
        break
    except Exception as e:
        print(e)
 
g = Game((game_size, game_size), game_size)

while True:
    clear_console()
    if g.is_end_draw():
        print(Fore.GREEN + "\nНичья!" + Fore.RESET)
        g = Game((game_size, game_size), game_size)
    print(g)
    
    if g.is_end():
        print(Fore.GREEN + f"\n{xo} выиграл!" + Fore.RESET)
        break
    
    if not change_xo:
        if xo == 'x':
            xo = 'o'
        elif xo == 'o':
            xo = 'x'
    else:
        print(change_xo)
    
    print(f'Игрок - {xo}')
    user_input = input('Выберете ячейку: ')
    if user_input in ['exit', 'stop', '']:
        break
    
    p = g.change_point(user_input, xo)
    if isinstance(p, str):
        change_xo = p
    else:
        change_xo = False    
