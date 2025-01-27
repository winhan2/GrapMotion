# coding: utf-8


class Quadrilateral(object):
    def __init__(self, coordinate):
        self.__coordinate = coordinate
        self.type = 'qrl'

    def set_x1(self, new_x1):
        self.__coordinate[0][0] = new_x1

    def get_x1(self):
        return self.__coordinate[0][0]

    def set_y1(self, new_y1):
        self.__coordinate[0][1] = new_y1

    def get_y1(self):
        return self.__coordinate[0][1]

    def set_x2(self, new_x2):
        self.__coordinate[1][0] = new_x2

    def get_x2(self):
        return self.__coordinate[1][0]

    def set_y2(self, new_y2):
        self.__coordinate[1][1] = new_y2

    def get_y2(self):
        return self.__coordinate[1][1]

    def set_x3(self, new_x3):
        self.__coordinate[2][0] = new_x3

    def get_x3(self):
        return self.__coordinate[2][0]

    def set_y3(self, new_y3):
        self.__coordinate[2][1] = new_y3

    def get_y3(self):
        return self.__coordinate[2][1]

    def set_x4(self, new_x4):
        self.__coordinate[3][0] = new_x4

    def get_x4(self):
        return self.__coordinate[3][0]

    def set_y4(self, new_y4):
        self.__coordinate[3][1] = new_y4

    def get_y4(self):
        return self.__coordinate[3][1]

    def get_all(self):
        return self.__coordinate

class Triangle(object):
    def __init__(self, coordinate):
        self.__coordinate = coordinate
        self.type = 'tri'

    def set_x1(self, new_x1):
        self.__coordinate[0][0] = new_x1

    def get_x1(self):
        return self.__coordinate[0][0]

    def set_y1(self, new_y1):
        self.__coordinate[0][1] = new_y1

    def get_y1(self):
        return self.__coordinate[0][1]

    def set_x2(self, new_x2):
        self.__coordinate[1][0] = new_x2

    def get_x2(self):
        return self.__coordinate[1][0]

    def set_y2(self, new_y2):
        self.__coordinate[1][1] = new_y2

    def get_y2(self):
        return self.__coordinate[1][1]

    def set_x3(self, new_x3):
        self.__coordinate[2][0] = new_x3

    def get_x3(self):
        return self.__coordinate[2][0]

    def set_y3(self, new_y3):
        self.__coordinate[2][1] = new_y3

    def get_y3(self):
        return self.__coordinate[2][1]

    def get_all(self):
        return self.__coordinate


class Grap(object):
    def __init__(self):
        self.__grap_list = []

    def add_grap(self, grap_obj):
        self.__grap_list.append(grap_obj)

    def get_grap(self, index):
        return self.__grap_list[index]

    def show_grap(self):
        return self.__grap_list

