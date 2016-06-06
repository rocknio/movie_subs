# -*- coding: utf-8 -*-

__author__ = 'Syn'

import os
import hashlib


class ShooterHash(object):
    """
    shooter的文件hash计算
    https://docs.google.com/document/d/1w5MCBO61rKQ6hI5m9laJLWse__yTYdRugpVyz4RzrmM/preview#
    """
    def compute_file_hash(self):
        try:
            f = open(self.filename, "rb")
        except IOError:
            self.richedit.WriteText('打开文件失败：%s\n' % self.filename)

        # 获取文件长度
        stat_info = os.stat(self.filename)
        file_length = stat_info.st_size

        # 计算4个4K数据的md5，连接成hash值
        ret = []
        for i in (4096, int(file_length / 3) * 2, int(file_length / 3), file_length - 8192):
            f.seek(i, 0)
            buf = f.read(4096)
            ret.append(hashlib.md5(buf).hexdigest())
        f.close()

        return ';'.join(ret)

    def __init__(self, filename, richedit):
        """
        Constructor
        """
        self.filename = filename
        self.richedit = richedit
