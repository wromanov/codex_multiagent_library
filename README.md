# Codex Multiagent Library

Biblioteca portátil de **duas skills independentes** e **19 perfis opcionais de agentes** para o Codex.

- `codex-task-router`: **somente invocação explícita pelo usuário**. Toda atividade começa em DIRECT, com zero subagentes. O ROOT pode avaliar delegação depois da invocação.
- `activity-progress-reporting`: relatórios de progresso para atividades com múltiplas etapas. A telemetria é aditiva e acompanha marcos reais (4%, 8%, ...); não inventa checkpoints.
- `agents/`: 19 perfis TOML opcionais para delegação autorizada, incluindo `principal_implementer` (GPT-6.1 Terra/Medium) para correções pontuais que exijam julgamento técnico local e escrita delimitada. O novo perfil dispensa contrato documental separado quando a solicitação e as instruções pertinentes já fornecem objetivo, autorização, escopo e aceite; não dispensa esses requisitos.

> A presença destes arquivos não comprova que determinado modelo ou subagente esteja disponível no runtime. A regra NO_WRITE dos agentes analíticos é funcional, não isolamento técnico.

## Instalação no Windows

Repositório oficial: https://github.com/wromanov/codex_multiagent_library

```powershell
git clone https://github.com/wromanov/codex_multiagent_library.git
cd codex_multiagent_library
.\scripts\validate.ps1
.\scripts\install.ps1 -Component all     # dry-run, sem gravação
.\scripts\install.ps1 -Component router -Apply
.\scripts\install.ps1 -Component progress -Apply
.\scripts\install.ps1 -Component agents -Apply
```

As skills vão por padrão para `$HOME\.agents\skills`; os perfis para `$CODEX_HOME\agents` ou `$HOME\.codex\agents`. É possível instalar cada componente separadamente com `-Component router|progress|agents|all`.

Arquivos existentes são **preservados por padrão**. Para atualizar intencionalmente uma instalação existente, execute primeiro o dry-run com `-Force` e depois `-Apply -Force`. As cópias anteriores ficam em `.install-backups` (ignoradas pelo Git). Verifique esses backups antes de descartar versões antigas. Recomenda-se reiniciar a sessão Codex e testar a descoberta explicitamente após a instalação.

```powershell
git pull --ff-only
.\scripts\update.ps1 -Component all -Force       # dry-run
.\scripts\update.ps1 -Component all -Force -Apply # atualiza com backup
```

Os scripts não alteram `config.toml` nem `AGENTS.md`. A progress skill pode ser descoberta implicitamente quando adequada, mas sua ativação em todas as atividades não é garantida pelo simples fato de estar instalada.

## Validação e publicação

```powershell
.\scripts\validate.ps1
git status --short
git diff --check
```

**Antes de qualquer publicação**, revisar `git status`, `git diff --cached`, as permissões e todos os arquivos para evitar exposição de segredos e dados pessoais. Não usar `git push --force`. A validação offline não substitui homologação runtime.

## Estrutura

```text
agents/                          # 19 perfis
skills/codex-task-router/        # roteamento explícito + catálogo portátil
skills/activity-progress-reporting/
scripts/install.ps1              # simulação por padrão
scripts/update.ps1               # atualização com simulação por padrão
scripts/validate.ps1             # validação local
scripts/validate_catalog.py      # parse TOML e integridade
```
