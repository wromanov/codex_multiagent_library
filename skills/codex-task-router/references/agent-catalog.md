# Agent Catalog — package R3

Este catálogo documenta os perfis distribuídos na biblioteca. Não comprova instalação, acesso ao modelo ou permissão técnica. O ROOT confere os perfis efetivamente disponíveis no Codex antes de delegar.

| Agente | Modelo declarado | Esforço | Função |
|---|---|---|---|
| architect | gpt-6.1-sol | high | Arquitetura, NO_WRITE |
| backend_engineer | gpt-6-luna | high | Implementação backend |
| data_bi_engineer | gpt-6-luna | high | Implementação dados e BI |
| diagnostic_analyst | gpt-6.1-sol | medium | Diagnóstico, NO_WRITE |
| frontend_engineer | gpt-6-luna | high | Implementação frontend |
| implementer | gpt-6-luna | high | Implementação geral |
| integration_engineer | gpt-6-luna | high | Integrações e APIs |
| principal_architect | gpt-6-astra | medium | Consultoria arquitetural, NO_WRITE, somente pedido explícito do usuário |
| python_cli_engineer | gpt-6-luna | high | Python/CLI |
| researcher | gpt-6-luna | high | Pesquisa, READ_ONLY funcional |
| reviewer | gpt-6.1-sol | high | Revisão independente, READ_ONLY funcional |
| scout | gpt-6-luna | medium | Descoberta, READ_ONLY funcional |
| scribe | gpt-6-luna | medium | Documentação |
| security_reviewer | gpt-6.1-sol | high | Segurança, READ_ONLY funcional |
| test_engineer | gpt-6-luna | high | Engenharia de testes |
| triage | gpt-6-luna | medium | Triagem, READ_ONLY funcional |
| ui_ux_analyst | gpt-6.1-sol | high | UI/UX, READ_ONLY funcional |
| validator | gpt-6-luna | high | Validação, READ_ONLY funcional |

Ao rodar o router, os perfis instalados normalmente ficam em `$CODEX_HOME/agents` ou `$HOME/.codex/agents`. Consulte as versões efetivamente instaladas; não presuma que os perfis desta tabela estão disponíveis.
