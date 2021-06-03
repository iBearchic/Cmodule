
# Веса для king
orig_k = 0.6
bvi_k = 0.4

def king(orig, bvi, orig_k, bvi_k, n):
    ''' Функция поиска внутреннего коэффициента '''
    return 0.00000001 + ((orig * orig_k + bvi * bvi_k ) / n)

def kong(kp, ko, kd):
    ''' Функция поиска внешнего коэффициента '''
    return (kp * kd)**(ko)

# Словарик с весом зон
k_dict = {'green': 8.3, 'yellow': 6, 'orange': 4.1}

def kp(p: list, k: dict):
    ''' Коэффициент участия '''
    return (150 - p[0]*k['green'] - p[1]*k['yellow'] - p[2]*k['orange']) / 100

def kd(p_s, k_s = 1.001203200114052001):
    return k_s * p_s

def p_s(n, nn = 25):
    ''' Коэффициент для kd'''
    temp = 1
    for i in range(n):
        temp -= king(main_lst[i][0][0], main_lst[i][0][1], orig_k, bvi_k, nn)
    return temp

def p(i, n):
    temp = 1
    for j in range(i):
        kpv = kp(main_lst[j][1], k_dict)
        if main_lst[j][2] == 0:
            kov = float(input(f"Введите коэффициент ко для конкурента номер {j}: "))
            main_lst[j][2] = kov
        else:
            kov = main_lst[j][2]
        kdv = kd( p_s(j, n) )
        temp -= king(main_lst[j][0][0], main_lst[j][0][1], orig_k, bvi_k, n) * kong(kpv, kov, kdv)
        if temp <= 0:
            temp = 0
            break
    return temp * 100

# База данных и прочее
rates = [2, 1.5, 1.2, 1]  # ko

main_lst = [ 
    [[0, 0], [0, 0, 0], rates[1]],
    [[0, 0], [6, 0, 0], rates[3]],
    [[0, 0], [5, 2, 0], rates[3]],
    [[0, 0], [0, 0, 0], rates[0]],
    [[1, 0], [9, 1, 0], rates[3]],
    [[0, 0], [0, 0, 0], rates[0]],
    [[1, 0], [11, 1, 0], rates[3]],
    [[0, 0], [9, 1, 0], rates[3]],
    [[0, 0], [6, 0, 2], rates[3]],
    [[0, 0], [8, 1, 0], rates[3]], 
    [[1, 0], [9, 0, 0], rates[0]],
    [[0, 0], [7, 1, 0], rates[3]],
    [[0, 0], [3, 0, 0], rates[2]],
    [[0, 0], [7, 0, 0], rates[3]],
    [[0, 0], [8, 0, 0], rates[3]],
    [[0, 0], [6, 0, 0], rates[3]],
    [[0, 0], [7, 1, 0], rates[3]],
    [[0, 0], [3, 3, 2], rates[3]],
    [[1, 0], [6, 0, 0], rates[0]],
    [[0, 0], [4, 5, 0], rates[3]],
    [[0, 0], [1, 0, 5], rates[3]],
    [[0, 0], [4, 2, 3], rates[3]],
    [[0, 0], [5, 3, 1], rates[3]],
    [[0, 0], [1, 3, 1], rates[3]],
    [[0, 0], [2, 5, 0], rates[2]],
    [[0, 0], [3, 0, 0], rates[3]],
    [[1, 0], [2, 4, 2], rates[0]],
    [[0, 0], [2, 3, 1], rates[2]],
    [[0, 0], [0, 0, 2], rates[1]],
    [[0, 0], [3, 3, 1], rates[2]],
    [[0, 0], [5, 1, 2], rates[3]],
    [[0, 0], [2, 1, 0], rates[2]],
    [[1, 0], [3, 2, 2], rates[0]],
    [[0, 0], [3, 2, 0], rates[2]],
    [[1, 0], [7, 2, 0], rates[3]], 
    [[1, 0], [0, 1, 2], rates[0]],
    [[0, 0], [3, 1, 0], rates[1]],
    [[0, 0], [5, 3, 3], rates[3]],
    [[0, 0], [3, 0, 1], rates[3]],
    [[1, 0], [4, 4, 2], rates[2]],
    [[0, 0], [1, 2, 0], rates[0]],
    [[0, 0], [6, 1, 1], rates[2]],
    [[0, 0], [1, 0, 0], rates[3]],
    [[0, 0], [4, 0, 2], rates[3]], 
    [[0, 0], [6, 2, 1], rates[3]],
    [[1, 0], [3, 0, 1], rates[3]],
    [[0, 0], [3, 2, 1], rates[0]],
    [[1, 0], [0, 0, 0], rates[1]],
    [[1, 0], [0, 0, 4], rates[0]],
    [[0, 0], [2, 0, 0], rates[0]],
    [[0, 0], [8, 0, 0], rates[2]],
    [[0, 0], [4, 0, 0], rates[3]],
    [[1, 0], [4, 0, 4], rates[0]]
]

if __name__ == '__main__':
    for i in range(53):
        print(f"Вероятность поступления {i} кандидата = {p(i, 25)}. kong = ({kp(main_lst[i][1], k_dict)} * {kd( p_s(i, 25))}) ** {main_lst[i][2]} = {( kp(main_lst[i][1], k_dict)*kd( p_s(i, 25)) )**main_lst[i][2]}")