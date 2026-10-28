param([string]$Root)
$ErrorActionPreference='Stop'
if(-not $Root){$Root=(Resolve-Path (Join-Path $PSScriptRoot '..')).Path}
$names=@('codex-task-router','activity-progress-reporting')
foreach($name in $names){
 $p=Join-Path $Root "skills\$name\SKILL.md"
 if(-not(Test-Path $p)){throw "Missing $p"}
 $s=Get-Content $p -Raw -Encoding UTF8
 if($s -notmatch "(?s)^---\s*\r?\nname:\s*$([regex]::Escape($name))\s*\r?\ndescription:"){throw "Invalid skill frontmatter: $name"}
 Write-Output "PASS skill $name"
}
$files=@(Get-ChildItem (Join-Path $Root 'agents') -Filter '*.toml' -File)
if($files.Count -ne 19){throw "Expected 19 agents, got $($files.Count)"}
python (Join-Path $Root 'scripts\validate_catalog.py')
if($LASTEXITCODE -ne 0){throw 'TOML validation failed'}
$router=Get-Content (Join-Path $Root 'skills\codex-task-router\SKILL.md') -Raw -Encoding UTF8
if($router -notmatch 'ROUTER_INVOCATION = USER_EXPLICIT_ONLY'){throw 'Router must be explicit'}
if($router -notmatch 'DEFAULT_EXECUTION_MODE = DIRECT'){throw 'Direct mode missing'}
if($router -notmatch 'DEFAULT_SUBAGENTS = 0'){throw 'Direct zero-spawn invariant missing'}
if($router -notmatch 'ROUTER_AUTO_INVOCATION = DISABLED'){throw 'Router auto-invocation must remain disabled'}
Write-Output 'VALIDATION=PASS; RUNTIME_DISCOVERY=UNVERIFIED'
