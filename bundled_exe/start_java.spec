# -*- mode: python -*-
a = Analysis(['start_java.py'],
             pathex=['E:\\work_mess\\workspaces\\pie\\parrot_sketch\\bundled_exe'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles + [('bundled_java_windows.zip', 'bundled_java_windows.zip', 'DATA')],
          a.datas,
          name=os.path.join('dist', 'start_java.exe'),
          debug=False,
          strip=None,
          upx=True,
          console=True )
