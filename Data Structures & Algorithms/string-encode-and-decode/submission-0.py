class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for st in strs:
            # Since strings are immutable, repeated += can create new strings each time.
            # In the worst case, this can become O(n²).
            #res += str(len(st)) + "#" + st
            res.append(f"{len(st)}#{st}") # This is a better approach
        return "".join(res)
        

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1: j+1 + length])
            i = j+1 + length
        return res

# Time: O(n) to encode and O(n) to decode
# Space: O(n) since slicing could take O(n) in worst case
# YT: https://www.youtube.com/watch?v=B1k_sxOSgv8
