# Once everyone has contributed their name, this file can be used to print out a list
# of members of COMP491

def print_names():
    names = ['John MacCormick',
             'Aaron Stern',
             'Christian Gonzalez', 
             'William Cheng',
             'Marcel Lee',
             'Hailie Mitchell',
             'Michael Krause',
             'Myra Hasan',
             'Melantha Chen'
             'Tanner Scott'
             'Myra Hasan'
             'Sai Atluri',
	           'Ethan Hart', 
             'Dzung Dinh'
             'Belgin Koç', 
             'Andrew Lai',
             'Dung Ha'
             'Tap Dang',
             ]
    print('Here are COMP491 members in alphabetical order:')
    sorted_names = sorted(names)
    for name in sorted_names:
        print(name)
    print('Good luck to everyone for a great semester!')


print_names()
