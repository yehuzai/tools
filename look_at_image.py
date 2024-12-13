
import os
import sys
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap

# 查看图片详细信息

# 接受用户输入
image_path = input("请输入图片完整路径：")

# 输出用户输入的内容
print(f"你输入的内容是：{image_path}")

if image_path == "" or image_path == None:
    image_path = "/Users/yanxuefeng/Downloads/yxf/pics/1f02af7c6321c170c06eab78849e212f_b.jpg"

try:
    # 创建QApplication实例
    app = QApplication(sys.argv)

    # 打开图片文件
    image = Image.open(image_path)

    # 这里是一个示例，使用QPixmap
    q_image = QPixmap(image_path)  # 从图片路径初始化QPixmap
    print("QPixmap成功创建。")
    
    # 打印image对象的所有可访问的属性和方法
    print("image对象可访问的所有属性和方法:")
    for attr in dir(image):
        # 过滤出公共属性和方法
        if not attr.startswith('_'):
            try:
                if callable(getattr(image, attr)):  # 检查是否可以调用
                    # 调用方法并获取返回值，排除toqimage
                    if attr == 'toqimage':
                        continue
                    # 调用方法并获取返回值
                    result = getattr(image, attr)()
                    print(f"{attr}(): {result}")
                else:
                    # 输出属性值
                    value = getattr(image, attr)
                    print(f"{attr}: {value}")
            except Exception as e:
                print(f"{attr}: 访问时出错 - {e}")

    # 获取图片的详细信息
    image_info = {
        '格式': image.format,
        '模式': image.mode,
        '尺寸': image.size,
        '宽度': image.width,
        '高度': image.height,
        '帧数': getattr(image, 'n_frames', 1),  # 帧数适用于多帧图片，如GIF
        'DPI': image.info.get('dpi', '未指定'),  # DPI信息
        '通道数': len(image.getbands())  # 通道数量
    }

    # 输出图片的详细信息
    print("图片基本信息:")
    for key, value in image_info.items():
        print(f'{key}: {value}')

    # 获取文件大小
    file_size = os.path.getsize(image_path)
    print(f'文件大小: {file_size} 字节')

    # 如果EXIF数据存在，解析并输出
    exif_data = image._getexif()

    # 输出EXIF信息
    print("\nEXIF信息:")
    if exif_data is not None:
        for tag_id, value in exif_data.items():
            # 获取标签名称
            tag_name = TAGS.get(tag_id, tag_id)
            print(f'{tag_name}: {value}')
    else:
        print("该图片没有EXIF信息。")

except Exception as e:
    print(f"出现错误: {e}")


