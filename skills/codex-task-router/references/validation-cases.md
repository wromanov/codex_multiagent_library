# Casos de validação do router

Estes casos descrevem o comportamento esperado da skill. Não são testes runtime nem homologação.

1. Nova tarefa sem invocação explícita do router: DIRECT, ROOT, zero subagentes e sem invocação automática.
2. Usuário invoca explicitamente o router: ROOT avalia roteamento e benefício dentro do escopo já autorizado; não pede confirmação adicional para etapas já cobertas.
3. Invocação explícita sem ganho material ou sem gate aprovado: permanece DIRECT, zero subagentes.
4. Delegação candidata: só avança quando competência, benefício material, escopo, autorização existente, permissões efetivas, segurança, ownership, dependências e capacidade estão claros.
5. Tarefa ou ação fora do escopo autorizado: não é habilitada pelo router; suspender só a ação afetada e solicitar decisão aplicável.
6. Pedido explícito de principal_architect: pode ser considerado; sem esse pedido, não selecionar o perfil.
7. Seleção de especialista não altera seus limites funcionais, modelo/esforço efetivos ou capacidades do runtime.
8. NO_WRITE funcional não comprova isolamento técnico; STRICT_READ_ONLY exige proteção efetiva antes do trabalho.
9. Handoff suficiente na solicitação do usuário e nas instruções do projeto não exige Card adicional nem arquivo de contrato separado.
10. Handoff opcional: organizar no prompt os campos úteis e omitir campos que já estejam claros.
11. ROOT integra a entrega e valida o resultado; validator fornece evidência e não corrige.
12. Nenhuma referência a política externa é necessária para interpretar esta skill ou decidir o gate.
13. Presença da skill não comprova carregamento nativo. Não declarar homologação sem evidência runtime.