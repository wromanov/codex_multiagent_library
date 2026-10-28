# Política de perfil, modelo e permissão — catálogo candidato

ROLE != MODEL != EFFORT != TOOL_SURFACE != FUNCTIONAL_PERMISSION != EFFECTIVE_TECHNICAL_SANDBOX. Alvos declarados não provam seleção, capacidade ou isolamento runtime.

| Perfil | Modelo | Esforço | Limite funcional |
|---|---|---|---|
| architect | gpt-6.1-sol | high | NO_WRITE; advisory leaf |
| diagnostic_analyst | gpt-6.1-sol | medium | NO_WRITE; diagnóstico leaf |
| principal_architect | gpt-6-astra | medium | NO_WRITE; user-explicit-only; leaf |
| reviewer | gpt-6.1-sol | high | READ_ONLY funcional; revisão sem correção |
| security_reviewer | gpt-6.1-sol | high | READ_ONLY funcional; auditoria sem exploração destrutiva |
| ui_ux_analyst | gpt-6.1-sol | high | READ_ONLY funcional; análise sem edição |
| backend_engineer | gpt-6-luna | high | WRITE_SCOPED; path atribuído |
| frontend_engineer | gpt-6-luna | high | WRITE_SCOPED; path atribuído |
| python_cli_engineer | gpt-6-luna | high | WRITE_SCOPED; path atribuído |
| integration_engineer | gpt-6-luna | high | WRITE_SCOPED; path atribuído |
| data_bi_engineer | gpt-6-luna | high | WRITE_SCOPED; path atribuído |
| test_engineer | gpt-6-luna | high | WRITE_SCOPED; testes atribuídos |
| implementer | gpt-6-luna | high | WRITE_SCOPED; ENGINEERING ou MECHANICAL autorizado |
| principal_implementer | gpt-6.1-terra | medium | WRITE_SCOPED; correções pontuais com julgamento técnico local; sem novo contrato documental quando instruções são suficientes |
| scout | gpt-6-luna | medium | READ_ONLY funcional |
| researcher | gpt-6-luna | high | READ_ONLY funcional |
| triage | gpt-6-luna | medium | READ_ONLY funcional |
| validator | gpt-6-luna | high | READ_ONLY funcional; valida sem corrigir |
| scribe | gpt-6-luna | medium | DOCUMENTATION_SCOPED; documento atribuído |

architect, diagnostic_analyst e principal_architect não criam, editam, formatam, renomeiam ou excluem arquivos; não implementam, alteram configuração, executam Git mutável, materializam documentos, migram, instalam ou publicam. ROOT verifica ausência de mudanças. Isto é limite funcional, não isolamento técnico. Scribe materializa documentos atribuídos/autorizados; implementação cabe ao implementer ou executor especializado.

Não exigir sandbox individual em TOML. Sandbox e aprovação efetivos são administrados pela sessão ROOT/runtime. Se authority/risco exigir STRICT_READ_ONLY, proteção técnica precisa existir antes do spawn/início; checagem POST não corrige falta de proteção prévia. Não converter auditoria formal em advisory.

principal_architect usa Astra/Medium somente por pedido explícito. Não há gate de insuficiência do architect nem escalada automática por gravidade, urgência, recorrência ou recomendação. É leaf e não delega.

Catálogo candidato: ROOT + 19 perfis (20 papéis). ROOT retém gate, seleção e integração. `principal_implementer` não possui authority ampliada; requer autorização, ownership e aceite como qualquer outro executor.
