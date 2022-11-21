from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACf454ac7e4d513e1621a3e5a786322e23"
# Your Auth Token from twilio.com/console
auth_token  = "4accc915ad1fb9c6d12bbeadfe44bd74"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12014222730", 
    from_="+17816508249",
    body="Hello!! Are you coming to tap this weekend?")

print(client.calls.get("SM4e1e5f17e56ac9a8fd739ced17f47b15"))