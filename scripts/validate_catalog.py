from pathlib import Path
import tomllib

root = Path(__file__).resolve().parents[1]
agent_files = sorted((root / "agents").glob("*.toml"))
assert len(agent_files) == 19, f"Expected 19 agents, found {len(agent_files)}"
profiles = {}
for path in agent_files:
    with path.open("rb") as stream:
        profile = tomllib.load(stream)
    assert profile.get("name") == path.stem, path
    for key in ("model", "model_reasoning_effort", "description", "developer_instructions"):
        assert profile.get(key), (path, key)
    profiles[path.stem] = profile

terra_r42 = {
    "ui_ux_analyst": "high",
    "backend_engineer": "high",
    "frontend_engineer": "high",
    "integration_engineer": "high",
    "test_engineer": "high",
    "validator": "medium",
    "scribe": "medium",
    "principal_implementer": "medium",
}
for name, effort in terra_r42.items():
    profile = profiles[name]
    assert profile["model"] == "gpt-6.1-terra", name
    assert profile["model_reasoning_effort"] == effort, name
assert "WRITE_SCOPED" in profiles["principal_implementer"]["developer_instructions"]

references = root / "skills" / "codex-task-router" / "references"
def parse_reference(relative_path):
    rows = {}
    for line in (references / relative_path).read_text(encoding="utf-8").splitlines():
        if not line.startswith("| "):
            continue
        fields = [field.strip() for field in line.strip().strip("|").split("|")]
        if len(fields) < 4 or fields[0] not in profiles:
            continue
        assert fields[0] not in rows, (relative_path, fields[0])
        rows[fields[0]] = (fields[1], fields[2])
    assert set(rows) == set(profiles), (relative_path, sorted(set(profiles) - set(rows)))
    return rows

for reference in ("agent-catalog.md", "model-policy.md"):
    rows = parse_reference(reference)
    for name, profile in profiles.items():
        assert rows[name] == (profile["model"], profile["model_reasoning_effort"]), (reference, name)

skill = (root / "skills" / "codex-task-router" / "SKILL.md").read_text(encoding="utf-8")
for invariant in (
    "DEFAULT_EXECUTION_MODE = DIRECT",
    "DEFAULT_SUBAGENTS = 0",
    "ROUTER_INVOCATION = USER_EXPLICIT_ONLY",
    "ROUTER_AUTO_INVOCATION = DISABLED",
    "principal_implementer",
):
    assert invariant in skill, invariant
assert "R4.2" in (references / "agent-catalog.md").read_text(encoding="utf-8")
print(f"PASS TOML: {len(profiles)} profiles; Terra R4.2 targets; catalog/policy parity; router invariants")
