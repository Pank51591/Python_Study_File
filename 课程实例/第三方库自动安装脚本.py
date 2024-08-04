#BatchIntall.py
import os
libs = {"numpy","matplotlib","pillow","sklearn","requests","jieba","beautifulsoup4",\
        "wheel","networkx","sympy","pyinstaller","django","flask",\
        "werobot","pyqt5","pandas","pyopengl","pypdf2","docopt","pygame"}
try:
    for lib in libs:
        os.system("pip install " + lib)   #后一个引号前要加空格
    print("successful")
except:
    print("Failed Somehow")
 