import re

def extract_code_blocks(markdown_text, language="python"):
    """Extracts code blocks from strings. Do NOT modify this function."""
    code_block_pattern = re.compile(rf"``{language}(.*?)``", re.DOTALL)

    # Find all matches
    code_blocks = code_block_pattern.findall(markdown_text)

    # Clean up the extracted code blocks by stripping
    # leading/trailing whitespace
    cleaned_code_blocks = [block.strip() for block in code_blocks]

    return cleaned_code_blocks


def extract_solution(llm_response: str) -> list[tuple[str, str]]:
    """Extract a list of file paths and code file contents.

    1. Attempts to extract code from Markdown-fenced blocks using extract_code_blocks.
    2. If no code is found, tries a fallback regex that captures code
       from 'from transformers' up to 'return encodings'.

    Args:
        llm_response: Any LLM's response to your concretized prompt.

    Returns:
        A list of tuple (file_path, code_content).
    """
    # First attempt: Use the function that extracts from fenced blocks
    code_solutions = extract_code_blocks(llm_response, language="python")

    if code_solutions:
        # We found code via the Markdown fences
        return [("solution.py", code) for code in code_solutions]

    # A regex capturing the snippet from "from transformers" up to the closing line "return encodings".
    fallback_pattern = re.compile(r"(from transformers.*?return encodings(?:\)|\n))", re.DOTALL)
    match = fallback_pattern.search(llm_response)
    if match:
        code_solutions = [match.group(1)]
        return [("solution.py", code) for code in code_solutions]

    return []