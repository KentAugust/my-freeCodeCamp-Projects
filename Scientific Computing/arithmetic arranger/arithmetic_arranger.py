import re
def arithmetic_arranger(problems, entry = False):
  num1 = list()
  num2 = list()
  result = list()
  space = list()
  lines = list()
  
  if len(problems) > 5:
    arranged_problems = "Error: Too many problems."
    return arranged_problems
    
  for aProblem in problems:
    if (re.search('\s([^+^-])\s', aProblem)):
      arranged_problems = "Error: Operator must be '+' or '-'."
      return arranged_problems
    elif (re.search('[^0-9 |^+^-]', aProblem)):
      arranged_problems = "Error: Numbers must only contain digits."
      return arranged_problems
    elif (re.search('\S[+/-]', aProblem)) or (re.search('[+/-]\S', aProblem)):
      arranged_problems = "Error: Invalid format."
      return arranged_problems

    probParts = aProblem.split()

    if len(probParts[0]) > 4 or len(probParts[2]) > 4:
      arranged_problems = "Error: Numbers cannot be more than four digits."
      return arranged_problems
    elif probParts[1] == "+":
      result.append(int(probParts[0]) + int(probParts[2]))
    elif probParts[1] == "-":
      result.append(int(probParts[0]) - int(probParts[2]))

    num1.append(int(probParts[0]))
    num2.append(int(probParts[1]+probParts[2]))

  for i in range(len(problems)):
    mayor = max(len(str(num1[i])), len(str(abs(num2[i])))) + 2
    space.append(mayor)
    lines.append('-'*mayor)
    num1[i] = '{:{spa}d}'.format(num1[i], spa=space[i])
    num2[i] = '{:=+{spa}d}'.format(num2[i], spa=space[i])
    result[i] = '{:{spa}d}'.format(result[i], spa=space[i])
  
  if entry == True:
    arranged_problems = ('    '.join(num1[:]), '    '.join(num2[:]), '    '.join(lines[:]), '    '.join(result[:]))
    arranged_problems = '\n'.join(arranged_problems[:])
  else:
    arranged_problems = ('    '.join(num1[:]), '    '.join(num2[:]), '    '.join(lines[:]))
    arranged_problems = '\n'.join(arranged_problems[:])

  return arranged_problems
  
#"Main.py"
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))