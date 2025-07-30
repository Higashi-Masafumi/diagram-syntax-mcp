"""Type definitions for file operations."""

from dataclasses import dataclass
from enum import Enum
from typing import Literal


class CategoryEnum(str, Enum):
    """Available diagram categories."""
    DRAWIO = "drawio"
    MERMAID = "mermaid"


# Type alias for category parameter
CategoryType = Literal["drawio", "mermaid"]


@dataclass
class FileInfo:
    """Basic file information."""
    filename: str
    category: str
    path: str


@dataclass
class FileMetadata:
    """File metadata from frontmatter."""
    title: str | None = None
    description: str | None = None
    type: str | None = None
    category: str | None = None
    tags: str | None = None
    status: str | None = None
    version: str | None = None
    created: str | None = None
    updated: str | None = None
    author: str | None = None


@dataclass
class FileWithMetadata:
    """File information with metadata."""
    filename: str
    category: str
    path: str
    metadata: FileMetadata
    error: str | None = None


@dataclass
class FileContent:
    """File content with metadata."""
    path: str
    metadata: FileMetadata
    content: str
    full_content: str
    error: str | None = None