def euclid(a, b):
    '''ユークリッドの互除法。d =ax+bYを見たすdを求める。'''
    a_list = []
    x_list = []
    y_list = []
    # step1
    a_list.append(a)
    a_list.append(b)
    # step2
    x_list.append(1)
    x_list.append(0)
    # step3
    y_list.append(0)
    y_list.append(1)
    # step4
    i = 1
    while (a_list[i] != 0):
        # step6
        r = a_list[i-1] % a_list[i]
        a_list.append(r)
        q = a_list[i-1]//a_list[i]
        # step7
        xiplus1 = x_list[i-1] - q*x_list[i]
        x_list.append(xiplus1)
        # step8
        yiplus1 = y_list[i-1] - q*y_list[i]
        y_list.append(yiplus1)
        i += 1
    d = a_list[i-1]
    return d
