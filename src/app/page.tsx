"use client";

import {
  withAuthenticator,
  ThemeProvider,
  Authenticator,
} from "@aws-amplify/ui-react";
import { Amplify } from "aws-amplify";
import "@aws-amplify/ui-react/styles.css";
import type { WithAuthenticatorProps } from "@aws-amplify/ui-react";
import config from "@/amplifyconfiguration.json";

Amplify.configure(config);

function App({ Component, pageProps, signOut, user }: WithAuthenticatorProps) {
  return (
    <>
      <h1>Hello {user?.username}</h1>
      <button onClick={signOut}>Sign out</button>
      <Component {...pageProps} />
    </>
  );
}

export default withAuthenticator(App);
