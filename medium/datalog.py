class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        contents = []
        full = []
        digit = []

        def binary_search(letter, log,iden,full):
            left, right = 0, len(letter)
            while left < right:
                mid = (left + right) // 2
                if letter[mid] == log:
                    if full[mid].split()[0] < iden:
                        left = mid + 1
                    else:
                        right = mid
                elif letter[mid] < log:
                    left = mid + 1
                else:
                    right = mid
            return left


        for i in range(len(logs)):
            splitdata = logs[i].split()
            if splitdata[1].isdigit():
                digit.append(logs[i])
            else:
                log = ' '.join(splitdata[1:])
                index = binary_search(contents,log,splitdata[0],full)
                contents.insert(index,' '.join(splitdata[1:]))
                full.insert(index,' '.join(splitdata))

        return full + digit