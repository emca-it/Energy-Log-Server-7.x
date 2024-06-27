# Empowered AI

`Empowered AI` is a module of Energy Logserver containing mathematical algorithms for data science. It is a licensed extension for SIEM deployment, designed to help SOC teams detect data that is difficult to identify with regular approaches. Advanced mathematical sorting, grouping, and forecasting enriched with statistics create a new outlook on security posture.

`Empowered AI` is an ongoing project, continuously improved by a team of mathematicians, data scientists, and security analysts.

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


## Common Elements

### Settings and Configuration for All Analytical Use Cases

The first step in the data analysis process in the *Empowered AI* module is to properly prepare the data and input it into an analytical rule using saved searches as data sources.

#### Step-by-Step Guide: How to Prepare Data and Input it into an Analytical Rule

1. **Log in to the application** and access the **Discover** module.
2. **Select the data source** you want to analyze (e.g., system logs, application records).
3. **Set filters** and search criteria to narrow down relevant data.
4. **Add a field as a column**, which allows selecting the field during rule creation.

    ![AddFieldAsColumn](/media/media/08_empowered_ai/add_field_as_column.png)

5. **Save the search** by clicking the **Save** button, naming your search, and clicking **Save** again.

    ![CreateSavedSearch](/media/media/08_empowered_ai/create_saved_search.png)

#### Using Saved Searches in the Empowered AI Module

1. **Go to the Empowered AI module**.
2. Select the **AI Rules** tab and click **Create New Rule** or edit an existing rule.
3. In the **Choose Data Source** section, select the saved search you created earlier.

    ![SelectSavedSearch](/media/media/08_empowered_ai/select_saved_search.png)

#### Configuring the Analytical Rule

1. **Name your rule** in the **AI Rule Name** section.
2. In the **Field to Analyse** section, select the data field you want to analyze.

    ![ConfigureRule](/media/media/08_empowered_ai/configure_rule.png)

#### Configuring the Scheduler

The rule can be run immediately using the Run Once option or cyclically using the Scheduled option.

1. For **Run Once** analysis, provide the "Build Time Frame" learning period and the analysis start time using the trained model "Start Date".

    ![RunOnce](/media/media/08_empowered_ai/run_once.png)
    ![BuildTimeFrame](/media/media/08_empowered_ai/build_time_frame.png)
    ![StartDate](/media/media/08_empowered_ai/start_date.png)

2. For **Scheduled** analysis, choose the run frequency (e.g., every hour, day, week, or month). Specify the learning period and the "Start Date Offset" for the data range to be analyzed.

    ![Scheduled](/media/media/08_empowered_ai/scheduled.png)
    ![Frequency](/media/media/08_empowered_ai/frequency.png)
    ![StartDateOffset](/media/media/08_empowered_ai/start_date_offset.png)

#### Accessing the Performance Tab

1. **Log in to the application** and navigate to the **Empowered AI** module.
2. Select the **AI Rules** tab and click on the rule for which you want to view the performance.
3. The **Performance** tab will open, displaying detailed analysis results.

#### Summary

This basic configuration is common to all analytical models. Some models require additional parameters, detailed in their dedicated documentation. Proper data preparation and configuration in the *Empowered AI* module are crucial for effective analysis.

#### FAQ

**Q: What data can I use in saved searches?**
A: Various types of data can be used, but different analysis models expect specific data types. For example, Text Anomaly detection requires textual values.

**Q: Can I edit saved searches?**
A: Yes, but be cautious as changes affect all rules using the same saved search.

#### Troubleshooting

- **Problem: I can't find saved searches in the Empowered AI module.**
  Solution: Ensure the search is saved in the Discover module and you have the appropriate permissions.

- **Problem: The rule does not analyze data as expected.**
  Solution: Check the rule configuration, time range, and search criteria.

---

### Univariate Anomaly Detection

**Univariate Anomaly Detection** identifies anomalies in a single data column. Below is a guide on configuring Univariate Anomaly Detection, highlighting its unique settings.

#### Step-by-Step Guide: How to Configure Univariate Anomaly Detection

##### Step 1: Configuring the Univariate Anomaly Detection Rule

