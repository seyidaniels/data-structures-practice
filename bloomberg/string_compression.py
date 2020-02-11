class Solution:
    def compress(self, chars: List[str]) -> int:
        write = anchor = 0

        for read, c in enumerate(chars):
            if len(chars) == read + 1 or chars[read+1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write
