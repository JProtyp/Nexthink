# Nexthink
## QA Recruitment Quiz

### Question 1:
Given the following shell script:
    #!/bin/sh <br />
    w=`who | grep $1` <br />
    if [ -z "$w" ]; then <br />
    echo "$1 ... "; <br />
    fi <br />
    a. What is doing this script? Replace the dots by the adequate text. <br />
    b. Correct this script such that it never makes an error and always answers something. <br />
### Question 2:
Consider the log file engine.log presented in folder Question2. This file contains the logs of <br />
the unix process nxengine starting and running. <br />
In the log: <br />
• starting nxengine indicates that the process is starting. <br />
• nxengine is running indicates that the process has started to run. <br />
Write a script (feel free to use any language you are comfortable with) to list the time  <br />
nxengine takes to be running. Output the result in the following format: <br />

Start Cycle: 1 Duration: HH:MM:SS <br />
Start Cycle: 2 Duration: HH:MM:SS <br />
... <br />
Start Cycle: n Duration: HH:MM:SS <br />

### Question 3:
Consider the log file messages.log presented in folder Question3. This log contains some alert <br />
information. Alert level could be: <br />
• warning <br />
• critical <br />
• error <br />

Write a command-line to print all the alerts. The output should be presented as follow:  <br />
Jun 26 06:15:00 nxengine NX[WARNING]: [2012-06-26 05:00:00] Sources with low disk space [2] <br />
Jun 26 06:19:00 nxengine NX[warning]: 2012-06-26T06:19:00 Sources with low disk space -1 [1] <br />
Jun 26 07:15:00 nxengine NX[CRITICAL]: [2012-06-26 06:00:00] Sources with low disk space [2] <br />
Jun 26 07:19:00 nxengine NX[ERROR]: 2012-06-26T07:19:00 Untitled alert 1 [1] <br />
Jun 26 07:57:30 nxengine NX[warning]: 2012-06-26T07:57:30 Sources with low disk space -1 [1] <br />
Jun 26 08:15:00 nxengine NX[CRITICAL]: [2012-06-26 07:00:00] Sources with low disk space [2] <br />
Jun 26 08:58:30 nxengine NX[warning]: 2012-06-26T08:58:30 Sources with low disk space -1 [1] <br />
Jun 26 09:19:30 nxengine NX[Error]: 2012-06-26T09:19:30 Untitled alert 1 [1] <br />
Jun 26 09:58:30 nxengine NX[Error]: 2012-06-26T09:58:30 Untitled alert 1 [1] <br />

### Question 4:
Consider the code presented in folder Question4 of the attached Java resources. <br />
Given the unit tests written in TestOption.java, write type Option<T>. <br />
Can you imagine some situations where these types could be useful? <br />
    
### Question 5:
Here is a simple login screen to connect to a server: <br />
How would you test this login screen? <br />
    
### Question 6:
What are the contents of a release notes document? <br />
    
### Question 7:
How do you use acceptance tests in your work? <br />
    
### Question 8:
In your own words, what is automation all about? <br />

 
## Answers
Answers can be found in folder **src**. Each question have it's own folder
