class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        rev_words = words[::-1]

        rev_str = ' '.join(rev_words)

        return rev_str
