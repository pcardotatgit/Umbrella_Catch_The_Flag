# Introduction

You have a Mission !

Some Endpoints had been infected into your organization. As a Security Investigator, you suspect that infection occured during web browsing.

And some evidences lead you to a public web site which seems to be the root cause of these infections. All Infected users said to you that their troubles began after having visiting a Web page on the INTERNET.

So You downloaded this suspicious web page in order to investigate it.

You copied and pasted the page source into your laptop and you called it :

- **page.html**

You are a Cisco Umbrella Customer, and you subscribded to the Investigate Backend. Lucky You !  You will be able to use Investigate APIs to understand what is the Origin of the problem.


## 1 - Installation

Installing these scripts is pretty straight forward . You can just copy  and paste them into you python environment but a good practice is to run them into a python virtual environment.

If dont have your python environment yet, basically you just need a python 3.7 ( or more ) interpreter. For windows users google search for **Python for windows** and install it. Don't forget to click on the **add to path** check box. And that's it.

Cisco DEVNET provide you with very good resources about the tools to install into your latop in order to build your development workstation.

Go to for example to [ Developer Workstation and Environment Setup ](https://developer.cisco.com/learning/tracks/devnet-express-security-v1-1/dev-setup/)

Select your Operating System and go thru the instructions.

All recommended tools in the DEVNET Section is good to install.

### Step 1 - Create a working directory into your laptop

Create a working directory into your laptop and open a terminal console into it. 

You will put all code into this working directory

### Step 2 - Create a Python virtual environment and start it

For Linux/Mac 

	python3 -m venv venv
	source bin activate

For Windows 
	
We assume that you already have installed git-bash.  If so open a git-bash console and type the 2 following commands :

	python -m venv venv 
	venv/Scripts/activate

**Remark :** you can run the code without having installing a python virtual environment. It will work as far you have all the required python modules

### Step 3 - clone the scripts into your laptop

**you have a git client** 

If you have a git client you can use the following command :

	git clone https://github.com/pcardotatgit/Umbrella_Catch_The_Flag.git
	cd umbrella_ctf_venv/

**you DON'T have a git client** 

You can download the zip package by clicking on the **clone** button on the top right of this git page. Click on **download.zip**. And then unzip the zip file into your working directory. 

### Step 4 -Install needed modules

The scripts need the following python modules

- urllib3==1.26.15
- requests
- crayons
- pyopenssl
- flask
- flask_request_params	

You can install them with the following  :
	
	python -m pip install --upgrade pip
	pip install -r requirements.txt

Or you can install required modules separatly :
	
	python -m pip install --upgrade pip
	pip install urllib3==1.26.15
	pip install requests
	pip install crayons
	pip install pyopenssl
	pip install flask
	pip install flask_request_params


## 2 - Learn about Umbrella and Umbrella Investigate APIs

If you want to learn about Umbrella APIs you can go to the following place which contains a very good summary.

 [DEVNET Threat Hunting Lab](https://developer.cisco.com/learning/tracks/devnet-express-security/security-threat-hunting/)

and go to **Chapter 3: Introduction to Umbrella API**

Use Umbrella APIs, goto to :

[Umbrella Investigate API documentation](https://docs.umbrella.com/investigate-api/docs)

We use in this lab the **Investigate APIs**

And try to find in the **API Refernce** the api endpoints which gives you back Domain Status.


# 3 - Start Your Mission


## 1 - Run the Umbrella Investigate simulator

In order to help you to jump on your mission, I have coded an Umbrella Investigate Simulator. It completely emulate the Umbrella Investigate behavior for this CTF. It is recommended to use it.

	If you have your own Umbrella Investigate License, you don't need to use the simulator. 

	This license is not easy to get. You have to pay for this.  And it's a long process to get an evaluation license.

	It is recommended to use the simulator because data inside the simulator will never expire and will always be the same. Which might not be the case for the real Umbrella BackEnd if data are too old.

From the python virtual environment you started prior, go to the **[./umbrella_investigate_simulator]** subfolder and start the web Server.

    - python app.py

The Server listen on port 4000 and you can connect to it at : **http://localhost:4000**

You will need an Investigate API Key to be able to send API call to this Web Server 

**FAKE_Investigate_API_Key = 31801821-b9a1-4ad3-82d9-dfe2c93ffake**

**Remark :** This is not a valid Umbrella API key. It doesn't work anywhere else than this CTF.

## 2 - Start Your Mission

Open a second CMD terminal into your working directory. 

Start a second python virtual environment.

For Linux/Mac 

	source bin activate

For Windows 
	
	venv/Scripts/activate

Go to the **[./TODO_your_mission_code]** folder. And figure out what you can do from there.

You can test the connectivity to the Umbrella Simulator by running the **0_test_server.py** script.

	python 0_test_server.py

If you got an anwser and saw into the simulator console that the http connexion was Okay... then you are ready to go.

Check that the **page.html** file is in this folder. This is the file you have to investigate

You are supposed to use the Python Scripts. They are here for helping you to answser to the questions.

If you prefer to Use POSTMAN instead of the python script ... It's UP to you !

The only thing to know about these python script is that they are all buggued. You have to modify them ot make them work.

Open them and search for **#TODO  MISSION :** statements into it. They will give you some hints.

All Umbrella information you need are above. 

But don't hesistate to go to the DCLOUD Umbrella instant demonstration as well, in order to see Umbrella Investigate in action.

It'up to you !!

# 4 - Questions you have to answer to

Question 1 : How many observables ( IP addresses, SHA256, Domains or URL ) the suspicious web page contains ?  

Question 2 : There is one link to a Malicious domain in this page.  What is the name of this malicious domain ? 

Question 3 : What are the categories to which belong this malicious domain ?

Question 4 : What is the registrant country of this malicious domain ?

Question 5 : In the Security Information, what is the value of the **entropy** of this malicious domain ?


# 5 - Solutions

Hum ... I think you downloaded some working scripts when you git cloned this CTF....
