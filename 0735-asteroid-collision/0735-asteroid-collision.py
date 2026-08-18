class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            alive = True

            #右向きと左向きの小惑星が向かいあっている間は衝突する
            while (
                alive
                and stack
                and stack[-1] > 0
                and asteroid < 0
                ):
                    if stack[-1] < abs(asteroid):
                        #現在の小惑星の方が大きい
                        stack.pop()
                    
                    elif stack[-1] == abs(asteroid):
                        #同じ大きさなので両方消滅
                        stack.pop()
                        alive = False
                    
                    else:
                        #stackの小惑星の方が大きい
                        alive = False
            
            if alive:
                stack.append(asteroid)
        
        return stack