import imaplib, email

# This function will return all emails from the inbox
def getemails(mail, inbox="inbox", search="ALL"):
    print ('Logged in as ' + usr_id) # print login message
    mail.select(inbox) # connect to inbox.
    typ, emails_id = mail.search(None, 'ALL') # search all email and return ids data
    
    for id in emails_id[0].split():  # for each ID in the list of IDs
        print(f'Processing email number {id}, {typ}') # print the ID number
        typ, email_body = mail.fetch(id, '(RFC822)')  # fetch the email body (RFC822) for the given ID 
        for body_parts in email_body: # for each part of the tuple msg_data returned by fetch
            if len(body_parts) >1:
                    try:
                        msg = email.message_from_bytes(body_parts[1]) # get the actual message content
                        print(msg['From']) # print the from field of the message
                        print(msg['Subject']) # print the subject field of the message
                        print(msg['Date']) # print the date field of the message
                        print(msg['To']) # print the to field of the message
                        payload = (msg.get_payload()) # the message body
                    except TypeError:
                        print("error")
    mail.close()
    mail.logout()

# This function will return all mailboxes
def getmailboxes(mail):
    mailboxes =[]
    for part in mail.list()[1]:
        decode_part=part.decode('utf-8')
        temp_decode = decode_part.split(' ')
        result = ' '.join(temp_decode[-1:])
        mailboxes.append(result)
    return mailboxes

# Main function
if __name__ == "__main__":
    # Login credentials
    host = " "
    usr_id = " "
    usrpass = " "
    port = 993

    # Connect to the server
    mail = imaplib.IMAP4_SSL(host, port)
    try:
        mail.login(usr_id, usrpass)
        mailboxes = getmailboxes(mail)
        getmailboxchoice = input(f'Choose mailbox from {mailboxes} ')
        getemails(mail, getmailboxchoice, 'ALL') 
    except imaplib.IMAP4.error:
        print("Login failed.")
        print("Check your credentials and try again.")
   

