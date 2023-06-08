# Cityscape_yolov5
 将Cityscape数据集转化为yolov5格式后，运行街景道路的目标检测任务

## Datasets:

> Cityscape数据集官网下载链接：https://www.cityscapes-dataset.com/news/
>
> Cityscape数据集个人网盘链接：链接: https://pan.baidu.com/s/1njtEAV11gs_ZWhtelB1iZw? 提取码: x5kx 

## 使用：

1. 创建新目录，解压下载文件到新目录下，并将文件重命名

```shell
mkdir ./cityscape
unzip gtFine_trainvaltest.zip -d ./cityscape
mv ./gtFine_trainvaltest ./getfine
mv ./leftImg8bit_trainvaltest ./leftImg8bit
```

2. 在当前目录下进行数据处理

```shell
mv handle.py ./cityscape
python handle.py
```

3. 生成images和labels目录
4. 提取labels中的class的顺序 (Recommend)

* __由于生成的class顺序不一定一样，推荐用以下方法读取自己的顺序__

```python
path = './cityscape/labels/classes.txt'
tmp = []
with open(path, "r") as f:
  for _ in f:
      tmp.append(_.replace('\n',''))  
print(tmp)
```

```shell
['rectification border', 'road', 'sidewalk', ··· , 'ridergroup', 'truckgroup'] # class names
```

5. 创建cityscape.yaml并写入以下内容

```shell
path: ../cityscape  # dataset root dir
train: images/train  # train images (relative to 'path') 118287 images
val: images/val  # val images (relative to 'path') 5000 images
test: images/test  

# Classes
nc: 38  # number of classes
names: ['rectification border', 'road', 'sidewalk', ··· , 'ridergroup', 'truckgroup'] # class names #把自己上面生成的复制进来！
```

6. 将cityscape.yaml复制到./yolov5/data中

至此，完成数据集的准备工作

7. Benchmark

```
mAP = 42.25(Full classes)
```

