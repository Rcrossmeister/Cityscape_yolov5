city = 'munich_'
city_index = '_000019_leftImg8bit.txt'

pic_number = 398 #待处理图片数量

local_path = '' # 数据集中Class.txt的存放位置
target_path = '' # 目标位置

class_list = [] # 想要进行检测的类别

for i in range(pic_number):
    zero_number = 6-len(str(i))
    path = local_path + city + str(zero_number*'0') + str(i) + city_index
    aim_path = target_path + city + str(zero_number * '0') + str(i) + city_index
    with open(aim_path, "w", encoding='utf-8') as g:
        with open(path) as f:
            for line in f:
                if line[1] != ' ':
                    class_number = line[0] + line[1]
                else:
                    class_number = line[0]
                if class_number in class_list:
                    continue
                else:
                    g.write(line)
f.close()
g.close()
