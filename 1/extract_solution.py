import re

def extract_code_blocks(
    markdown_text,
    language="c",
):
    """Extracts code blocks from strings. Do NOT modify this function."""
    code_block_pattern = re.compile(rf'```{language}(.*?)```', re.DOTALL)
    # Find all matches
    code_blocks = code_block_pattern.findall(markdown_text)

    # Clean up the extracted code blocks by stripping leading/trailing whitespace
    cleaned_code_blocks = [block.strip() for block in code_blocks]

    return cleaned_code_blocks


def remove_main_function(code):
    """Removes the entire main function, including its content."""
    lines = code.splitlines()
    result = []
    inside_main = False
    brace_count = 0

    for line in lines:
        # Detect the start of the main function
        if not inside_main and re.match(r"\s*int\s+main\s*\(", line):
            inside_main = True
            brace_count = line.count("{") - line.count("}")
            continue

        # If inside the main function, track braces and skip lines
        if inside_main:
            brace_count += line.count("{") - line.count("}")
            if brace_count <= 0:
                inside_main = False  # End of the main function
            continue

        # If not inside the main function, keep the line
        result.append(line)

    return "\n".join(result)


def extract_solution(llm_response: str) -> list[tuple[str, str]]:
    """Extracts all code blocks and combines them into a single file.

    Args:
        llm_response: Any LLM's response to your concretized prompt.

    Returns:
        A list containing a single tuple (file_path, combined_file_content).
    """
    # Preprocess the response to unify markers
    for candidate_marker in ["```c/c++", "```cpp", "```c++"]:
      llm_response = llm_response.replace(candidate_marker, "```c")

    code_blocks = extract_code_blocks(llm_response)

    result = []
    solution_path = 'solution.cpp'

    for code_block in code_blocks:
      if 'main' in code_block:
        code_block = remove_main_function(code_block)
      result.append((solution_path, code_block))

    return result