1. **Contamination Factor**
    - **Contamination Factor**: This setting defines the approximate percentage of data considered anomalous. The suggested value ranges between 0.5% and 3%.

    ![ContaminationFactor](/media/media/08_empowered_ai/contamination_factor.png)

2. **Data Aggregation**
    - **Data Aggregation**: Select the aggregation interval to be used for training the model. Available intervals are 30 minutes, 1 hour, 2 hours, 4 hours, 8 hours, 12 hours, and 1 day.

    ![DataAggregation](/media/media/08_empowered_ai/data_aggregation.png)

3. **Other Settings**
    - Complete the configuration of other settings, such as **Start Date**, **Build Time Frame**, **Scheduler options**, and **Field to Analyse**. These settings are the same as those described in the common configuration guide.

##### Step 2: Running the Rule

After configuring all settings, click **Save** or **Save & Run** to save the rule and start the anomaly detection process.

#### Summary

Configuring Univariate Anomaly Detection in the *Empowered AI* module involves setting the contamination factor and selecting the data aggregation interval. Proper data preparation and precise rule configuration enable effective anomaly detection in a single data column.

#### FAQ

**Q: What value should I set for the contamination factor?**
A: The contamination factor should be set between 0.5% and 3%, representing the approximate percentage of data considered anomalous.

**Q: How often should I run the Univariate Anomaly Detection rule?**
A: The frequency depends on the nature of your data and how often you need to monitor it. For continuous monitoring, consider setting a scheduled analysis at regular intervals.

#### Troubleshooting

- **Problem: The rule does not detect anomalies as expected.**
  Solution: Check the contamination factor and data aggregation settings. Adjust these parameters to better fit your data characteristics.

- **Problem: Too many anomalies are detected.**
  Solution: Fine-tune the contamination factor to reduce the number of false positives.

---

### Performance Tab for Univariate Anomaly Detection

The Performance Tab provides a visual representation of the model's performance, particularly focusing on the detected anomalies in a single data column over time.

#### Understanding the Performance Graph

The performance graph displays the actual values of the monitored data and highlights detected anomalies. The x-axis represents the timeline, while the y-axis shows the values of the selected data field, such as `netflow.bytes` in the given example.

![ModelPerformanceGraph](/media/media/08_empowered_ai/model_performance_graph.png)

##### Key Elements of the Performance Graph

1. **Actual Values (Blue Line)**
    - The blue line represents the actual values of the monitored data over time. This line helps in visualizing the normal behavior of the data and identifying patterns or trends.

2. **Anomalies (Red Markers)**
    - Red markers indicate the points where anomalies have been detected. These markers are overlaid on the blue line, showing the specific times when the data deviated from the normal pattern.

##### Interpreting the Graph

- **Spikes and Drops**: Significant spikes or drops in the blue line could indicate unusual activity or anomalies in the data. Red markers on these spikes or drops confirm the detection of anomalies by the model.
- **Consistency**: Consistent patterns in the blue line without red markers suggest stable data behavior with no detected anomalies.

##### Using the Performance Graph

1. **Monitoring Trends**: The graph allows you to monitor trends and identify periods of abnormal activity.
2. **Investigating Anomalies**: By examining the red markers, you can investigate the corresponding timestamps to understand the context of the anomalies.
3. **Adjusting Parameters**: If too many or too few anomalies are detected, consider adjusting the contamination factor or other model parameters to improve detection accuracy.

#### Summary

The performance graph in the Performance Tab of the Univariate Anomaly Detection use case provides a clear visual representation of data behavior and detected anomalies over time. By understanding and utilizing this graph, users can effectively monitor and investigate anomalies, ensuring better data analysis and system optimization.

#### FAQ

**Q: What does the blue line represent in the performance graph?**
A: The blue line represents the actual values of the monitored data over time.

**Q: What do the red markers indicate in the performance graph?**
A: The red markers indicate points where anomalies have been detected by the model.

#### Troubleshooting

- **Problem: No anomalies are detected despite unusual data patterns.**
  Solution: Adjust the contamination factor or data aggregation settings to refine the model's sensitivity.

- **Problem: Too many anomalies are detected, including normal data variations.**
  Solution: Fine-tune the contamination factor to reduce the number of false positives.

---

