# Python 103 exercise 2
#tip calculator per person

bill = input('How much was your bill: ')

#turning bill var into a float
bill_int = float(bill)

#defining var for level of service
serv_lev = input('Rate your service (Good, Fair, or Bad): ')

#making users answer all lowercase
serv_lev_lower = serv_lev.lower()

#defining number of ways to split
split = input('How many ways would you like to split this: ')

#making split an integer
split_int = int(split)

#defining var values for service levels good, fair, & bad
good_tip = round(.2 * bill_int, 2)
fair_tip = .15 * bill_int
bad_tip = .1 * bill_int

#defining total
good_total = round(good_tip) + bill_int
fair_total = round(fair_tip, 2) + bill_int
bad_total = round(bad_tip) + bill_int

#defining per person total
good_pp = round((good_total / split_int), 2)
fair_pp = round((fair_total / split_int), 2)
bad_pp = round((bad_total / split_int), 2)

#checking answer from user and print tip amount
if serv_lev_lower == 'good':
    print(f'Tip Amount: ${good_tip}')
elif serv_lev_lower == 'fair':
    print(f'Tip Amount: ${fair_tip}')
else:
    print(f'Tip Amount: ${bad_tip}')

# checking answer from user and printing total bill amount
if serv_lev_lower == 'good':
    print(f'Total Bill: ${good_total}')
elif serv_lev_lower == 'fair':
    print(f'Total Bill: ${fair_total}')
else:
    print(f'Total Bill: ${bad_total}')

#giving per person total
if serv_lev_lower == 'good':
    print(f'Amount per person: ${good_pp}')
elif serv_lev_lower == 'fair':
    print(f'Amount per person: ${fair_pp}')
else:
    print(f'Amount per person: ${bad_pp}')









