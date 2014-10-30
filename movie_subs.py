# -*- coding: utf-8 -*-

__author__ = 'syn'


import os
import urllib
import httplib
import io
import ConfigParser
import logging
import hashlib


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d -- %(message)s',
    filename='./movie_subs.log',
)


def md5(content):
    """
    MD5加密
    :param content:
    :return:
    """
    m = hashlib.md5
    m.update(content)
    return m.hexdigest


def gen_movie_hash(filename):
    """
    计算文件hash,算法:
    取文件第4k位置，再根据floor( 文件总长度/3 )计算，取中间2处，
    再取文件结尾倒数第8k的位置， 4个位置各取4k区块做md5。
    共得到4个md5值，均设为索引。可以进行智能匹配。 （可以应用于不完全下载的p2p文件）
    """
    if filename is None:
        return

    movie_hash = ""

    # 计算需要计算hash的4个位置
    file_length = os.path.getsize(filename)
    if file_length < 8192:
        logging.info(u"文件小于8K，略过 [%s]", filename)
        return

    offsets = [4096, file_length / 3, (file_length / 3) * 2, file_length - 8192]

    try:
        f = open(filename, 'rb')
        for one_offset in offsets:
            f.seek(one_offset, io.SEEK_SET)
            buf = f.read(4096)
            md5_string = md5(buf)

            if movie_hash != "":
                movie_hash += u';'
            movie_hash += md5_string

        f.close()
    except Exception, e:
        logging.error('open file {%s} fail! err = %s', e[0])

    return movie_hash


def do_shooter_api(filename, shooter_hash):
    """
    调用射手网API

    """
    if filename == "" or shooter_hash == "":
        return False

    p = {"filehash": shooter_hash, "pathinfo": filename, "format": "json", "lang": "Chn"}
    params = urllib.urlencode(p)

    exception = None
    http_client = None
    try:
        try:
            http_client = httplib.HTTPConnection("https://www.shooter.cn/api/subapi.php")
            http_client.request(method="POST", url="https://www.shooter.cn/api/subapi.php", body=params)
            response = http_client.getresponse()
            if response.status == 200:
                return
            else:
                logging.warn("response code %d" % response.status)
                logging.warn("response code %s" % response.read())
        except Exception, err:
            exception = err
    finally:
        if http_client:
            http_client.close()
        if exception:
            logging.error(exception)
            return False

    return True


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

    # 计算文件hash
    shooter_hash = gen_movie_hash(filename)
    if shooter_hash == "":
        return

    # 从shooter.com.cn获取字母文件url
    ret = do_shooter_api(filename, shooter_hash)
    if ret is not True:
        logging.warn(u"获取字幕失败，[%s -- %s]", filename, shooter_hash)


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
    root_dir, movie_suffix, subs_suffix = get_configure()
    if root_dir is None:
        logging.error('GetConfigure fail!')
        print u'获取配置参数失败，请检查movie_subs.ini中配置是否正确！\n'
        return

    subs_suffix_list = subs_suffix.split(',')
    movies_suffix_list = movie_suffix.split(',')

    root_dir_list = root_dir.split(',')
    for scan_dir in root_dir_list:
        start_get_movie_subs(scan_dir)


if __name__ == '__main__':
    main()
