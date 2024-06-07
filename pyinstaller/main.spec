# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files

datas = []
datas += collect_data_files('langchain')
datas += collect_data_files('langchain_community')
datas += collect_data_files('llama_cpp')


a = Analysis(
    ['main.py'],
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
    name='main',
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
    icon=['META & Microsoft Team Up on LlaMA 2.ico'],
)
