#
# Copyright (c) 2023 by Delphix. All rights reserved.
#

from enum import Enum
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class Status(Enum):
    CREATED = "CREATED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"


class ExecutionStatus(BaseModel):
    status: Status = Field(..., description="The status of the load process.")
    error: Optional[str] = Field(None, description="Optional, error detail.")
