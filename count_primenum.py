while True:
        try:
                start = int(input('Enter a number(starting point):'))
                stop = int(input('Enter a number(end point):'))
        except ValueError:
                print('Sorry, that is not a number. Please input a valid number')
        if start > stop:
                print("The range given is invalid")
        elif start<0:
                print('negative integers cannot be a starting point')
                continue
        count=0
        for p in range(start, stop+1):
                for q in range(2, p):
                        if p % q == 0:
                                print(p, 'equals', q, '*', p//q)
                                break
                else:
                        print(p, 'is a prime number')
                        count+=1
        if count>1:
                print('There are', count, 'prime numbers between', start, 'and', stop)
        elif count==0:
                print('No prime numbers found between', start, 'and', stop)
                continue
        print('Only one prime number is present within', start, 'and', stop)
