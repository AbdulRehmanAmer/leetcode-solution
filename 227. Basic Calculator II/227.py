class Solution:
    def calculate(self, s: str) -> int:
        stack = [1]
        self.high_priority, self.low_priority = {'*': True, '/': True}, {'+': True, '-': True}
        expression = self.pre_processing(s)
        i = 0
        while i < len(expression):
            n1 = int(expression[i])
            i += 1
            if i == len(expression): 
                stack.append(n1)
                stack.append(1)
                break
            operator = expression[i]
            i += 1
            n2 = int(expression[i])

            if operator in self.low_priority:
                stack.append(n1)
                stack.append(1 if operator == '+' else -1)
            else:
                expression[i] = (n1 * n2) if operator == '*' else int(n1 / n2)
                
        stack.pop()
        self.stack = stack
        return self.evaluate_stack()

    def pre_processing(self, s):
        expression = ['']
        for x in s:
            if x in self.high_priority or x in self.low_priority:
                expression += [x] + ['']
            elif x == ' ': continue 
            else: expression[-1] += x
        return expression
    
    def evaluate_stack(self, res = 0):
        for i in range(0, len(self.stack), 2): res += (self.stack[i] * self.stack[i + 1])
        return res