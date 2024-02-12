import json
import logging
from send_grid.sendgridmanager import SendGridManager

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def handler(event, context):

    logger.info("Received an event from Post-authenticated user:")
    logger.info(event)

    event_json = json.loads(event)
    sendgrid: SendGridManager = SendGridManager()

    if sendgrid.send_email_message(
        to_email=event_json["request"]["userAttributes"]["email"]
    ):
        logger.info("Success!")

        return event
