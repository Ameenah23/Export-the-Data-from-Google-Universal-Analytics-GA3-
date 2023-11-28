# Export the Data from Google Universal Analytics (GA3)
Date: Nov 16, 2023

XXXXData Ltd Project Summary 

Ameenah Al-Haidari


 
### INTRODUCTION
This is the summary document of ZZZZZ Academy’s work on the Extracting Data from Google Universal Analytics project at xxx Data from Sep 20,2023 to Nov 30, 2023. 

Our client is ZZZZZ is a learning academy that providing the best quality data skills & AI training to the students with Career counselling services, and also for corporate clients.

The main service for this part from the project that xxxData team provided to them was on these parts:
- Retrieve the Historical user activity data from Google Universal Analytics starting from 2020-01-01 to 2023-07-24;
- Storage those Historical Data in PostgreSqL;
- Design the Universal Analytics Glossary;
- Break down the most differentiators between the two platforms "the Universal Analytics and Google Analytics 4" with an aim to give a clear understanding of the new platform for better migration preparedness.
  
The project of Extracting Data from Google Universal Analytics will be discussed in this article.

### PROBLEM STATEMENT
Google Analytics is a web analytics service offered by Google that tracks and reports website traffic and also the mobile app traffic & events, currently as a platform inside the Google Marketing Platform brand.

Starting on July 1, 2023, standard Google Universal Analytics properties stopped processing new data, and all customers will lose access to the Universal Analytics interface and API starting on July 1, 2024. To maintain your website measurement, you'll need a Google Analytics 4 property.
One of the primary questions on the minds of marketers, analysts, and developers is:

- How to Save your historical Universal Analytics data.
- What’s the difference between Universal Analytics to Google Analytics 4?
- What is the best tool to storage your hostrical data?
- 
The need to preserve this data is the driving force behind this project. Our responsibility will be to help to ingest the historical [user activity data] from Google Universal Analytics. This data type focuses on user interactions with a website or app, capturing metrics such as page views, session duration, bounce rate, event tracking, and e-commerce transactions. User behaviour data offers insights into visitor navigation patterns, the pages they visit most, the length of their stay, and actions they undertake, like filling out a form or making a purchase.

Tools used: Python(pandas, numpy, matplotlib, seaborn, sqlalchemy), BeautifulSoup (bs4), Selenium, google.oauth2, googleapiclient, oauth2client, apiclient, PostgreSqL, GitHub, Notion.

### MAJOR WORKS
We have built different scripts and documents to Extracting Data from Google Universal Analytics;
1.	Google Analytics Reporting API from google.oauth2 and oauth2client;
2.	Google’s User Explorer in Universal Analytics (userActivity.search);
3.	Google Anlytics data with pagination and unsampled data;
4.	Discover the Technical Challenges to get the Number of Indexed Pages on Google and Sitemap (SEO) using BeautifulSoup (bs4) and Selenium;
5.	Script to create any config (ini) file for SQLAlchemy;
6.	Script to importing Data from a Pandas to a PostgreSql using SQLAlchemy;
7.	Wrote a document to collect the most important Universal Analytics Glossary;
8.	Wrote a document to show the difference between the Universal Analytics and Google Analytics 4.

All scripts and documents of this project are posted to xxxxdata repository on Github "xxxx-data/ga3_ameenah_a_202309"
https://github.com/xxxx-data/ga3_ameenah_a_202309


#### Google Analytics Reporting API
This script requests a report from Google Analytics Reporting API from google.oauth2 and oauth2client and returns the response as a DataFrame. It can handle pivot and dimensions reports, summary reports with no pivot and dimensions. With the Google Analytics Reporting API, we:
-	Build custom dashboards to display Google Analytics data.
-	Automate complex reporting tasks to save time.
-	Integrate the Google Analytics data with other business applications.


#### Samples from the Dashboard;

