# Python Modules
from tempfile import TemporaryDirectory 
from os import path

# Third-Party Modules
from yaml import safe_load

# Local Modules
from yambler.manifest import Manifest
from yambler.yaml_builder import YAMLBuilder
from tests.common import make_sample_manifest

def test_yaml_builder_output():
    with TemporaryDirectory() as tmpdir:
        toml_path = path.join(tmpdir, "manifest.toml")
        make_sample_manifest(toml_path)
        manifest = Manifest(toml_path)

    builder = YAMLBuilder(manifest)
    yaml_str = builder.build_yaml()
    data = safe_load(yaml_str)
    assert isinstance(data, dict)
    assert "groups" in data and isinstance(data["groups"], dict)
    groups = data["groups"]
    assert set(groups.get("g2", [])) == {"bar", "qux"}
    assert set(groups.get("g1", [])) == {"bar"}