### Multivariate Anomaly Detection

**Multivariate Anomaly Detection** identifies anomalies across multiple data columns. Below is a guide on configuring this use case.

#### Step-by-Step Guide: How to Configure Multivariate Anomaly Detection

##### Step 1: Configuring the Multivariate Anomaly Detection Rule

1. **Choose Between Analyzing Single and Multiple Signals**
    - **Multi Values**: Ensure the toggle for analyzing multiple signals is enabled. This setting defines how the data is ingested. Single value analysis operates on the numeric aggregation of a selected field, while multi-value analysis uses raw data. Field selection in the former is defined by saved search columns.

    ![MultiValues](/media/media/08_empowered_ai/multi_values.png)

2. **Contamination Factor**
    - **Contamination Factor**: This setting defines the approximate percentage of data that is considered anomalous. The suggested value ranges from 0.5% to 3%.

    ![ContaminationFactor](/media/media/08_empowered_ai/contamination_factor.png)

##### Additional Configuration

- **Start Date**, **Build Time Frame**, and **Scheduler Options**: Complete the configuration of these settings as described in the common configuration guide.

##### Step 2: Running the Rule

After configuring all settings, click **Save** or **Save & Run** to save the rule and start the anomaly detection process.

#### Summary

Configuring multivariate anomaly detection in the *Empowered AI* module involves setting the contamination factor and ensuring the analysis mode is set to multi-values. Proper data preparation and precise rule configuration allow for effective detection of anomalies across multiple data columns.

#### FAQ

**Q: What value should I set for the contamination factor?**
A: The contamination factor should be set between 0.5% and 3%, representing the approximate percentage of data considered anomalous.

**Q: How often should I run the Multivariate Anomaly Detection rule?**
A: The frequency depends on the nature of your data and how often you need to monitor it. For continuous monitoring, consider setting a scheduled analysis at regular intervals.

#### Troubleshooting

- **Problem: The rule does not detect anomalies as expected.**
  Solution: Check the contamination factor and analysis mode settings. Adjust these parameters to better fit your data characteristics.

- **Problem: Too many anomalies are detected.**
  Solution: Fine-tune the contamination factor to reduce the number of false positives.

---

### Performance Tab for Multivariate Anomaly Detection

The Performance Tab provides comprehensive visualizations and detailed information on detected anomalies over time.

#### Visualizing Anomalies Over Time

- **Anomalies Over Time Chart**: Displays detected anomalies over time. The X-axis represents time, while the Y-axis represents the anomaly score. Each red vertical line indicates an anomaly detected by the model at a specific time. This visualization helps in identifying periods of high anomaly activity.

    ![Anomalies Over Time](/media/media/08_empowered_ai/anomalies_over_time.png)

- **Spread of Anomalies Chart**: Shows the distribution of anomaly scores across the entire dataset. Each dot represents an anomaly score, and this chart helps to understand the spread and severity of anomalies in the data.

    ![Spread of Anomalies](/media/media/08_empowered_ai/spread_of_anomalies.png)

- **List of Anomalies**: Below the charts is a detailed table listing the detected anomalies. The table includes the following columns:
    - **Time**: Timestamp of the detected anomaly.
    - **Anomaly Score**: Score indicating the severity of the anomaly.
    - **Network.bytes**: Specific field from the data that might have contributed to the anomaly.
    - **Source**: Additional context or source information about the anomaly.

    This table allows users to review anomaly details and gain insights into specific instances of unusual behavior.

    ![List of Anomalies](/media/media/08_empowered_ai/list_of_anomalies.png)

#### Summary

The performance tab for multivariate anomaly detection in the *Empowered AI* module provides critical information about anomalies detected by the model. Various charts and tables allow users to visualize anomalies over time, understand their distribution, and review detailed information about each detected anomaly. Correct interpretation of these visualizations is crucial for effectively leveraging anomaly detection capabilities.

#### FAQ

**Q: What does the red line on the "Anomalies Over Time" chart represent?**
A: The red line represents an anomaly detected at a specific moment. The height of the line indicates the anomaly score.

**Q: How can I use the "Spread of Anomalies" chart?**
A: The "Spread of Anomalies" chart helps to understand the distribution of anomaly scores in the dataset, which can indicate the severity and frequency of anomalies.

