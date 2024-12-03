
def validity_check(report):
    prev_value = report[0]
    
    # increasing
    if (report[0] < report[1]):
        for level in report[1:]:
            level = int(level)
            if (level <= prev_value) or not (3 >= abs(level - prev_value) >= 1):
               return False 
            prev_value = level
        return True 
    
    # decreasing 
    elif (report[0] > report[1]):
        for level in report[1:]:
            if (level >= prev_value) or not (3 >= abs(level-prev_value) >= 1):
                return False
            prev_value = level
        return True
        
    # constant
    else:
        return False

with open ('input.txt', 'r') as file:
    count = 0
    for line in file:
        report = list(map(int, line.split()))
        if validity_check(report):
            count += 1
    print(count)
