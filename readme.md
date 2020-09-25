# Introduction

You've got a Mission !

Some Endpoints had been infected into your organization. As a Security Investigator, you suspect that infection occured during web browsing.

And some evidences lead you to a public web site which seems to be the origin of these infections. All Infected users said to you that their troubles began after visiting a Web page on the INTERNET.

So You downloaded this suspicious web page in order to investigate it.

You copied and pasted the page source into your laptop and you called it :

- **page.html**

You are a Cisco Umbrella Customer, and you subscribded to the Investigate Backend. Lucky You !  You will be able to use Investigate APIs to understand what is the Origin of the problem.


## Installation

Installing these scripts is pretty straight forward . You can just copy / and paste them into you python environment but a good practice is to run them into a python virtual environment.

If dont have your python environment yet, Cisco DEVNET provide you with very good resources.

Go to for example [ DevNet Express for Cisco DNA v3 ]https://developer.cisco.com/learning/devnet-express/dnav3-track

and then go to the **Developer Workstation and Environment Setup** chapter.  Select your Operating System and go thru the instructions.


### Install a Python virtual environment

For Linux/Mac 

	python3 -m venv venv
	source bin activate

For Windows 
	
We assume that you already have installed git-bash.  If so open a git-bash console and :

	python -m venv umbrella_ctf_venv 
	source /umbrella_ctf_venv/Scripts/activate

**Remark :** you can run the code without having installing a python virtual environment.

### git clone the scripts

	git clone https://github.com/pcardotatgit/Umbrella_Catch_The_Flag.git
	cd umbrella_ctf_venv/
	
### install needed modules

The scripts need the following python modules

- requests
- flask
	
you can install them with the following  :
	
	pip install -r requirements.txt

## 2 Learn about Umbrella and Umbrella Investigate APIs

If you want to learn about Umbrella APIs you can go to the following place which contains a very good summary.

 [Security Programmabililty Mission](https://developer.cisco.com/learning/modules/threat-hunting)

and go to **Chapter 3: Introduction to Umbrella API**

Use Umbrella APIs, goto to :

[Umbrella Investigate API documentation](https://docs.umbrella.com/investigate-api/docs)


And try to find the api url which send a **query for a single domain**


# 3 - Start Your Mission


## Run the Umbrella Investigate simulator

If you have your own Umbrella Investigate License, you don't need to start this simulator.

But this license is not easy to get. We have to pay for this.  And it's a long process to get an evaluation license.

In order to help you to jump on your mission, I have coded an Umbrella Investigate Simulator. 

From your python virtual environment go to the **[./umbrella_investigate_simulator]** folder and start the web Server.

    - python app.py

The Server listen on port 4000 and you can connect to it at : **http://localhost:4000**

You will need an Investigate API Key to be able to send API call to this Web Server 

**Investigate_API_Key = 31801821-b9a1-4ad3-82d9-dfe2c93ff9ef**

**Remark :** This is not a valid Umbrella API key. It doesn't work anywhere else than this CTF.

Run the **0_test_server.py** script to test it.

## Start Your Mission

Go to the **[./TODO_your_mission_code]** folder. And figure out what you can do from there.

Check that the **page.html** file is in this folder. This is the file you have to investigate

Python Scripts are there only for helping you to answser to the questions.

If you prefer to Use POSTMAN instead of the python script ... It's UP to you !

But if you decide to use the python scripts, then the only thing to know is that you have to modify these scripts accordingly to what is needed to make them work.

Open them and search for **#TODO  MISSION :**

All Umbrella information you need are above. 

And don't hesistate to go to the DCLOUD Umbrella instant demonstration as well, in order to see Umbrella Investigate in action.

It'up to you !!

# 4 - Questions you have to answer to

Question 1 : How many observables ( IP addresses, SHA256, Domains or URL ) the suspicious web page contains ?  

Question 2 : There is one link to a Malicious domain in this page.  What is the name of this malicious domain ? 

Question 3 : What are the categories to which beling this malicious domain ?

Question 4 : What is the registrant country of this malicious domain ?

Question 5 : In the Security Information, what is the value of the **entropy"** of this malicious domain ?


# 5 - Solutions

Hum ... I think you downloaded some working scripts when you git cloned this CTF....
