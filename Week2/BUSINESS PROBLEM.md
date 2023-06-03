# BUSINESS PROBLEM

## Background

As we mentioned in the Week 1, you will be served as a data analst in the data and analytics team, and will be received the data request from your stakeholder - The Approval Team. You will work closely with a few stakeholders below:

- Data Engineers:
    - DE will assist you to set up the working environment (including Coding Env, permissions of accessing the DB)
    - Briefly Introduction of how to use Snowpark Python to do data analysis
- Business Analyst:
    - Create, manage and groom the backlog in each sprint
    - Allocate tasks to you in each sprint
    - Facililate regular stand-up meetings in an Agile environment
    - Play the role of liasion between the data team and the approval team to analyze the business requirements

## Business Problem Introduction

The Approval team currently uses a hardware decision-making system developed by Equifax to finalize decisions when customers purchase digital products through retail or online channels. The system assesses customers' credit and fraud history based on data points measured against other credit and fraud bureaus (including banks, 3rd-party credit bureaus, Telco companies, financial companies, etc.). If the system cannot make a decision based on current data, it assigns an alert code to this customer. The approval team then reviews the code to create new policies based on the new alert codes after a certain time or event to avoid similar issues and improve detection discrimination. The purpose of this group is to block as many customers in the high-risk group as they can because they have already found the high risky group has a high possibility of not paying the bill on time and our client is a medium-sized company which is focusing on the cost and decrease it to ensure they could survive in the pandemic period.

In July 2021, the approval team noticed an increase in the volume of manual queue checks for high-risk groups but did not pay much attention as they had enough human resources to handle the issue. However, the volume of the manual queue checks continued to increase, and by September 2021, it reached around 95% of the total. The team seeks data-driven solutions to increase detection accuracy and determine the reason for the issue.

## Analytics Project Objective

Based on the data provided by the client, they want us to do three tasks:

- Summary the top 5 alert code based on the data on Sep/21
- Provide the data-driven solutions to deal with the situation and use the following month data to validate our solutions
- Estabilishment of a dashboards for automatically monitoring this issue