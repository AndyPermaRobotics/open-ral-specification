#!/usr/bin/env python3
"""
Script to combine predefined files into a single Markdown document.
JSON files are wrapped in code blocks with filename headers.
"""

from pathlib import Path
from typing import List


def read_file_content(file_path: Path) -> str:
    """
    Read and return the content of a file.

    Args:
        file_path: Path to the file to read

    Returns:
        Content of the file as string

    Raises:
        FileNotFoundError: If the file does not exist
        IOError: If there's an error reading the file
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading file {file_path}: {e}")


def format_file_content(filename: str, content: str) -> str:
    """
    Format file content based on file extension.
    JSON files are wrapped in code blocks with filename headers.

    Args:
        filename: Name of the file
        content: Content of the file

    Returns:
        Formatted content string
    """
    if filename.endswith(".json"):
        return f"{filename}:\n```json\n{content}\n```"

    if filename.endswith(".yml") or filename.endswith(".yaml"):
        return f"{filename}:\n```yml\n{content}\n```"

    else:
        return content


def combine_files(file_list: List[str], output_filename: str, base_path: Path) -> None:
    """
    Combine multiple files into a single Markdown document.

    Args:
        file_list: List of filenames to combine (in order)
        output_filename: Name of the output file
        base_path: Base directory path where files are located

    Raises:
        FileNotFoundError: If any input file does not exist
        IOError: If there's an error reading or writing files
    """
    combined_content = []

    for filename in file_list:
        file_path = base_path / filename
        print(f"Reading {filename}...")

        content = read_file_content(file_path)
        formatted_content = format_file_content(filename, content)
        combined_content.append(formatted_content)

    # Join all content with double blank lines between files
    output_content = "\n\n\n".join(combined_content)

    # Write to output file
    output_path = base_path / output_filename
    print(f"Writing combined content to {output_filename}...")

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(output_content)
        print(f"Successfully created {output_filename}")
    except IOError as e:
        raise IOError(f"Error writing to {output_path}: {e}")


def main() -> None:
    """
    Main entry point for the script.
    Combines predefined files into a single Markdown document.
    """
    # Hardcoded list of files to combine (in order)
    files_to_combine = [
        "open_ral.md",
        "open_ral.schema.json",
        "openapi_semantic.yml",
        "openapi.yml",
    ]

    output_file = "open_ral_overview.md"

    # Get the script's directory as base path
    base_path = Path(__file__).parent

    try:
        combine_files(files_to_combine, output_file, base_path)
    except (FileNotFoundError, IOError) as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":
    main()
