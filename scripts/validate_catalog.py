from pathlib import Path
import tomllib
root=Path(__file__).resolve().parents[1]
agents=sorted((root/"agents").glob("*.toml"))
assert len(agents)==18, f"Expected 18, found {len(agents)}"
for path in agents:
    with path.open("rb") as f: data=tomllib.load(f)
    assert data.get("name")==path.stem, path
    for k in ("model","model_reasoning_effort","description","developer_instructions"):
        assert data.get(k), (path,k)
print(f"PASS TOML: {len(agents)} profiles")
