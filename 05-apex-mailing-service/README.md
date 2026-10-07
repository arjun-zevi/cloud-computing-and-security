# Program 5: Implement a mailing service using Apex (Salesforce)


## Aim
To implement a mailing service using the Apex programming language of Salesforce.

## Prerequisites
- Salesforce Developer Org

## Repository contents
```
05-apex-mailing-service/
├── .gitignore
├── README.md
├── code.txt
├── output/output_screenshot.png
├── src/EmailManager.cls
├── src/run_anonymous.apex
```
`code.txt` contains every program/command used, in one plain-text file.

## Procedure
1. Open the **Developer Console**.
2. **File > New > Apex Class**, name it `EmailManager`.
3. Replace the default body with the code in `src/EmailManager.cls` and save.
4. **Debug > Open Execute Anonymous Window**, paste `src/run_anonymous.apex` (put **your own e-mail address**) and click **Execute**.
5. Check your inbox.

## Expected output
Debug log shows `Email sent successfully` and the e-mail arrives in the inbox.


## Result
The Apex mailing service sent an e-mail successfully.

