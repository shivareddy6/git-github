#! python3

dict = {'Top_L':'X','Top_M':' ','Top_R':'X','Mid_L':'O','Mid_M':' ','Mid_R':' ','Low_L':' ','Low_M':' ','Low_R':' '}
def board():
    print(' ',dict['Top_L'],'| ',dict['Top_M'],' | ',dict['Top_R'])
    print('---------------')
    print(' ',dict['Mid_L'],'| ',dict['Mid_M'],' | ',dict['Mid_R'])
    print('---------------')
    print(' ',dict['Low_L'],'| ',dict['Low_M'],' | ',dict['Low_R'])
    
    

board()
