# coding=utf-8
"""Subclass of ShootSubs, which is generated by wxFormBuilder."""

import wx
import os
import movies_subs_gui
import ConfigParser
from shooter_api import Shooter
import glob
import time


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

        return u'%s' % folder, u'%s' % subs, u'%s' % movies
    except Exception:
        return None, None, None


def set_configure_folder(path):
    """
    根据用户选取的目录，更新配置文件
    :param path:
    :return:
    """
    try:
        config = ConfigParser.SafeConfigParser()
        filename = "movie_subs.ini"
        config.read(filename)

        config.set("FOLDER", "folder", path)
        config.write(open(filename, "w"))
    except Exception:
        pass


# Implementing ShootSubs
class MoviesSubsShootSubs(movies_subs_gui.ShootSubs):
    def do_close(self, event):
        super(MoviesSubsShootSubs, self).do_close(event)
        wx.GetApp().ExitMainLoop()

    def do_init_config(self, event):
        super(MoviesSubsShootSubs, self).do_init_config(event)
        self.root_dir, self.subs_suffix, self.movie_suffix = get_configure()
        if self.root_dir is None:
            self.m_rich_log.WriteText(u'获取配置参数失败，请检查movie_subs.ini中配置是否正确！\n')
            return
        self.subs_suffix_list = self.subs_suffix.split(',')
        self.movies_suffix_list = self.movie_suffix.split(',')

        # 设置界面元素
        self.m_dirPicker.SetPath(self.root_dir)
        self.m_rich_log.WriteText(u'************************** Config ************************\n')
        self.m_rich_log.WriteText(u'folder = %s\n' % self.root_dir)
        self.m_rich_log.WriteText(u'subs = %s\n' % self.subs_suffix)
        self.m_rich_log.WriteText(u'movies = %s\n' % self.movie_suffix)
        self.m_rich_log.WriteText(u'************************** Config ************************\n')

    def __init__(self, parent):
        movies_subs_gui.ShootSubs.__init__(self, parent)
        self.root_dir, self.subs_suffix, self.movie_suffix = None, None, None
        self.subs_suffix_list, self.movies_suffix_list = None, None


    # Handlers for ShootSubs events.
    def do_ok_click(self, event):
        self.m_dirPicker.SetFocus()
        self.root_dir = self.m_dirPicker.GetPath()
        set_configure_folder(self.root_dir)
        root_dir_list = self.root_dir.split(',')
        for scan_dir in root_dir_list:
            self.m_rich_log.WriteText(u'开始处理目录：' + u'%s\n' % scan_dir)
            self.start_get_movie_subs(scan_dir)

        self.m_rich_log.WriteText(u'处理完成：' + u'%s\n' % self.root_dir)

    def deal_with_file(self, filename):
        """
        处理单个文件
        :param filename:
        """
        if filename is None:
            return

        # 以.分割文件名，如果没有，表示文件名格式不正确
        filename_split = os.path.splitext(filename)
        if len(filename_split) < 2:
            return

        # 如果后缀不在需要处理的范围内，不做处理
        if filename_split[1] not in self.movies_suffix_list:
            return

        # 判断是否已经有字幕
        for suffix in self.subs_suffix_list:
            pattern = filename_split[0] + u'*' + suffix
            for subs_file in glob.iglob(pattern):
                self.m_rich_log.WriteText(u'字幕已经存在：' + u'%s' % subs_file + u'\n')
                return

        # 开始获取字幕文件
        self.m_rich_log.WriteText(u'开始处理：' + u'%s' % filename + u'\n')
        shooter = Shooter(filename, self.m_rich_log)
        shooter.start()


    def start_get_movie_subs(self, scan_dir):
        """
        扫描目录中的文件
        递归的扫描目录中的子目录以及文件
        :param scan_dir:
        :return:
        """
        if scan_dir is None:
            return

        for filename in os.listdir(scan_dir):
            # 暂停0.1秒，等richedit刷新
            time.sleep(0.2)

            path = os.path.join(scan_dir, filename)
            if os.path.isdir(path):
                self.start_get_movie_subs(path)
            else:
                self.deal_with_file(u'%s' % path)
