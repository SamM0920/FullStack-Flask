import pythoncom
from flask import Flask, jsonify, request
import win32com.client

app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    to = data['to']
    subject = data['subject']
    body = data['body']
    
    pythoncom.CoInitialize()
    outlook = win32com.client.Dispatch('Outlook.Application', "C:\Program Files (x86)\Microsoft Office\root\Office16\OUTLOOK.EXE")
    mail = outlook.CreateItem(0)
    mail.To = to
    mail.Subject = subject
    mail.Body = body
    mail.Send()

    return jsonify({"message": "Email sent successfully"})

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0",port=5000)