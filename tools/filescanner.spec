# -*- mode: python -*-
a = Analysis(['filescanner.py'],
             pathex=['E:\\work_mess\\workspaces\\pie\\parrot_sketch\\tools'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'filescanner.exe'),
          debug=False,
          strip=None,
          upx=True,
          console=True )
