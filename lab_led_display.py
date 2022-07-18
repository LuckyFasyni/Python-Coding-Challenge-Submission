def led(strng):
    try:
        has = {'a':'   ', 'b':'#  ', 'c':' # ', 'd':'  #', 'e':'## ', 'f':' ##', 'g':'# #', 'h':'###'}
        cod = {'1':'ddddd', '2':'hdhbh', '3':'hdhdh', '4':'gghdd', '5':'hbhdh', '6':'hbhgh',\
            '7':'hdddd', '8':'hghgh', '9':'hghdh', '0':'hgggh'} 
        for i in range(5):
            for j in strng:
                a = cod[j][i]
                print(has[a], end=' ')
            i += 1
            print('')
    except:
        print('Something is wrong!')
        
led('9081726354')
