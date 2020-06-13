from math import sin, pi, factorial

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
        angle = eval(input("Enter the angle of the experiment:"))
        if angle > 180:
            print("The angle is out of the proper range")
            print("U finished this program")
            break
        n = eval(input("Enter the term you want:"))
        half_angle = angle*(pi/360)
        print(time(n, half_angle))


if __name__ == '__main__':
    main()
    term_number = int(input("Enter the number of term you want (>=1):"))
    print_coe(term_number)
