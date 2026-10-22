param(
 [ValidateSet('all','router','progress','agents')][string]$Component='all',
 [switch]$Apply,
 [switch]$Force,
 [string]$CodexHome,
 [string]$SkillsHome
)
Set-StrictMode -Version Latest
$ErrorActionPreference='Stop'
$repo=(Resolve-Path (Join-Path $PSScriptRoot '..')).Path
if([string]::IsNullOrWhiteSpace($CodexHome)){$CodexHome=if($env:CODEX_HOME){$env:CODEX_HOME}else{Join-Path $HOME '.codex'}}
if([string]::IsNullOrWhiteSpace($SkillsHome)){$SkillsHome=Join-Path $HOME '.agents\skills'}
$backup=Join-Path $repo ('.install-backups\'+(Get-Date -Format 'yyyyMMdd-HHmmss'))
$items=@()
if($Component -in @('all','router')){$items+=@(@{Source=(Join-Path $repo 'skills\codex-task-router');Dest=(Join-Path $SkillsHome 'codex-task-router');Kind='directory'})}
if($Component -in @('all','progress')){$items+=@(@{Source=(Join-Path $repo 'skills\activity-progress-reporting');Dest=(Join-Path $SkillsHome 'activity-progress-reporting');Kind='directory'})}
if($Component -in @('all','agents')){Get-ChildItem -LiteralPath (Join-Path $repo 'agents') -Filter '*.toml' -File | ForEach-Object {$items+=@(@{Source=$_.FullName;Dest=(Join-Path (Join-Path $CodexHome 'agents') $_.Name);Kind='file'})}}
foreach($i in $items){
 if(-not(Test-Path -LiteralPath $i.Source)){throw "Missing source: $($i.Source)"}
 $exists=Test-Path -LiteralPath $i.Dest
 if($exists -and -not $Force){Write-Output "SKIP_EXISTS $($i.Dest)";continue}
 if(-not $Apply){Write-Output "$(if($exists){'WOULD_BACKUP_REPLACE'}else{'WOULD_INSTALL'}) $($i.Source) -> $($i.Dest)";continue}
 if($exists){
   $relative=if($i.Kind -eq 'file'){'agents\'+[IO.Path]::GetFileName($i.Dest)}else{'skills\'+[IO.Path]::GetFileName($i.Dest)}
   $backupTarget=Join-Path $backup $relative
   New-Item -ItemType Directory -Force -Path (Split-Path $backupTarget -Parent) | Out-Null
   Copy-Item -LiteralPath $i.Dest -Destination $backupTarget -Recurse -Force
   Remove-Item -LiteralPath $i.Dest -Recurse -Force
   Write-Output "BACKUP $backupTarget"
 }
 New-Item -ItemType Directory -Force -Path (Split-Path $i.Dest -Parent) | Out-Null
 Copy-Item -LiteralPath $i.Source -Destination $i.Dest -Recurse -Force
 Write-Output "INSTALLED $($i.Dest)"
}
Write-Output "MODE=$(if($Apply){'APPLY'}else{'DRY_RUN'}) COMPONENT=$Component"
