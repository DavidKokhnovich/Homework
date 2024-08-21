def operator_range(start, end, step, operator):
    result = start
    for n in range(start+step, end+1, step):
        if operator == '+':
            result += n
        elif operator == '*':
            result *= n
        elif operator == '-':
            result -= n
        elif operator == '/':
            result /= n
    return result

print(operator_range(1, 5, 1,"+"))
