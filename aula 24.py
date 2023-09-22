A, B = map(int, input().split())
if A <= 10000 and B <= 10000:
    while True:
        if A == 0 and B == 0:
            break

        i = 0
        j = 0
        d_A = 0
        x = list(input().split())
        y = list(input().split())
        while i < A and j < B:
            if x[i] != y[j]:
                i += 1
                j += 0
                d_A += 1
            else:
                i += 0
                j += 1
                d_A += 0
        print(d_A)

        '''d_B = 0
        for c in x:
            for d in y:
                if c <= A and d <= B:
                    if c == d:
                        d_B += 0
                    else:
                        d_B += 1'''
