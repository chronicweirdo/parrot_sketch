'''
Created on Jul 8, 2012

@author: silviu

build with pyinstaller:
E:\work_mess\workspaces\pie\parrot_sketch\bundled_exe>python c:\pyinstaller\util
s\Build.py start_java.spec
'''


import subprocess, zipfile, os, sys

'''
print __file__
if hasattr(sys, '_MEIPASS'):
    print sys._MEIPASS
    zippath = sys._MEIPASS + '\\bundled_java_windows.zip'
    print os.path.exists(zippath)
    z = zipfile.ZipFile(zippath)
    extractpath = sys._MEIPASS + '\\bundled_java_windows\\'
    os.makedirs(extractpath)
    z.extractall(extractpath)
print os.path.exists('bundled_java_windows.zip')
'''

def resourcePath(path):
    if hasattr(sys, '_MEIPASS'):
        return sys._MEIPASS + '\\' + path
    return path

zippath = resourcePath('bundled_java_windows.zip')
print os.path.exists(zippath)
z = zipfile.ZipFile(zippath)
extractpath = resourcePath('bundled_java_windows\\')
if not os.path.exists(extractpath):
    os.makedirs(extractpath)
z.extractall(extractpath)

#z = zipfile.ZipFile(resource_path('bundled_java_windows.zip'))
#z.extractall()

'''
for f in z.namelist():
    if f.endswith('/'):
        os.makedirs(f)
    else:
        f.extract()
'''

command = [resourcePath('bundled_java_windows\\bin\\java.exe'), '-version']
subprocess.call(command)

sys.stdin.readline()