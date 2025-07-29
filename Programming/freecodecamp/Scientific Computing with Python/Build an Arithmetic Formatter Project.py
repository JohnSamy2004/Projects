def arithmetic_arranger(problems, show_answers=False):
    # check if problems greater than 5 or no
    if len(problems) > 5:
        return 'Error: Too many problems.'

    
    row1, row2, row3 = [], [], []
    answers = []
    #format
    # extract the parts
    for problem in problems:
        num1, operator, num2 = problem.split()

        # check is operator is just '+' or '-'
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        # check is num1 and num2 are digits or no
        if num1.isdigit() and num2.isdigit():
            if len(num1) > 4 or len(num2) > 4:
                return 'Error: Numbers cannot be more than four digits.'
        else:
            return 'Error: Numbers must only contain digits.'

    
        width  = max(len(num1), len(num2)) + 2
        row1.append(num1.rjust(width))
        row2.append(operator + num2.rjust(width - 1))
        row3.append('-' * width)

        if show_answers == True:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            answers.append(result.rjust(width))

    arranged_problems = '    '.join(row1) + '\n' + \
                        '    '.join(row2) + '\n' + \
                        '    '.join(row3)
    
    if show_answers == True:
        arranged_problems += '\n' + '    '.join(answers)

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')
