#
# Copyright (c) 2023 by Delphix. All rights reserved.
#

from __future__ import annotations

from typing import Dict
from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import Field
from pydantic import constr


class DataInfoItem(BaseModel):
    source_key: Dict[str, str] = Field(
        ...,
        description="object providing the information like schema_name, "
        "table_name or file_name of the source datasource",
    )
    schema_name: constr(min_length=1) = Field(
        ..., description="schema name of the target datasource."
    )
    table_name: constr(min_length=1) = Field(
        ..., description="table name of the target datasource."
    )
    stream_size: Optional[int] = Field(
        256000,
        description="The stream size to be used by sqlldr oracle utility "
        "which specifies the size (in bytes) of the data stream "
        "sent from the client to the server.",
    )
    column_array_rows: Optional[int] = Field(
        20000,
        description="The number of column array rows to be used by sqlldr "
        "oracle utility which determines the number of rows "
        "loaded before the stream buffer is built",
    )


class DataSet(BaseModel):
    id: Optional[int] = None
    connector_id: int = Field(
        ..., description="ID of the registered Connector " "model."
    )
    mount_filesystem_id: int = Field(
        ..., description="ID of the registered Mount Filesystem model."
    )
    data_info: List[DataInfoItem] = Field(
        ...,
        description="Array of multiple objects, each object providing the "
        "information like sourceKey, schema_name, table_name "
        "and STREAMSIZE.",
        max_items=10000,
        min_items=1,
    )


class TargetConfigs(BaseModel):
    max_concurrent_target_connection: Optional[int] = Field(
        None,
        description="Maximum number of parallel connection that hyperscale "
        "can have with target datasource.",
    )
    parallelism_degree: Optional[int] = Field(
        None, description="Degree of parallelism for target database"
    )


class DataSetMapping(BaseModel):
    id: Optional[int] = None
    target_configs: Optional[TargetConfigs] = Field(
        None, description="configuration properties for source datasource"
    )
    data_set_id: int = Field(
        ..., description="ID of the registered Data " "Set model."
    )  # noqa
    job_id: int = Field(..., description="ID of the registered Job model.")


class FileInfoItem(BaseModel):
    file_path: constr(min_length=1) = Field(
        ..., description="relative path of the masked file."
    )
    file_metadata: Dict[str, str] = Field(
        ...,
        description="file metadata details like enclosure, delimiter and "
        "endOFRecord etc.",
    )


class LoadMetadatum(BaseModel):
    source_key: Dict[str, str] = Field(
        ...,
        description="object providing the information like schema_name, "
        "table_name or file_name of the source datasource",
    )
    file_info: List[FileInfoItem] = Field(
        ...,
        description="Array of multiple objects, each object providing the "
        "information like file path and file metadata.",
        max_items=10000,
        min_items=1,
    )
