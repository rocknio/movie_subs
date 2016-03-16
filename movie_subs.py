# -*- coding: utf-8 -*-

__author__ = 'syn'


import wx
import movies_subs_gui


def main():
    app = wx.App()
    main_frm = movies_subs_gui.ShootSubs(None)
    main_frm.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