**Q: What information can I find in the "List of Anomalies" table?**
A: The "List of Anomalies" table provides detailed information about each detected anomaly, including the detection time, anomaly score, and relevant data fields.

#### Troubleshooting

- **Issue: Charts do not display data correctly.**
  Solution: Ensure the data source and configuration settings are correct. Refresh the page or rerun the analysis if necessary.

- **Issue: Anomaly results appear incorrect.**
  Solution: Review the contamination factor and other model settings to ensure they are appropriately configured for your data.

Proper data preparation and configuration of the multivariate anomaly detection rule in the *Empowered AI* module are crucial for effective analysis and system optimization. Use this guide to fully leverage the capabilities of this module.

---

### Clustering

**Clustering** groups similar data into clusters. Below is a guide on configuring clustering in the *Empowered AI* module.

#### Step-by-Step Guide: How to Configure Clustering

##### Step 1: Configuring the Clustering Rule

1. **Navigate to the** **Empowered AI** **module**.
2. In the **Clusters** section, specify the number of clusters to be created. This number depends on the nature of your data and the objectives of your analysis.

    ![Clusters](/media/media/08_empowered_ai/clusters.png)

3. Complete the configuration by setting other parameters like **AI Rule Name** and **Field to Analyse**.

##### Step 2: Running the Rule

After configuring all settings, click **Save** or **Save & Run** to save the rule and start the clustering process.

#### Summary

Configuring clustering in the *Empowered AI* module is a straightforward process that involves setting the number of clusters and preparing the appropriate data. Proper data preparation and precise rule configuration enable effective grouping of similar data points.

#### FAQ

**Q: How many clusters should I choose?**
A: The number of clusters depends on the nature of your data and the objectives of your analysis. It is recommended to test different values to find the optimal number of clusters for your use case.

**Q: Can I edit the number of clusters after saving the rule?**
A: Yes, you can edit the number of clusters by editing the existing rule in the **AI Rules** tab.

#### Troubleshooting

- **Problem: Clustering does not work as expected.**
  Solution: Check the rule configuration and ensure that all fields are correctly set and that the data is appropriate for clustering.

- **Problem: I cannot find saved searches in the Empowered AI module.**
  Solution: Ensure that you have saved the search in the Discover module and that you have the necessary permissions to view it.

---

### Performance Tab for Clustering

The Performance Tab provides comprehensive visualizations and detailed information on clustering results.

#### Elbow Method and Optimal Number of Clusters

The elbow method is a commonly used technique in clustering analysis to determine the optimal number of clusters. It involves plotting cluster quality against the number of clusters and identifying the point where the quality improvement slows down, forming an "elbow" shape on the graph. This point indicates the optimal number of clusters.

##### Cluster Quality Chart

The **Cluster Quality Chart** visualizes the relationship between the number of clusters and the cluster quality. The x-axis represents the number of clusters, and the y-axis represents the cluster quality score. The goal is to identify the point where adding more clusters does not significantly improve quality, which is the optimal number of clusters.

![Cluster Quality Chart](/media/media/08_empowered_ai/cluster_quality_chart.png)

In this example, the optimal number of clusters is 3, as indicated on the chart.

#### Cluster Distribution Chart

Below the elbow method chart in the **Performance** tab, there is a cluster distribution chart. This chart shows the distribution of documents among clusters along with their centers. Each dot on the chart represents a document assigned to a specific cluster.


- **Clicking on a Dot**: Clicking on any dot on the chart will display a preview of the document it represents. The preview contains detailed information about the document, such as the message content.
  
![ClusterDistributionChart](/media/media/08_empowered_ai/cluster_distribution_chart.png)

- **Indicative Number of Documents**: The chart shows an indicative number of documents, meaning it does not display the entire dataset. This is done to avoid overcrowding the chart and to provide better readability and data analysis.

##### Benefits of the Cluster Distribution Chart

The cluster distribution chart helps in:

- **Visualizing Document Groupings**: It enables understanding how documents are grouped into clusters and their distributions.
- **Quick Anomaly Identification**: By analyzing the document distribution, unusual groupings can be quickly identified, which may indicate anomalies.
- **Analyzing Cluster Centers**: Cluster centers help evaluate which features are most representative of a given cluster.

