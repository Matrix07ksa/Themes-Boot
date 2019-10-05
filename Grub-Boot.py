#!/usr/bin/python3 
# -*- coding: utf-8 -*-#
# Code by Hejab Zaeri KSA 
import os
import subprocess
import shutil
import platform
import re
import npyscreen


global grub2
global grub 
grub = "grub"
grub2 = "grub2"
if os.getgid() != 0 :
    print("Plese Root Running !")
    exit()
if platform.system == "Windows":
    print("Use Platform Linux !")
    exit()

try :
    def backup():
        subprocess.call(["cp -an '/etc/default/grub' '/etc/default/grub.bak'"],shell=True)
    def Clear_themes ():
        "Clear Background Grub"
        subprocess.call(["sed -i '/^GRUB_THEME=/d' '/etc/default/grub'"],shell=True)
        subprocess.call(["sed -i '/^GRUB_BACKGROUND=/d' '/etc/default/grub'"],shell=True)

    def Great_Themes():
        try:
            os.mkdir('/boot/%s/themes/'%(grub))
            pass
        except FileExistsError :
            pass
        except TypeError:
            os.mkdir('/boot/%s/themes/'%(grub2))

        try:
            os.mkdir('/boot/%s/themes/%s' %(grub,m))        
        except FileExistsError:
            pass
        except TypeError:
            os.mkdir('/boot/%s/themes/%s' %(grub2,m))

        try:    
            if Lang == ["Arabic"]:
                c = shutil.copy("Arabic/theme.txt", '/boot/%s/themes/%s/'%(grub,m), follow_symlinks=True)
            if Lang == ["English"]:
                c = shutil.copy("English/theme.txt", '/boot/%s/themes/%s/'%(grub,m), follow_symlinks=True)
        except:
            if Lang == ["Arabic"]:
                c = shutil.copy("Arabic/theme.txt", '/boot/%s/themes/%s/'%(grub2,m), follow_symlinks=True)
            if Lang == ["English"]:
                c = shutil.copy("English/theme.txt", '/boot/%s/themes/%s/'%(grub2,m), follow_symlinks=True)
        h = open("/etc/default/grub","a").write("GRUB_THEME=/boot/grub/themes/%s/theme.txt"%(m))
        try:
            shutil.copy(FILE, '/boot/%s/themes/%s/background.png'%(grub,m), follow_symlinks=True)#Backgound
            shutil.copy("terminal_box_c.png", '/boot/%s/themes/%s'%(grub,m), follow_symlinks=True)
            shutil.copy("selected_item_c.png", '/boot/%s/themes/%s'%(grub,m), follow_symlinks=True)
            shutil.copy("item_c.png", '/boot/%s/themes/%s'%(grub,m), follow_symlinks=True)
            icons = os.system("cp -rf 'icons/' '/boot/%s/themes/%s/'"%(grub,m))
            progress = os.system("cp -rf 'progress/' '/boot/%s/themes/%s/'"%(grub,m))
        except:
            shutil.copy(FILE, '/boot/%s/themes/%s/background.png'%(grub2,m), follow_symlinks=True)#Backgound
            shutil.copy("terminal_box_c.png", '/boot/%s/themes/%s'%(grub2,m), follow_symlinks=True)
            shutil.copy("selected_item_c.png", '/boot/%s/themes/%s'%(grub2,m), follow_symlinks=True)
            shutil.copy("item_c.png", '/boot/%s/themes/%s'%(grub2,m), follow_symlinks=True)
            icons = os.system("cp -rf 'icons/' '/boot/%s/themes/%s/'"%(grub2,m))
            progress = os.system("cp -rf 'progress/' '/boot/%s/themes/%s/'"%(grub2,m))


        
    class FormObject (npyscreen.ActionForm):
        def create (self):
            self.fname= self.add(npyscreen.TitleText,name= "🤠 Themes Grub name:#",hidden=False,begin_entry_at=25)
            self.nextrely+=1
            self.github = self.add(npyscreen.MultiLineEdit, 
                value = """🤠   Cody By Hejab Zaeri Ksa \ngithub:https://github.com/Matrix07ksa⁵¹⁵    🤠\n""", 
                        max_height=5,)

            self.lname = self.add(npyscreen.TitleFilenameCombo,name= "File Name Image Png :#",hidden=False,begin_entry_at=25,)
            self.myDepartment = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=5, name='Lang Boot',value = [0,], values = ['Arabic', 'English'])
        def afterEditing(self):
            self.parentApp.setNextForm(None)
            pass
        def on_ok (self):
            try:
                    
                
                global Lang
                global m
                global FILE
                global Lang
                m = self.fname.value
                FILE = self.lname.value
                Lang = self.myDepartment.get_selected_objects()
                backup()
                Clear_themes()
                Great_Themes()
                def install_themes ():
                    g = open("/etc/os-release").read()
                    if re.findall("ID=(.*)",g)[0] == "ubuntu" or "debian" or "solus" :                  #ubuntu|debian|solus 
                        subprocess.call(["update-grub"],shell=True)
                    elif re.findall("ID=(.*)",g)[0] == "arch" or "gentoo" :                               #arch|gentoo
                        subprocess.call(["grub2-mkconfig -o /boot/grub2/grub.cfg"],shell=True)
                    elif re.findall("ID=(.*)",g)[0] == "centos" or "fedora" or "opensuse" :               #centos|fedora|opensuse
                        subprocess.call(["grub2-mkconfig -o /boot/grub2/grub.cfg"],shell=True)
                    else:
                        pass
                        
                install_themes()
                npyscreen.notify_confirm("❤️❤️ install Finsh  Themes Grub ❤️❤️ !")
            except:
                npyscreen.notify_ok_cancel("no input False 🤨❌#! !")
        def on_cancel (self):
            npyscreen.notify_confirm("good bye!",editw=1)
        def handle_mouse_event(self, mouse_event):
            mouse_id, rel_x, rel_y, z, bstate = self.interpret_mouse_event(mouse_event)
    class App (npyscreen.NPSAppManaged):
        def onStart(self):
            npyscreen.setTheme(npyscreen.Themes.DefaultTheme)
            self.addForm("MAIN",FormObject,name = "Welcome to Themes Grub boot\t\t"  
            "Code By hejab Zaeri ⁵¹⁵")

            
    if (__name__=="__main__"):
        app = App().run()
        
except KeyboardInterrupt:
    print("good bye!")
    
