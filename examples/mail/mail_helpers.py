import sendgrid
import os


sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

##################################################
# Send an email template with custom fields and custom sender name.
# See full helper doc here:
# [here](https://github.com/sendgrid/sendgrid-python/blob/master/use_cases/README.md).
# Including a [full feature example](https://github.com/sendgrid/sendgrid-python/blob/master/use_cases/kitchen_sink.md)

template_id = "[YOUR TEMPLATE ID]" # d-xxx
template_data = {
    "my_field_1": "Field 1 Value",
    "my_field_2": "Field 2 Value",
}

message = Mail(
    from_email=("sender@example.com", "Sender Name"),
    to_emails=To("recipient@example.com"))

message.template_id = template_id
message.dynamic_template_data = data


try:
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers) 
except Exception as e:
    print(e.message)

