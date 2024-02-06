def is_valid_number(num):
    return 0 <= num < 2**20

def solution(S):
    stack = []

    operations = S.split()

    for operation in operations:
        if operation.isdigit():
            value = int(operation)
            if not is_valid_number(value):
                return -1  # Overflow error
            stack.append(value)

        elif operation == "POP":
            if stack:
                stack.pop()
            else:
                return -1  # Underflow error: empty stack

        elif operation == "DUP":
            if stack:
                value = stack[-1]
                stack.append(value)
            else:
                return -1  # Invalid operation: empty stack

        elif operation == "+":
            if len(stack) >= 2:
                result = stack[-1] + stack[-2]
                if not is_valid_number(result):
                    return -1  # Overflow error
                stack.pop()
                stack.pop()
                stack.append(result)
            else:
                return -1  # Invalid operation: not enough elements

        elif operation == "-":
            if len(stack) >= 2:
                result = stack[-1] - stack[-2]
                if not is_valid_number(result):
                    return -1  # Overflow error
                stack.pop()
                stack.pop()
                stack.append(result)
            else:
                return -1  # Invalid operation: not enough elements
        else:
            return -1  # Invalid operation

        print(stack)

    if stack:
        return stack[-1]
    else:
        return -1  # empty stack

# Example usage:
input_str = "1048575 DUP +"
result = solution(input_str)
print(result)
