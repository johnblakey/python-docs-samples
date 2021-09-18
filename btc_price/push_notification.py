import logging

from access_secrets import access_secret_version
from twilio.rest import Client


def send_sms():
    # Get secrets from Secret Google Service
    project_id = "personal-crypto-over-9000"
    account = access_secret_version(project_id, "twilio-account-jb", "1")
    token = access_secret_version(project_id, "twilio-token-jb", "1")
    twilio_phone = access_secret_version(project_id, "twilio-phone-jb", "1")
    receiver_phone = access_secret_version(project_id, "phone-jb", "1")

    # Create twilio client
    client = Client(account, token)

    message = client.messages \
                    .create(
                        body="Gas prices are cray cray! ;)",
                        from_=twilio_phone,
                        to=receiver_phone
                    )

    logging.info("Message sent with twillio: {}".format(message))

    return "SMS sent"
