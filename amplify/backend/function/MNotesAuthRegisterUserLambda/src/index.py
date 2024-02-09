import logging

from validateRegister.validate_user import User

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    logger.info("Received an event from Pre-signed up user:")
    logger.info(event)

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

        logger.info(
            "Sending response to user with code: %s and message %s",
            status_code,
            status_message,
        )
        return event

    raise AttributeError("Error: birth date is invalid!")
