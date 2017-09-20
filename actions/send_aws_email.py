import boto3

class SendAWSEmail(Action):
  def run(self, email_from, email_to, subject, message, region):
    client = boto3.client('ses', region_name = region)
    response = client.send_email(
        Destination = {
            'ToAddresses': [
               email_to
            ],
        },
        Message = {
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': message,
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': subject,
            },
        },
        Source = email_from,
    )
    return
