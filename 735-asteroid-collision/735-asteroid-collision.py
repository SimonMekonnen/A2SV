class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        des_ast = []
        astroid = 0
        while astroid < len(asteroids):
            if des_ast and (des_ast[-1] > 0 and asteroids[astroid] < 0):
                if abs(des_ast[-1]) > abs(asteroids[astroid]):
                    astroid+=1
                elif abs(des_ast[-1]) == abs(asteroids[astroid]):
                    des_ast.pop()
                    astroid+=1
                else:
                    des_ast.pop()      
            else:
                des_ast.append(asteroids[astroid])
                astroid+=1
        return des_ast
       
        
            


        
        
        
        
        
    
        
        
        