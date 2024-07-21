class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        res = []
        left = deque()
        while asteroids:
            recent = asteroids[-1]
            if recent < 0:
                asteroids.pop()
                left.appendleft(recent)
    
            else:
                if not left:
                    res.append(recent)
                    asteroids.pop()
                else:
                    if abs(left[0]) > recent:
                        asteroids.pop()

                    elif abs(left[0]) == recent:
                        asteroids.pop()
                        left.popleft()
                    
                    else:
                        left.popleft()
                    
                

        return list(left) + res[::-1] 
