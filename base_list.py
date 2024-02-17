with open('base_list.txt', 'r', encoding='utf-8') as f:
    file = f.readlines()

file = [[int(i) for i in i.replace('\n', '').split(' ')] for i in file]
result = [file[0]]
i = 0
while file:
    j = file[i]
    file.remove(j)
    m = min(file, key=lambda x: x[0]**2 + x[2]**2 - j[0]**2 - j[2]**2)
    result.append(m)
    
    i += 1

print(result + file)