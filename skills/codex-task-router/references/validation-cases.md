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
25. Após gate MULTIAGENT aprovado, várias frentes independentes, com ganho material e dentro da capacidade/runtime, são atribuídas a perfis adequados com ownership, escopo e aceite claros e iniciadas em paralelo sem pedido adicional do usuário; o número de frentes é proporcional, sem ocupar slots artificialmente.
26. Após gate aprovado, ROOT mapeia dependências e executa frentes dependentes na ordem necessária, iniciando cada uma quando seus inputs estiverem prontos.
27. Duas frentes que exigem escrita no mesmo arquivo/recurso não recebem ownership conflitante: ROOT define ownership exclusivo ou serializa a escrita e coordena integração.
28. Com gate aprovado, ROOT mantém integração/build/QA ou outro trabalho próprio do caminho crítico quando apropriado, mas não centraliza correções independentemente delegáveis com benefício material; monitora bloqueios, integra contribuições e valida o conjunto.
29. Sem invocação explícita, mesmo diante de várias frentes e agentes disponíveis, ROOT permanece DIRECT e cria zero agentes.
30. Gate aprovado não obriga usar todos os agentes nem spawn sem ganho material; capacidade de runtime, permissão ou autorização insuficiente mantém a frente em DIRECT ou bloqueia somente a ação afetada com causa explícita.
31. Planejamento de paralelismo não cria papéis, cards, gates ou documentos por formalidade e não transfere de ROOT a accountability final.
32. Agente READ_ONLY/NO_WRITE recebe apenas atribuição compatível com seu limite funcional; capacidade de spawn ou ownership claro não autoriza edição. Capacidade runtime não observável permanece UNVERIFIED, sem alegação de comprovação.
33. H04 — Distribuição antes da edição: com MULTIAGENT aprovado e trabalho independente elegível, ROOT explicita responsáveis, ownership, dependências, contratos compartilhados e aceite antes da primeira edição relevante da fase; despacha as frentes independentes prontas antes de iniciar sua própria edição independente, respeitando capacidade e benefício material.
34. H05 — Descoberta para implementação: uma descoberta delegada conclui e revela trabalho de implementação distribuível. Antes da primeira edição da fase seguinte, ROOT reavalia o trabalho restante, atualiza a distribuição, confere os critérios pertinentes à nova missão e despacha as frentes prontas. A delegação de discovery não substitui essa transição.
35. H06 — Dependências e contratos compartilhados: duas frentes dependem de preparação ou contrato comum. ROOT atribui ownership explícito, pode executar a preparação necessária e despacha as dependentes quando os inputs estiverem prontos; mantém em andamento frentes independentes elegíveis e impede escrita sobreposta no mesmo recurso.
36. H07 — Limites funcionais na reutilização: um agente READ_ONLY/NO_WRITE conclui uma análise e a próxima missão exige implementação. ROOT revalida competência, escopo e permissões, preserva o limite funcional e atribui a escrita a executor compatível. Uma nova instrução, disponibilidade ou contexto preservado não converte o agente consultivo em implementador.
37. H10 — Integração e validação: agentes entregam relatórios individuais positivos, mas o resultado integrado pode violar um contrato compartilhado ou critério de aceite. ROOT confere o conjunto, identifica a inconsistência, encaminha a correção ao owner e repete a validação afetada; não declara conclusão apenas pelos relatórios dos agentes.

38. R01 — O rollout próprio do filho é correlacionado à criação e ao vínculo pai-filho; seu primeiro turn_context próprio registra modelo e esforço, que são classificados separadamente como RUNTIME_VERIFIED e comparados às fontes declarada e solicitada disponíveis.
39. R02 — O rollout inclui contexto herdado do pai e turnos próprios do filho; ROOT usa somente o primeiro contexto próprio comprovado. Se a origem não puder ser distinguida, classifica modelo/esforço como UNVERIFIED.
40. R03 — O rollout ainda não existe, está inacessível, não contém os campos necessários ou não pode ser correlacionado; ROOT informa UNVERIFIED e a causa, sem simular comprovação nem exigir espera/polling. Uma delegação consultiva comum pode prosseguir; se a prova for critério de aceite anterior a uma ação, somente essa ação fica pendente, e uma consulta posterior não prova gate retroativo.
41. R04 — O modelo ou esforço observado diverge de uma declaração ou solicitação identificada; ROOT relata os valores, fontes, evidência e impacto da divergência, sem alterar configuração, substituir agente ou repetir o spawn automaticamente.
42. R05 — Configurações locais e globais declaram valores diferentes; ROOT registra as fontes separadamente e não presume qual arquivo foi carregado, nem infere que o modelo/esforço foram solicitados a partir do perfil.
43. R06 — Uma delegação consultiva comum não tem verificação de modelo/esforço como critério material de risco, custo ou aceite; ROOT não faz busca extensa em logs por rotina.
44. R07 — A consulta usa apenas sessão correlacionada e autorizada e extrai os metadados necessários; ROOT não expõe conteúdo integral de logs, prompts, credenciais, tokens ou dados pessoais, não transmite logs a subagentes e não altera sessão, log ou configuração.
45. P01 — `principal_implementer` é candidato Terra/Medium para correção pontual com incerteza técnica local, quando o gate de delegação passar; sua existência não aciona o router nem altera o padrão DIRECT.
46. P02 — Pedido, Card ou instruções do projeto já definem objetivo, autorização, ownership, restrições e aceite: o novo perfil pode investigar, implementar e validar sem exigir contrato documental adicional.
47. P03 — Solicitação sem autorização material, ownership ou limite de escrita claro: não presumir permissão; retornar a decisão ao ROOT e bloquear apenas a parte afetada.
48. P04 — Correção local encontra alteração de arquitetura, contrato público, segurança, dados ou migração material: parar antes da alteração consequencial e encaminhar alternativas/evidências ao ROOT.
49. P05 — `implementer` MECHANICAL permanece preferível para tarefa fechada; `principal_implementer` não substitui especialista de domínio nem revisor independente; custo e ganho material orientam a seleção.
50. P06 — O perfil declara GPT-6.1 Terra/Medium e WRITE_SCOPED, mas a invocação real, o modelo, o esforço e o sandbox permanecem UNVERIFIED sem evidência runtime. Nenhuma escalada, mudança de modo ou subdelegação é implícita.
51. M01 — A R4.3 preserva 19 perfis, e todos os oito agentes que declaram gpt-6.1-terra usam medium.
52. M02 — Os cinco antigos Terra/High passam a Terra/Medium; validator, scribe e principal_implementer permanecem Terra/Medium, sem ampliacao de permissao.
53. M03 — Luna, Sol e Astra nao mudam; DIRECT, zero subagentes, invocacao explicita e gate ROOT permanecem inalterados. Atualizar a skill nao substitui a sincronizacao dos TOMLs instalados.
