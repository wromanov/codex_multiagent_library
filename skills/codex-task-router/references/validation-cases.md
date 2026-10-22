# Casos de validação do router

Estes casos descrevem o comportamento esperado da skill. Não são testes runtime nem homologação.

1. Sem invocação explícita do router: DIRECT, ROOT, zero subagentes e nenhuma invocação automática.
2. O mesmo usuário impôs anteriormente `MULTI_AGENT = DISABLED`, `SUBAGENTS = FORBIDDEN` ou “não usar subagentes” e depois invoca explicitamente `$codex-task-router`: a proibição anterior desse usuário é revogada no escopo aplicável; ROOT executa o gate. A chamada comunica `MULTIAGENT_AUTHORIZATION=GRANTED`, `PRIOR_USER_SUBAGENT_BAN=REVOKED` e `ROUTER_GATE=REQUIRED` como convenção da skill, não parâmetros nativos.
3. O gate falha em qualquer critério cumulativo: permanece DIRECT, zero subagentes, e ROOT informa o critério concreto que falhou.
4. A invocação foi explícita e autorizada, mas o runtime não oferece ferramenta de spawn: permanece DIRECT para execução local possível e reporta-se bloqueio de capacidade do runtime, não falta de autorização.
5. Proibição expressa atual que acompanha a invocação, instrução de prioridade superior, limite de segurança ou sandbox/runtime: não é revogada nem superada; não delegar a ação afetada.
6. A invocação não muda o escopo: objetivo, recursos graváveis, acesso externo e ações autorizadas continuam limitados pelo pedido e instruções aplicáveis existentes.
7. Não há invocação implícita; a mera presença de TOML de perfil ou arquivos de agentes não autoriza spawn nem comprova que o runtime carregou ou executou um agente.
8. Delegação candidata: só avança quando competência, benefício material, escopo, autorização existente, permissões efetivas, segurança, ownership, dependências e capacidade estão claros.
9. Tarefa ou ação fora do escopo autorizado: não é habilitada pelo router; suspender só a ação afetada e solicitar decisão aplicável.
10. Pedido explícito de principal_architect: pode ser considerado; sem esse pedido, não selecionar o perfil.
11. Seleção de especialista não altera seus limites funcionais, modelo/esforço efetivos ou capacidades do runtime.
12. NO_WRITE funcional não comprova isolamento técnico; STRICT_READ_ONLY exige proteção efetiva antes do trabalho.
13. Handoff suficiente na solicitação do usuário e nas instruções do projeto não exige Card adicional nem arquivo de contrato separado.
14. Handoff opcional: organizar no prompt os campos úteis e omitir campos que já estejam claros.
15. ROOT integra a entrega e valida o resultado; validator fornece evidência e não corrige.
16. Nenhuma referência a política externa é necessária para interpretar esta skill ou decidir o gate.
17. Presença da skill não comprova carregamento nativo. Não declarar homologação sem evidência runtime.
18. Reaproveitar agente ativo e adequado quando reduzir inicialização ou preservar contexto; não repetir análise já válida sem necessidade concreta.
19. Tarefas dependentes seguem a ordem necessária; paralelismo é reservado a partes independentes quando houver ganho material.
20. Escolher perfil de menor custo quando competência e qualidade esperada forem equivalentes; selecionar perfil Sol mais caro somente quando sua especialização melhorar materialmente a análise.
21. `implementer` pode executar em modo MECHANICAL quando especificação, aceite e decisões materiais estiverem definidos; se faltar decisão relevante, suspender somente a parte afetada ou manter abordagem de engenharia.
22. Para documentação substancial delegada, preferir `scribe` quando adequado, sem torná-lo perfil exclusivo para qualquer escrita.
23. Revisão independente só é acrescentada quando solicitada, exigida pelo aceite ou justificada por risco/necessidade concreta; sem ganho material, manter DIRECT.
24. Competência efetiva, escopo, autorização, permissões e proteção continuam gates cumulativos; heurísticas de custo ou disponibilidade não os substituem.
