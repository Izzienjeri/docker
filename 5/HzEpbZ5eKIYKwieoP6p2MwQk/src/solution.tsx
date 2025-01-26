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