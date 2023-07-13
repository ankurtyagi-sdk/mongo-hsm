#
# Copyright (c) 2023 by Delphix. All rights reserved.
#

from typing import Optional

from pydantic import BaseModel
from pydantic import Field
from pydantic import constr


class ConnectorResponse(BaseModel):
    id: Optional[int] = Field(
        None, description="The Connector object entity ID."
    )  # noqa
    user: constr(min_length=1, max_length=256) = Field(
        ..., description="The username of this connector."
    )
    jdbc_url: str = Field(..., description="The jdbc url of this connector.")
    ssl: Optional[bool] = Field(
        False, description="Is the authentication based on SSL."
    )
    certificate_key_file: Optional[str] = Field(
        "", description="Certificate key file path."
    )
    tls_ca_file: Optional[str] = Field("", description="TLS CA file path.")


class ConnectorValidator(ConnectorResponse):
    password: constr(min_length=1, max_length=256) = Field(
        ..., description="The password of this connector."
    )
