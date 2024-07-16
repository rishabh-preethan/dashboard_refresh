import smtplib

def send_email():
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'rishabhp5902@gmail.com'  # Your Gmail address
    smtp_password = 'nxyl ukdp pgtf rjwr'     # App-specific password

    # List of recipient email addresses
    to_addresses = ['rishabh_preethan@thirdray.ai', 'aditi_l@thirdray.ai']

    # Create SMTP server object
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    try:
        # Login to the SMTP server with app-specific password
        server.login(smtp_username, smtp_password)

        # Compose and send the email
        from_address = 'rishabhp5902@gmail.com'
        subject = 'Test Message'
        body = 'This is a test message'

        for to_address in to_addresses:
            message = f'Subject: {subject}\n\n{body}'
            server.sendmail(from_address, to_address, message)
            print(f"Email sent successfully to {to_address}!")

    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication Error: {e}")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

    finally:
        server.quit()

if __name__ == "__main__":
    send_email()
