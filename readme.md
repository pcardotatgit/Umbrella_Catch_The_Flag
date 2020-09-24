#Introduction

Some Endpoints had been infected into your organization. As a Security Investigator you suspect that infection occured during web browsing.

And some evidences lead you to a public web site which seems to be the origin of these infection. All Infected users browsed said to you that their troubles began after visiting a Web page.

So You retrieved this suspicious web page un order to investigate it.

- page.html

You are a Cisco Umbrella Customer, and you subscribded to the Investigate Backend. Lucky You !  You will be able to use Investigate APIs to understand what is the problem.

If you want to learn about Umbrella APIs you can go to the following place which contains a very good summary

https://developer.cisco.com/learning/modules/threat-hunting

and go to Chapter 3: Introduction to Umbrella API


Start to use Umbrella APIs

goto to 

https://docs.umbrella.com/investigate-api/docs

And try to find the api url which send a query for a single domain


https://docs.umbrella.com/investigate-api/docs/domain-status-and-categorization-1


Question 1 : How many observables ( IP addresses, SHA256, Domains or URL ) the suspicious web page contain ?  ( response : 28 )

Question 2 : There is one link to a Malicious domain in this page.  What is the name of this malicious domain ? ( response : www.goloduha.info )

Question 3 : What are the categories to which beling this malicious domain ?

You can use the DCLOUD Umbrella instant demonstration to see Investigate in action.

Question 4 : What is the registrant country of this malicious domain ?



