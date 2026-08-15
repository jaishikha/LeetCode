class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        newS = s+s
        if len(s) != len(goal):
            return False
        if goal in newS:
            return True
        else:
            return False