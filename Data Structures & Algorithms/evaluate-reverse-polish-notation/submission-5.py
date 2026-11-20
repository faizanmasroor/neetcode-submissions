class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+", "-", "*", "/"}
        r = []
        for token in tokens[::-1]:
            r.append(token)
        # print(r)
        l = []
        while r:
            curr = r.pop()
            if curr in ops:
                second = l.pop()
                first = l.pop()
                if curr == "+":
                    l.append(first + second)
                elif curr == "-":
                    l.append(first - second)
                elif curr == "*":
                    l.append(first * second)
                else:
                    l.append(int(first / second))
            else:
                l.append(int(curr))
        return l.pop()
        