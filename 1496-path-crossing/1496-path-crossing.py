class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x,y = 0,0
        visited = [(0,0)]
        
        for j in path:
            if j == 'N':
                y+=1
            elif j == 'S':
                y-=1
            elif j == 'E':
                x+=1
            else:
                x-=1

            if (x,y) in visited:
                return True

            visited.append((x,y))

        return False
