# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class ShootSubs
###########################################################################

class ShootSubs ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"射手字幕下载器", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.Size( 800,600 ), wx.Size( 800,600 ) )
		
		fgSizer1 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer3 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer3.SetMinSize( wx.Size( 800,80 ) ) 
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"选择目录：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer3.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_dirPicker = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 700,-1 ), wx.DIRP_DEFAULT_STYLE )
		self.m_dirPicker.SetMinSize( wx.Size( 700,-1 ) )
		self.m_dirPicker.SetMaxSize( wx.Size( 700,-1 ) )
		
		fgSizer3.Add( self.m_dirPicker, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_btn_ok = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_btn_ok, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		fgSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 1, 1, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer2.SetMinSize( wx.Size( 800,520 ) ) 
		self.m_rich_log = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.m_rich_log.SetMinSize( wx.Size( 800,500 ) )
		
		fgSizer2.Add( self.m_rich_log, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		fgSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.do_init_config )
		self.m_btn_ok.Bind( wx.EVT_LEFT_UP, self.do_ok_click )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def do_init_config( self, event ):
		event.Skip()
	
	def do_ok_click( self, event ):
		event.Skip()
	

