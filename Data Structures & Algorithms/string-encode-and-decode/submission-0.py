class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for string in strs:
            encodedString += str(len(string)) + "#" + string
        return encodedString
    def decode(self, s: str) -> List[str]:
        decodedArray = []
        val = 0
        ptr = 0
        
        while ptr < len(s):
            if s[ptr] == "#":
                decodedArray.append(s[ptr+1:ptr+val+1])
                ptr+= val
                val = 0
            else:
                val = val * 10 + int(s[ptr])
            ptr+=1

        return decodedArray
