import yaml

class ControlPlaneRules:
    def __init__(self, state_model, dep_graph):
        self.state_model = state_model
        self.dep_graph = dep_graph

    def validate_state_transition(self, current, target):
        allowed = self.state_model['transitions'].get(current, [])
        return target in allowed

    def enforce_lifecycle(self, artifact, state, dependencies):
        errors = []

        if state == 'accepted':
            for dep in dependencies:
                if dep.get('status') not in ['validated', 'accepted']:
                    errors.append(f"Dependency {dep['name']} not validated")

        if state == 'in-progress' and not dependencies:
            errors.append("Execution without planning dependency")

        return errors

    def validate_dependency_direction(self, artifact, deps):
        errors = []
        current_lane = self.dep_graph['artifacts'][artifact]['lane']

        for dep in deps:
            dep_lane = self.dep_graph['artifacts'][dep]['lane']
            if dep_lane == 'validation' and current_lane == 'planning':
                errors.append(f"Invalid backward dependency: {artifact} -> {dep}")

        return errors
