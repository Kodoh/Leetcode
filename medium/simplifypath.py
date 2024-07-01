class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace('//', '/')
        path = deque(path.split('/'))


        result = deque()
        for i in path:
            if i == '..':
                if result:  
                    result.pop()
            elif i == '.' or i == '':
                continue
            else:
                result.append(i)


        return '/' + '/'.join(result)
