class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        scores = []
        for i in range(len(operations)):
            if operations[i] == "+":
                scores.append(scores[-1] + scores[-2])

            elif operations[i] == "D":
                scores.append(scores[-1] * 2)

            elif operations[i] == "C":
                scores.pop()

            else:
                scores.append(int(operations[i]))
        
        summ = sum(scores)
        return summ