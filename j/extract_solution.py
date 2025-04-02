import re

from typing import Optional
from pathlib import Path


def extract_code_blocks(markdown_text):
    """Extracts code blocks from strings. Do NOT modify this function."""    
    code_block_pattern = re.compile(r'```([^\n`]+)\n(.*?)```', re.DOTALL) # Changed for Universal Script

    code_blocks = code_block_pattern.findall(markdown_text)

    # Clean up the extracted code blocks by stripping leading/trailing whitespace
    cleaned_code_blocks = [(lang.strip(), code.strip()) for lang, code in code_blocks] # Changed for consistency

    return cleaned_code_blocks


def extract_solution(llm_response: str) -> list[tuple[str, str]]:
    """Extracts code blocks from the response and returns them as solution files."""
    valid_languages = {
        'js', 'jsx', 'ts', 'tsx',
        'javascript', 'typescript', 'javascript/typescript',
        'html','css',
        'python', 'json', 'java',
        'csharp', 'c#', 
        'c++', 'cpp', 'c','c/c++'
    }
    
    code_blocks = extract_code_blocks(llm_response)
    
    solutions = []
    
    for index, (language, code) in enumerate(code_blocks):
        if language.lower() not in valid_languages:
            continue
        
        file_extension = get_file_extension(language)

        if file_extension in ['js','ts']: 
            code = ensure_js_export_statement(code)
        elif file_extension == 'cpp':
            code = remove_cpp_main_function(code)
        elif file_extension == "java":
            code = add_package_name(code)

        file_path = ""   # Replace with your actual project structure (if any) 

        # file_name = f"{file_path}solution." + file_extension if index == 0 else f"{file_path}solution_{index}.{file_extension}"
        file_name = f"{file_path}solution_{index+1}.{file_extension}"

        solutions.append((file_name, code))
    
    return solutions


def get_file_extension(language: str) -> str:
    """Map a language string to the correct file extension."""
    lang = language.lower()
    if "javascript/typescript" in lang:
        lang = "javascript"

    if "c/c++" in lang:
        lang = "cpp" 
    
    if lang in ["typescript", "tsx", "ts"]:
        return "ts"
    elif lang in ["javascript", "jsx", "js"]:
        return "js"
    elif lang in ["python"]:
        return "py"
    elif lang in ["java"]:
        return "java"
    elif lang in ["csharp", "c#"]:
        return "cs"
    elif lang in ["c/c++","c++", "cpp"]:
        return "cpp"
    elif lang == "c":
        return "c"
    elif lang == "html":
        return "html"
    elif lang == "css":
        return "css"
    elif lang == "json":
        return "json"
    else:
        return "txt"  # Fallback
    
def ensure_js_export_statement(code: str) -> str:
    """
    Ensure JavaScript/TypeScript code contains an export statement.
    If none exists, extract the function signature name and append an export default statement.
    """

    # Only add export if none exists
    if 'export ' in code or 'module.exports' in code:
        return code

    # Try pattern for a standard function declaration: "function functionName(...)"
    match = re.search(r'^\s*function\s+(\w+)\s*\(', code, re.MULTILINE)
    if match:
        func_name = match.group(1)
    else:
        # Try pattern for an arrow function or function expression assigned to a variable:
        match = re.search(r'^\s*(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s*)?(?:\([^\)]*\)|\w+)\s*=>', code, re.MULTILINE)
        if match:
            func_name = match.group(1)
        else:
            # Fallback if no function name is detected
            func_name = "myModule"

    # return code + f'\n\n module.exports = {func_name};' #For CommonJS Based Tasks
    return code + f'\n\n export default {func_name};' #For ES Modules Based Tasks

def remove_cpp_main_function(code: str) -> str:
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
    
def is_test_file(file_path: Path) -> bool:
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        return False
    return "@Test" in content

def find_first_test_file_from_root(root="."):
    root_path = Path(root)
    for file in root_path.rglob("*.java"):
        if is_test_file(file):
            return file
    return None

def get_java_package_name(java_file_path: str) -> Optional[str]:
    try:
        with open(java_file_path, "r") as f:
            code = f.read()
            package_pattern = r"^\s*package\s+([a-zA-Z_][a-zA-Z0-9_]*(\.[a-zA-Z_][a-zA-Z0-9_]*)*)\s*;"
            match = re.search(package_pattern, code, re.MULTILINE)
            if match:
                return match.group(1)
            else:
                return None
    except FileNotFoundError:
        return None
    except Exception as e:
        return None

def add_package_name(code: str) -> str:
    test_file_path = find_first_test_file_from_root()
    if not test_file_path:
        return code
    test_package_name = get_java_package_name(test_file_path)
    if not test_package_name:
        return code
    package_pattern = r"^\s*package\s+([a-zA-Z_][a-zA-Z0-9_]*(\.[a-zA-Z_][a-zA-Z0-9_]*)*)\s*;"
    match = re.search(package_pattern, code, re.MULTILINE)
    if match:
        existing_package_name = match.group(1)
        if existing_package_name != test_package_name:
            code = re.sub(package_pattern, f"package {test_package_name};\n", code)
    else:
        code = f"package {test_package_name};\n\n" + code
    return code