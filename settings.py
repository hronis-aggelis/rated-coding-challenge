# settings.py

import os
import typing


def load_variable(
    name: str,
    default: typing.Any = None,
    is_int: bool = False,
    is_float: bool = False,
    is_list: bool = False,
) -> typing.Any:
    variable = os.environ.get(name, default)

    if is_int:
        return int(variable)
    elif is_float:
        return float(variable)
    elif is_list:
        return [variable]
    return variable

# Database
RDS_DB_USER = load_variable(
    name="RDS_DB_USER",
    default="root"
)
RDS_DB_PASSWORD = load_variable(
    name="RDS_DB_PASSWORD",
    default="password"
)
RDS_DB_HOST = load_variable(
    name="RDS_DB_HOST",
    default="0.0.0.0"
)

DATABASE_URL = f"mysql://{RDS_DB_USER}:{RDS_DB_PASSWORD}@{RDS_DB_HOST}/rated"