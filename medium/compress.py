class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 0:
            return 0
        
        write_index = 0  
        read_index = 0   
        
        while read_index < n:
            current_char = chars[read_index]
            count = 0
            
            while read_index < n and chars[read_index] == current_char:
                read_index += 1
                count += 1
            
            chars[write_index] = current_char
            write_index += 1
            
            if count > 1:
                for c in str(count):
                    chars[write_index] = c
                    write_index += 1
        
        return write_index
