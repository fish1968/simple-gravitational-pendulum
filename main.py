from math import sin, pi, factorial

g = 9.8 #gravitational constant

def T0(length):
    return 2 * pi * (length/g) ** 0.5

def odd(n):
    #return the mutiplication of odd number from n to 1
    # example:
    # odd(3) => 3*1 = 3
    # odd(9) => 9*7*5*3*1 = 945
    if n == 1:
        return 1
    else:
        return odd(n-2)*n

def coe(n):
    #return the coeffiency of the (n+1)th term
    #example:
    #coe(1) => 1 + "1/4" + 0.140625 + ...
    #coe(2) => 1 + 1/4 + "0.140625"
    numerator = odd(2*n -1)
    denominator = factorial(n)**2
    return (numerator/denominator/2)**2

def term(n,angle):
    return coe(n)*sin(angle)**(2*n)

def time(n,angle):
    #return ratio of estimated time divided by simple estimated time
    t = 1
    for i in range(1,n):
        t += term(i,angle)
    return t

def print_coe(term_number):
    # Test, get the coefficiency of term 2 to term 10 and also it's summation
    if term_number >= 1:
        print(1, '\t', 1)
    for i in range(1,term_number):
        print(i+1,'\t',1+coe(i))
    for i in range(1,term_number+1):
        co = 0
        for j in range(1,i+1):
            co += coe(j)
        print('term1 add up to {:2d}\t{:5f}'.format(i+1,1+co))

def main():
    # The mian part of the function
    while True:
        angle = eval(input("Enter the angle of the experiment (0-180 degree):"))
        if angle > 180:
            print("The angle is out of the proper range")
            print("U finished process-1")
            break
        n = eval(input("Enter the term you want:"))
        half_angle = angle*(pi/360)
        print(time(n, half_angle))
    
    while True:
        length = input("enter the length of the pendulum (q or None to quit):")
        if length == 'q' or len(length) == 0:
            print("U finished process-2")
            break
        length = eval(length)
        if length > 0:
            t = T0(length)
            ratio = 1
            for i in range(1,10):
                ratio += coe(i)
        print("The period of the pendulum is {}".format(ratio*t))
    
    while True:
        term_number = input("Enter the number of terms you want (>=1):")
        if term_number == 'q' or len(term_number) == 0:
            print("U finished process-3")
            print("U have finisehd the program")
            break
        print_coe(term_number)
        
                
if __name__ == '__main__':
    main()
