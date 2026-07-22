# -*- mode: python ; coding: utf-8 -*-
import os
import sys

is_mac = sys.platform == 'darwin'
is_win = sys.platform == 'win32'

# Pick the right icon file for the host OS (falls back to no icon if missing).
if is_mac and os.path.exists('MINJOUR.icns'):
    icon_file = 'MINJOUR.icns'
elif is_win and os.path.exists('MINJOUR.ico'):
    icon_file = 'MINJOUR.ico'
else:
    icon_file = None

# universal2 (Intel + Apple Silicon) is a macOS-only concept.
target_arch = 'universal2' if is_mac else None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
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
    [],
    exclude_binaries=True,
    name='minjour',
    icon=icon_file,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=target_arch,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='minjour',
)

# .app bundles only exist on macOS.
if is_mac:
    app = BUNDLE(
        coll,
        name='MINJOUR.app',
        icon=icon_file,
        bundle_identifier='com.jonathancozier.minjour',
        info_plist={
            'CFBundleName': 'MINJOUR',
            'CFBundleDisplayName': 'MINJOUR',
            'CFBundleShortVersionString': '1.0.0',
            'CFBundleVersion': '1.0.0',
            'NSHighResolutionCapable': True,
        },
    )
