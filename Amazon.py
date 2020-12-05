class Solution:
    def dietPlanPerformance(self, calories, k, lower, upper):
        total=0
        #Iterate over calories
        t=sum(calories[0:k])
        # If T < lower, they performed poorly on their diet and lose 1 point; 
        if(t<lower):
            total-=1
        # If T > upper, they performed well on their diet and gain 1 point;
        elif(t>upper):
            total+=1
        # Otherwise, they performed normally and there is no change in points.
        print(total)
        for i in range(k,len(calories)):
            t=t+calories[i]-calories[i-k]
            # If T < lower, they performed poorly on their diet and lose 1 point; 
            if(t<lower):
                total-=1
            # If T > upper, they performed well on their diet and gain 1 point;
            elif(t>upper):
                total+=1
            # Otherwise, they performed normally and there is no change in points.
        return total
            
    
def main():
    s=Solution()
    calories = [6,5,0,0]
    k = 2
    lower = 1
    upper = 5
    print(s.dietPlanPerformance(calories,k,lower,upper))

main()
