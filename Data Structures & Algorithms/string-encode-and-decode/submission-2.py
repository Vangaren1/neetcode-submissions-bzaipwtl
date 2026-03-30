class Solution:
    def strEncode(self, s: str):
        tmp = ""
        for c in s:
            tmp += c.encode("utf-8").hex()
            tmp += "."
        return tmp

    def encode(self, strs: List[str]) -> str:
        tmp = ""
        for s in strs:
            e = self.strEncode(s)
            tmp += e
            tmp += "/"
        return tmp

    def strDecode(self, s):
        charList = [bytes.fromhex(c).decode("utf-8") for c in s.split(".")]
        return "".join(charList)

    def decode(self, s: str) -> List[str]:
        retVal = [self.strDecode(c) for c in s.split("/")]
        retVal.pop(-1)
        return retVal