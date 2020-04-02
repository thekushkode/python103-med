#Python103 medium, exercise 3
#How many coins do you want?

#defining coint_ct
coin_ct = 0

#defining if user wants a coin
want_cn = input("Do you want a coin (yes/no): ")
want_coin = want_cn.lower()

#checking if user wants coins and adding or saying bye
while coin_ct >= 0:
    if want_coin == 'yes':
        coin_ct += 1
        print(f'You have {coin_ct} coin(s)!')
        #reassing want_coin for users 2nd answer
        want_coin = input("Do you want another (yes/no): ")
    elif want_coin == 'no':
        print(f'OK, Bye!')
        break
    else:
        print(f'Response not accepted. Please type yes or no')
