import os
from typing import Literal
import logging
import boto3
from botocore.exceptions import UnknownParameterError
from sendgrid.helpers.mail import Mail, Email, To, Content
from sendgrid import SendGridAPIClient, SendGridException
from infisical_client import ClientSettings, InfisicalClient, GetSecretOptions

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

SUBJECT_DEFAULT: Literal["Welcome to MNotes! :)"] = "Welcome to MNotes! :)"
CONTENT_DEFAULT: Literal[
    "Hey, welcome to my personal notes web app.\n I hope you like it!"
] = "Hey, welcome to my personal notes web app.\n I hope you like it!"


class SendGridManager:

    client: SendGridAPIClient
    from_email: Email
    content: Content
    mail: Mail

    def __init__(self):

        infisical_client_id, infisical_secret_client, project_id = (
            # pylint: disable=undefined-variable
            _get_ssm_infisical_secret_values()
        )

        infisical_client = InfisicalClient(
            ClientSettings(
                client_id=infisical_client_id,
                client_secret=infisical_secret_client,
            )
        )

        api_key = infisical_client.getSecret(
            options=GetSecretOptions(
                environment="prod",
                project_id=project_id,
                secret_name="SENDGRID_API_KEY",
            )
        )

        self.client = SendGridAPIClient(api_key=api_key.secret_value).client

    @staticmethod
    def _get_ssm_infisical_secret_values() -> tuple[str, str, str]:
        """
        Get SSM parameter store values for retrieving the secrets from Infisical

        Required environment variables:
        - INFISICAL_CLIENT_ID: /infisical/client_id (encrypted)
        - INFISICAL_CLIENT_SECRET: /infisical/client_secret (encrypted)
        - PROJECT_ID: /infisical/project_id (not encrypted)
        """

        try:
            client_ssm_param_store = boto3.client("ssm")

            parameter_decrypted_value = client_ssm_param_store.get_parameter(
                Name=os.environ.get("INFISICAL_CLIENT_ID"), WithDecryption=True
            )

            infisical_client_id = parameter_decrypted_value["Parameter"]["Value"]

            parameter_decrypted_value = client_ssm_param_store.get_parameter(
                Name=os.environ.get("INFISICAL_CLIENT_SECRET"), WithDecryption=True
            )

            infisical_secret_client = parameter_decrypted_value["Parameter"]["Value"]

            parameter_decrypted_value = client_ssm_param_store.get_parameter(
                Name=os.environ.get("PROJECT_ID"), WithDecryption=False
            )

            project_id = parameter_decrypted_value["Parameter"]["Value"]

            return infisical_client_id, infisical_secret_client, project_id

        except UnknownParameterError as err:
            raise UnknownParameterError(
                f"_get_ssm_infisical_secret_values error: {err}"
            ) from err

    def send_email_message(
        self,
        to_email: str,
        from_email: str = os.environ.get("FROM_EMAIL", ""),
        subject: str = SUBJECT_DEFAULT,
        content: str = CONTENT_DEFAULT,
    ) -> bool:
        """
        Send an email message using SendGrid API
        """

        self.from_email = Email(from_email)
        self.content = Content("text/plain", content)

        self.mail = Mail(self.from_email, To(to_email), subject, self.content)
        # Prepare mail to JSON object
        prepared_mail = self.mail.get()

        try:
            # Send an HTTP POST request to /mail/send
            response = self.client.mail.send.post(request_body=prepared_mail)

            logging.info(
                "Status code: %s \n , Headers: %s ",
                response.status_code,
                response.headers,
            )

        except SendGridException as err:
            raise SendGridException(f"Error: {err}") from err

        return True
