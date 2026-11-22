class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += f"{len(word)}#"
            res += word
        return res


    def decode(self, s: str) -> List[str]:
        num = h = 0
        res = []
        while h < len(s):
            if s[h] == "#":
                n = int(s[num:h])
                res.append(s[h+1:h+1+n])
                num = h+1+n
                h = num + 1
            else:
                h += 1
        return res