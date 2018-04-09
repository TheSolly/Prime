import time


def main():
    print '''A function to determine if a number > 1 is a Prime'''
    loop = True
    while loop:
        prime = True
        num1 = input('please input a number = ')
        print 'Your number is {}, let me check for you...'.format(num1), '\n'
        time.sleep(2)
        for i in range(2, num1):
            if (num1 % i) == 0:
                print num1, 'is not a prime number!'
                prime = False
                break
        if prime:
            print num1, 'is a prime number'
        autoLoop = raw_input('''
        Do you want to try another number?
        y for yes, any other key for no: ''')
        print '\n'
        if autoLoop != 'y':
            loop = False
            print 'Thanks for using this function, bye!'


if __name__ == '__main__':
    main()
