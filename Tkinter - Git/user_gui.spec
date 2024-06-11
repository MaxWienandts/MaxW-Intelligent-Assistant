# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files

datas = [('class_llama2chat.py', '.'), ('QR Code PayPal.png', '.'), ('Llama-2-2147x2147-20p.ico', '.')]
datas += collect_data_files('langchain')
datas += collect_data_files('langchain_community')
datas += collect_data_files('llama_cpp')


a = Analysis(
    ['user_gui.py'],
    pathex=['C:\\\\Users\\\\014206631\\\\AppData\\\\Local\\\\miniconda3\\\\envs\\\\llamaChat\\\\Lib\\\\site-packages'],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=['./hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='user_gui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['Llama-2-2147x2147-20p.ico'],
)
