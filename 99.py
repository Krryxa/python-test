for i in range(1, 10):
    for j in range(1, i+1):
        # print(j, 'x', i, '=', j*i, end='\t')
        print('{} x {} = {}\t'.format(j, i, j*i), end='')
    print()