#### Clustering Result Examples

Below the cluster distribution chart, the **Performance** tab displays example documents from each cluster. These documents correspond to the dots on the chart and are not a full set but a representative sample.

##### Understanding the Clustering Result Examples

- **Document Representation**: Each cluster section shows a list of example documents that belong to that cluster. The documents are represented by their content, such as log messages or text data.

    ![ClusteringResultExamples](/media/media/08_empowered_ai/clustering_result_examples.png)

- **Sample Data**: The documents shown are not exhaustive. Only a sample is displayed to give an idea of the type of data grouped into each cluster. This helps in understanding the nature and characteristics of the clusters without overwhelming the user with too much data.

##### Benefits of Viewing Clustering Result Examples

The clustering result examples help in:

- **Validating Cluster Quality**: By looking at the example documents, you can quickly assess whether the clustering algorithm has grouped the documents meaningfully.
- **Identifying Patterns**: Seeing sample documents from each cluster allows you to identify common patterns or features within each cluster.
- **Quick Reference**: The representative samples provide a quick reference to the kinds of documents in each cluster, aiding in faster analysis and decision-making.

#### Summary

The Performance Tab for clustering in the *Empowered AI* module is a powerful tool for evaluating clustering analysis results. By using the elbow method and the Cluster Quality Chart, users can determine the optimal number of clusters for their data. Additionally, the ability to view clusters in the Discover module allows for a detailed examination of the data points in each cluster.

#### FAQ

**Q: What is the elbow method?**
A: The elbow method is a technique used in clustering analysis to determine the optimal number of clusters by identifying the point where the improvement in cluster quality slows down, forming an "elbow" shape on the graph.

**Q: How do I interpret the Cluster Quality Chart?**
A: The x-axis represents the number of clusters, and the y-axis represents the cluster quality score. The optimal number of clusters is the point where adding more clusters does not significantly improve quality, indicated by the elbow point on the chart.

#### Troubleshooting

- **Problem: The Cluster Quality Chart does not display correctly.**
  Solution: Ensure that the data is appropriately prepared and that the clustering rule is correctly configured. Check for errors in the data source or clustering parameters.

- **Problem: I cannot view clusters in the Discover module.**
  Solution: Ensure you have the necessary permissions to access the Discover module and that the data is correctly indexed.

Proper use of the Performance tab for clustering analysis in the *Empowered AI* module is crucial for effective data grouping and system optimization. Use this guide to fully leverage the capabilities of this functionality.

---

### Forecasting

**Forecasting** involves setting the data aggregation interval and the forecast time frame.

#### Step-by-Step Guide: How to Configure Forecasting

##### Step 1: Data Aggregation

- **Data Aggregation**: Select the aggregation interval to be used for training the model. Available intervals are 30 minutes, 1 hour, 2 hours, 4 hours, 8 hours, 12 hours, and 1 day. This setting defines how the data will be grouped over time to build the forecasting model.

    ![Data Aggregation](/media/media/08_empowered_ai/data_aggregation.png)

##### Step 2: Forecast Time Frame

- **Forecast Time Frame**: Choose the future time period for which the model will attempt to predict values. Available options are 4 hours, 8 hours, 12 hours, 1 day, 2 days, 3 days, 1 week, and 1 month. This setting determines the period for which the model's forecasts will be applied.

    ![Forecast Time Frame](/media/media/08_empowered_ai/forecast_time_frame.png)

##### Summary

Configuring forecasting in the *Empowered AI* module involves setting the data aggregation interval and the forecast time frame. Correct configuration of these settings ensures that the model is trained on appropriately grouped data and that forecasts are made for the desired future period.

##### FAQ

**Q: What is the purpose of the Data Aggregation setting?**
A: The Data Aggregation setting defines how data will be grouped over time for training the forecasting model. It determines the interval at which data points are aggregated.

**Q: How do I choose the appropriate Forecast Time Frame?**
A: The Forecast Time Frame should be selected based on the specific needs of your analysis. Consider the period for which you need the forecast and choose the appropriate time from the available options.

##### Troubleshooting

