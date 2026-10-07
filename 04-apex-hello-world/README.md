# Program 4: Develop a simple application using Apex (Salesforce)



## Aim
To develop a simple custom application using the Apex programming language on the Salesforce cloud platform.

## Prerequisites
- Free Salesforce Developer Org (developer.salesforce.com/signup)

## Repository contents
```
04-apex-hello-world/
├── .gitignore
├── README.md
├── code.txt
├── output/output_screenshot.png
├── src/HelloWorldApp.cls
├── src/run_anonymous.apex
```
`code.txt` contains every program/command used, in one plain-text file.

## Procedure
1. Sign up for / log in to a Salesforce Developer Org.
2. Open the **Developer Console** (gear icon > Developer Console).
3. **File > New > Apex Class**, name it `HelloWorldApp`.
4. Paste the code from `src/HelloWorldApp.cls` and save (**File > Save**).
5. **Debug > Open Execute Anonymous Window**, enter the code from `src/run_anonymous.apex`, tick **Open Log**, click **Execute**.
6. In the log, tick **Debug Only** to see the message.

## Expected output
`WELCOME TO APEX PROGRAMMING` appears in the debug log.


## Result
A simple Apex class was created and executed on the Salesforce platform.
