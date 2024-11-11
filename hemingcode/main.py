from math import log2, ceil

class IntBinaryList:
    def __init__(self, number: int) -> None:
        self.number = number
        
    def __len__(self) -> int:
        return self.number.bit_length()
    
    def __getitem__(self, index: int) -> bool:
        return bool((self.number >> index) & 1)
    
    def __setitem__(self, index: int, value: bool) -> None:
        self.number = self.number - (self[index] << index) + (value << index)
    
    def __iter__(self) -> bool:
        for i in range(len(self)):
            yield self[i]
    
    def __str__(self) -> str:
        result = ""
        
        for i in range(len(self)):
            result += str(1 if self[i] else 0)
        
        return result[::-1]
    
    def __int__(self) -> int:
        return self.number

# def is2power(number: int) -> bool:
#     while number > 1:
#         if number & 1 == 1:
#             return False
#         number = number >> 1
    
#     return number == 1

# # Checks is heming code correct
# def check_correctness(number: int) -> bool:
#     number = IntBinaryList(number)
#     print(number)

#     for i in range(1, len(number) + 1):
#         if is2power(i):
            
                


# check_correctness(0b1100101)

def check_hamming_code(code: int):
    # Определяем количество контрольных битов
    code = IntBinaryList(code)
    r = len(code).bit_length()
    
    # Вычисляем синдром ошибки
    syndrome = 0
    for i in range(1, len(code) + 1):
        if code[i-1]:
            syndrome ^= i
    
    # Если синдром равен 0, ошибок нет
    if syndrome == 0:
        return True, "Ошибок не обнаружено"
    
    # Если синдром не равен 0, исправляем ошибку
    if syndrome <= len(code):
        corrected_code = IntBinaryList(int(code))
        corrected_code[syndrome-1] = not code[syndrome-1]
        return False, f"Обнаружена ошибка в бите {syndrome}. Исправленный код: {str(corrected_code)}"
    else:
        return False, "Обнаружена неисправимая ошибка"

# Пример использования
code = 0b001
is_correct, message = check_hamming_code(code)
print(f"Код {bin(code)} {'корректен' if is_correct else 'некорректен'}. {message}")

# Проверка с ошибкой
code_with_error = 0b1111001  # Ошибка в третьем бите
is_correct, message = check_hamming_code(code_with_error)
print(f"Код {bin(code_with_error)} {'корректен' if is_correct else 'некорректен'}. {message}")