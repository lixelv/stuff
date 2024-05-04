from itertools import combinations

def find_min_dis(obj_1: tuple | list, obj_2: tuple | list) -> int | float:
    obj = (obj_1[0][0] - obj_2[0][0], obj_1[0][1] - obj_2[0][1]), (obj_1[1][0] - obj_2[1][0], obj_1[1][1] - obj_2[1][1])
    
    if obj[1][0]*obj[0][0] + obj[1][1]*obj[0][1] > 0 or obj[1] == (0, 0):
        return (obj[0][0]**2 + obj[0][1]**2) ** 0.5
    
    a = obj[0][1] - obj[1][1] * obj[0][0] / obj[1][0] if obj[1][0] != 0 else None
    b = obj[0][0] - obj[1][0] * obj[0][1] / obj[1][1] if obj[1][1] != 0 else None
    
    if a is None:
        return abs(b)
    elif b is None:
        return abs(a)
    elif a == 0 or b == 0:
        return 0.
    else:
        return abs(a*b) / (a**2 + b**2) ** 0.5
    
def sim_phys(list_of_objects: list):
    result = dict()
    for i in combinations(range(len(list_of_objects)), 2):
        result[i] = find_min_dis(list_of_objects[i[0]], list_of_objects[i[1]])
    return result[min(result, key=result.get)], min(result, key=result.get)
        
    
print(sim_phys([((1, 1), (1, 0)), ((-2, 1), (0, 0)), ((3, 3), (1, 1))]))