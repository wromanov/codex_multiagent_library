param([ValidateSet('all','router','progress','agents')][string]$Component='all',[switch]$Apply,[switch]$Force,[string]$CodexHome,[string]$SkillsHome)
$ErrorActionPreference='Stop'
$installer=Join-Path $PSScriptRoot 'install.ps1'
& $installer -Component $Component -Apply:$Apply -Force:$Force -CodexHome $CodexHome -SkillsHome $SkillsHome
