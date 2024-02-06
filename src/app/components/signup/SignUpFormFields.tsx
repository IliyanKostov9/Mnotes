import { MaskData } from "@/class/MaskData";
import { Label, TextField, VisuallyHidden } from "@aws-amplify/ui-react";
import { StorageManager } from "@aws-amplify/ui-react-storage";
import { useMemo, useState } from "react";

const defaultImageName = "2d0d83a3a03ac97d9c609527842693c1ae0b480d.jpg";

export const SignUpFormFields = () => {
  const [formState, setFormState] = useState({
    name: "",
    birthdate: "",
    email: "",
    password: "",
    confirmPassword: "",
    imageName: defaultImageName,
  });

  const handleInputChange =
    (name: string) => (e: { target: { value: any } }) => {
      setFormState((prevState) => ({
        ...prevState,
        [name]: e.target.value,
      }));
    };

  const validateEmail = useMemo(() => {
    const re = /\S+@\S+\.\S+/;
    return () => !re.test(formState.email);
  }, [formState.email]);

  const validatePassword = useMemo(() => {
    const passwordRegex =
      /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    return () => !passwordRegex.test(formState.password);
  }, [formState.password]);

  return (
    <>
      <VisuallyHidden>
        <TextField
          name="picture"
          value={formState.imageName}
          readOnly
          label="Picture"
        />
      </VisuallyHidden>

      <TextField
        name="name"
        label="Name"
        required
        value={formState.name}
        errorMessage="Please enter your name."
        onChange={handleInputChange("name")}
      />
      <TextField
        name="birthdate"
        label="Birthdate"
        type="date"
        required
        value={formState.birthdate}
        errorMessage="Please enter your birthdate."
        onChange={handleInputChange("birthdate")}
      />

      <TextField
        name="email"
        label="Email"
        required
        value={formState.email}
        hasError={validateEmail()}
        errorMessage="Please enter a valid email."
        onChange={handleInputChange("email")}
      />

      <TextField
        type="password"
        name="password"
        label="Password"
        required
        value={formState.password}
        hasError={validatePassword()}
        errorMessage="Password must contain at least 8 characters, one uppercase letter, one lowercase letter, one number and one special character."
        onChange={handleInputChange("password")}
      />

      <TextField
        type="password"
        name="confirmPassword"
        label="Confirm Password"
        required
        hasError={formState.password !== formState.confirmPassword}
        value={formState.confirmPassword}
        errorMessage="Passwords do not match."
        onChange={handleInputChange("confirmPassword")}
      />

      <Label>Upload a picture</Label>
      <StorageManager
        acceptedFileTypes={["image/*"]}
        accessLevel="guest"
        maxFileCount={1}
        isResumable={true}
        autoUpload={true}
        processFile={(file) => MaskData.hashImageFile(file)}
        onUploadSuccess={(file) => {
          setFormState((prevState) => ({
            ...prevState,
            imageName: file.key,
          }));
        }}
        onFileRemove={(file) => {
          setFormState((prevState) => ({
            ...prevState,
            imageName: defaultImageName,
          }));
        }}
      />
    </>
  );
};