![image](https://github.com/beam-data/ga3_ameenah_a_202309/assets/123785380/7a1344a8-7177-455c-a5c4-6356eaeed365)

 	 
### Google’s User Explorer in Universal Analytics (userActivity.search);
To pull out the User Explorer report with Python (userActivity.search), we did it in three stages;

First stage: retrieve and export Client Ids with number of sessions from a Universal Analytics using "analytics.reports().batchGet" and store that in csv file.

Second stage: read client IDs file and request Analytics Reporting API V4 using "analytics.userActivity().search

![image](https://github.com/beam-data/ga3_ameenah_a_202309/assets/123785380/8448703a-8fb5-4ece-bb69-290ee2ff7de7)

The result is a table with nested dictionary under the “activities” column;

![image](https://github.com/beam-data/ga3_ameenah_a_202309/assets/123785380/e7f35c72-9036-4af9-85b4-c0c2ce96f080)

Third stage: flatten “activities” column, convert it to list and then to DataFrame. After that concat it to the original table. And the last step is export it to csv file. 

The final table shape that exported to PostgreSql;

![image](https://github.com/beam-data/ga3_ameenah_a_202309/assets/123785380/45c01ff3-3bbf-4124-a311-434d52eb6ec4)
![image](https://github.com/beam-data/ga3_ameenah_a_202309/assets/123785380/874486d4-abef-4b48-bb7a-e67154bb7440)

The name of columns;

![image](https://github.com/beam-data/ga3_ameenah_a_202309/assets/123785380/5c8cc6ed-c0e8-4cbd-8230-bad79d9df0fe)


### Google Anlytics data with pagination and unsampled data
Pulls Google Analytics data with pagination and unsampled data. Data was retrieved from 2020-01-01 to 2023-07-24. We counted and found the number of Sessions about 406864.0.

![image](https://github.com/beam-data/ga3_ameenah_a_202309/assets/123785380/330b1743-0e79-4d79-817b-b510506ee1d2)
![image](https://github.com/beam-data/ga3_ameenah_a_202309/assets/123785380/aabcad3b-375c-4ae7-9dd9-1f2a30bd10cf)


### Discover the Technical Challenges to get the Number of Indexed Pages on Google and Sitemap (SEO) using BeautifulSoup (bs4) and Selenium
This Python script performs a search to check the number of indexed pages on Google for multiple sites using Selenium, bs4 and Python. And compare that with the real indexed pages from Sitemap-parser. 
For the aim to know and to get an idea of how committed a site is in a market. Around how many pages does the business deal with 200 or 200M. And to have an idea of the competitor’s index sizes when building an SEO strategy.
We found;

 ![image](https://github.com/beam-data/ga3_ameenah_a_202309/assets/123785380/6147c4d8-06ad-487c-9d1c-d3b7408d85d9)

- the Number of Indexed Pages that scraped from weclouddata sitemap is 1008 whereas from google is about max 471, with poor performance (46.73%).
- the Number of Indexed Pages that scraped from brainstation.io sitemap is 11298 whereas from google is about max 13,700, with extra performance (121.26%).
- the Number of Indexed Pages that scraped from lighthouselabs.ca sitemap is 1118 whereas from google is about max 2,420, with extra performance (216.46%).

### Wrote two Documentations;
-	 to collect the most important Universal Analytics Glossary
-	 to show the difference between the Universal Analytics and Google Analytics 4.
-	 
The Universal Analytics (UA) is the previous version of Google Analytics, and was used by many websites for tracking their traffic. After Google Analytics 4 (GA4) released, you might find it challenging to understand all the terminologies attached to the platforms related to the various Google Analytics versions.

There are so many reports and so much data inside the UA and GA4 (GA4). With huge information on the Internet sites of the different Google Analytics versions that makes kind of confusion especially for the beginners. Beside that, one of the primary questions on the minds of marketers, analysts, and developers is: What’s the difference between Universal Analytics to Google Analytics 4?  Thus, we;

- break down the most differentiators between the two platforms.
- Write Google Universal Analytics glossary.
 	 
![image](https://github.com/beam-data/ga3_ameenah_a_202309/assets/123785380/d94e5b98-a5c1-4985-918e-3354d3a87061)

### CHALLENGES
Google Analytics put limits and quotas on API requests to protect the system from receiving more data than it can handle, and to ensure an equitable distribution of the system resources.
![image](https://github.com/beam-data/ga3_ameenah_a_202309/assets/123785380/1d5ad915-0f33-42eb-a047-abe0efc729ce)

The project is done on Nov 16, 2023, but because of these limits and quotas, we only retrieve less than 10,000 per day. And with crowded traffic day, we can ingest less than 8,000 per day. Thus, the extracting data will continue for around 3 weeks after this date.


### FUTURE WORKS
if any

### ACHIEVEMENTS AND CONCLUSIONS
The key achievements that xxxxdata made through the Extracting Data from Google Universal Analytics project were;

- help the client to ingest and export the historical [user activity data] before the aforementioned deadline;
- support the BI to build custom dashboards to display Google Analytics data;
- be able to compare between the two platforms the UA and GA4;
- build good knowledge to understand the most differentiators between the two platforms and cover the most important terminology with the aim to give a clear understanding of the new platform GA4 for better migration preparedness.
- recommend improving KEYwords for SEO.




