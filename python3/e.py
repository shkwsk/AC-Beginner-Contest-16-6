import math

def main():
    N = int(input())
    Al = [int(x) for x in input().split()]
    center = int(N/2)
    cnt = 0
    for idx,A in enumerate(Al):
        i = idx+1
        to = i+A
        if to >= N:
            to = N-1
        if i < center:
            print(A,Al[to],abs(A - Al[to]),i,Al)
            if abs(A - Al[to]) == i:
                cnt += 1
        else:
            print(A,Al[to],abs(A - Al[to]),i-center,Al)
            if abs(A - Al[to]) == i - center:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
