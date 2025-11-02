from tempfile import TemporaryDirectory
from os import path
from yambler.manifest import Manifest
from tests.common import make_sample_manifest

def test_manifest_parsing():
    with TemporaryDirectory() as tmpdir:
        toml_path = path.join(tmpdir, "manifest.toml")
        make_sample_manifest(toml_path)
        m = Manifest(toml_path)
        
        assert "foo" in m.items
        assert "g1" in m.groups
        assert m.items["foo"].value == "bar"
        assert m.groups["g1"].groups == ["g2"]

def test_items_in_groups():
    with TemporaryDirectory() as tmpdir:
        toml_path = path.join(tmpdir, "manifest.toml")
        make_sample_manifest(toml_path)
        m = Manifest(toml_path)

        # g2 should have both foo and baz due to group membership
        assert set(m.items_in_groups["g2"]) == {"foo", "baz"}
        assert set(m.items_in_groups["g1"]) == {"foo"}

    