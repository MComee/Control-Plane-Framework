import os
import yaml
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
REGISTRY_PATH = os.path.join(BASE_DIR, 'framework', 'ARTIFACT-REGISTRY.yaml')
STATE_PATH = os.path.join(BASE_DIR, 'framework', 'STATE-MODEL.yaml')


def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def extract_metadata(path):
    full = os.path.join(BASE_DIR, path)
    if not os.path.exists(full):
        return None

    with open(full, 'r') as f:
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

    registry = load_yaml(REGISTRY_PATH)
    state_model = load_yaml(STATE_PATH)

    artifact_meta = {}

    # Load metadata for all artifacts
    for name, data in registry['artifacts'].items():
        meta = extract_metadata(data['path'])
        if not meta:
            errors.append((name, "MISSING_METADATA"))
            continue
        artifact_meta[name] = meta

    # Dependency validation
    for name, meta in artifact_meta.items():
        deps = meta.get('dependencies', [])
        for dep in deps:
            if dep not in artifact_meta:
                errors.append((name, f"MISSING_DEPENDENCY:{dep}"))

    # Lifecycle validation
    for name, meta in artifact_meta.items():
        state = meta.get('status')
        deps = meta.get('dependencies', [])

        if state == 'accepted':
            for dep in deps:
                dep_state = artifact_meta.get(dep, {}).get('status')
                if dep_state not in ['validated', 'accepted']:
                    errors.append((name, f"INVALID_ACCEPTANCE:{dep}"))

    if errors:
        print("VALIDATION V4 FAILED")
        for e in errors:
            print(e)
        sys.exit(1)
    else:
        print("VALIDATION V4 PASSED")


if __name__ == '__main__':
    main()
