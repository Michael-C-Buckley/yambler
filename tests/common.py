TEST_MANIFEST = """
[item.foo]
value = "bar"
groups = ["g1"]

[item.baz]
value = "qux"
groups = ["g2"]

[group.g1]
groups = ["g2"]

[group.g2]
groups = []
"""

def make_sample_manifest(path):
    with open(path, "wb") as f:
        f.write(TEST_MANIFEST.encode())