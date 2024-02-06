"use client";

import config from "@/amplifyconfiguration.json";
import { Authenticator } from "@aws-amplify/ui-react";
import "@aws-amplify/ui-react/styles.css";
import { Amplify } from "aws-amplify";
import { SignUpFormFields } from "../components/signup/SignUpFormFields";

Amplify.configure(config, { ssr: false });

export default function App() {
  return (
    <Authenticator
      initialState="signUp"
      components={{
        SignUp: {
          FormFields: () => <SignUpFormFields />,
        },
      }}
    />
  );
}
