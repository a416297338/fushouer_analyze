import ctypes
import os
# 调用 Windows 的 MessageBox 函数
from deepface import DeepFace

if os.path.exists("test.jpg"):
    try:
        result_data = DeepFace.find(img_path = "test.jpg", db_path = "my_db", detector_backend = 'retinaface', align = True, threshold=100)
    except:
        ctypes.windll.user32.MessageBoxW(0, "图片中需要有且仅有一个人的清晰人脸",
                                         "傅首尔长相相似分析器V1.0", 0)
    else:
        all_distance = 0
        for distance in result_data[0].distance:
            all_distance += float(distance) - 0.68
        all_length = len(result_data)
        all_distance /= len(result_data[0])
        if all_distance < -0.02:
            ctypes.windll.user32.MessageBoxW(0, "恭喜傅首尔本尔", "傅首尔长相相似分析器V1.0", 0)
            root.update()
        else:
            all_distance = (0.2 - all_distance)/0.2 * 100
            print("there")
            ctypes.windll.user32.MessageBoxW(0, "与傅首尔相似度为"+str(max(all_distance, 0)) + "%", "傅首尔长相相似分析器V1.0", 0)
else:
    ctypes.windll.user32.MessageBoxW(0, "请放置一张 test.jpg 到当前文件夹下", "傅首尔长相相似分析器V1.0", 0)