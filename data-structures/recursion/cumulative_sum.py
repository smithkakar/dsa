import argparse

def cumulative_sum(n):
    if n == 0:
        return 0
    else:
        return n + cumulative_sum(n-1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int)
    args = parser.parse_args()
    print(f'cumulative sum of digits of {args.number} is: {cumulative_sum(args.number)}')