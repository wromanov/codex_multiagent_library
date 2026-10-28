from pathlib import Path
import tomllib
root=Path(__file__).resolve().parents[1]
agents=sorted((root/"agents").glob("*.toml"))
assert len(agents)==19, f"Expected 19, found {len(agents)}"
for path in agents:
    with path.open("rb") as f: data=tomllib.load(f)
    assert data.get("name")==path.stem, path
    for k in ("model","model_reasoning_effort","description","developer_instructions"):
        assert data.get(k), (path,k)
principal = root / "agents" / "principal_implementer.toml"
with principal.open("rb") as f:
    profile = tomllib.load(f)
assert profile["model"] == "gpt-6.1-terra"
assert profile["model_reasoning_effort"] == "medium"
assert "WRITE_SCOPED" in profile["developer_instructions"]
for reference in (
    "skills/codex-task-router/SKILL.md",
    "skills/codex-task-router/references/agent-catalog.md",
    "skills/codex-task-router/references/model-policy.md",
    "skills/codex-task-router/references/routing-matrix.md",
    "skills/codex-task-router/references/validation-cases.md",
):
    assert "principal_implementer" in (root / reference).read_text(encoding="utf-8"), reference
print(f"PASS TOML: {len(agents)} profiles; principal_implementer references")
