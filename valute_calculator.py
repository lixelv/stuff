# import re

# def factorial(n):
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result

# def C(k, n):
#     return factorial(n)/(factorial(k)*factorial(n-k))

# def list_to_string(terms, variable):
#     result = []
#     for coef, exp in reversed(terms):

#         if coef == 1 and exp != 0:
#             term = f"{variable}" if exp == 1 else f"{variable}^{exp}"
#         elif coef == -1 and exp != 0:
#             term = f"-{variable}" if exp == 1 else f"-{variable}^{exp}"
            
#         else:
#             if exp == 0:
#                 term = str(coef)
#             elif exp == 1:
#                 term = f"{coef}{variable}"
#             else:
#                 term = f"{coef}{variable}^{exp}"

#         result.append(term)

#     return "+".join(result).replace("+-", "-")
    

# def expand(expr):
#     x = re.findall(r'[a-z]', expr)[0]
#     a = int(re.findall(r'\((\-?\d+)[a-z]', expr)[0] if re.findall(r'\((\-?\d+)[a-z]', expr) else (-1 if re.findall(r'\-[a-z]', expr)else 1))
#     b = int(re.findall(r'[a-z]([\-\+]\d+)', expr)[0])
#     n = int(re.findall(r'\^(\d+)', expr)[0])
    
#     result = []
    
#     for k in range(n+1)[::-1]:
#         result.append((C(k, n) * (a**(n-k)) * (b**k), n-k))
        
#     result = [(int(coef), exp) for coef, exp in result]
        
#     return list_to_string(result, x)
    
    
# print(expand("(-v-8)^4"))
# import itertools
# def permutations(s):
#     return ["".join(i) for i in list(set(itertools.permutations(list(s))))]

# print(permutations(input()))

# import re

# def calc_sq(s: str): # ax^2 + bx + c = 0
#     a = re.findall(r'([-+]?\d*)x\^2', s)
#     a = int(a[0] if a != [''] and a != ['-'] else '-1' if a == ['-'] else '1')
    
#     b = re.findall(r'(\d*)x[^\^]', s)
#     b_sign = re.findall(r'([-+])\s*\d*x[^\^]', s)
#     b = (1 if b_sign == ['+'] else -1 if b_sign == ['-'] else 0) * int(b[0] if b != [''] else '1')
    
#     c = re.findall(r'x\s*([-+]\s*\d*)\s*\=', s)
#     c = int(c[0].replace(' ', '') if c else '0')
    
#     D = b**2 - 4*a*c
#     if D < 0:
#         return None
#     elif D == 0:
#         return -b/(2*a)
#     else:
#         return sorted(tuple([(-b + (i * D**0.5))/(2*a) for i in [1, -1]]))
    
# print(calc_sq(input()))

# def primes(n):
#     a = [i for i in range(n+1)]

#     a[1] = 0

#     i = 2
#     while i <= n:
#         if a[i] != 0:
#             j = i + i
#             while j <= n :
#                 a[j] = 0
#                 j = j + i
#         i += 1

#     a = list(set(a))
#     a.remove(0)
    
#     return a
        
# def get_mults(n):
#     result = []
#     prime = primes(n)
#     i = 0
    
#     while i < len(prime):
#         if n % prime[i] == 0:
#             n //= prime[i]
#             result.append(prime[i])
#             i -= 1
#         i += 1
        
#     return result

# def prime_factors(n):
#     result = ''
#     mults = get_mults(n)
    
#     while len(mults):
#         j = mults[0]
        
#         if mults.count(j) > 1:
#             result += f"({j}**{mults.count(j)})"
            
#         else:
#             result += f"({j})"
            
#         while j in mults:
#             mults.remove(j)
    
#     return result

# print(prime_factors(int(input())))
# result = dict()
# for j in range(10):
#     result[j] = list()
#     for i in range(1, 10):
#         if result[j].count((j**i)%10) == 1:
#             break
#         result[j].append((j**i)%10)
# print(result)

# def remove_duplicates_from_end(lst):
#     return list(set(lst))

# # Пример использования
# lst = [5, 4, 3, 2, 1, 1, 1, 2, 3, 2, 3, 4, 5, 6]
# print(remove_duplicates_from_end(lst))
# class Vector:
#     def __init__(self, vector):
#         self.vector = vector
        
#     def norm(self):
#         return sum(i**2 for i in self.vector)**0.5
    
#     def add(self, other):
#         if len(self.vector) != len(other.vector):
#             raise Exception("Error, different vector sizes!")
#         return Vector([self.vector[i] + other.vector[i] for i in range(len(self.vector))])
    
#     def subtract(self, other):
#         if len(self.vector) != len(other.vector):
#             raise Exception("Error, different vector sizes!")
#         return Vector([self.vector[i] - other.vector[i] for i in range(len(self.vector))])
    
#     def dot(self, other):
#         if len(self.vector) != len(other.vector):
#             raise Exception("Error, different vector sizes!")
#         return Vector([self.vector[i] * other.vector[i] for i in range(len(self.vector))])
    
#     def equals (self, other):
#         return self.vector == other.vector
    
# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result


# def prime(n):
#     i = 0
#     prime = {i: True for i in range(2, n+1)}
#     for i in range(2, n+1):
#         if prime[i]:
#             for j in range(i*2, n+1, i):
#                 prime[j] = False
#     return [i for i in range(2, n+1) if prime[i]]

# import bisect

# def insert_sorted(lst, item):
#     pos = bisect.bisect_left(lst, item)
#     if lst.count(item) == 0:
#         lst.insert(pos, item)
# import random

# from functools import lru_cache
# rgb_dict = {'R': 0, 'G': 1, 'B': 2}
# rgb_dict_reverse = {0: 'R', 1: 'G', 2: 'B'}

# @lru_cache(maxsize=None)
# def f3c_v2(a, b):
#     return a if a == b else 3 - a - b

# def f3c(n, l):
#     result = 0
#     for i in range(l-1):
#         a = n // 3
#         result += f3c_v2(n % 3, a % 3) * (3 ** i)
#         n = a
#     return result

# def triangle(row):
#     l = len(row)
#     row = sum([rgb_dict[row[i]]*(3**i) for i in range(l)])
#     while l != 1:
#         row = f3c(row, l)
#         l -= 1
#     return row
def read(arg, registers):
    if arg.isnumeric():
        return int(arg)
    else:
        return registers[arg]

def simple_assembler(program):
    registers = dict()
    
    program = program.split('\n')
    cursor = 0
    
    while cursor < len(program):
        line = program[cursor]
        cmd = line.split(' ')[0]
        key = line.split(' ')[1:]
        
        if cmd == "mov":
            registers[key[0]] = read(key[1], registers)
        elif cmd == "dec":
            registers[key[0]] -= 1
        elif cmd == "inc":
            registers[key[0]] += 1
        elif cmd == "jnz":
            if registers[key[0]] != 0:
                cursor += read(key[1], registers) - 1
            
        cursor += 1
    
    return registers

print('-1'.isnumeric())