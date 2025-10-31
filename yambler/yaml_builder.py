"""
yaml_builder.py: Generate YAML output from manifest
"""
# Third-Party Modules
import yaml

# Local Modules
from yambler.manifest import Manifest

class YAMLBuilder:
    def __init__(self, manifest: Manifest) -> None:
        self.manifest: Manifest = manifest

    def build_yaml(self) -> str:
        group_to_values = {}
        for group, names in self.manifest.items_in_groups.items():
            group_to_values[group] = [self.manifest.items[name].value for name in names]
        return yaml.dump({"groups": group_to_values}, sort_keys=True)

