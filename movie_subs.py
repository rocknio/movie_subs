# -*- coding: utf-8 -*-

__author__ = 'syn'


import os
import urllib


def gen_movie_hash():
    """
    计算文件hash,算法:
    取文件第4k位置，再根据floor( 文件总长度/3 )计算，取中间2处，
    再取文件结尾倒数第8k的位置， 4个位置各取4k区块做md5。
    共得到4个md5值，均设为索引。可以进行智能匹配。 （可以应用于不完全下载的p2p文件）
    """
    pass


def do_shooter_api():
    """
    调用射手网ＡＰＩ

    """
    pass


def get_folder_list(folder):
    """
    获取ｉｎｉ配置文件里ｆｏｌｄｅｒ目录下的子目录列表
    包括配置的ｆｏｌｄｅｒ本身

    """
    pass


def get_movie_file_name(folder):
    """
    获取目录下文件列表
    :param folder:
    """
    pass