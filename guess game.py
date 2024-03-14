sec_num=9
limit=3
count=0

while count<limit:
    
    guess=int(input('guess the number'))
    count+=1

    if guess==sec_num:
        print('you won!')
        break

else:
    print('you loose')        

   
