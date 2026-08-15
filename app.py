# Sample Flask Webhook Structure for Verification Only
from flask import Flask, request

app = Flask(__name__)


@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
  # Inbound command listener logic placeholder
  incoming_msg = request.values.get("Body", "").lower()
  if "new invoice" in incoming_msg:
    return "200 OK - Processing Command"
  return "200 OK"


if __name__ == "__main__":
  app.run()
