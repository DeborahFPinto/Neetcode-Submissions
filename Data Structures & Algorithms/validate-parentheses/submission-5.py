class Solution:
    def isValid(self, s: str) -> bool:
        teste = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                teste.append(char)
            elif teste == []:
                return False
            elif char == ')':
                if teste.pop() != '(':
                    return False
            elif char == ']':
                if teste.pop() != '[':
                    return False
            elif char == '}':
                if teste.pop() != '{':
                    return False


        if teste == []:
            return True
        else:
            return False