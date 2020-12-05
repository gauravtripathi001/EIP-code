def production_plan(forecast,days):
    A=0
    B=1
    
    profit=[[0 for col in range(days)] for row in range(2)]
    profit[A][0]=forecast[A][0]
    profit[B][0]=forecast[B][0]
    profit[A][1]=forecast[A][0]+forecast[A][1]
    profit[B][1]=forecast[B][0]+forecast[B][1]
    
    
    for col in range(2,days):
        for row in range(2):
            if(row==A):
                row1=B
            else:
                row1=A
            profit[row][col]=max(profit[row][col-1],profit[row1][col])+forecast[row][col]

    return max(profit[A][days-1],profit[B][days-1])
        
