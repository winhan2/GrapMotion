# coding: utf-8

import cmd
from core.grap import Quadrilateral
from core.grap import Triangle
from lib.od_to_td import od_to_td
from core.show import show
from lib.input_to_list import input_to_list


class Cli(cmd.Cmd):
    def __init__(self, logger, grap_obj):
        super().__init__()
        self.logger = logger
        self.prompt = '请输入命令>>>'
        self.intro = '''欢迎使用GrapMotion
使用help命令获取帮助'''
        self.grap = grap_obj

    def do_help(self, arg: str) -> None:
        if arg == 'exit':
            ehm = '退出程序'
            print(ehm)
        elif arg == 'show':
            shm = '''
作用：显示图形
语法：show 图形id
注：[]内内容为选写，其他为必写
            '''
            print(shm)
        elif arg == 'draw':
            dhm = '''
作用：绘制图形
语法：draw 图形类型 图形位置 [图形是否填充（0为不填充，1为填充，默认为0)] [图形填充颜色（表示格式：{red, green, blue}，默认为0, 0, 255）

图形类型：
qrl 四边形
tia 三角形

图形位置：
矩形 <<左上角点x, 左上角点y>, <右上角点x, 右上角点y>, <左下角点x, 左下角点y>, <右下角点x, 右下角点y>>
三角形 <<最上角点x, 最上角点y>, <中间或左下角点x, 中间或左下角点y>, <下方或右下角点x, 下方或右下角点y>>
平行四边形 <<左上角点x, 左上角点y>, <右上角点x, 右上角点y>, <左下角点x, 左下角点y>, <右下角点x, 右下角点y>>
梯形 <<左上角点x, 左上角点y>, <右上角点x, 右上角点y>, <左下角点x, 左下角点y>, <右下角点x, 右下角点y>>

注：[]内内容为选写，其他为必写
            '''
            print(dhm)
        elif arg == 'rmm':
            rhm = '''
作用：删除图形
语法：rmm 图形id
            '''
            print(rhm)
        elif arg == 'dm':
            dhm = '''
作用：平移图形
语法：dm 图形id 平移方向 平移距离 [是否保留动画（0为不保留，1为保留，默认为0]
注：[]内内容为选写，其他为必写
            '''
            print(dhm)
        elif arg == 'rot':
            rhm = '''
作用：旋转图形
语法：rot 图形id 旋转中心 旋转方向 旋转角度(90° 180° 270°) [是否保留动画（0为不保留，1为保留，默认为0]
注：[]内内容为选写，其他为必写
            '''
            print(rhm)
        elif arg == 'asy':
            ahm = '''
作用：将图形的另一半补好，使图形成为轴对称图形
语法：asy 图形id 对称轴
            '''
            print(ahm)
        elif arg == 'save':
            shm = '''
作用：将画面保存
语法：save 文件名
            '''
            print(shm)
        elif arg == 'load':
            lhm = '''
作用：将画面文件导入并显示
语法：load 文件路径
            '''
            print(lhm)
        else:
            help_msg = \
                """
命令\t\t\t作用
help\t\t获取帮助
help 命令\t获取某个命令的具体信息
exit\t\t退出
show\t\t显示图形
draw\t\t绘制图形
rmm\t\t\t删除图形
dm\t\t\t平移图形
rot\t\t\t旋转图形
asy\t\t\t将图形的另一半补好，使图形成为轴对称图形
save\t\t将画面保存
load\t\t将画面文件导入并显示
                """
            print(help_msg)

    def default(self, line: str) -> None:
        print(f'没有这个命令 {line}')

    @staticmethod
    def do_exit():
        print('程序已退出')
        exit()

    def do_show(self, lines: str):  # draw rec <<2, 1>, <2, 4>, <1, 6>, <9, 1>>
        show(self.grap)

    def do_draw(self, lines: str):
        grap_type = lines[:3]

        gis_data = lines[4:]  # gis_data: grap input str data
        grap_location = input_to_list(gis_data, ['<', '>', '<<', '>>'])
        grap_location = od_to_td(grap_location)

        if grap_type == 'qrl':
            qrl = Quadrilateral(grap_location)
            self.grap.add_grap(qrl)
        elif grap_type == 'tri':
            triangle = Triangle(grap_location)
            self.grap.add_grap(triangle)

    def do_rmm(self, lines: str):
        pass

    def do_dm(self, lines: str):
        pass

    def do_rot(self, lines: str):
        pass

    def do_asy(self, lines: str):
        pass

    def do_save(self, line: str):
        pass

    def do_load(self, line: str):
        pass

    def main(self):
        self.cmdloop()
