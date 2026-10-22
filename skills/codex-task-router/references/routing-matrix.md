# Matriz de intenção e roteamento

DIRECT é o padrão para toda nova atividade. A tabela identifica especialistas possíveis, não aciona o router nem exige delegação.

Somente após pedido explícito para usar o router o ROOT avalia a delegação, dentro do escopo do usuário. Toda delegação depende de benefício material, competência, autorização existente, permissões efetivas, segurança, ownership, dependências e capacidade. Sem ganho relevante ou sem gate aprovado, ROOT segue em DIRECT.

| Intenção | Candidato quando houver delegação | Consideração |
|---|---|---|
| Atividade nova | ROOT | DIRECT; zero subagentes por padrão. |
| Correção simples e delimitada | ROOT | Preferir execução direta quando suficiente. |
| Exploração factual | scout | Localizar arquivos, símbolos, fluxos ou dependências. |
| Pesquisa técnica | researcher | Usar quando documentação ou compatibilidade externa for necessária. |
| Diagnóstico | triage ou diagnostic_analyst | Escalar para diagnóstico especializado quando houver ganho real. |
| Análise arquitetural | architect | Somente para julgamento arquitetural material. |
| Arquitetura principal | principal_architect | Apenas por pedido explícito do usuário; Astra/Medium; NO_WRITE; leaf. |
| Revisão de código | reviewer | Revisão independente somente quando necessária ou solicitada. |
| Avaliação de segurança | security_reviewer | Respeitar proteção técnica e limites de leitura aplicáveis. |
| Avaliação de UI/UX | ui_ux_analyst | Análise sem escrita. |
| Implementação backend | backend_engineer | Escrita nos caminhos atribuídos e autorizados. |
| Implementação frontend | frontend_engineer | Escrita nos caminhos atribuídos e autorizados. |
| Implementação Python/CLI | python_cli_engineer | Escrita nos caminhos atribuídos e autorizados. |
| Integração técnica | integration_engineer | Ação externa exige autorização abrangente. |
| Implementação de dados/BI | data_bi_engineer | Escrita nos caminhos atribuídos e autorizados. |
| Implementação técnica geral | implementer | Engenharia para trabalho que exige decisões técnicas; modo MECHANICAL quando especificação, aceite e decisões materiais estiverem suficientemente fechados. |
| Testes | test_engineer | Somente escopo de testes atribuído e autorizado. |
| Validação independente | validator | Retorna evidências; não corrige. |
| Triage inicial | triage | Investiga; não valida nem corrige. |
| Documentação | scribe | Materializa documentos atribuídos; não cria decisões normativas. |

ROOT mantém o gate, a seleção, a delegação, a integração e a responsabilidade final. Reaproveite agentes ativos adequados, evite repetir análise válida e paralelize somente trabalho independente com ganho material. Prefira menor custo quando a qualidade esperada for equivalente; use especialização Sol quando ela melhorar materialmente a análise. `scribe` é preferência para documentação substancial delegada, não exclusividade de escrita. Revisão independente e demais gates devem ser proporcionais ao aceite, risco e benefício.

O perfil candidato não confirma disponibilidade de modelo, ferramenta ou isolamento no runtime.