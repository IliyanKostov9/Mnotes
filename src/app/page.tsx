"use client";

import config from "@/amplifyconfiguration.json";
import type { WithAuthenticatorProps } from "@aws-amplify/ui-react";
import {
  Authenticator,
  TextField,
  withAuthenticator,
} from "@aws-amplify/ui-react";
import "@aws-amplify/ui-react/styles.css";
import { Amplify } from "aws-amplify";
import { StorageManager } from "@aws-amplify/ui-react-storage";

Amplify.configure(config);

const signUpFields = {
  signUp: {
    profile: {
      placeholder: "Enter your name",
      isRequired: true,
      label: "Name",
      order: 4,
    },
  },
};

export default function App({}) {
  return (
    <Authenticator
      initialState="SignUp"
      formFields={signUpFields}
      components={{
        SignUp: {
          FormFields() {
            return (
              <>
                <StorageManager
                  label="Picture"
                  name="picture"
                  accessLevel="guest"
                  maxFileCount={1}
                  isResumable
                />
                <Authenticator.SignUp.FormFields />
              </>
            );
          },
        },
      }}
    ></Authenticator>
  );
}
