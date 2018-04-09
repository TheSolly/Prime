# A function to detrmine if a number is prime or not
# for n > 1


def isprime(n):
    if n == 2:
        return "Prime"
    for i in range(2, n):
        if n % i != 0:
            continue
        else:
            return 'Not Prime'
    return "Prime"


def main():
    print '''A function to detrmine if a number is prime or not for n > 1'''
    autoLoop = False
    while not autoLoop:
        n = input("please input a number for testing greater than 1: ")
        print '\n'
        print 'Your number {} is {}'.format(n, isprime(n))
        endFunction = raw_input('''if you want to try another number press y,
or press any other key to exit: ''')
        if endFunction == 'y':
            print '\n'
            continue
        else:
            autoLoop = True
        print 'Function end'


if __name__ == '__main__':
    main()
