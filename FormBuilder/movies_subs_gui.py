# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MovieSubsDialog
###########################################################################

class MovieSubsDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"射手网字幕下载器", pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.CLOSE_BOX|wx.DEFAULT_DIALOG_STYLE|wx.MINIMIZE_BOX, name = u"main_dialog" )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer1 = wx.GridSizer( 4, 1, 0, 0 )
		
		gSizer2 = wx.GridSizer( 1, 2, 0, 0 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"请选择电影目录：", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText4.Wrap( -1 )
		gSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, u".", u"Select a Dir", u"*.*", wx.DefaultPosition, wx.Size( 400,-1 ), wx.FLP_CHANGE_DIR|wx.FLP_DEFAULT_STYLE )
		gSizer2.Add( self.m_filePicker1, 0, wx.ALL, 5 )
		
		
		gSizer1.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		fgSizer1 = wx.FlexGridSizer( 1, 1, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		gSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		gSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		gSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

