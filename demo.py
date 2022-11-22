# write a function that ask a user to enter an amount in naira convert the value to dollar.
# Add and commit your code.

# write another function that ask a user to enter an amount in naira convert the value to euros.
# add and commit the code.

# revert your code to the first commit

# https://emmakodes.com/how-to-use-git-and-github-for-your-personal-project



def user(name):
    print(f'Hello, {name}')

def amount(amount):
    amount *= 500
    print(f'You have {amount} dollars')

name = input('What is your name: ')
number = int(input('enter any amount: '))

user(name)
amount(number)