import itertools

if __name__ == '__main__':

    bin_n = str('b101011')

    count = 0
    previous_n = False
    consecutive = []

    for i in range(len(bin_n)):
        next_n = i % len(bin_n)
        
        print('prev_n = ', previous_n)
        if bin_n[i] == '1':
            count += 1
            if bin_n[next_n] != '1':
                consecutive.append(count)
                count = 0
    print(max(consecutive))
# 1011b01