- **Problem: The model's forecasts do not match the actual data.**
  Solution: Review the Data Aggregation and Forecast Time Frame settings to ensure they are appropriate for your data. Consider adjusting these settings or retraining the model with different intervals.

- **Problem: The forecast time frame is too short or too long.**
  Solution: Re-evaluate your analysis requirements and select a more suitable forecast time frame. The chosen period should match the needed time resolution of your forecasts.

---

### Performance Tab for Forecasting

The Performance Tab provides detailed visualizations and insights into the accuracy and effectiveness of the forecasting model over time.

#### Forecast vs Actual Data Chart

- **Forecast vs Actual Data Chart**: This chart shows forecasted data compared to actual data over time. The chart uses different colors to distinguish between forecasted data (purple) and actual data (yellow).

    ![ForecastVsActual](/media/media/08_empowered_ai/forecast_vs_actual_data.png)

#### Performance Analysis Over Time

The performance tab allows users to scroll and zoom in on the timeline to closely examine specific periods where the forecasting model performed well or poorly. This can help identify patterns or anomalies that may affect the forecast's accuracy.

#### Summary

The performance tab for forecasting in the *Empowered AI* module provides crucial insights into the accuracy and performance of the forecasting model. Various charts and metrics allow users to visualize forecast accuracy over time, compare predicted values with actual data, and gain insights into the model's reliability. Proper interpretation of these visualizations is essential for effectively utilizing forecasting capabilities.

#### FAQ

**Q: What do the colors on the "Forecast vs Actual Data" chart represent?**
A: On the chart, the purple color represents forecasted data, while the yellow color represents actual data. This color distinction helps in visually comparing the predicted values with the actual values.

**Q: How can I use the performance metrics provided in this tab?**
A: Performance metrics such as MAE and RMSE provide quantitative measures of the forecasting model's accuracy. Lower values indicate better accuracy and reliability of the model.

#### Troubleshooting

- **Problem: The forecast data does not match the actual data.**
  Solution: Review the model configuration and ensure that the input data is correct. Check the historical data used to train the model and adjust the model parameters if necessary.

- **Problem: The performance metrics indicate high error values.**
  Solution: Re-evaluate the model parameters and consider retraining the model with a different dataset or using additional features to improve accuracy.

Proper data preparation and configuration of the forecasting model in the *Empowered AI* module are crucial for effective analysis and system optimization. Use this guide to fully leverage the capabilities of this module.


---


### Text Anomaly Detection

**Text Anomaly Detection** focuses on analyzing textual data for anomalies.

#### Key Features

- **Actual Log Count**: Specify the exact number of logs for analysis.
- **Create Alert**: Automatically create alert rules for detected anomalies.
- **Default Text Anomaly Detection Rules**: Automatically apply default rules for text anomaly detection at startup.
- **Exclude Pattern & Words**: Exclude specific patterns or words from the analysis.
- **Performance Tab**: Monitor and evaluate model performance.
- **Rareness Threshold**: Set the threshold for word rarity in analyzed documents.
- **Sampling Rate**: Control the percentage of sampled documents for analysis.
- **Skipping Numerical Values**: Automatically skip irrelevant numerical data during analysis.

#### Step-by-Step Guide: How to Use Key Features in Text Anomaly Detection


**Actual Log Count**: Specify the number of logs to be analyzed.
    ![ActualLogCount](/media/media/08_empowered_ai/configure_actual_log_count.png)

**Create Alert**: Automatically create alerts for detected anomalies.
    ![CreateAlert](/media/media/08_empowered_ai/create_alert.png)



**Exclude Pattern & Words**: Define patterns and words to be excluded from the analysis.
    ![ExcludePatternAndWords](/media/media/08_empowered_ai/exclude_pattern_and_words.png)


**Rareness Threshold**: Set thresholds for detecting rare words.
    ![RarenessThreshold](/media/media/08_empowered_ai/configure_rareness_threshold.png)

**Sampling Rate**: Adjust the percentage of documents to be sampled for analysis.
    ![SamplingRate](/media/media/08_empowered_ai/configure_sampling_rate.png)

**Skipping Numerical Values**: Skip irrelevant numerical data during analysis.
    ![SkippingNumbers](/media/media/08_empowered_ai/activate_skip_numbers.png)

