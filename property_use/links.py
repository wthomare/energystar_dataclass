from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class LinkType:
    """
    :ivar id: Indicates the unique Portfolio Manager identifier used to
        define this entity.
    :ivar link_description: The description of the link.
    :ivar link: The URL to a web service call for subsequent processing.
    :ivar http_method: The HTTP method to the web service call.
    :ivar hint: A brief description of the information returned from the
        link.
    """

    class Meta:
        name = "linkType"

    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    link_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "linkDescription",
            "type": "Attribute",
        },
    )
    link: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    http_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "httpMethod",
            "type": "Attribute",
        },
    )
    hint: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class LinksType:
    class Meta:
        name = "linksType"

    link: List[LinkType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
