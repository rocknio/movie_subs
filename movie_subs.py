# -*- coding: utf-8 -*-

__author__ = 'syn'


import wx
import MoviesSubsShootSubs


def main():
    app = wx.App()
    main_frm = MoviesSubsShootSubs.MoviesSubsShootSubs(None)
    main_frm.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
