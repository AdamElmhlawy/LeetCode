class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        output = []

        for token in tokens:
            if token == "+":
                second = output.pop()
                first = output.pop()
                output.append(int(first + second))
                
            elif token == "*":
                second = output.pop()
                first = output.pop()
                output.append(int(first * second))

            elif token == "/":
                second = output.pop()
                first = output.pop()
                output.append(int(first / second))

            elif token == "-":
                second = output.pop()
                first = output.pop()
                output.append(int(first - second))

            else:
                output.append(int(token))
        
        return output.pop()
        