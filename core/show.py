# coding: utf-8

import pygame
from lib.config import Config
from lib.od_to_td import od_to_td

def draw_table(s_width, s_height, t_width, t_height, screen):
    for i in range(int(s_width / t_width) + 1):
        pygame.draw.line(screen, [0, 0, 0], [i * t_width, 0], [i * t_width, s_height])
    for i in range(int(s_height / t_height) + 1):
        pygame.draw.line(screen, [0, 0, 0], [0, i * t_width], [s_width, i * t_width])

class Show(object):
    def __init__(self, config):
        self.width = int(config.read('screen', 'width'))
        self.height = int(config.read('screen', 'height'))
        self.t_width = int(config.read('table', 't_width'))
        self.t_height = int(config.read('table', 't_height'))
        self.background_color = []
        self.config = config
        self.background_color = config.read('screen', 'background_color').split(',')

        for color_str in self.background_color:
            self.background_color[self.background_color.index(color_str)] = int(color_str)

        self.screen = pygame.display.set_mode([self.width, self.height])  # 创建窗口
        self.screen.fill(self.background_color)  # 填充颜色

        draw_table(self.width, self.height, self.t_width, self.t_height, self.screen)
        pygame.display.flip()

    def show_qrl(self, qrl_obj):
        show_dot = qrl_obj.get_all()
        draw_dot = []
        for i in show_dot:
            for j in i:
                draw_dot.append(j * self.t_width)
        draw_dot = od_to_td(draw_dot)
        draw_dot[-1], draw_dot[-2] = draw_dot[-2], draw_dot[-1]

        pygame.draw.lines(self.screen, [0, 0, 255], True, draw_dot, width=2)
        pygame.display.flip()

    def show_tri(self, tri_obj):
        show_dot = tri_obj.get_all()
        draw_dot = []
        for i in show_dot:
            for j in i:
                draw_dot.append(j * self.t_width)
        draw_dot = od_to_td(draw_dot)

        pygame.draw.lines(self.screen, [0, 0, 255], True, draw_dot, width=2)
        pygame.display.flip()

    def main(self, graps_obj):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            for grap_obj in graps_obj.show_grap():
                if grap_obj.type == 'qrl':
                    self.show_qrl(grap_obj)
                elif grap_obj.type == 'tri':
                    self.show_tri(grap_obj)
        pygame.quit()

def show(graps_obj):
    pygame.init()

    conf_obj = Config(f'conf/screen.ini')
    show_obj = Show(conf_obj)
    show_obj.main(graps_obj)

