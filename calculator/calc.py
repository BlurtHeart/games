#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, -1, title=title, size=(300,100))
		# self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
		self.CreateStatusBar()

		filemenu = wx.Menu()
		menuAbout = filemenu.Append(wx.ID_ABOUT, 'About', 'information about program')
		filemenu.AppendSeparator()
		menuExit = filemenu.Append(wx.ID_EXIT, 'Exit', "exit")

		menuBar = wx.MenuBar()
		menuBar.Append(filemenu, 'file')
		self.SetMenuBar(menuBar)

		self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
		self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

		panel = wx.Panel(self, -1)
		self.button = wx.Button(panel, -1, "Hello", pos=(50,20))
		self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
		self.button.SetDefault()

		self.Show(True)

	def OnClick(self, e):
		self.button.SetLabel("Clicked!")

	def OnAbout(self, e):
		dlg = wx.MessageDialog(self, 'a smaller text editor', 'about sample editor', wx.OK)
		dlg.ShowModal()
		dlg.Destroy()

	def OnExit(self, e):
		self.Close(True)


app = wx.App(False)
frame = MainWindow(None, 'Small editor')
app.MainLoop()
