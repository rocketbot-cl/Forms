



# Rocketbot Xperience
  
Connect and work with Rocketbot Forms Xperience  

*Read this in other languages: [English](Manual_Forms.md), [Português](Manual_Forms.pr.md), [Español](Manual_Forms.es.md)*
  
![banner](imgs/Banner_Forms.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

## Como usar este modulo



## Description of the commands

### Login NOC
  
Login to NOC using one of the options, API Key, noc.ini file, or credentials.
|Parameters|Description|example|
| --- | --- | --- |
|URL Server|Server URL|https://roc.myrb.io/|
|Select a method to connect to the Orchestrator|Options to login to R.O.C, you can use user credentials, API Key or by selecting noc.ini file||
|Do not verify SSL certificate|If checked, the submitted request does not verify the SSL certificate.||
|Assign result to a Variable|Variable where the state of the connection will be stored, returns True if it is successful or False otherwise|Variable|

### Get Form queue
  
Get queues
|Parameters|Description|example|
| --- | --- | --- |
|Form Token|Form Token|8YWUW8AXAV3UPNKY|
|Set to var|Variable to store result without {}|var|

### Get Form queue data
  
Get form data from queue. It must have as many variables as the form has 'inputs', they must be called like the 'Element ID' of the 'input'.
|Parameters|Description|example|
| --- | --- | --- |
|Queue ID|Queue ID|1|
|Form Token|Form Token|8YWUW8AXAV3UPNKY|
|Set to var|Variable to store result without {}|var|

### Download Form File
  
Download a file uploaded in a form
|Parameters|Description|example|
| --- | --- | --- |
|Queue ID|Queue ID|1|
|File|Var that contains file path of queue||
|Save file to|Path where file will be saved|C:\Rocketbot\file.ini|

### Update Form queue status
  
Change status to form queue
|Parameters|Description|example|
| --- | --- | --- |
|Status|Select the status of the queue||
|Queue ID|Enter the ID of the queue|1|
|Set to var|Var without {} where the result will be saved||

### Return Message to Xperience
  
Returns a message to the Xperience form
|Parameters|Description|example|
| --- | --- | --- |
|Xperience Token|Xperience Token|{xperience}|
|Message to return|Message to return||
