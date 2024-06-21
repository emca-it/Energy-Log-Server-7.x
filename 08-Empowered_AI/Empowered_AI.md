# Empowered AI

`Empowered AI` is a module of Energy Logserver containing mathematical algorithms for data science.

It is licenced extention for SIEM deplyment. Main purpose of the `Empowered AI` is to help SOC teams see that data which are difficult to detect with regular approach. Advance mathematical sorting, grouping, forecastig enriched with statistics create a new outlook of security posture.

`Empowered AI` is an ongoing project. Our team of mathematicians, data scientists and security analysts continue their work addressing more and more new usecases.

## AI Rules

In the `Empowered AI`  section you will find a summary of the existing rules. At the top, you'll find the total number of rules and the number of scheduled and unscheduled rules. Here is the search field and buttons `Refresh rules list`  and `Create New Rule`  Below is the table. It contains `AI Rule Name`, `Search/Index Name`  -  data source, `Last Executed`  - date, `Last Modified` - date, selected `Use Case`,  `Schedule`  - scheduling frequency, `Status`  and `Action`  icons.

![](/media/media/okno.png)

### Status

The rule has one of the following statuses:

- Waiting to start - `Run once` rule starts by clicking symbol play.
- Scheduled - the scheduled rule starts automatically.
- Scoring
- Building
- Finished - click on the `AI Rule Name`  to get the forecast results preview `AI Rules>Performance`.
- Error -  check error details in the results preview  `Performance>AI Rule Configuration>Exceptions`.

### Actions

Icons of actions:

 - Play – run or rerun the rule,
 - Stop – unschedule periodic rule, after this action rule type changes to Run Once,
 - Pencil - edit the rule's configuration,
 - Bin – delete the rule.

### Prepare your data set

Save your `Discover`  search so you can use it the same way as in visualizations and dashboards.

### Create New Rule

To create a rule choose ``Empowered AI`>AI Rules>Create New Rule`. In pop-up form `Select Use Case`. The `Empowered AI` module contains AI models for various use cases: `Forecasting`, `Anomaly Detection - Number`, `Anomaly Detection - Text`, `Clustering` and `Relationship Mining`.

![](/media/media/wybor.png)

### Performance

To see the result of the finished rule click on the link in the column `AI Rule Name`. Here we have `AI Rule Configuration` and `Model Performance`.

 ![](/media/media/result.png)

In `AI Rule Configuration` you will find detailed configuration parameters and information about the training data set. Exception details will also appear here in case of misconfiguration. `Model Performance` is the presentation of data and analysis results. Depending on the use case, these are charts, relationship visualizations, and tables.

### Forecasting

Predicting future conditions is a crucial aspect of decision-making in any organization. To anticipate upcoming events, historical data analysis is indispensable. Energy Logserver `Empowered AI` Module suggests utilizing the XGBoost algorithm, also known as eXtreme Gradient Boosting, for forecasting your environmental variables in the near future.

XGBoost is an advanced machine learning algorithm that excels at handling datasets with multiple variables. This algorithm can accurately model complex relationships within data, enabling precise predictions of future events. XGBoost is a popular choice in the field of Data Science, particularly for solving regression and classification problems, thanks to its efficiency and effectiveness.

### Create a rule

To create a rule choose `Empowered AI`>`AI Rules`>`Create New Rule`. In pop-up form `Select Use Case>Forecasting` and insert the rule's name.

 ![](/media/media/nazwa_i_dane.png)

### Choose data

`Choose Data Source`  is a drop-down list with your saved data, choose one of them. After loading the source, we can select `Field to Analyse`  - the id-field to be predicted. The system default loads headers of the appropriate data type for the specified use case. You can also choose the checkbox displaying all the fields. The proper mapping is necessary for appropriate header recognition. As numerical data, you can also use the number of documents instead of field values. To do that, choose the checkbox. `Multiply by Field`  allows you to obtain separate forecasts e.g., for several (or all) hosts, users and domains, in one rule.

 ![](/media/media/multiply.png)

### Scheduler options

In this field, you can choose the frequency at which the rule runs `Run Once` or `Scheduled`.

#### Run Once

Range of dates you choose from the interactive calendars, click on icons.
`Build Time Frame` is a piece of data used to create and train the model. More training data allows the algorithm to obtain more accurate signal patterns and trend information. If there is too little and incomplete data, the forecast may not be accurate.
`Start Date` is the starting point of predictions.

 ![](/media/media/agregacja.png)

#### Scheduled

