from pathlib import Path

from mcp.server.fastmcp import FastMCP

from schemas.file_types import (
    CategoryType,
    FileMetadata,
    FileWithMetadata,
)

# Initialize FastMCP server
mcp = FastMCP("diagram-syntax-server")

# Constants
DOCUMENTS_PATH = Path(__file__).parent / "documents"
DRAWIO_PATH = DOCUMENTS_PATH / "drawio"
MERMAID_PATH = DOCUMENTS_PATH / "mermaid"


def parse_frontmatter(content: str) -> tuple[FileMetadata, str]:
    """Parse frontmatter from markdown content."""
    if not content.startswith("---"):
        return FileMetadata(), content

    try:
        parts: list[str] = content.split("---", 2)
        if len(parts) < 3:
            return FileMetadata(), content

        frontmatter_text: str = parts[1].strip()
        body: str = parts[2].strip()

        # Parse YAML-like frontmatter
        metadata_dict: dict[str, str] = {}
        lines: list[str] = frontmatter_text.split("\n")
        for line in lines:
            if ":" in line:
                key: str
                value: str
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                metadata_dict[key] = value

        # Filter valid attributes for FileMetadata
        valid_attrs: dict[str, str] = {
            k: v for k, v in metadata_dict.items() if hasattr(FileMetadata, k)
        }
        return FileMetadata(**valid_attrs), body
    except Exception:
        return FileMetadata(), content


def get_files_with_metadata() -> list[FileWithMetadata]:
    """Get list of all files with their metadata."""
    files: list[FileWithMetadata] = []
    category_paths: list[Path] = [DRAWIO_PATH, MERMAID_PATH]

    for category_path in category_paths:
        if not category_path.exists():
            continue

        category: str = category_path.name
        file_paths: list[Path] = list(category_path.glob("*.md"))

        for file_path in file_paths:
            try:
                content: str = file_path.read_text(encoding="utf-8")
                metadata, _ = parse_frontmatter(content)

                file_with_metadata: FileWithMetadata = FileWithMetadata(
                    filename=file_path.name,
                    category=category,
                    path=str(file_path.relative_to(DOCUMENTS_PATH)),
                    metadata=metadata,
                )
                files.append(file_with_metadata)
            except Exception as e:
                error_file: FileWithMetadata = FileWithMetadata(
                    filename=file_path.name,
                    category=category,
                    path=str(file_path.relative_to(DOCUMENTS_PATH)),
                    metadata=FileMetadata(),
                    error=str(e),
                )
                files.append(error_file)

    sorted_files: list[FileWithMetadata] = sorted(
        files, key=lambda x: (x.category, x.filename)
    )
    return sorted_files


@mcp.tool()
def get_file_content(file_paths: str) -> str:
    """Get the content of one or more diagram syntax files.

    Args:
        file_paths: Comma-separated list of file paths (e.g., "mermaid/flowchart.md,drawio/examples_Flowchart.md")

    Returns the raw file content.
    """
    # Parse the input - handle both single files and comma-separated lists
    paths: list[str] = [path.strip() for path in file_paths.split(",") if path.strip()]

    if not paths:
        return "No file paths provided. Please specify one or more file paths separated by commas."

    output: list[str] = []

    for file_path in paths:
        try:
            full_path: Path = DOCUMENTS_PATH / file_path
            if not full_path.exists():
                output.append(f"Error: File not found - {file_path}")
                continue

            content: str = full_path.read_text(encoding="utf-8")

            if len(paths) > 1:
                output.append(f"\n{'='*60}")
                output.append(f"FILE: {file_path}")
                output.append(f"{'='*60}")

            output.append(content)

        except Exception as e:
            output.append(f"Error reading {file_path}: {str(e)}")

    return "\n".join(output)


@mcp.tool()
def list_files_by_category(category: CategoryType | None = None) -> str:
    """List diagram syntax files filtered by category.

    Args:
        category: Category to filter by ("drawio" or "mermaid"). If None, lists all categories available.

    Returns filtered list of files or available categories.
    """
    files: list[FileWithMetadata] = get_files_with_metadata()

    if not files:
        return "No files found in the documents directory."

    # If no category specified, list available categories
    if category is None:
        categories = sorted(set(file_info.category for file_info in files))
        result = ["Available categories:"]
        for cat in categories:
            count = sum(1 for f in files if f.category == cat)
            result.append(f"  - {cat} ({count} files)")
        return "\n".join(result)

    # Filter by category
    filtered_files = [f for f in files if f.category == category]

    if not filtered_files:
        return f"No files found for category '{category}'."

    result_by_category: list[str] = [f"Files in category '{category}':\n"]

    for file_info in filtered_files:
        result_by_category.append(f"{file_info.filename}")
        result_by_category.append(f"   Path: {file_info.path}")

        if file_info.error:
            result_by_category.append(f"   Error: {file_info.error}")
        else:
            metadata: FileMetadata = file_info.metadata
            if metadata.title:
                result_by_category.append(f"   Title: {metadata.title}")
            if metadata.description:
                result_by_category.append(f"   Description: {metadata.description}")
            if metadata.type:
                result_by_category.append(f"   Type: {metadata.type}")
            if metadata.tags:
                result_by_category.append(f"   Tags: {metadata.tags}")
        result_by_category.append("")  # Add blank line between files

    return "\n".join(result)


@mcp.tool()
def search_files_by_tag(tag: str) -> str:
    """Search diagram syntax files by tag.

    Args:
        tag: Tag to search for (e.g., "flowchart", "sequence", "business")

    Returns files that contain the specified tag.
    """
    files: list[FileWithMetadata] = get_files_with_metadata()

    if not files:
        return "No files found in the documents directory."

    # Filter by tag
    filtered_files = []
    for file_info in files:
        if file_info.error:
            continue
        if file_info.metadata.tags and tag.lower() in file_info.metadata.tags.lower():
            filtered_files.append(file_info)

    if not filtered_files:
        return f"No files found with tag '{tag}'."

    result: list[str] = [f"Files with tag '{tag}':\n"]
    current_category: str | None = None

    for file_info in sorted(filtered_files, key=lambda x: (x.category, x.filename)):
        if current_category != file_info.category:
            current_category = file_info.category
            result.append(f"{current_category.upper()}:")

        result.append(f"  {file_info.filename}")
        result.append(f"     Path: {file_info.path}")

        metadata: FileMetadata = file_info.metadata
        if metadata.title:
            result.append(f"     Title: {metadata.title}")
        if metadata.description:
            result.append(f"     Description: {metadata.description}")
        result.append("")

    return "\n".join(result)


if __name__ == "__main__":
    mcp.run(transport="stdio")
