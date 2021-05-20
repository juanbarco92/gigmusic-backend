from fastapi_mail import FastMail, MessageSchema,ConnectionConfig

''' Modulo de envio de emails '''

# Inicializacion
conf = ConnectionConfig(
   MAIL_USERNAME=from_,
   MAIL_PASSWORD="************",
   MAIL_PORT=587,
   MAIL_SERVER="smtp.gmail.com",
   MAIL_TLS=True,
   MAIL_SSL=False
)

fm = FastMail(conf)

# Envio de emails
async def send_email(email: str):
	template = '''
		<html>
		<body>
			<h4>Bienvenido</h4>
			<br>
			<p>Te registraste correctamente en GIG</p>
		</body>
		</html>
	'''
	message = MessageSchema(
        subject="GIG - Bienvenida",
        recipients=email, 
        body=template,
        subtype="html"
       )
	await fm.send_message(message)
	return {'ok': 'ok'}

