from EmailValidation import app, mail
from flask import request, url_for
from flask_mail import Message, Mail
from itsdangerous import URLSafeTimedSerializer, SignatureExpired


# Tạo một serializer với token có hạn sử dụng (giây)
s = URLSafeTimedSerializer('a_secret_key_here')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return '<form action="/" method="POST"><input name="email"><input type="submit"></form>'
    email = request.form['email']
    # Tạo mã xác thực
    token = s.dumps(email, salt='email-confirm')
    # Tạo mẫu thư được gửi đi, recipients là địa chỉ nhận được nhập bên trên
    msg = Message('Confirm email', sender='tqthost@gmail.com', recipients=[email])
    # Tạo liên kết xác thực trong nội dung thư
    link = url_for('confirm_email', token=token, _external=True)
    # Tạo nội dung thư
    msg.body = 'Your link is {}'.format(link)
    # Lệnh gửi thư
    mail.send(msg)
    return '<h1>Please check inbox. The email your entered is: {} and the token is: {} </h1>'.format(email, token)


@app.route('/confirm_email/<token>')
def confirm_email(token):
    try:
        # Thuộc tính salt phải trùng với token được tạo từ dumps trên kia mới so sánh xem hợp lệ không được
        email = s.loads(token, salt='email-confirm', max_age=20)
        # Bắt lỗi token hết hạn trả về thông báo custom thân thiện hơn
    except SignatureExpired:
        return "<h2>The token is expired</h2>"
    return 'The email worked'


if __name__ == '__main__':
    app.run(debug=True, port='2100')
