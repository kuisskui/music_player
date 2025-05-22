# -*- mode: python ; coding: utf-8 -*-

import sys


# 1) ANALYSIS: add data files (your JPG, JSON, etc.)
a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[
        # e.g. ('/path/to/extra/lib.dylib', '.') if you ever need to bundle a .dylib
    ],
    datas=[('resource', 'resource')],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

# 2) PYZ: usually leave this alone
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

# 3) EXE: here’s where you pick onefile vs onedir, windowed vs console, and icon
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,      # leave your pure‐Python code here
    name='Player',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,              # <-- `--windowed` / `--noconsole`
    icon='icon.icns',  # <-- `--icon`
)

# 4) COLLECT: only for onedir mode
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    name='Player',
)

# 5) BUNDLE: only on macOS; you can also code-sign here
app = BUNDLE(
    coll,
    name='Player.app',
    icon='resource/icon.icns',
    # bundle_identifier='com.yourcompany.musicplayer',     # optional
    # codesign_identity='Developer ID Application: ...', # optional
    # entitlements_file='entitlements.plist',             # optional
)
