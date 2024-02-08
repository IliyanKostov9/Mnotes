import json
import logging
from validateRegister.validate_user import User

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    logger.info("Received an event from Pre-signed up user:")
    logger.info(event)
    status_code: int = 400
    status_message: str = "Error, birth date is invalid!"

    user_attributes = event["request"]["userAttributes"]

    # Map the provided user input to `User` class
    user: User = User(
        user_attributes["name"],
        user_attributes["email"],
        user_attributes["picture"],
        user_attributes["birthdate"],
    )
    # Validate the birth date
    if user.validate_birth_date():
        status_code = 200
        status_message = "Sucess, birth date is valid now!"

    return {"statusCode": status_code, "body": json.dumps(status_message)}
