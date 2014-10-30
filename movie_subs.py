# -*- coding: utf-8 -*-

__author__ = 'syn'


import os
import ConfigParser
from shooter_api import Shooter


def get_configure():
    """
    读取配置文件

    :return:
    """
    try:
        config = ConfigParser.SafeConfigParser()
        filename = "movie_subs.ini"
        config.read(filename)

        folder = config.get("FOLDER", "folder")
        subs = config.get("SUFFIX", "subs")
        movies = config.get("SUFFIX", "movies")

        return folder, subs, movies
    except Exception:
        return None, None, None


def deal_with_file(filename):
    """
    处理单个文件
    :param filename:
    """
    if filename is None:
        return

    # 以.分割文件名，如果没有，表示文件名格式不正确
    filename_split = filename.split('.')
    if len(filename_split) < 2:
        return

    # 如果后缀不在需要处理的范围内，不做处理
    if filename_split[1] not in movies_suffix_list:
        return

    shooter = Shooter(filename)
    shooter.start()


def start_get_movie_subs(scan_dir):
    """
    扫描目录中的文件
    递归的扫描目录中的子目录以及文件
    :param scan_dir:
    :return:
    """
    if scan_dir is None:
        return

    for filename in os.listdir(scan_dir):
        path = os.path.join(scan_dir, filename)
        print path
        if os.path.isdir(path):
            start_get_movie_subs(path)
        else:
            deal_with_file(path)


def main():
    # noinspection PyGlobalUndefined
    global root_dir, movie_suffix, subs_suffix, subs_suffix_list, movies_suffix_list

    # 读取配置文件
    root_dir, subs_suffix, movie_suffix = get_configure()
    if root_dir is None:
        print u'获取配置参数失败，请检查movie_subs.ini中配置是否正确！\n'
        return

    subs_suffix_list = subs_suffix.split(',')
    movies_suffix_list = movie_suffix.split(',')

    root_dir_list = root_dir.split(',')
    for scan_dir in root_dir_list:
        start_get_movie_subs(scan_dir)


if __name__ == '__main__':
    main()
