"""
manifest.py: Parse TOML manifest and build relationships
"""

from tomli import load

from dataclasses import dataclass


@dataclass
class Item:
    name: str
    value: str
    groups: list[str]


@dataclass
class Group:
    name: str
    groups: list[str]


class Manifest:
    def __init__(self, toml_path: str) -> None:
        with open(toml_path, "rb") as f:
            self.data: dict[str, dict[str, str | list[str]]] = load(f)

        self.items: dict[str, Item] = {
            k: Item(k, value=v["value"], groups=v["groups"])
            for k, v in self.data["item"].items()
        }

        self.groups: dict[str, Group] = {
            k: Group(k, groups=v.get("groups")) for k, v in self.data["group"].items()
        }

        # VALIDATE EXISTENCE

        self.items_in_groups: dict[str, set[str]] = self.bind_items_to_groups()

    def bind_items_to_groups(self) -> dict[str, set[str]]:
        """
        Core logic to create the mappings defined of in the manifest
        """
        populated_groups: dict[str, set[str]] = {k: set() for k in self.groups}

        # Groups receive the items they are assigned
        for item in self.items.values():
            if not item.groups:
                continue
            for group in item.groups:
                populated_groups[group].add(item.name)

        # Groups that are members of other groups will have all their items shared
        for group in self.groups.values():
            if not group.groups:
                continue
            for parent_group in group.groups:
                # merge the sets
                populated_groups[parent_group].update(populated_groups[group.name])


        return populated_groups
