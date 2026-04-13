import os
import yaml
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CONTRACT_PATH = os.path.join(BASE_DIR, 'framework', 'FRAMEWORK-CONTRACT.yaml')


def load_contract():
    with open(CONTRACT_PATH, 'r') as f:
        return yaml.safe_load(f)


def check_files(file_list):
    missing = []
    for f in file_list:
        if not os.path.exists(os.path.join(BASE_DIR, f)):
            missing.append(f)
    return missing


def check_headings(file_path, required_headings):
    full_path = os.path.join(BASE_DIR, file_path)
    if not os.path.exists(full_path):
        return ["FILE_MISSING"]

    with open(full_path, 'r') as f:
        content = f.read()

    missing = []
    for h in required_headings:
        if h not in content:
            missing.append(h)

    return missing


def main():
    contract = load_contract()
    errors = []

    # Protocol layer
    missing_protocol = check_files(contract['protocol_layer']['required_files'])
    if missing_protocol:
        errors.append(("protocol_layer", missing_protocol))

    # Lanes
    for lane, data in contract['lanes'].items():
        missing = check_files(data['required_files'])
        if missing:
            errors.append((f"lane:{lane}", missing))

    # Artifacts
    for artifact, rules in contract['artifacts'].items():
        missing = check_headings(artifact, rules['required_headings'])
        if missing:
            errors.append((f"artifact:{artifact}", missing))

    # Support files
    missing_support = check_files(contract['required_support_files'])
    if missing_support:
        errors.append(("support_files", missing_support))

    if errors:
        print("VALIDATION FAILED")
        for e in errors:
            print(e)
        sys.exit(1)
    else:
        print("VALIDATION PASSED")


if __name__ == '__main__':
    main()
