from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from utils.utils import EMAIL_USER, EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_SERVER

''' Modulo de envio de emails '''

# Inicializacion
conf = ConnectionConfig(
   MAIL_USERNAME = EMAIL_USER,
   MAIL_PASSWORD = EMAIL_PASSWORD,
   MAIL_FROM = EMAIL_SENDER,
   MAIL_PORT=587,
   MAIL_SERVER=EMAIL_SERVER,
   MAIL_TLS=True,
   MAIL_SSL=False,
   USE_CREDENTIALS = True
)

fm = FastMail(conf)

# Template de Email
template = '''
	<html>
		<body>
			<h4>Bienvenido</h4>
			<br>
			<p>Te registraste correctamente en GIG</p>
		</body>
   </html>
'''

# Envio de emails
async def send_email(email: str):
	message = MessageSchema(
        subject="GIG - Bienvenida",
        recipients=[email], 
        body=template,
        subtype="html"
       )
	await fm.send_message(message)
	return 'OK'