#### Performance Tab for Text Anomaly Detection

##### Understanding the Performance Graphs


![ModelPerformance](/media/media/08_empowered_ai/model_performance_graphs.png)

- **Anomalies Over Time Chart**: Displays detected anomalies over time. The X-axis represents time, while the Y-axis represents the number of detected anomalies.
- **Spread of Anomalies Chart**: Shows the distribution of detected anomalies across the dataset. Each dot represents an anomaly score.

##### Using the Performance Graphs

1. **Monitoring Trends**: Allows you to monitor trends and identify periods of abnormal activity.
2. **Investigating Anomalies**: By examining the anomaly markers, you can investigate the corresponding timestamps to understand the context.
3. **Adjusting Parameters**: If too many or too few anomalies are detected, consider adjusting the rareness threshold or sampling rate.

##### Anomaly Detection Table

At the bottom of the **Performance** tab, there is an anomaly detection table that provides detailed information about each detected case.

**Anomaly Detection Table**
![AnomalyDetectionTable](/media/media/08_empowered_ai/anomaly_table.png)

##### Information in the Anomaly Detection Table:

- **@timestamp**: The timestamp when the anomaly was detected.
- **Word anomaly score**: The anomaly score for the word, indicating the level of atypicality.
- **Log anomaly score**: The anomaly score for the entire log.
- **No. of rare words**: The number of rare words detected in the log.
- **Rare words**: The list of rare words detected in the log.
- **Text**: A fragment of the text containing the detected anomalies.

##### Expanding a Row

Click the arrow icon next to a specific row to expand detailed information about the anomaly. After expanding the row, you will see the full text containing the anomaly and the list of rare words that have been identified.

![ExpandingRow](/media/media/08_empowered_ai/expand_row.png)

##### Filtering by Rare Words

At the top of the table, there is a **Rare Words Filters** section that allows you to filter anomalies based on rare words. You can enter a rare word to see only the logs that contain that word. To add a filter, click the **+** icon next to the word. To remove a filter, click the **-** icon.

![FilteringRareWords](/media/media/08_empowered_ai/rare_words_filter.png)

##### Actions in the Table

- **Create Incident**: A button that allows you to create an incident based on the selected anomaly.
- **Reset**: A button that allows you to reset the filter and refresh the table.

#### Distinct Anomaly List Table

The **Distinct Anomaly List** tab contains the same anomaly data as the first table but without duplicates. If the message is the same, it is displayed only once. In the first table, all analyzed documents detected as anomalies are displayed, even if one document appears 200 times.


#### Summary

The **Performance Tab** in Text Anomaly Detection provides key information about detected anomalies. Various charts and tables allow users to visualize anomalies over time, understand their distribution, and review detailed information about each detected anomaly. Correct interpretation of these visualizations is crucial for effectively leveraging anomaly detection capabilities.

#### FAQ

**Q: What types of texts can be analyzed?**
A: The system is capable of analyzing various types of textual data, including emails, social media posts, reports, and other textual documents.

**Q: Does the system support multiple languages?**
A: Yes, the text analysis system supports multiple languages, making it a versatile tool on an international scale.

#### Troubleshooting

- **Problem: The system does not analyze the exact number of logs specified.**
  Solution: Ensure that the number of logs is correctly set and that the available data meets the analysis criteria.

- **Problem: Delays in text analysis.**
  Solution: Verify system resources and configuration to increase processing efficiency.

### Conclusion

The *Empowered AI* module offers comprehensive tools for data analysis, including anomaly detection, clustering, and forecasting. Proper data preparation and rule configuration are crucial for effective analysis. Use the provided guides to leverage the full capabilities of this module.


---

### Default AI Rules

Default Rules automatically deploy a set of rules for the syslog index at startup, enabling users to quickly start analyzing data.

1. **Navigate to the Empowered AI module**.
2. Select the **AI Rules** tab and click on the default forecasting rules.
3. Configure the default rules as per your requirements.

    ![GoToEmpoweredAIModule](/media/media/08_empowered_ai/go_to_empowered_ai.png)
    ![SelectForecastingRule](/media/media/08_empowered_ai/select_default_rule.png)
