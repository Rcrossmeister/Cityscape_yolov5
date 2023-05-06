city = 'mainz_'
mid_index = '000003_'
last_name = '_leftImg8bit.txt'

total_number = 50000

local_path = '' # 数据集中Class.txt的存放位置
target_path = '' # 目标位置

class_list = [] # 想要进行检测的类别

for i in range(total_number):
    zero_number = 6-len(str(i))
    path = local_path + city + mid_index + str(zero_number*'0') + str(i) + last_name
    aim_path = target_path + city + mid_index + str(zero_number*'0') + str(i) + last_name

    try:
        with open(path) as f:
            with open(aim_path, "w", encoding='utf-8') as g:
                for line in f:
                    if line[1] != ' ':
                        class_number = line[0] + line[1]
                    else:
                        class_number = line[0]
                    if class_number in class_list:
                        continue
                    else:
                        g.write(line)
    except:
        continue
f.close()
g.close()
