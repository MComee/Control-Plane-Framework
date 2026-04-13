import os
import yaml
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CONTRACT_PATH = os.path.join(BASE_DIR, 'framework', 'FRAMEWORK-CONTRACT.yaml')
STATE_PATH = os.path.join(BASE_DIR, 'framework', 'STATE-MODEL.yaml')
DEP_PATH = os.path.join(BASE_DIR, 'framework', 'DEPENDENCY-GRAPH.yaml')


def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def check_metadata(file_path):
    full_path = os.path.join(BASE_DIR, file_path)
    if not os.path.exists(full_path):
        return ["FILE_MISSING"]

    with open(full_path, 'r') as f:
        content = f.read()

    if not content.startswith('---'):
        return ["MISSING_METADATA"]

    return []


def validate_dependencies(dep_graph):
    errors = []
    for artifact, data in dep_graph['artifacts'].items():
        deps = data.get('depends_on', [])
        if artifact != 'mission' and not deps:
            errors.append((artifact, "NO_DEPENDENCIES"))
    return errors


def main():
    errors = []

    contract = load_yaml(CONTRACT_PATH)
    state_model = load_yaml(STATE_PATH)
    dep_graph = load_yaml(DEP_PATH)

    # Validate metadata existence
    for artifact in contract['artifacts'].keys():
        meta_errors = check_metadata(artifact)
        if meta_errors:
            errors.append((artifact, meta_errors))

    # Validate dependency graph
    dep_errors = validate_dependencies(dep_graph)
    if dep_errors:
        errors.extend(dep_errors)

    if errors:
        print("VALIDATION V2 FAILED")
        for e in errors:
            print(e)
        sys.exit(1)
    else:
        print("VALIDATION V2 PASSED")


if __name__ == '__main__':
    main()
