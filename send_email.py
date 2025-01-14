import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email details
sender_email = "bc.game.bcd.airdrrop@gmail.com"
sender_password = "Haafiz@1000"  # Use App Password if using Gmail with 2FA enabled
receiver_email = "math.nic.in@gmail.com"
subject = "Welcome to Our Service!"

# Create the email content
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Email Template</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }
    .email-container {
      width: 100%;
      max-width: 600px;
      margin: 0 auto;
      background-color: #ffffff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }
    .email-header {
      text-align: center;
      padding-bottom: 20px;
    }
    .email-body {
      padding: 10px;
      line-height: 1.6;
      color: #333333;
    }
    .button {
      display: inline-block;
      background-color: #007bff;
      color: #ffffff;
      padding: 10px 20px;
      text-decoration: none;
      border-radius: 5px;
      margin-top: 20px;
    }
    .footer {
      text-align: center;
      font-size: 12px;
      color: #888888;
      padding-top: 20px;
    }
    @media screen and (max-width: 600px) {
      .email-container {
        width: 100%;
        padding: 15px;
      }
    }
  </style>
</head>
<body>
  <div class="email-container">
    <div class="email-header">
      <h1>Welcome to Our Service!</h1>
    </div>
    <div class="email-body">
      <p>Hello [Recipient Name],</p>
      <p>Thank you for signing up with us. We are excited to have you on board. To get started, please click the button below:</p>
      <a href="https://www.example.com" class="button">Get Started</a>
      <p>If you have any questions, feel free to reach out to our support team.</p>
    </div>
    <div class="footer">
      <p>Thank you for being a part of our community!</p>
      <p>&copy; 2025 Company Name | All rights reserved</p>
    </div>
  </div>
</body>
</html>
"""

# Set up the MIME
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the HTML content to the email
msg.attach(MIMEText(html_content, 'html'))

# Set up the SMTP server and send the email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Use your email provider's SMTP server if not using Gmail
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()
