days_ago = int(input('How many days ago have you purchased the item? '))
used = input('Have you used the item at all [y/n]?  ')
broken = input('Has the item broken down on its own [y/n]? ')
if days_ago <= 10 and used == 'n' or broken == 'y':
    print('You can get a refund.')
else:
    print('You cannot get a refund.')