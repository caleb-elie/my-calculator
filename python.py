from functools import wraps

ROLE_HIERARCHY = {"user": [], "manager": ["user"], "admin": ["manager", "user"]}

current_user_role = "user"  

def authorize(*required_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            def has_permission(role, required_role):
                if role == required_role:
                    return True
                return required_role in ROLE_HIERARCHY.get(role, [])

            if any(has_permission(current_user_role, role) for role in required_roles):
                print(f"Access granted for role: {current_user_role}")
                return func(*args, **kwargs)
            else:
                print(
                    f"Access Denied. {current_user_role} does not have permission to perform this action."
                )
                return None

        return wrapper

    return decorator


@authorize("admin")
def delete_file(filename):
    print(f"File '{filename}' has been deleted.")


@authorize("manager", "admin")
def approve_request(request):
    print(f"Request '{request}' has been approved.")



delete_file("important_document.txt")  
current_user_role = "manager"
delete_file("important_document.txt")  
approve_request("Vacation Approval")  
