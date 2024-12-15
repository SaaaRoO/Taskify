from flask import Flask, jsonify, request
from flask_mail import Mail, Message
from flask_swagger_ui import get_swaggerui_blueprint
import os

# إنشاء تطبيق Flask
def create_app():
    app = Flask(__name__)

    # إعدادات Swagger UI
    SWAGGER_URL = '/swagger'  # رابط Swagger UI
    API_URL = '/static/swagger.json'  # رابط ملف التوثيق
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "Task Management API"}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    # إعدادات البريد الإلكتروني
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', 'your-email@gmail.com')  # استخدم environment variable أو قيم صريحة
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD', 'your-email-password')  # استخدم environment variable أو قيم صريحة
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME', 'your-email@gmail.com')
    mail = Mail(app)

    # نموذج المهام
    tasks = []

    # الإيميل: إرسال إشعار عند إضافة مهمة جديدة
    def send_email(to, subject, body):
        msg = Message(subject, recipients=[to], body=body)
        mail.send(msg)

    # تسجيل المهمة
    @app.route("/api/tasks", methods=["POST"])
    def create_task():
        task_data = request.json.get('task_name')  # استخدام JSON
        if not task_data:
            return jsonify({'message': 'Task name is required'}), 400
        
        task_id = len(tasks) + 1
        task = {"task_id": task_id, "task_name": task_data}
        tasks.append(task)
        
        # إرسال إشعار عبر البريد الإلكتروني
        send_email('user-email@example.com', 'New Task Created', f'Your task "{task_data}" has been created.')
        
        return jsonify(task), 201

    # الحصول على كل المهام
    @app.route("/api/tasks", methods=["GET"])
    def get_tasks():
        return jsonify(tasks), 200

    # الحصول على مهمة حسب ID
    @app.route("/api/tasks/<int:task_id>", methods=["GET"])
    def get_task(task_id):
        task = next((t for t in tasks if t["task_id"] == task_id), None)
        if not task:
            return jsonify({'message': 'Task not found'}), 404
        return jsonify(task), 200

    return app
