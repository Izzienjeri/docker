import React from "react";
import { render } from "@testing-library/react";
import "@testing-library/jest-dom";
import PublicWrapper from "./src/solution";

// Define a mock Session type for testing
export interface Session {
  user?: {
    name?: string;
    email?: string;
  };
  [key: string]: any;
}

describe("PublicWrapper", () => {
  it("correctly clones and passes props to a ReactElement child", () => {
    const session: Session = { user: { name: "John Doe" } };

    const { getByText } = render(
      <PublicWrapper session={session}>
        <div>Hello</div>
      </PublicWrapper>
    );

    const element = getByText("Hello");
    expect(element).toHaveAttribute("data-session");
  });

  it("handles nested ReactElement children", () => {
    const session: Session = { user: { name: "John Doe" } };

    const { getByText } = render(
      <PublicWrapper session={session}>
        <div>
          <span>Nested Child</span>
        </div>
      </PublicWrapper>
    );

    expect(getByText("Nested Child")).toBeInTheDocument();
  });

  it("handles fragments as children", () => {
    const session: Session = { user: { name: "John Doe" } };

    const { getByText } = render(
      <PublicWrapper session={session}>
        <>
          <div>Fragment Child 1</div>
          <div>Fragment Child 2</div>
        </>
      </PublicWrapper>
    );

    expect(getByText("Fragment Child 1")).toBeInTheDocument();
    expect(getByText("Fragment Child 2")).toBeInTheDocument();
  });
});