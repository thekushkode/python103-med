# Python103 Medium Excersise 1
# create a tip calculator based on users input/experience

bill = input('How much was your bill: ')

#turning bill var into a float
bill_int = float(bill)

#defining var for level of service
serv_lev = input('Rate your service (Good, Fair, or Bad): ')

#making users answer all lowercase
serv_lev_lower = serv_lev.lower()

#defining var values for service levels good, fair, & bad
good_tip = round(.2 * bill_int, 2)
fair_tip = .15 * bill_int
bad_tip = .1 * bill_int

#defining total
good_total = round(good_tip) + bill_int
fair_total = round(fair_tip, 2) + bill_int
bad_total = round(bad_tip) + bill_int

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


