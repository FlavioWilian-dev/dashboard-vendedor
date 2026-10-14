a = Analysis(
    ['launcher.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('..\\frontend', 'frontend'),
    ],
    hiddenimports=[
        'app',
        'app.main',
        'app.config',
        'app.config.settings',
        'app.database',
        'app.database.connection',
        'app.database.shalon',
        'app.database.veracci',
        'app.routes',
        'app.routes.auth',
        'app.routes.dashboard',
        'app.services',
        'app.services.auth_service',
        'app.services.dashboard_service',
        'app.queries',
        'app.queries.usuario',
        'app.queries.dashboard_dia',
        'app.queries.dashboard_mes',
        'app.utils',
        'app.utils.password',
        'app.utils.security',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)


pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='DashboardVendedor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)