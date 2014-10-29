# -*- coding: utf-8 -*-

__author__ = 'syn'


import os
import urllib
import ConfigParser
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d -- %(message)s',
    filename='./movie_subs.log',
)


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
    调用射手网API

    """
    pass


def get_folder_list(folder):
    """
    获取INI配置文件里FOLDER目录下的子目录列表
    包括配置的FOLDER本身

    """
    pass


def get_movie_file_name(folder):
    """
    获取目录下文件列表
    :param folder:
    """
    pass


def get_configure():
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


def start_get_movie_subs(scan_dir):
    if scan_dir is None:
        return

    for lists in os.listdir(scan_dir):
        path = os.path.join(scan_dir, lists)
        print path
        if os.path.isdir(path):
            start_get_movie_subs(path)


def main():
    # noinspection PyGlobalUndefined
    global root_dir, movie_suffix, subs_suffix

    # 读取配置文件
    root_dir, movie_suffix, subs_suffix = get_configure()
    if root_dir is None:
        logging.error('GetConfigure fail!')
        print u'获取配置参数失败，请检查movie_subs.ini中配置是否正确！\n'
        return

    root_dir_list = root_dir.split(',')
    for scan_dir in root_dir_list:
        start_get_movie_subs(scan_dir)


if __name__ == '__main__':
    main()
