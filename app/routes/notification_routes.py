from flask import Blueprint, jsonify
from app.services.email_service import send_email

bp = Blueprint('notifications', __name__)

@bp.route("/api/notify/email", methods=["POST"])
def send_notification():
    send_email(
        subject="Test Notification",
        recipients=["user@example.com"],
        body="This is a test email notification!"
    )
    return jsonify({"message": "Email sent successfully!"})
