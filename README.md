# Getting started

## Prerequisites

- AWS CLI
- Amplify CLI
- git
- NodeJS
- Python

## Setup your environment

Clone the repo

```bash
git clone git@github.com:IliyanKostov9/Mnotes.git
```

Go to the project root directory and install the neccessary dependencies

```bash
npm install
```

Pull the amplify repo by using:

```bash
amplify pull --appId <AppID> --envName prod
```

Run the development server to check if everything is running fine:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Create a virtual environment in each of the lambda functions:

```bash
cd amplify/backend/function/MNotesAuthRegisterUserLambda
pipenv install
```

Connect the MNotesAuthRegisterUserLambda lambda to your AWS Cognito User pool properties as a Pre sign-up trigger Lambda trigger (currently only done manually via the web UI)
