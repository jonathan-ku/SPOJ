'''
Created on Jan 2, 2015

@author: Jonathan
'''


def is_prime(number):
    if number == 2 or number == 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    for i in xrange(5, int(number ** 0.5) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


def main():
    N = int(raw_input())
    for _ in xrange(N):
        bounds = raw_input()
        lower_bound = int(bounds.split()[0])
        upper_bound = int(bounds.split()[1])
        if upper_bound % 2 == 0:
            print upper_bound
        elif not is_prime(upper_bound):
            print upper_bound
        elif upper_bound - 1 > lower_bound:
            print upper_bound - 1


if __name__ == '__main__':
    main()
