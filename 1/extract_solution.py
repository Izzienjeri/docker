import re

claude_bad_block = '''const formik = useFormik({
  initialValues: {
    ipd_enrollment_id: id,
    price_per_item: 0,
    quantity: 1,
    ipd_bill_category_id: "",
    ipd_bill_item_id: "",
    amount: 0
  },
  validationSchema: validationSchema,
  validate: (values) => {
    const errors = {};
    Object.keys(values).forEach((key) => {
      if (typeof values[key] === 'string') {
        values[key] = values[key].trim();
      }
    });
    return errors;
  },
  onSubmit: async (values, formikHelpers) => {
    await handleFormSubmit(values, formikHelpers);
  },
});
'''



def extract_code_blocks(
        markdown_text,
        language='python',
):
    """Extracts code blocks from strings. Do NOT modify this function."""
    code_block_pattern = re.compile(rf'``{language}(.*?)``', re.DOTALL)

    # Find all matches
    code_blocks = code_block_pattern.findall(markdown_text)

    # Clean up the extracted code blocks by stripping leading/trailing whitespace
    cleaned_code_blocks = [block.strip() for block in code_blocks]

    return cleaned_code_blocks


def extract_solution(llm_response: str) -> list[tuple[str, str]]:
    """Extracts a list of file paths and code file contents from any LLM's response.

  Args:
    llm_response: Any LLM's response to your concretized prompt.

  Returns:
    A list of tuple (file_path, file_content) with the file path relative to the current working directory and its content."""

    code_solutions = extract_code_blocks(llm_response, language="javascript")

    result = code_solutions[0]

    result = result.replace(claude_bad_block, "")

    imports = '''const id = 123; // Mocked ID
const headers = { Authorization: "Bearer token" }; // Mocked headers
import { toast } from "react-toastify";
import axios from "axios";
export '''
    final = imports + result
    return [('solution.mjs', final)]
