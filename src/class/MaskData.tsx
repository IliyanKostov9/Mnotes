import { StorageManagerProps } from "@aws-amplify/ui-react-storage";

export class MaskData {
  private static generateRandomHex(length: number = 8): string {
    const randomBytes = new Uint8Array(length / 2);
    window.crypto.getRandomValues(randomBytes);

    return Array.from(randomBytes)
      .map((byte) => byte.toString(16).padStart(2, "0"))
      .join("");
  }

  public static hashImageFile({ file }): any {
    const fileExtension = file.name.split(".").pop();

    return file
      .arrayBuffer()
      .then((filebuffer) => window.crypto.subtle.digest("SHA-1", filebuffer))
      .then((hashBuffer) => {
        const hashArray = Array.from(new Uint8Array(hashBuffer));
        const hashHex = hashArray
          .map((a) => a.toString(16).padStart(2, "0"))
          .join("");

        const randomHex = this.generateRandomHex(8);
        const hashHexImage: string = `${hashHex}${randomHex}.${fileExtension}`;

        return { file, key: hashHexImage };
      });
  }
}
