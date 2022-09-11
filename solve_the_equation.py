# Solve a given equation and return the value of 'x' in the form of a string "x=#value". The equation contains only '+', '-' operation, 
# the variable 'x' and its coefficient. You should return "No solution" if there is no solution for the equation, or "Infinite solutions"
# if there are infinite solutions for the equation.

# If there is exactly one solution for the equation, we ensure that the value of 'x' is an integer.

 

# Example 1:

# Input: equation = "x+5-3+x=6+x-2"
# Output: "x=2"
# Example 2:

# Input: equation = "x=x"
# Output: "Infinite solutions"
# Example 3:

# Input: equation = "2x=x"
# Output: "x=0"

class Solution:
    def solveEquation(self, equation: str) -> str:
        
        def find_coefs(statement):
            results = []

            stack_x = []
            stack = []
            
            stack_x.append(0)
            stack.append(0)
            
            tracker_num = ""
            tracker_oper = ""
            met_x = False
            first_minus = False
            for i in range(len(statement)):
                if statement[i].isdigit():
                    tracker_num += statement[i]
                elif statement[i] == '+':
                    if first_minus:
                        first_minus = False
                        if tracker_num != '':
                            tracker_num = str(0 - int(tracker_num))
                    if len(stack) == 1 and tracker_num != "":
                        if tracker_oper == "" or tracker_oper == "+":
                            stack.append(int(tracker_num))
                        else:
                            stack.append(0 - int(tracker_num))
                    else:
                        if tracker_num != "":
                            if tracker_oper == "+":
                                stack.append(stack[-1] + int(tracker_num))
                            else:
                                stack.append(stack[-1] - int(tracker_num))
                    tracker_oper = "+"
                    tracker_num = ""
                elif statement[i] == "-":
                    if first_minus:
                        first_minus = False
                        if tracker_num != '':
                            tracker_num = str(0 - int(tracker_num))
                    if i == 0:
                        first_minus = True
                    else:
                        if len(stack) == 1 and tracker_num != "":
                            stack.append(int(tracker_num))
                        else:
                            if tracker_num != "":
                                if tracker_oper == "+":
                                    stack.append(stack[-1] + int(tracker_num))
                                else:
                                    stack.append(stack[-1] - int(tracker_num))
                        tracker_oper = "-"
                        tracker_num = ""
                elif statement[i] == "x":
                    if tracker_num == "":
                        if first_minus:
                            tracker_num = "-1"
                        else:
                            tracker_num = "1"
                    else:
                        if first_minus:
                            tracker_num = str(0 - int(tracker_num))
                    if not met_x:
                        met_x = True
                        if tracker_oper == "-":
                            stack_x.append(0 - int(tracker_num))
                        else:
                            stack_x.append(int(tracker_num))
                    else:
                        if tracker_oper == "+":
                            stack_x.append(stack_x[-1] + int(tracker_num))
                        else:
                            stack_x.append(stack_x[-1] - int(tracker_num))
                    tracker_oper = ""
                    tracker_num = ""
                if i == len(statement)-1 and statement[i] != 'x':
                    if first_minus:
                        tracker_num = str(0 - int(tracker_num))
                    if tracker_oper == '+':
                        stack.append(stack[-1] + int(tracker_num))
                    elif tracker_oper == '-':
                        stack.append(stack[-1] - int(tracker_num))
                    else:
                        stack.append(int(tracker_num))
            
            results.append(stack_x[-1])
            results.append(stack[-1])
            
            return results
        
        
        left_side,right_side = equation.split("=") 
        left_results = find_coefs(left_side)
        right_results = find_coefs(right_side)
        
        right_left = right_results[1] - left_results[1]
        left_left = left_results[0] - right_results[0]
        
        if left_left == 0 and right_left == 0:
            return "Infinite solutions"
        elif left_left == 0 and right_left != 0:
            return "No solution"
        elif left_left == 1:
            return f"x={right_left}"
        elif left_left == -1:
            return f"x={0-right_left}"
        else:
            return f"x={right_left//left_left}"
          
          
