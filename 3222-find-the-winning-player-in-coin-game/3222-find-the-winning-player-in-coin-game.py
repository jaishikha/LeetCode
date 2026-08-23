class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        ans = min(x, y//4)
        if ans % 2 == 0:
            return "Bob"
        else:
            return "Alice"