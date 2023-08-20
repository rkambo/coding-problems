class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        operands = {"+":operator.add, "-": operator.sub, "/":operator.truediv, "*":operator.mul}
        stack = []
        for token in tokens:
            if operands.get(token) == None:
                stack.append(token)
            else:
                exp1 = int(stack.pop())
                exp2 = int(stack.pop())
                print("Performing " + token + " on " + str(exp1) + " and "+ str(exp2))
                print("Result: " + str(int(operands.get(token)(exp2,exp1))))
                stack.append(int(operands.get(token)(exp2,exp1)))
        return stack[0]