from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime


@dataclass
class LogType:
    """
    :ivar created_by: The username of the user who created the record.
        This information is only available in an XML response.
    :ivar created_by_account_id: The id of the user who created the
        record.  This information is only available in an XML response.
    :ivar created_date: The date and time stamp the record was created
        (in EST).  This information is only available in an XML
        response.
    :ivar last_updated_by: The username of the user who performed the
        last update.   This information is only available in an XML
        response.
    :ivar last_updated_by_account_id: The id of the user who performed
        the last update.   This information is only available in an XML
        response.
    :ivar last_updated_date: The date and time stamp of the last update
        (in EST).   This information is only available in an XML
        response.
    """

    class Meta:
        name = "logType"

    created_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "createdBy",
            "type": "Element",
            "namespace": "",
        },
    )
    created_by_account_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "createdByAccountId",
            "type": "Element",
            "namespace": "",
        },
    )
    created_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "createdDate",
            "type": "Element",
            "namespace": "",
        },
    )
    last_updated_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastUpdatedBy",
            "type": "Element",
            "namespace": "",
        },
    )
    last_updated_by_account_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "lastUpdatedByAccountId",
            "type": "Element",
            "namespace": "",
        },
    )
    last_updated_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastUpdatedDate",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Log(LogType):
    class Meta:
        name = "log"
