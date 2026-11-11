class Solution:

    def encode(self, strs: List[str]) -> str:
        compressed_str = ""
        metadata = ""
        for s in strs:
            compressed_str += s
            metadata += str(len(s)) + " "

        metadata += str(len(strs))
        return compressed_str + " " + metadata
            

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        len_str = len(s)
        if s[len_str-2] == " ":
            n_str = int(s[len_str-1])
        elif s[len_str-3] == " ":
            n_str = int(s[len_str-2:])
        else:
            n_str = int(s[len_str-3:])

        metadata = self.decode_meta(s, n_str)
        
        pos = 0
        for d in metadata:
            decoded_list.append(s[pos: pos + int(d)])
            pos += int(d)

        return decoded_list

    def decode_meta(self, s:str, n_str: int):
        if n_str > 100:
            pos = len(s)-5
            last_pos = len(s)-4
        elif n_str > 10:
            pos = len(s)-4
            last_pos = len(s)-3
        else:
            pos = len(s)-3
            last_pos = len(s)-2
        count = 0
        print(s)
        metadata = []
        print(n_str)
        while (count < n_str):
            if s[pos] == " ":
                metadata.append(s[pos+1: last_pos])
                last_pos = pos
                count += 1
            pos -= 1

        print(metadata)
        metadata.reverse()
        return metadata