# BUSINESS PROBLEM

## Background

As mentioned in Week 1, you will serve as a data analyst in the data and analytics team and receive data requests from your stakeholder, the Approval Team. You will work closely with the following stakeholders:

- Data Engineers:
    - They will assist you in setting up the working environment, including the coding environment and permissions for accessing the database.
    - They will give you a brief introduction on how to use Snowpark Python for data analysis.
- Business Analyst:
    - They will create, manage, and groom the backlog in each sprint.
    - They will allocate tasks to you in each sprint.
    - They will facilitate regular stand-up meetings in an Agile environment.
    - They will act as a liaison between the data team and the Approval Team to analyze the business requirements.

## Business System Introduction

- Hardware decision-making system:
    
    A hardware decision-making system is designed to evaluate an applicant's credit risk and assess their potential for causing financial loss due to fraud and credit risk. Its primary objective is to provide accurate judgments on the risk associated with an application, ensuring the protection of a company's financial interests.
    
- Data sources for credit risk and fraud history:
    
    The hardware decision-making system relies on comprehensive data provided by Equifax, a prominent third-party bureau company. Equifax aggregates and summarizes credit risk and fraud history information obtained from various sources, including banks, financial institutions, telecommunications companies, retailers, and other relevant entities. This data serves as a critical foundation for the system's assessment process 
    
- Overview of Equifax:
    
    Equifax Inc. is a leading American multinational consumer credit reporting agency headquartered in Atlanta, Georgia. It is one of the three largest consumer credit reporting agencies globally, along with Experian and TransUnion. Equifax specializes in gathering, analyzing, and providing credit-related information, assisting businesses in making informed decisions regarding credit risk and fraud mitigation.
    
- Decision-making process and judgment finalization:
    
    The hardware decision-making system employs a set of predefined policies to evaluate an applicant's potential risk. If an applicant does not meet the criteria established by these default policies, the system generates an alert code to notify business users of the specific factors contributing to the applicant's disapproval. For instance, if an applicant has a history of consistent late bill payments across multiple companies, their request to utilize the Up Front Payment (UFP) method for purchasing a product might be declined due to the associated high risk.
    
    In such cases, the system escalates the application to the approval team for manual review. This involves involving specialists who possess the expertise to thoroughly evaluate the applicant's profile, taking into account additional factors or mitigating circumstances. The manual review process ensures that a final decision is made by incorporating a human perspective and expertise in cases where the default policies alone may not provide a conclusive judgment.
    
- System Flow Chart
    
    ![Business_Process_Flow_Chart.png](Week2/Business_Process_Flow_Chart.png)
    

## Business Problem Introduction

In July 2021, the approval team observed a notable surge in the number of manual queue checks required for customers categorized as high-risk by the hardware decision-making system developed by Equifax. Initially, this increase in workload did not raise significant concerns since the team possessed sufficient human resources to manage the situation. However, as time progressed, the volume of manual queue checks continued to escalate, reaching an alarming level of approximately 95% of the total by September 2021.

To address this issue and enhance the effectiveness of the decision-making process, the approval team is actively seeking data-driven solutions. The team aims to achieve two primary objectives: improve detection accuracy and identify the underlying reasons for this unprecedented rise in manual queue checks.

## Analytics Project Objective

The objective of this analytics project is to address the increasing volume of manual queue checks for high-risk customers and provide data-driven solutions to improve detection accuracy. The project will involve the following tasks:

- Summary of Top 5 Alert Codes (September 2021):
    
    Analyze the data from September 2021 and identify the top 5 alert codes that are most frequently assigned to customers. Provide a summary of these alert codes, including their descriptions, associated risk factors
    
- Data-Driven Solutions:
    
    Develop data-driven solutions to mitigate the issue of high manual queue checks. This involves conducting a comprehensive analysis of historical data, identifying patterns and anomalies, and proposing strategies to enhance the accuracy of risk assessment. The solutions may include adjustments to the hardware decision-making system's policies, machine learning algorithms, or collaboration with Equifax to address potential data discrepancies.
    
- Validation using data from OCT/21 to Jan/22:
    
    Validate the proposed data-driven solutions using the data from October 2021 to January 2022. Assess the effectiveness of the implemented measures by comparing the volume of manual queue checks before and after the implementation. Evaluate the manual queue ratio of the total based on the validation results.
    
- Dashboard Establishment:
    
    Create a dashboard for monitoring the issue of high manual queue checks automatically. The dashboard should provide real-time updates on the number of manual queue checks, alert codes assigned, and any relevant metrics related to risk assessment. This will enable the approval team to track the progress of the implemented solutions and take proactive measures if any new issues arise.
    

The ultimate goal of this analytics project is to optimize the hardware decision-making system's performance, reduce the reliance on manual reviews, and ensure accurate identification of high-risk customers. By leveraging data-driven insights and implementing effective solutions, the client can enhance their risk management processes and streamline operations in the face of the ongoing pandemic.
