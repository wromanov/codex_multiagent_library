---
name: codex-task-router
description: Use only when the user explicitly invokes codex-task-router or explicitly asks to use this skill. It guides ROOT and never delegates autonomously.
---

# Codex Task Router

DEFAULT_EXECUTION_MODE = DIRECT
DEFAULT_SUBAGENTS = 0

ROUTER_INVOCATION = USER_EXPLICIT_ONLY
ROUTER_AUTO_INVOCATION = DISABLED

MULTIAGENT_GATE_OWNER = ROOT
AGENT_SELECTION_OWNER = ROOT
DELEGATION_OWNER = ROOT
RESULT_INTEGRATION_OWNER = ROOT

## Acionamento e escopo

O router só é consultado quando o usuário o invoca explicitamente ou pede explicitamente seu uso. Complexidade, convenções de card, conteúdo sobre agentes ou volume de trabalho nunca o invocam por conta própria.

Antes da invocação explícita, a atividade permanece em DIRECT, com zero subagentes. Depois da invocação, ROOT avalia se MULTIAGENT agrega benefício real. A invocação autoriza essa avaliação e a delegação que passar pelo gate dentro do escopo já autorizado pelo usuário; não requer nova confirmação para agentes, etapas ou ações já abrangidos. Não autoriza expansão de escopo, ação externa ou mudança consequencial fora dessa autorização.

A solicitação do usuário, o Card Único e as instruções pertinentes do projeto podem constituir contrato operacional suficiente quando definirem objetivo, escopo, responsabilidades, recursos que podem ser alterados, restrições, resultado esperado e validação. Não exija um card adicional ou um documento separado quando esses elementos já estiverem claros.

## Avaliação do ROOT

Quando o usuário invocar o router:

1. Analise a solicitação e o trabalho restante.
2. Consulte o catálogo em [catálogo portátil de agentes](references/agent-catalog.md).
3. Identifique necessidades de análise, pesquisa, diagnóstico, documentação, implementação e validação.
4. Avalie se a divisão e a especialização trazem benefício material em relação à execução direta.
5. Selecione os perfis apropriados, conforme suas responsabilidades, modelos e permissões declaradas.
6. Defina dependências, ownership, paralelismo e limite de concorrência.
7. Confirme que o trabalho permanece no escopo autorizado, que as permissões efetivas e os recursos de segurança são suficientes, e que o runtime oferece a capacidade necessária.
8. Se o gate passar, delegue somente o trabalho autorizado, integre e valide os resultados. Caso contrário, permaneça em DIRECT.

Gates cumulativos para delegar: benefício material; tarefa delimitada e atribuível; competência adequada; escopo e autorização já cobrindo o trabalho; permissões e proteção efetivas; ownership e dependências claros; capacidade disponível. Se uma lacuna material exigir autorização ou decisão fora do pedido, suspenda somente a ação afetada e consulte o usuário.

O router é consultivo. ROOT decide o gate, seleciona agentes, autoriza a delegação dentro do escopo, integra o resultado e responde pela validação final. Invocar o router não obriga a criar subagentes.

## Perfis e limites

O catálogo técnico está em [catálogo portátil de agentes](references/agent-catalog.md). A matriz de intenção está em [routing-matrix.md](references/routing-matrix.md); critérios de perfil e disponibilidade declarada estão em [model-policy.md](references/model-policy.md). [handoff-contract.md](references/handoff-contract.md) oferece um resumo opcional para handoff, não um documento obrigatório. Casos ilustrativos estão em [validation-cases.md](references/validation-cases.md).

- architect — GPT-6.1 Sol / High; análise arquitetural; NO_WRITE funcional.
- diagnostic_analyst — GPT-6.1 Sol / Medium; diagnóstico; NO_WRITE funcional.
- principal_architect — GPT-6 Astra / Medium; NO_WRITE funcional; somente mediante pedido explícito do usuário nesta atividade; leaf.
- scribe — materializa documentação atribuída dentro da permissão efetiva.
- implementer — implementação técnica autorizada e delimitada.
- Os demais especialistas são considerados pelo ROOT apenas quando a tarefa exige sua competência.

NO_WRITE é limite funcional, não prova de isolamento técnico. Quando STRICT_READ_ONLY for necessário, confirme proteção técnica efetiva antes da atribuição. Perfis, TOML e texto de instruções não comprovam sandbox.

## Handoff e salvaguardas

Forneça ao agente o contexto suficiente na instrução de trabalho: objetivo, escopo, ownership, recursos autorizados, restrições, resultado e validação. Use o resumo opcional somente para organizar informação que ainda não esteja clara na solicitação ou nas instruções aplicáveis. Não crie um arquivo separado por formalidade.

Antes da atribuição, confira autorização e escopo, capacidade, ferramenta de delegação, perfil/modelo pretendido, permissões efetivas, ownership, dependências e limites de segurança. Não exija identificadores ou metadados de um filho antes de sua criação.

A verificação POST_SPAWN, antes de liberar trabalho substantivo, limita-se a informações pertinentes que o runtime exponha. ROOT registra os valores efetivamente observados e sua fonte: identidade, modelo/esforço, vínculo pai-filho, permissões/aprovações, ambiente/sandbox e capacidades relevantes. Valores de perfil ou configuração, bem como autodeclarações do filho sem confirmação do runtime, não provam a execução efetiva.

Para cada metadado não observável, registre `UNVERIFIED`. Esse estado indica ausência de evidência; não representa conformidade comprovada. A ausência isolada de telemetria não bloqueia tarefas consultivas comuns quando o contexto e a atribuição são identificáveis, o trabalho está autorizado, os limites funcionais podem ser aplicados, não se exige garantia técnica de identidade/modelo/isolamento e o agente não recebe acesso ou autoridade além do permitido.

Se a tarefa exigir comprovação efetiva de isolamento, identidade, modelo, privilégio, independência formal ou capacidade, a ausência ou divergência da evidência bloqueia somente a operação dependente dessa garantia. Uma instrução textual `NO_WRITE` é um limite funcional, não uma proteção técnica; não a apresente como comprovação de isolamento. Não contorne o bloqueio por substituição silenciosa, elevação, retry ou fallback automático.

A disponibilidade real de modelos, ferramentas, sandbox e invocação nativa depende do runtime. Não presuma suporte nativo pela presença destes arquivos. A leitura manual após pedido explícito não demonstra carregamento ou homologação nativa.