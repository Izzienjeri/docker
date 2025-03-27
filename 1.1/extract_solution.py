import re


def extract_code_blocks(
        markdown_text,
        language='python',
    ):
    """Extracts code blocks from strings. Do NOT modify this function."""
    code_block_pattern = re.compile(rf'```{language}(.*?)```', re.DOTALL)

    # Find all matches
    code_blocks = code_block_pattern.findall(markdown_text)

    # Clean up the extracted code blocks by stripping leading/trailing whitespace
    cleaned_code_blocks = [block.strip() for block in code_blocks]

    return cleaned_code_blocks


def preprocess_markers(llm_response: str, target_marker="python") -> str:
    """Standardizes code block markers in the LLM response to a single target marker."""
    llm_response = llm_response.replace("```python", f"```{target_marker}")
    return llm_response


def extract_solution(llm_response: str) -> list[tuple[str, str]]:
    """Extracts a list of file paths and code file contents from any LLM's response.

    Args:
        llm_response: Any LLM's response to your concretized prompt.

    Returns:
        A list of tuple (file_path, file_content) with the file path relative to the
        current working directory and its content.
    """

    # Preprocess the response to unify markers
    llm_response = preprocess_markers(llm_response, target_marker="python")

    # Example implementation that extracts the first code block and save it to solution.py.
    code_solution = extract_code_blocks(llm_response)[0]

    # Add export statement to the code block.
    if 'module.exports = transformScript;' not in code_solution:
        code_solution += '\n\nmodule.exports = transformScript;'

    return [('solution.py', code_solution)]