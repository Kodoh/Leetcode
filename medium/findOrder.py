from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph = {i: [] for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            self.graph[prereq].append(course)
        
        self.seen = set()
        self.res = []
        self.temp = set()  
        
        def getSchedule(course):
            if course in self.temp:  
                return False
            if course in self.seen: 
                return True
            
            self.temp.add(course)  
            for next_course in self.graph[course]:
                if not getSchedule(next_course):
                    return False  
            
            self.temp.remove(course) 
            self.seen.add(course)  
            self.res.append(course)  
            return True
        
        for i in range(numCourses):
            if i not in self.seen:
                if not getSchedule(i):
                    return []  
        
        return self.res[::-1]  
