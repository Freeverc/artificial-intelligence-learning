from enum import Enum
from random import randint
import globalVar

BLOCK_NUM= globalVar.get_value('BLOCK_NUM')

class Color(Enum):
    ''' 颜色 '''
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    @staticmethod
    def random_color():
        '''设置随机颜色'''
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)

class Map(object):
    def __init__(self, mapsize):
        self.mapsize = mapsize

    def generate_cell(self, cell_width, cell_height):
        '''
        定义一个生成器，用来生成地图中的所有节点坐标
        :param cell_width: 节点宽度
        :param cell_height: 节点长度
        :return: 返回地图中的节点
        '''
        x_cell = -cell_width
        for num_x in range(self.mapsize[0] // cell_width):
            y_cell = -cell_height
            x_cell += cell_width
            for num_y in range(self.mapsize[1] // cell_height):
                y_cell += cell_height
                yield (x_cell, y_cell)

def gen_blocks(width, height):
    '''
    随机生成障碍物
    :param width: 地图宽度
    :param height: 地图高度
    :return:返回障碍物坐标集合
    '''
    i, blocklist = 0, []
    while(i < BLOCK_NUM):
        block = (randint(0, width-1), randint(0, height-1))
        if block not in blocklist:
            blocklist.append(block)
            i+=1

    return blocklist