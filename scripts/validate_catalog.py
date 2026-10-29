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

expected_r44 = {
    "backend_engineer": ("gpt-6-luna", "xhigh"),
    "frontend_engineer": ("gpt-6-luna", "xhigh"),
    "test_engineer": ("gpt-6-luna", "xhigh"),
    "validator": ("gpt-6-luna", "xhigh"),
    "scribe": ("gpt-6-luna", "high"),
    "reviewer": ("gpt-6.1-terra", "medium"),
    "security_reviewer": ("gpt-6.1-terra", "medium"),
    "integration_engineer": ("gpt-6.1-terra", "medium"),
    "ui_ux_analyst": ("gpt-6.1-terra", "medium"),
    "principal_implementer": ("gpt-6.1-terra", "medium"),
}
for name, (model, effort) in expected_r44.items():
    profile = profiles[name]
    assert (profile["model"], profile["model_reasoning_effort"]) == (model, effort), name
for name, profile in profiles.items():
    if profile["model"] == "gpt-6.1-terra":
        assert profile["model_reasoning_effort"] == "medium", name
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
assert "R4.4" in (references / "agent-catalog.md").read_text(encoding="utf-8")
print(f"PASS TOML: {len(profiles)} profiles; R4.4 requested assignments; catalog/policy parity; router invariants")
