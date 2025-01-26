import React from "react";
import { createRoot } from "react-dom/client";
import PublicWrapper from "./solution";

export interface Session {
  user?: {
    id?: string;
    name?: string;
    email?: string;
  };
  accessToken?: string;
}

// Explicit return type fixes ReactNode vs ReactElement issues
export const ChildComponent: React.FC<{ session: Session }> = ({ session }) => {
  return (
    <div className="wrapper">
      <h1>Welcome, {session.user?.name || "Guest"}!</h1>
      <p className="user-info">Email: {session.user?.email || "Not provided"}</p>
      <p className="user-info">Access Token: {session.accessToken || "None"}</p>
    </div>
  );
};


const session: Session = {
  user: { id: "123", name: "John Doe", email: "john.doe@example.com" },
  accessToken: "abc123",
};

const root = createRoot(document.getElementById("root")!);
root.render(
  <PublicWrapper session={session}>
    <ChildComponent session={session} />
  </PublicWrapper>
);
