import re

def extract_solution(llm_response: str) -> list:
    """
    Extracts code blocks from a string, replaces '\n' with '\\n' in string literals,
    excluding docstrings and comments, and returns a list of (file_name, code) tuples.

    Args:
        llm_response: The string containing code blocks.

    Returns:
        A list of tuples, where each tuple contains a file name ("solution.py", "solution1.py", etc.) and the
        extracted code with '\n' replaced by '\\n' in string literals. Returns an empty list if no code block is found.
    """
    
    code_blocks = re.findall(r"```python\n(.*?)\n```", llm_response, re.DOTALL)
    
    if not code_blocks:
        return []
    
    solutions = []
    for i, extracted_code in enumerate(code_blocks):
        
        def replace_newline(match):
            s = match.group(0)
            # Check if it's a triple-quoted string (docstring)
            if s.startswith('"""') or s.startswith("'''"):
                return s  # Don't modify docstrings
            # Check if it's a comment
            elif s.startswith('#'):
                return s  # Don't modify comments
            else:
                return s.replace('\n', '\\n')

        # Regex to match single-quoted strings, double-quoted strings, triple-quoted strings, and comments.
        extracted_code = re.sub(r'(""".*?""")|(\'\'\'.*?\'\'\')|(".*?")|(\'.*?\')|(#[^\n]*)', replace_newline, extracted_code, flags=re.DOTALL)
        
        if i == 0:
            file_name = "solution.py"
        else:
            file_name = f"solution{i}.py"  # solution1.py, solution2.py, etc.
            
        solutions.append((file_name, extracted_code))
    
    return solutions