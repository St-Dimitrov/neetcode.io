class Codec:
    def encode(self, strs):
        encoded = ""
        for s in strs:
            # Prefix each string with its length and a delimiter
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s):
        decoded = []
        i = 0
        while i < len(s):
            # Find the position of the delimiter
            j = s.find("#", i)
            # Extract the length of the next string
            length = int(s[i:j])
            # Extract the string using the length
            decoded.append(s[j + 1 : j + 1 + length])
            # Move the pointer to the next encoded string
            i = j + 1 + length
        return decoded

solution = Codec()
strs = ["Hello", "World", "test"]
encode = solution.encode(strs)
decode = solution.decode(encode)
print(decode)
