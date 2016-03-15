import wx
import movies_subs_gui

app = wx.App()
main_frm = movies_subs_gui.ShootSubs(None)
main_frm.Show()
app.MainLoop()
