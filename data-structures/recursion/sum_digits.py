import argparse

def sum_digits(n):
    # print(n)
    if len(str(n)) == 1:
        return n
    else:
        return (n % 10 + sum_digits(n//10))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int)
    args = parser.parse_args()
    result = sum_digits(args.number)
    print(f'sum of digits in {args.number} is: ', result)