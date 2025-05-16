# rbac_system.py

class Permission:
    def __init__(self, name):
        self.name = name

class Role:
    def __init__(self, name):
        self.name = name
        self.permissions = set()

    def add_permission(self, permission):
        self.permissions.add(permission)

class User:
    def __init__(self, username):
        self.username = username
        self.roles = set()

    def assign_role(self, role):
        self.roles.add(role)

    def has_permission(self, permission):
        return any(permission in role.permissions for role in self.roles)


# Sample data setup
def setup_system():
    # Define permissions
    deploy = Permission("deploy")
    view_logs = Permission("view_logs")
    run_tests = Permission("run_tests")
    access_secrets = Permission("access_secrets")

    # Define roles and their permissions
    dev_role = Role("Developer")
    dev_role.add_permission(run_tests)

    qa_role = Role("QA")
    qa_role.add_permission(view_logs)
    qa_role.add_permission(run_tests)

    ops_role = Role("DevOps")
    ops_role.add_permission(deploy)
    ops_role.add_permission(view_logs)
    ops_role.add_permission(access_secrets)

    admin_role = Role("Admin")
    admin_role.permissions = {deploy, view_logs, run_tests, access_secrets}

    # Create users and assign roles
    alice = User("Alice")
    alice.assign_role(dev_role)

    bob = User("Bob")
    bob.assign_role(qa_role)

    fatima = User("Fatima")
    fatima.assign_role(ops_role)

    john = User("John")
    john.assign_role(admin_role)

    return [alice, bob, fatima, john]


# Check access
def check_access(user, action):
    if user.has_permission(Permission(action)):
        print(f"✅ {user.username} is allowed to {action}.")
    else:
        print(f"❌ {user.username} is NOT allowed to {action}.")


if __name__ == "__main__":
    users = setup_system()

    actions_to_test = ["deploy", "run_tests", "access_secrets", "view_logs"]

    for user in users:
        print(f"\nPermissions for {user.username}:")
        for action in actions_to_test:
            check_access(user, action)
