import os
import yaml
import sys
from control_plane_rules import ControlPlaneRules

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATE_PATH = os.path.join(BASE_DIR, 'framework', 'STATE-MODEL.yaml')
DEP_PATH = os.path.join(BASE_DIR, 'framework', 'DEPENDENCY-GRAPH.yaml')


def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def extract_metadata(file_path):
    full_path = os.path.join(BASE_DIR, file_path)
    if not os.path.exists(full_path):
        return None

    with open(full_path, 'r') as f:
        lines = f.readlines()

    if not lines or not lines[0].startswith('---'):
        return None

    yaml_block = []
    for line in lines[1:]:
        if line.startswith('---'):
            break
        yaml_block.append(line)

    return yaml.safe_load(''.join(yaml_block))


def main():
    errors = []

    state_model = load_yaml(STATE_PATH)
    dep_graph = load_yaml(DEP_PATH)
    rules = ControlPlaneRules(state_model, dep_graph)

    artifacts = dep_graph['artifacts']

    for name, data in artifacts.items():
        file_guess = f"framework/{data['lane']}/{name}.template.v2.md"
        meta = extract_metadata(file_guess)

        if not meta:
            errors.append((name, "MISSING_METADATA"))
            continue

        deps = meta.get('dependencies', [])
        state = meta.get('status')

        # Lifecycle enforcement
        lifecycle_errors = rules.enforce_lifecycle(name, state, [{'name': d, 'status': 'draft'} for d in deps])
        if lifecycle_errors:
            errors.append((name, lifecycle_errors))

        # Dependency direction
        dir_errors = rules.validate_dependency_direction(name, deps)
        if dir_errors:
            errors.append((name, dir_errors))

    if errors:
        print("VALIDATION V3 FAILED")
        for e in errors:
            print(e)
        sys.exit(1)
    else:
        print("VALIDATION V3 PASSED")


if __name__ == '__main__':
    main()
