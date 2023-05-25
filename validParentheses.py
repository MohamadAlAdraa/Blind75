
# I thought about using stack directly. Stack in python is just a list
def is_valid(s: str) -> bool:
    stack = []
    mapPar = {"(": ")", "{": "}", "[": "]"}
    valid = True
    if len(s) == 1:
        valid = False
    else:
        for i in range(len(s)):
            if s[i] not in list(mapPar.keys()) and len(stack) == 0:
                valid = False
                break
            elif s[i] in list(mapPar.keys()):
                stack.append(s[i])
            else:
                if s[i] == mapPar[stack[-1]]:
                    stack.pop()
                else:
                    valid = False
                    break

    if len(stack) != 0 and valid:
        valid = False

    return valid

if __name__ == '__main__':
    s1 = "()[]{}"
    b = is_valid(s1)
    print(b)
