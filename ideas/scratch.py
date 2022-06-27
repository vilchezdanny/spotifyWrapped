from enum import Enum


class OrganizationRole(Enum):
    MANAGER = "manager"


class OrgRoleRange(Enum):
    MANAGER = range(1)


def main():
    my_role = OrganizationRole.MANAGER
    print(my_role)
    print(my_role.value)


if __name__ == "__main__":
    main()
