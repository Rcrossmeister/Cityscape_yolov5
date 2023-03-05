city = 'mainz_'
mid_index = '000003_'
last_name = '_leftImg8bit.txt'

total_number = 50000

local_path = '/Users/rcross/Desktop/工作/科研/SCI/Dataset/cityscape/labels/test/'
target_path = '/Users/rcross/Desktop/工作/科研/SCI/Dataset/cityscape_original/labels/test/'

class_list = ['25','33','26','3','23','14','15','28','19','22','10','6','11','7','17','18','21','27','28','29']
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