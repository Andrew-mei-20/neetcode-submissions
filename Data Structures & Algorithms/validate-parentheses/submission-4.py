class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for i in s:
            if(i == "}"):
                if (len(res) == 0 or res.pop() != "{"):
                    return False
            elif(i == ")"):
                if (len(res) == 0 or res.pop() != "("):
                    return False
            elif(i == "]"):
                if (len(res) == 0 or res.pop() != "["):
                    return False
            else:
                res.append(i)
        return len(res) == 0