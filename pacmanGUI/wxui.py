import wx
import subproc

class myui(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "My Simple GUI App.")#, size = (700,600)
        self.panel = wx.Panel(self, style=wx.TAB_TRAVERSAL | wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)

        self.text1 = wx.TextCtrl(self.panel, -1, pos = (10,10), size=(380,-1))
        self.text = wx.TextCtrl(self.panel, -1, pos = (10, 130), size = (380, 460),style = wx.TE_MULTILINE | wx.TE_READONLY )


        self.buttonsearch = wx.Button(self.panel, label = 'pacman -Ss', pos=(10, 50), size=(100, -1))
        self.buttoninstall = wx.Button(self.panel, label = 'pacman -S', pos=(150, 50), size=(100,-1))
        self.buttonuninstall = wx.Button(self.panel, label='pacman -R', pos=(290, 50), size=(100,-1))
        self.buttonhasInstall = wx.Button(self.panel, label = 'pacman -Qs', pos = (10,90), size = (100,-1))
        self.buttonman= wx.Button(self.panel, label = 'man pacman', pos= (150,90), size = (100,-1))
        self.Bind(wx.EVT_BUTTON, self.search, self.buttonsearch)
        self.Bind(wx.EVT_BUTTON, self.install, self.buttoninstall)
        self.Bind(wx.EVT_BUTTON, self.uninstall, self.buttonuninstall)
        self.Bind(wx.EVT_BUTTON, self.hasInstall, self.buttonhasInstall)
        self.Bind(wx.EVT_BUTTON, self.man, self.buttonman)

        self.buttonhide = wx.Button(self.panel, pos = (290,90),size=(100,-1))
        self.isShown = True
        self.buttonhide.SetLabel(u'Hide Detail')
        self.text.Show()
        self.SetClientSize((400,600))
        self.Bind(wx.EVT_BUTTON, self.touch, self.buttonhide)
        self.Bind(wx.EVT_CLOSE, self.destroy)

    def touch(self, event):
        if self.isShown:
            self.buttonhide.SetLabel(u'Show Detail')
            self.text.Hide()
            self.isShown = False
            self.SetClientSize((400,150))
        else:
            self.text.Show()
            self.buttonhide.SetLabel(u'Hide Detail')
            self.isShown = True
            self.SetClientSize((400,600))
        self.text.Layout()

    def destroy(self,event):
        self.Destroy()

    def search(self, event):
        self.text.Clear()
        l = self.text1.GetValue()
        lst = 'pacman -Ss '+ l
        txt = subproc.noSudoList(lst)
        if txt:
            self.text.write(txt)
        else:
            self.text.write('SORRY, NOTHING EXISTS!')
            self.text1.Clear()

    def install(self,event):
        self.text.Clear()
        l = self.text1.GetValue()
        lst = 'sudo -S pacman -S ' + l
        box = wx.TextEntryDialog(None, "what's your password", '123', style=wx.TE_PASSWORD | wx.OK | wx.CANCEL)
        if box.ShowModal()==wx.ID_OK:
            psw = box.GetValue()
            txt1 = subproc.SudoList(lst, psw)
            if len(txt1)>30:
                b = wx.MessageDialog(None, 'do you want to install?', 'install?', wx.YES_NO)
                if b.ShowModal() == wx.ID_YES:
                    txt = subproc.SudoY(lst)
                    self.text.write(txt)
                else:
                    self.text.write('you give up to install!')
            else:
                self.text.write('your password is wrong!')
        else:
            self.text.write('you give up to enter the password!')

    def uninstall(self, event):
        self.text.Clear()
        l = self.text1.GetValue()
        lst = 'sudo -S pacman -R ' + l
        box = wx.TextEntryDialog(None, "what's your password", '123', style=wx.TE_PASSWORD | wx.OK | wx.CANCEL)
        if box.ShowModal()==wx.ID_OK:
            psw = box.GetValue()
            txt1 = subproc.SudoList(lst, psw)
            if len(txt1)>30:
                b = wx.MessageDialog(None, 'do you want to uninstall?', 'uninstall?', wx.YES_NO)
                if b.ShowModal() == wx.ID_YES:
                    txt = subproc.SudoY(lst)
                    self.text.write(txt+ 'uninstall successfully!')
                    self.text1.Clear()
                else:
                    self.text.write('you just give up to uninstall!')
            else:
                self.text.write('your password is wrong!')

        else:
            self.text.write('you give up to enter the password!')

    def hasInstall(self, event):
        self.text.Clear()
        l = self.text1.GetValue()
        lst = 'pacman -Qs '+ l
        txt = subproc.noSudoList(lst)
        if txt:
            self.text.write(txt)
        else:
            self.text.write('SORRY, NO THING has installed!')
            self.text1.Clear()

    def man(self, event):
        self.text.Clear()
        lst = 'man pacman'
        txt = subproc.man(lst)
        self.text.write(txt)
        self.text1.Clear()


if __name__=='__main__':
    app = wx.PySimpleApp()
    frame = myui(None, -1)
    frame.Show()
    app.MainLoop()
