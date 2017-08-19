#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
from math import *

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		super(MainWindow, self).__init__(parent, title=title, size=(600, 400))

		panel = wx.Panel(self)
		boxsize = wx.BoxSizer(wx.VERTICAL)
		gridbox = wx.GridSizer(rows=6, cols=5, hgap=1, vgap=1)
		self.equation = ''

		self.textprint = wx.TextCtrl(panel, -1, '', style=wx.TE_RIGHT)
		self.bgFont = wx.Font(25, wx.SWISS, wx.NORMAL, wx.BOLD)

		self.textprint.SetFont(self.bgFont)
		self.textprint.SetBackgroundColour((210, 210, 210))
		self.textprint.SetForegroundColour((10, 10, 10))

		self.buttonData = ['7', '8', '9', 'DEL', 'AC', '4', '5', '6', '*', '/', '1', '2', '3', '+', '-', '0', '%', 'pi', 'e', 'sqrt', '^', 'sin', 'cos', 'tan', 'log10', 'ln', '(', ')', '.', '=']

		buttonLength = len(self.buttonData)
		for label in self.buttonData:
			buttonItem = wx.Button(panel, label=label)
			self.createHandler(buttonItem, label)
			gridbox.Add(buttonItem, 0, flag=wx.EXPAND)
		boxsize.Add(self.textprint, 1, flag=wx.EXPAND)
		boxsize.Add(gridbox, 5, flag=wx.EXPAND)
		panel.SetSizerAndFit(boxsize)

		# create status bar
		self.CreateStatusBar()

		# create menu
		filemenu = wx.Menu()
		menuAbout = filemenu.Append(wx.ID_ABOUT, 'About', 'information about program')
		filemenu.AppendSeparator()
		menuExit = filemenu.Append(wx.ID_EXIT, 'Exit', "exit")

		menuBar = wx.MenuBar()
		menuBar.Append(filemenu, 'file')
		self.SetMenuBar(menuBar)

		self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
		self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

		self.Show(True)

	def OnAbout(self, e):
		dlg = wx.MessageDialog(self, 'a smaller text editor', 'about sample editor', wx.OK)
		dlg.ShowModal()
		dlg.Destroy()

	def OnExit(self, e):
		self.Close(True)

	def createHandler(self, button, labels):
		item = 'DEL AC ='
		if labels not in item:
			self.Bind(wx.EVT_BUTTON, self.OnAppend, button)
		elif labels == 'DEL':
			self.Bind(wx.EVT_BUTTON, self.OnDel, button)
		elif labels == 'AC':
			self.Bind(wx.EVT_BUTTON, self.OnAC, button)
		else:
			self.Bind(wx.EVT_BUTTON, self.OnResult, button)

	def OnAppend(self, e):
		eventButton = e.GetEventObject()
		label = eventButton.GetLabel()
		self.equation += label
		self.textprint.SetValue(self.equation)

	def OnDel(self, e):
		self.equation = self.equation[:-1]
		self.textprint.SetValue(self.equation)

	def OnAC(self, e):
		self.textprint.Clear()
		self.equation = ''

	def OnResult(self, e):
		string = self.equation
		if '^' in string:
			string = string.replace('^', '**')
		if 'ln' in string:
			string = string.replace('ln', 'log')
		try:
			result = eval(string)
			self.equation = str(result)
			self.textprint.SetValue(self.equation)
		except SyntaxError:
			dlg = wx.MessageDialog(self, 'format error', 'attention', wx.OK|wx.ICON_INFORMATION)
			dlg.ShowModal()
			dlg.Destroy()

class App(wx.App):
	def OnInit(self):
		self.frame = MainWindow(None, 'Calculator')
		self.frame.Centre()
		return True

if __name__ == "__main__":
	app = App()
	app.MainLoop()
