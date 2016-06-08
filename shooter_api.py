# -*- coding: utf-8 -*-

__author__ = 'Syn'

from Shooter_hash import ShooterHash
from urllib import urlencode
from urllib2 import Request, urlopen
import json


class Shooter(object):
    """
    实现射手网api
    """
    # 射手网api的调用url
    shooter_url = u"http://shooter.cn/api/subapi.php"

    def start(self):
        shoot_hash = ShooterHash(self.filename, self.richedit)
        self.movie_hash = shoot_hash.compute_file_hash()
        values = dict(filehash=self.movie_hash, pathinfo=self.filename, format="json", lang="Chn")
        try:
            data = urlencode(values).encode('utf-8', 'replace')
        except Exception, e:
            self.richedit.WriteText(u'文件名不合法：' + u'%s' % self.filename + u'\n')
            return

        req = Request(self.shooter_url, data)
        rsp = urlopen(req)
        content = rsp.read().decode('utf-8', 'replace')

        # 解析返回的json串
        try:
            json_content = json.loads(content)
            for idx_i, i in enumerate(json_content):
                # print(i)

                # 如果有delay文件，进行处理
                if i["Delay"] != 0:
                    delay_filename = '.'.join((self.filename, "chn%s" % ("" if idx_i == 0 else idx_i), "delay"))
                    with open(delay_filename, 'w') as output:
                        output.write(str(i["Delay"]))

                # 字幕有可能多个，逐个下载
                for idx_j, j in enumerate(i["Files"]):
                    out_filename_list = [self.filename, "chn%s" % ("" if idx_i == 0 else idx_i), str(j["Ext"])]
                    if len(i["Files"]) != 1:
                        out_filename_list.insert(2, str(idx_j))
                    out_filename = '.'.join(out_filename_list)
                    download_link = j["Link"]
                    # print(download_link)

                    # 开始下载
                    response = urlopen(download_link)
                    download_content = response.read()

                    # 写字幕文件
                    with open(out_filename, 'wb') as output:
                        self.richedit.WriteText(u'写入字幕文件：' + u'%s' % out_filename + u'\n')
                        output.write(download_content)
        except Exception, e:
            # self.richedit.WriteText(u'获取字幕返回码解析错误! 错误：{}\n'.format(e))
            pass

    def __init__(self, filename, richedit):
        """
        Constructor
        """
        self.filename = filename
        self.richedit = richedit
        self.movie_hash = ""
