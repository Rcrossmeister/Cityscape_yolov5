city = 'munich_'
city_index = '_000019_leftImg8bit.txt'

pic_number = 398

local_path = '/Users/rcross/Desktop/工作/科研/SCI/Dataset/cityscape/labels/test/'
target_path = '/Users/rcross/Desktop/工作/科研/SCI/Dataset/cityscape_original/labels/test/'

class_list = ['25','33','26','3','23','14','15','28','19','22','10','6','11','7','17','18','21','27','28','29']

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
