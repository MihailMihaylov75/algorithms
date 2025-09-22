"""
Problem:
Provide a reusable decorator that enforces access control on functions based on a
user's security level contained in an input mapping (e.g., {'secure_level': 'admin'}).

Rules:
- The decorated function must receive a user mapping (by default via the 'user' kwarg
  or as the first positional argument) that contains the key `secure_level`.
- If the user's level matches the required level, the function executes.
- Otherwise, a PermissionError is raised.

Examples:
    @access_level("admin")
    def get_admin_password(user: Mapping[str, Any]) -> int:
        return int(user["password"])

    @access_level("guest")
    def get_user_password(user: Mapping[str, Any]) -> int:
        return int(user["password"])
"""

import functools
from collections.abc import Callable, Mapping
from typing import Any, TypeVar, cast

# Define a generic type variable F that represents "some function type".
# By bounding it to Callable[..., Any], we guarantee F can only be a function
# (with any arguments and any return type). This allows the decorator to:
# 1) Accept a function of type F.
# 2) Return a function of the exact same type F.
# -> This way the original function signature is preserved across decoration.
F = TypeVar("F", bound=Callable[..., Any])


def _resolve_user(
    args: tuple[Any, ...],
    kwargs: dict[str, Any],
    user_arg: str,
) -> Mapping[str, Any]:
    """Resolves the 'user' mapping from the call-site.

    Resolution order:
    1) Prefer keyword argument named `user_arg` (e.g., 'user') if present and a Mapping.
    2) Else, use the first positional argument if it is a Mapping.
    3) Otherwise, raise ValueError to fail fast.

    Notes:
    - Works best for free functions where `user` is provided as `user=...` or first positional.
    - For bound methods (where `self` is args[0] and `user` is next), consider the
      'inspect.signature' approach shown below.
    """
    # Prefer explicit keyword: user=<mapping>
    if user_arg in kwargs and isinstance(kwargs[user_arg], Mapping):
        return cast(Mapping[str, Any], kwargs[user_arg])
    # Fallback: first positional is a mapping (common in simple call patterns)
    if args and isinstance(args[0], Mapping):
        return cast(Mapping[str, Any], args[0])
    # Fail fast with a clear message
    raise ValueError("User mapping is required as first arg or 'user' kwarg.")


def access_level(
    required_level: str,
    *,
    user_arg: str = "user",
    level_key: str = "secure_level",
) -> Callable[[F], F]:
    """
    Decorator factory that creates an access-control decorator.

    Usage:
        @access_level("admin")
        def get_admin_data(user: dict[str, Any]) -> str:
            return "secret"

    Explanation of parts:
    ---------------------
    - required_level: the role/string we want to enforce (e.g., 'admin', 'guest').
      This is the only positional parameter for readability.
    - * : marker that forces all parameters after it to be keyword-only.
    - user_arg: the name of the parameter that should hold the user mapping.
      Default is "user".
    - level_key: the key inside the user mapping that stores the access level.
      Default is "secure_level".
    - Returns: a decorator that wraps the original function.

    Inside:
    -------
    1. The outer function `access_level` is a *decorator factory*:
       it captures the required_level and returns the actual decorator.
    2. `decorator(func)` is the real decorator. It receives the function to be protected.
    3. `wrapper(*args, **kwargs)` is what runs instead of the original function.
       - It resolves the `user` mapping from the call arguments.
       - Checks that `user[level_key] == required_level`.
       - If not, raises PermissionError.
       - If yes, calls the original function with the same args/kwargs.
    4. `functools.wraps(func)` preserves the original function’s metadata
       (name, docstring, annotations).
    5. `cast(F, wrapper)` tells the type checker:
       “treat wrapper as having the same type signature as func”,
       because mypy cannot infer it automatically.
    6. Complexity: O(1) — constant-time overhead to look up the user and compare levels.
    """

    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            user = _resolve_user(args, kwargs, user_arg)
            level = user.get(level_key)
            if level != required_level:
                raise PermissionError("Access denied")
            return func(*args, **kwargs)

        return cast(F, wrapper)

    return decorator


@access_level("admin")
def get_admin_password(user: Mapping[str, Any]) -> int:
    """
    Returns the admin user's password.

    :param user: Mapping with at least 'secure_level' and 'password'.
    :return: Password as integer.
    """
    return int(user["password"])


@access_level("guest")
def get_user_password(user: Mapping[str, Any]) -> int:
    """
    Returns the guest user's password.

    :param user: Mapping with at least 'secure_level' and 'password'.
    :return: Password as integer.
    """
    return int(user["password"])