Scheduled rules require dates to be a relative distance from now. You choose number and time unit: minutes, hours, days, weeks, months. `Build Time Frame Offset`  is historical data used to build the model.  `Period: time selection`   is time distance before end point `TO: now - time selection` of the data set. `Start Date Offset  is the starting point of forecast. It must be set inside the build time frame offset.

![](/media/media/scheduled.png)

### Data Aggregation and Forecast Time Frame

The data set is divided into small intervals specified in the `Data Aggregation> 30 min | 1 h | 2 h | 4 h | 8 h | 12 h | 1 d`  parameter. The algorithm uses this unit as the training and reporting frequency. `Forecast Time Frame> 4 h | 8 h | 12 h | 1 d | 2 d | 3 d | 1 w` is the period of the requested forecast. A shorter time gives a better estimation. Value of forecast time frame must be a multiplicity of time data aggregation.

### Launch

You can find the newly created rule in the table with the `Waiting to start` status. Click `Play` and wait for a moment. Refresh the rules list. If it has the status `Finished`, click on the rule's name to see the results.

 ![](/media/media/finished.png)

### Results

![](/media/media/result.png)

### Difference Multi Pattern - alert rule

Users of SIEM Plan can leverage Empowered AI in alert rules. For forecasting, a special rule called Multi Pattern Difference has been created. In the form  `Create Alert Rule`, we compare two patterns, index_name-* and index_name-forecast-*, along with the fields used in the forecast, `field_name` and `ai.field_name`. It's crucial to note that the `agg_min` value should not be lower than the aggregation window used in the forecast; it must be a multiple thereof.
Fill in the remaining fields following the convention used for other alert rules.

![](/media/media/multi_difference_alert1.png)

## Default AI Forecasting Rules

In today's rapidly evolving world of technology, the ability to predict and respond to potential IT threats and challenges is crucial for maintaining operational continuity and system security. Our new functionality, **Default Forecasting Rules** within the *Empowered AI* module, has been designed to meet these challenges by offering advanced analysis and forecasting capabilities in the context of syslog data.

The goal of our functionality is simple yet ambitious: to automatically deploy a set of default forecasting rules for the syslog index right after the system starts up. This enables users to immediately make use of advanced analytical tools that help in identifying and responding to data anomalies, potential security threats, and other significant patterns that may impact the system and organizational operations.

By using **Default Forecasting Rules**, users can:

- **Quickly start analyzing data**: Default rules eliminate the need for manual system configuration, allowing users to focus on the analysis and interpretation of data.
- **Increase the effectiveness of threat detection**: Applying advanced AI algorithms and machine learning in forecasting allows for faster and more precise identification of potential threats.
- **Improve operational efficiency**: Automating the forecasting process saves time and resources while increasing overall operational efficiency.

Our functionality is designed with ease of use and accessibility in mind, ensuring that organizations of any size or industry can leverage the power of predictive analytics to optimize their IT operations.

## Step-by-Step Guide: How to Use Default Forecasting Rules in the Empowered AI Module

This guide shows how to quickly and easily start using default forecasting rules in our Empowered AI module. By following these simple steps, you will be able to effectively utilize the power of AI for data analysis and forecasting.

### Prerequisites

Ensure you are logged into the application and have the appropriate permissions to use the Empowered AI module.

### Step 1: Go to the Empowered AI Module in the Application

Find and open the Empowered AI module in the application. You can do this by selecting the appropriate option in the main menu.

![GoToEmpoweredAIModule](/media/media/go_to_empowered_ai.png)

### Step 2: Select One of the Default Forecasting Rules

Upon entering the Empowered AI module, you will see a list of available forecasting rules. Select the one that best fits your needs by clicking on it.

![SelectForecastingRule](/media/media/select_default_rule.png)

### Step 3: Run Forecasting Rule

With the selected rule, click the "run" button to start the data analysis process. This may take some time, depending on the amount of data to be processed.

![LaunchForecasting](/media/media/run_rule.png)

### Step 4: Check the Results

After forecasting is complete, the results will be displayed in the module. Review them to understand potential patterns and dependencies in the data.

![CheckForecastingResults](/media/media/check_results.png)

### FAQ

**Q: How often can I run forecasting?**  
A: Forecasting can be run as often as needed. However, keep in mind that each forecasting run is a computational process and may take some time.

**Q: Can I modify the default forecasting rules?**  
A: Yes, default rules can be modified.

### Troubleshooting

- **Problem: Forecasting is not launching.**  
Solution: Ensure you have the appropriate permissions and that all required data is correctly loaded into the system.

- **Problem: Forecasting results seem to be inaccurate.**  
Solution: Check if the selected forecasting rule is suitable for the type and character of your data. Consider modifying the rule for better alignment.