import wx
import movies_subs_gui

app = wx.App()
main_frm = movies_subs_gui.MovieSubsDialog(None)
main_frm.Show()
app.MainLoop()
