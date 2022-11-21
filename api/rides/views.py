from twilio.twiml.messaging_response import MessagingResponse
from django.http import HttpResponse

from .models import User

# Create your views here.
def test_parse(request):
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    print(body)
    resp.message(f"This is a test, you said {body}.")

    return HttpResponse("Hello, world. You're at the TEST PLACE.")

