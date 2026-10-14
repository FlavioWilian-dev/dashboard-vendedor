#define MyAppName "Dashboard Vendedor"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Dashboard Vendedor"
#define MyAppExeName "DashboardVendedor.exe"

[Setup]
AppId={{8F7A7F8A-7A31-4D31-9C1D-DASHBOARDVENDEDOR}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}

DefaultDirName={autopf}\Dashboard Vendedor
DefaultGroupName=Dashboard Vendedor

OutputDir=.
OutputBaseFilename=DashboardVendedorSetup

Compression=lzma
SolidCompression=yes

PrivilegesRequired=admin

ArchitecturesInstallIn64BitMode=x64compatible


[Files]

; Executável do Dashboard
Source: "..\backend\dist\DashboardVendedor.exe"; DestDir: "{app}"; Flags: ignoreversion

; Arquivo de configuração
Source: "..\backend\.env"; DestDir: "{app}"; Flags: ignoreversion

; Instalador do Microsoft ODBC Driver 17
Source: "msodbcsql17.msi"; DestDir: "{tmp}"; Flags: deleteafterinstall


[Icons]

; Atalho no Menu Iniciar
Name: "{autoprograms}\Dashboard Vendedor"; Filename: "{app}\DashboardVendedor.exe"

; Atalho na Área de Trabalho
Name: "{autodesktop}\Dashboard Vendedor"; Filename: "{app}\DashboardVendedor.exe"


[Registry]

; Iniciar Dashboard automaticamente com o Windows
Root: HKCU; \
Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; \
ValueType: string; \
ValueName: "Dashboard Vendedor"; \
ValueData: """{app}\DashboardVendedor.exe"""; \
Flags: uninsdeletevalue


[Run]

; Instalar Microsoft ODBC Driver 17
Filename: "msiexec.exe"; \
Parameters: "/i ""{tmp}\msodbcsql17.msi"" /qn IACCEPTMSODBCSQLLICENSETERMS=YES"; \
StatusMsg: "Instalando Microsoft ODBC Driver 17 para SQL Server..."; \
Flags: waituntilterminated

; Iniciar o Dashboard ao finalizar a instalação
Filename: "{app}\DashboardVendedor.exe"; \
Description: "Iniciar Dashboard Vendedor"; \
Flags: nowait postinstall skipifsilent