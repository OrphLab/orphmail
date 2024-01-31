This simple Python script uses the imaplib and email modules to connect to an email server, retrieve emails from a specified mailbox, and display relevant information such as sender, subject, date, and recipient.

#Usage
Make sure you have Python installed on your system.

Copy the script to your local machine.

Fill in the required information:

host: the IMAP server host address.
usr_id: your email address.
usrpass: your email password.
port: the IMAP server port (usually 993 for SSL).
Run the script.

The script will prompt you to choose a mailbox from a list of available mailboxes.

It will then retrieve and display information about each email in the selected mailbox.

#Script Structure
The script is divided into two main functions:

1. getemails
def getemails(mail, inbox="inbox", search="ALL"):

Connects to the specified mailbox.
Retrieves email IDs based on the search criteria (default is all emails).
Iterates through each email ID, fetching and displaying relevant information.
email_body is a tuple.
body_parts is an element of that tuple.
The first element is typically the response type, and the second element is a dictionary containing the email data.

2. getmailboxes
def getmailboxes(mail):

Retrieves a list of mailboxes using the list method.
Decodes and extracts mailbox names.
Returns a list of available mailboxes.

#How to Run
Replace the placeholders for host, usr_id, usrpass, and port with your own email server details.

Run the script using a Python interpreter.

Follow the on-screen prompts to choose a mailbox and view email details.

Note: Ensure that your email provider allows IMAP connections and provides the necessary server details.

Feel free to modify the script as needed for your specific use case or integrate it into a larger project.









