# DATA CONCEPT INTRODUCTION

## APPLICATIONS

| COLUMN NAME | DATA TYPE  | NULL VALUE |
| --- | --- | --- |
| UUID | NUMBER(15,0) | NOT NULL |
| SUBMIT_DT | DATETIME | NOT NULL |
| NAME | VARCHAR | NOT NULL |
| OTHER NAME | VARCHAR | NULL |
| INITAL DECISION | VARCAHR | NULL |
| FINAL DECISION | VARCHAR | NULL |
| CHANNLE_ID | VARCHAR | NOT NULL |
| CUST_NO | VARCHAR | NOT NULL |
| MODIFY_ID  | VARCHAR | NOT NULL |
| CUTOMER_TYPE | VARCHAR | NOT NULL |
| SEGEMENT_CD | VARCHAR | NOT NULL |
| FG_COMPLETE | NUMBER(15,0) | NOT NULL |
| AM_DEVICE | NUMBER(15,0) | NULL |
| AMOUNT_UPFRONT_CALCULATED | NUMBER(15,0) | NULL |
| AM_UPFRONT_PAID | NUMBER(15,0) | NULL |
| CT_GENERICC_ACCESSORY | NUMBER(15,0) | NULL |
| PRODUCT_TYPE | VARCHAR | NULL |
| PRODUCT_CLASS | VARCHAR | NULL |
| PRODUCT_NAME | VARCHAR | NULL |
| AM_PRICE_RETAIL_RECOMMENDED | NUMBER(15,0) | NULL |
| AM_PRICE_NET | NUMBER(15,0) | NULL |

COLUMN EXPLNATION:

- UUID: Order id, primary key
- SUBMIT_DT: Order time, be aware of that this is UTC time
- NAME: Customer name
- OTHER NAME: Customer nickname
- INITAL DECISION: As we only look at the referred order, so the decision is REFER
- FINAL DECISION: The final decision made by approval specialist
- CHANNEL ID: The channel that the product be purchased
- CUST NO: customer number
- MODIFY ID: The employee id who review the order
- CUSTOMER TYPE: Default value as a comsumer customer
- SEGEMENT_CD: Consumer Customer: 1, Commercial Customer: 2
- FG_COMPLETE: Finished: 1, In Process: 0
- AM_DEVICE: Offical product price
- AMOUNT_UPFRONT_CALCULATED: the amount that the customer should paid under UPF
- AM_UPFRONT_PAID: the amount that the customer actuall paid
- CT_GENERICC_ACCESSORY: 1: this product has accessory; 0: this product does not have any accessory
- PRODUCT_TYPE: default value as “device”
- PRODUCT_CLASS: default value as “Consumer Product”
- PRODUCT_NAME: Product Name
- AM_PRICE_RETAIL_RECOMMENDED: product retail price
- AM_PRICE_NET: product net price

## ALERT

| COLUMN NAME | DATA TYPE  | NULL VALUE |
| --- | --- | --- |
| UUID | NUMBER(15,0) | NOT NULL |
| SUBMIT_DT | DATETIME | NOT NULL |
| CD_TYPE_VISA | VARCHAR | NOT NULL |
| MODIFY_ID  | VARCHAR | NULL |
| MODIFY_DT | DATETIME | NOT NULL |
| STATUS | VARCHAR | NULL |
| ALERT_CODE | VARCHAR | NOT NULL |

COLUMN EXPLNATION:

- UUID: Order id, primary key
- SUBMIT_DT: Order time, be aware of that this is UTC time
- CD_TYPE_VISA: Visa Type
- MODIFY_ID: The employee id who review the order
- MODIFY_DT: The employee id when review the order
- STATUS: Decision Type, “Decline-pending”, “Refer”, “BitometricsRequired”, “Approval”, “Hold”
- ALERT_CODE: Alert Code

## QUEUE HISTORY

| COLUMN NAME | DATA TYPE  | NULL VALUE |
| --- | --- | --- |
| UUID | NUMBER(15,0) | NOT NULL |
| SUBMIT_DT | DATETIME | NOT NULL |
| QUEUE_ID | VARCHAR | NOT NULL |
| MODIFY_ID  | VARCHAR | NULL |
| MODIFY_DT | DATETIME | NOT NULL |
| OUTGOING_ACTION_ID | VARCHAR | NOT NULL |

COLUMN EXPLNATION:

- UUID: Order id, primary key
- SUBMIT_DT: Order time, be aware of that this is UTC time
- QUEUE_ID: Why the order trigger the manual check
- MODIFY_ID: The employee id who review the order
- MODIFY_DT: The employee id when review the order
- OUTGOING_ACTION_ID: Order Status

## PASSPORT

| COLUMN NAME | DATA TYPE  | NULL VALUE |
| --- | --- | --- |
| UUID | NUMBER(15,0) | NOT NULL |
| VISA_TYPE | VISA_TYPE | NOT NULL |
| VISA_NO | NUMBER(15,0) | NOT NULL |
| VISA_EXPIRY_DT | DATETIME | NOT NULL |
| MODIFY_DT | DATETIME | NOT NULL |
| MODIFY_ID  | VARCHAR | NULL |

COLUMN EXPLNATION:

- UUID: Order id, primary key
- VISA_TYPE: Visa type
- VISA_NO: Visa number
- MODIFY_ID: The employee id who review the order
- MODIFY_DT: The employee id when review the order
- VISA_EXPIRY_DT: Visa expiry date

## ALERT CODE

| COLUMN NAME | DATA TYPE  | NULL VALUE |
| --- | --- | --- |
| ALERT_CODE  | VARHCAR | NOT NULL |
| ALERT_DESC | VARCHAR | NOT NULL |

COLUMN EXPLNATION:

- ALERT_CODE:  Alert Code
- ALERT_DESC: Alert code description

## Entity Relationship Diagram

![Database ER diagram (crow's foot).png](DATA%20CONCEPT%20INTRODUCTION%209043909d782f444f817cf1e09d83077c/Database_ER_diagram_(crows_foot).png)