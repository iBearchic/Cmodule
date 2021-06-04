import my_mod
import kingkong

rates = [2, 1.5, 1.2, 1]  # ko

main_lst = [ 
    [[0, 0], [0, 0, 0], rates[1]],
    [[0, 0], [6, 0, 0], rates[3]],
    [[0, 0], [5, 2, 0], rates[3]],
    [[0, 0], [0, 0, 0], rates[0]],
    [[1, 0], [9, 1, 0], rates[3]]]

man0 = main_lst[2]

print("kingC:", my_mod.king(man0[0][1], man0[0][1]))
print("king:", kingkong.king(man0[0][1], man0[0][1], 0.6, 0.4, 25))

print("kpC:", my_mod.kp(man0[1]))
print("kp:", kingkong.kp(man0[1]))

print("kdC:", my_mod.kd(4, main_lst))
print("kd:", kingkong.kd(kingkong.p_s(4)))

print("kongC", my_mod.kong(my_mod.kp(man0[1]), my_mod.kd(4, main_lst), man0[2]))
print("kong", kingkong.kong(my_mod.kp(man0[1]), my_mod.kd(4, main_lst), man0[2]))
