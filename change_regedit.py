'''
Author: MulaRoakee
Date: 2020-08-06 05:37:37
LastEditTime: 2020-08-06 14:40:17
LastEditors: MulaRoakee
Description: 修改注册表的demo 用于实现在右键菜单里添加vscode三件套
                三件套修改方法参照的网址：https://www.jianshu.com/p/e8c29211fba9
'''

from winreg import *
import sys, io, time

# 实现vscode输出里显示中文（需要sys io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


subDirFile = r'*\shell'
subDir_folder = r'Directory\shell'
subDirFolderBlank = r"Directory\Background\shell"
vscode_path = r"C:\Z_SoftWare\Vscode\Microsoft VS Code\Code.exe"

def setVscodeInRightClickMenu():

    # 在文件上右键打开
    reg = CreateKey(HKEY_CLASSES_ROOT, subDirFile)
    reg2 = CreateKey(HKEY_CLASSES_ROOT, subDirFile+"\\Vscode")

    SetValue(reg, "Vscode", REG_SZ, "用Vscode打开文件")
    SetValueEx(reg2,"Icon",1,REG_EXPAND_SZ,"\""+vscode_path+"\"")
    SetValue(reg2, "Command", REG_SZ, "\""+vscode_path+"\""+" "+"\"%1\"")



    # 在文件夹上右键打开
    reg = CreateKey(HKEY_CLASSES_ROOT, subDir_folder)
    reg2 = CreateKey(HKEY_CLASSES_ROOT, subDir_folder+"\\Vscode")

    SetValue(reg, "Vscode", REG_SZ, "用Vscode打开文件夹")
    SetValueEx(reg2,"Icon",1,REG_EXPAND_SZ,"\""+vscode_path+"\"")
    SetValue(reg2, "Command", REG_SZ, "\""+vscode_path+"\""+" "+"\"%V\"")

    
    
    # 在文件夹内空白处右键打开
    reg = CreateKey(HKEY_CLASSES_ROOT, subDirFolderBlank)
    reg2 = CreateKey(HKEY_CLASSES_ROOT, subDirFolderBlank+"\\Vscode")

    SetValue(reg, "Vscode", REG_SZ, "用Vscode打开文件夹")
    SetValueEx(reg2,"Icon",1,REG_EXPAND_SZ,"\""+vscode_path+"\"")
    SetValue(reg2, "Command", REG_SZ, "\""+vscode_path+"\""+" "+"\"%V\"")

    print("设置结束！"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    CloseKey(reg)
    CloseKey(reg2)
    
if __name__ == '__main__':

    print("=============================================================")
    print("请知悉:运行前确认vscode路径的正确性")
    print("填错也没有关系，不会引发系统性故障（就是功能不起作用？")
    print("一般而言，运行本程序后 右键菜单「用vscode打开xx」无图标即路径有误")
    print("=============================================================\n")

    try:
        setVscodeInRightClickMenu()
    except:
        print("请以管理员运行vscode")
    

    