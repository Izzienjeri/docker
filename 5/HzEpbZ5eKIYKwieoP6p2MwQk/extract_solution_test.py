import os
from extract_solution import extract_solution

llm_response = """```typescript
import React, { ReactNode, ReactElement, isValidElement } from "react";
import { Session } from "./index"; 

interface WithSession {
  session: Session;
  "data-session": string;
}

export default function PublicWrapper({
  children,
  session,
}: {
  children: ReactNode;
  session: Session;
}) {
  if (!children) {
    throw new Error("Invalid children: children must be a valid React element.");
  }

  const processChild = (child: ReactNode): ReactNode => {
    if (!React.isValidElement(child)) {
      return null;
    }

    if (child.type === React.Fragment) {
      const element = child as ReactElement<{ children?: ReactNode }>;
      return React.Children.map(element.props.children, processChild);
    }

    return React.cloneElement<WithSession>(
      child as ReactElement<WithSession>,
      {
        session,
        "data-session": JSON.stringify(session)
      }
    );
  };

  const processedChildren = React.Children.map(children, processChild);

  const firstChild = processedChildren?.[0]
  if (processedChildren?.length === 1 && isValidElement(firstChild)) {
      return firstChild;
  }

  return React.createElement(React.Fragment, null, processedChildren);
}
```
"""

try:
    response = extract_solution(llm_response=llm_response)

    if not isinstance(response, list):
        raise ValueError("Expected response to be a list of (file_name, code) tuples.")

    for item in response:

        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("Invalid tuple.")

        file_name, code = item

        # Check if the file itself exists
        if not os.path.isfile(file_name):
            raise FileNotFoundError(
                f"The file '{file_name}' does not exist. Please check the path."
            )

        # Proceed to write only if the file already exists
        with open(file_name, "w") as file:
            file.write(code)

        print(f"File '{file_name}' written successfully.")

except FileNotFoundError as fnf_error:
    print(f"File error: {fnf_error}")

except Exception as e:
    print(f"An error occurred while running extract solution test: {e}")
