# User Manual

## Introduction

Energy Logserver is an innovation solution allowing for centralized IT
systems events. It allows for an immediate review, analysis, and
reporting of system logs - the amount of data does not matter.
Energy Logserver is a response to the huge demand for the storage and analysis of large amounts of data from IT systems.Energy Logserver is an innovation solution that responds to the need to effectively process large amounts of data coming from the IT
environments of today's organizations. Based on the open-source
project Elasticsearch valued on the market, we have created an
efficient solution with powerful data storage and searching
capabilities. The System has been enriched with functionality that
ensures the security of stored information, verification of users,
data correlation and visualization, alerting, and reporting.

![](/media/media/image2_js.png)

Energy Logserver project was created to centralize events of all IT
areas in the organization. We focused on creating a tool that
functionality is most expected by IT departments. Because an effective
licensing model has been applied, the solution can be implemented in
the scope expected by the customer even with a very large volume of
data. At the same time, the innovation architecture allows for
servicing a large portion of data, which cannot be dedicated to solutions with limited scalability.

### Elasticsearch ##

Elasticsearch is a NoSQL database solution that is the heart of our
system. Text information sent to the system, application, and system
logs are processed by Logstash filters and directed to Elasticsearch.
This storage environment creates, based on the received data, their
respective layout in a binary form, called a data index. The Index is
kept on Elasticsearch nodes, implementing the appropriate assumptions
from the configuration, such as:

- Replication index between nodes,
- Distribution index between nodes.

The Elasticsearch environment consists of nodes:

- Data node - responsible for storing documents in indexes,
- Master node - responsible for the supervision of nodes,
- Client node - responsible for cooperation with the client.

Data, Master, and Client elements are found even in the smallest
Elasticsearch installations, therefore often the environment is
referred to as a cluster, regardless of the number of nodes
configured. Within the cluster, Elasticsearch decides which data
portions are held on a specific node.

Index layout, their name, and set of fields are arbitrary and depend on the form of system usage. It is common practice to put data of a
similar nature to the same type of index that has a permanent first
part of the name. The second part of the name often remains the date
the index was created, which in practice means that the new index is
created every day. This practice, however, is conventional and every
index can have its rotation convention, name convention, construction scheme, and its own set of other features. As a result of passing the document through the

The Indexes are built with elementary parts called shards. It is good
practice to create Indexes with the number of shards that is the
multiple of the Elasticsearch data nodes number. Elasticsearch in the 7.x version has a new feature called Sequence IDs that guarantees more successful and efficient shard recovery. \

Elasticsearch uses *mapping* to describe the fields or properties that documents of that type may have. Elasticsearch in the 7.x version restricts indices to a single type.

### Kibana

Kibana lets you visualize your Elasticsearch data and navigate the Elastic Stack. Kibana gives you the freedom to select the way you give
shape to your data. And you don’t always have to know what you're looking for. Kibana core ships with the classics: histograms, line
graphs, pie charts, sunbursts, and more. Plus, you can use Vega grammar to design your visualizations. All leverage the full
aggregation capabilities of Elasticsearch.  Perform advanced time series analysis on your Elasticsearch data with our curated time series
UIs. Describe queries, transformations, and visualizations with powerful, easy-to-learn expressions. Kibana 7.x has two new features - a new "Full-screen" mode for viewing dashboards, and a new "Dashboard-only" mode which enables administrators to share dashboards safely.

### Logstash

Logstash is an open-source data collection engine with real-time pipelining capabilities. Logstash can dynamically unify data from
disparate sources and normalize the data into destinations of your choice. Cleanse and democratize all your data for diverse advanced
downstream analytics and visualization use cases.

While Logstash originally drove innovation in log collection, its capabilities extend well beyond that use case. Any type of event can be
enriched and transformed with a broad array of input, filter, and output plugins, with many native codecs further simplifying the
ingestion process. Logstash accelerates your insights by harnessing a greater volume and variety of data.

Logstash 7.x version supports native support for multiple pipelines. These pipelines are defined in a *pipelines.yml* file which is loaded by default.
Users will be able to manage multiple pipelines within Kibana. This solution uses Elasticsearch to store pipeline configurations and allows for on-the-fly reconfiguration of Logstash pipelines.

### ELK

"ELK" is the acronym for three open-source projects: Elasticsearch, Logstash, and Kibana. Elasticsearch is a search and analytics
engine. Logstash is a server‑side data processing pipeline that ingests data from multiple sources simultaneously, transforms it,
and then sends it to a "stash" like Elasticsearch. Kibana lets users visualize data with charts and graphs in Elasticsearch.
The Elastic Stack is the next evolution of the ELK Stack.

## Data source

Where does the data come from?

Energy Logserver is a solution allowing effective data processing
from the IT environment that exists in the organization.

The Elsasticsearch engine allows the building database in which large amounts of data are stored in ordered indexes. The Logstash module is responsible for loading data into Indexes, whose function is to collect
data on specific TCP/UDP ports, filter them, normalize them, and place them in the appropriate index. Additional plugins, that we can use in
Logstash reinforce the work of the module and increase its efficiency,
enabling the module to quickly interpret data and parse it.

Below is an example of several of the many available Logstash plugins:

**exec** - receive an output of the shell function as an event;

**imap** - read email from IMAP servers;

**jdbc** - create events based on JDC data;

**jms** - create events from Jms broker;

Both Elasticsearch and Logstash are free Open-Source solutions.

More information about the Elasticsearch module can be found at:
[https://github.com/elastic/elasticsearch](https://github.com/elastic/elasticsearch)

List of available Logstash plugins:
[https://github.com/elastic/logstash-docs/tree/master/docs/plugins](https://github.com/elastic/logstash-docs/tree/master/docs/plugins)

## System services

For proper operation, Energy Logserver requires starting the following system services:

- elasticsearch.service -
  we can run it with a command:

```bash
systemctl start elasticsearch.service
```

  we can check its status with a command:

  ```bash
systemctl status elasticsearch.service
  ```

![](/media/media/image86.PNG)

- kibana.service -
  we can run it with a command:

```bash
systemctl start kibana.service
```

  we can check its status with a command:

```bash
systemctl status kibana.service
```

![](/media/media/image87.PNG)

- logstash.service -
   we can run it with a command:

```bash
systemctl start logstash.service
```

   we can check its status with a command:

```bash
systemctl status logstash.service
```

![](/media/media/image88.PNG)

## First login

If you log in to Energy Logserver for the first time, you must
specify the Index to be searched. We have the option of entering the
name of your index, indicating a specific index from a given day, or using the asterisk () to indicate all of them matching a specific
index pattern. Therefore, to start working with the Energy Logserver application, we log in to it (by default the user:
logserver/password:logserver).

![](/media_base/image3.png)

After logging in to the application click the button "Set up index pattern" to add a new index pattern in Kibana:

![](/media/media/image3_js.png)

In the "Index pattern" field enter the name of the index or index pattern (after
confirming that the index or sets of indexes exist) and click the "Next step" button.

![](/media/media/image4.png)

In the next step, from a drop-down menu select the "Time filter field name", after which individual event (events) should be sorted. By default the *timestamp* is set, which is the time of occurrence of the event, but depending on the preferences. It may also be the time of the indexing or other selected
based on the fields indicated on the event.

![](/media/media/image4_js.png)

At any time, you can add more indexes or index patterns by going to the main tab selecting „Management" and next selecting „Index Patterns".

## Index selection

After logging into Energy Logserver, you will be going to the „Discover" tab, where you can interactively explore your data. You have access to every document in every index that matches the selected index patterns.

If you want to change the selected index, drop-down menu with the name of the current object in the left panel. Clicking on the object from the expanded list of previously created index patterns will change the searched index.

![](/media/media/image6.png)






## Discovery

### Time settings and refresh

In the upper right corner, there is a section that defines the
range of time that Energy Logserver will search in terms of conditions contained in
the search bar. The default value is the last 15 minutes.

![](/media/media/image7.png)

After clicking this selection, we can adjust the scope of the search by selecting one of the three tabs in the drop-down window:

- **Quick**: contains several predefined ranges that should be clicked.
- **Relative**: in this window specify the day from which Energy Logserver should search for data.
- **Absolute**: using two calendars we define the time range for which the search results are to be returned.

![](/media/media/image8.png)

### Fields

Energy Logserver in the body of searched events, recognize fields
that can be used to create more precision queries. The extracted
fields are visible in the left panel. They are divided into three types:
timestamp, marked on the clock icon; text, marked with the letter "t"![](/media/media/image10.png), and digital, marked with a hashtag![](/media/media/image11.png).

Pointing to them and clicking on an icon![](/media/media/image12.png), they are automatically transferred to the „Selected Fields" column and in the place of events, a table with selected columns is created regularly. In the "Selected Fields" selection you can also delete specific fields from the table by clicking![](/media/media/image13.png) on the selected element.

![](/media/media/image14_js.png)

### Filtering and syntax building

We use the query bar to search for interesting events. For example, after
entering the word „error", all events that contain the word will be
displayed, additional highlighting them with a yellow background.

![](/media/media/image15_js.png)

#### Syntax

Fields can be used similarly by defining conditions that interest us. The syntax of such queries is:

```lucene
fields_name:<fields_value>
```

Example:

```lucene
status:500
```

This query will display all events that contain the „status" fields
with a value of 500.

#### Filters

The field value does not have to be a single, specific value. For
digital fields we can specify a range in the following scheme:

```lucene
fields_name:[<range_from TO <range_to]
```

Example:

```lucene
status:[500 TO 599]
```

This query will return events with status fields that are in the
range 500 to 599.

#### Operators

The search language used in Energy Logserver allows to you use logical operators
„AND", „OR" and „NOT", which are key and necessary to build more
complex queries.

- **AND** is used to combine expressions, e.g. `error AND "access denied"`. If an event contains only one expression or the word `error` and `denied` but not the word access, then it will not be displayed.

- **OR** is used to search for the events that contain one OR other
   expression, e.g. `status:500 OR denied`. This query will display
   events that contain the word „denied" or a status field value of 500. Energy Logserver uses this operator by default, so query `„status:500" "denied"` would return the same results.

- **NOT** is used to exclude the following expression e.g. „status:[500
   TO 599] NOT status:505" will display all events that have a status field, and the value of the field is between 500 and 599 but will
   eliminate from the result events whose status field value is exactly 505.

- **The above methods** can be combined by building even
   more complex queries. Understanding how they work and joining it, is
   the basis for effective searching and full use of Energy Logserver.

   Example of query built from connected logical operations:

```lucene
status:[500 TO 599] AND („access denied" OR error) NOT status:505
```

Returns in the results all events for which the value of status fields
are in the range of 500 to 599, simultaneously contain the word
„access denied" or „error", omitting those events for which the status
field value is 505.

#### Wildcards

Wildcard searches can be run on individual terms, using `?` to replace a single character, and * to replace zero or more characters:

`qu?ck bro*`

Be aware that wildcard queries can use an enormous amount of memory and perform very badly — just think how many terms need to be queried to match the query string "a* b* c*".

#### Regular expressions

Regular expression patterns can be embedded in the query string by wrapping them in forward-slashes ("/"):

`name:/joh?n(ath[oa]n)/`

The supported regular expression syntax is explained in Regular expression syntax [https://www.elastic.co/guide/en/elasticsearch/reference/7.10/regexp-syntax.html](https://www.elastic.co/guide/en/elasticsearch/reference/7.10/regexp-syntax.html)

#### Fuzziness

You can run fuzzy queries using the ~ operator:

`quikc~ brwn~ foks~`

For these queries, the query string is normalized. If present, only certain filters from the analyzer are applied. For a list of applicable filters, see Normalizers.

The query uses the Damerau-Levenshtein distance to find all terms with a maximum of two changes, where a change is the insertion, deletion, or substitution of a single character or transposition of two adjacent characters.

The default edit distance is 2, but an edit distance of 1 should be sufficient to catch 80% of all human misspellings. It can be specified as:

`quikc~1`

#### Proximity searches

While a phrase query (e.g. "john smith") expects all of the terms in the same order, a proximity query allows the specified words to be further apart or in a different order. In the same way that fuzzy queries can specify a maximum edit distance for characters in a word, a proximity search allows us to specify a maximum edit distance of words in a phrase:

`"fox quick"~5`

The closer the text in a field is to the original order specified in the query string, the more relevant that document is considered to be. When compared to the above example query, the phrase "quick fox" would be considered more relevant than "quick brown fox".

#### Ranges

Ranges can be specified for date, numeric, or string fields. Inclusive ranges are specified with square brackets [min TO max] and exclusive ranges with curly brackets {min TO max}.

 - All days in 2012:

    `date:[2012-01-01 TO 2012-12-31]`

 - Numbers 1..5

    `count:[1 TO 5]`

 - Tags between alpha and omega, excluding alpha and omega:

    `tag:{alpha TO omega}`

 - Numbers from 10 upwards

    `count:[10 TO *]`

 - Dates before 2012

   `date:{* TO 2012-01-01}`

Curly and square brackets can be combined:

 - Numbers from 1 up to but not including 5

    `count:[1 TO 5}`

 - Ranges with one side unbounded can use the following syntax:

```bash
    age:>10
    age:>=10
    age:<10
    age:<=10
```

### Saving and deleting queries

Saving queries enables you to reload and use them in the future.

#### Save query

To save the query, click on the "Save" button under the query bar:

![](/media/media/image16.png)

This will bring up a window in which we give the query a name and then
click the button![](/media/media/image17.png).

![](/media/media/image18_js.png)

Saved queries can be opened by going to „Open" from the main menu
at the top of the page, and selecting saved search from the search list:

![](/media/media/image19.png)

Additionally, you can use "Saved Searchers Filter.." to filter the search list.

#### Open query

To open a saved query from the search list, you can click on the name of the query
you are interested in.

After clicking on the icon![](/media/media/image21.png) on the name of the saved query and choosing "Edit Query DSL", we will gain access to the advanced editing mode, so that we can change the query at a lower level.

![](/media/media/image21.png)

It is a powerful tool designed for advanced users, designed to modify
the query and the way it is presented by Energy Logserver.

#### Delete query

To delete a saved query, open it from the search list, and
then click on the button![](/media/media/image23.png) .

If you want to delete many saved queries simultaneously go to the "Management Object"
 -> "Saved Object" -> "Searches" select it in the list (the icon![](/media/media/image22.png) to the left of the query name), and then click the "Delete" button.

![](/media/media/image24_js.png)

From this level, you can also export saved queries in the same way. To
do this, you need to click on![](/media/media/image25.png) and choose the save location. The file will be saved in .json format. If you then want to import such a file to Energy Logserver, click on a button![](/media/media/image26.png), at the top of the page and select the desired file.

### Manual incident

The `Discovery` module allows you to manually create incidents that are saved in the `Incidents` tab of the `Alerts` module. Manual incidents are based on search results or filtering.
For a manual incident, you can save the following parameters:

- Rule name
- Time
- Risk
- Message

![](/media/media/image141.png)

After saving the manual incident, you can go to the Incident tab in the Alert module to perform the incident handling procedure.

![](/media/media/image142.png)

### Change the default width of columns

To improve the readability of values in Discovery columns, you can set a minimum column width. The column width setting is in the CSS style files:

```bash
/usr/share/kibana/built_assets/css/plugins/kibana/index.dark.css
/usr/share/kibana/built_assets/css/plugins/kibana/index.light.css
```

To set the minimum width for the columns, e.g. 150px, add the following entry `min-width: 150px` in the CSS style files:

```css
.kbnDocTableCell__dataField {
   min-width: 150px;
   white-space: pre-wrap; }
```

## Visualizations

Visualize enables you to create visualizations of the data
in your Energy Logserver indices. You can then build dashboards
that display related visualizations. Visualizations are based
on Energy Logserver queries. By using a series of Energy Logserver
aggregations to extract and process your data, you can create
charts that show you the trends, spikes, and dips.

### Creating visualization

#### Create

To create a visualization, go to the „Visualize" tab from the main menu.
A new page will appear where you can create or load
visualization.

#### Load

To load previously created and saved visualization, you
must select it from the list.

![](/media/media/image89.PNG)

To create a new visualization, you should choose the preferred method of data presentation.

![](/media/media/image89_js.PNG)

Next, specify whether the created visualization will be based on a new or
previously saved query. If on a new one, select the index whose
visualization should concern. If visualization is created from a saved
query, you just need to select the appropriate query from the list, or
(if there are many saved searches) search for them by name.

![](/media/media/image90.PNG)

### Visualization types

Before the data visualization will be created, first you have to
choose the presentation method from an existing list. Currently, there
are five groups of visualization types. Each of them serves different purposes.
If you want to see only the current number of products
sold, it is best to choose „Metric", which presents one value.

![](/media/media/image27_js.png)

However, if we would like to see user activity trends on pages at different hours and days, a better choice will be the „Area chart", which displays a chart with time division.

![](/media/media/image28_js.png)

The „Markdown widget" view is used to place text e.g. information
about the dashboard, explanations, and instructions on how to navigate.
Markdown language was used to format the text (the most popular use is
GitHub).
More information and instructions can be found at this link:
[https://help.github.com/categories/writing-on-github/](https://help.github.com/categories/writing-on-github/)

### Edit visualization and saving

#### Editing

Editing a saved visualization enables you to directly modify the object
definition. You can change the object title, add a description, and modify
the JSON that defines the object properties.
After selecting the index and the method of data presentation, you can enter
the editing mode. This will open a new window with an empty visualization.

![](/media/media/image29_js.png)

At the very top, there is a bar of queries that can be edited
throughout the creation of the visualization. It works in the same way
as in the "Discover" tab, which means searching the raw data, but
instead of the data being displayed, the visualization will be edited.
The following example will be based on the „Area chart". The
visualization modification panel on the left is divided into three tabs:
„Data", "Metric & Axes" and „Panel Settings".

In the „Data" tab, you can modify the elements responsible for which data
and how should be presented. In this tab, there are two sectors:
"metrics", in which we set what data should be displayed, and
„buckets" in which we specify how they should be presented.

Select the Metrics & Axes tab to change the way each metric is shown
on the chart. The data series are styled in the Metrics section, while the axes
are styled in the X and Y axis sections.

In the „Panel Settings" tab, there are settings relating mainly to visual
aesthetics. Each type of visualization has separate options.

To create the first graph in the char modification panel, in the „Data" tab we
add X-Axis in the "buckets" sections. In „Aggregation" choose „Histogram",
in „Field" should automatically be located "timestamp" and "interval":
"Auto" (if not, this is how we set it). Click on the
icon on the panel. Now our first graph should show up.

Some of the options for „Area Chart" are:

   **Smooth Lines** - is used to smooth the graph line.

![](/media/media/image30.png)

- **Current time marker** -- places a vertical line on the graph that
    determines the current time.

- **Set Y-Axis Extents** -- allows you to set minimum and maximum
    values for the Y axis, which increases the readability of the
    graphs. This is useful, if we know that the data will never be less than (the minimum value), or to indicate the goals of the company (maximum value).

- **Show Tooltip** -- option for displaying the information window
    under the mouse cursor, after pointing to the point on the graph.

   ![](/media/media/image31.png)

#### Saving

To save the visualization, click on the "Save" button under the query bar:
![](/media/media/image16.png)
give it a name and click the button![](/media/media/image17.png).

#### Load

To load the visualization, go to the "Management Object"
 -> "Saved Object" -> "Visualizations" and select it from the list. From this place,
we can also go into advanced editing mode. To view the visualization
use![](/media/media/image17_js.png) button.

## Dashboards

Dashboard is a collection of several visualizations or searches.
Depending on how it is built and what visualization it contains, it
can be designed for different teams e.g.:

- SOC - which is responsible for detecting failures or threats in
the company;
- business - which thanks to the listings can determine the popularity
of products and define the strategy of future sales and promotions;
- managers and directors - who may immediately have access to information
about the performance units or branches.

### Create

To create a dashboard from previously saved visualizations and queries,
go to the „Dashboard" tab in the main menu. When you open it, a
new page will appear.

![](/media/media/image32.png)

Clicking on the icon "Add" at the top of the page select the "Visualization" or "Saved Search"
tab.

![](/media/media/image32_js.png)

and selecting a saved query and/or visualization from the list will
add them to the dashboard. If, there are a large number of saved objects,
use the bar to search for them by name.

Elements of the dashboard can be enlarged arbitrarily (by clicking on
the right bottom corner of the object and dragging the border) and moving
(by clicking on the title bar of the object and moving it).

### Saving

You may change the time period of your dashboard.

At the upper right-hand corner, you may choose the time range of your dashboard.

![](/media/media/image147.png)

Click save and choose 'Store time with dashboard' if you are editing an existing dashboard. Otherwise, you may choose 'Save as a new dashboard' to create a new dashboard with the new time range.

To save a dashboard, click on the "Save" button at the up of the query bar
and give it a name.

### Load

To load the Dashboard, go to the "Management Object"
 -> "Saved Object" -> "Dashboard" and select it from the list. From this place,
we can also go into advanced editing mode. To view the visualization
use![](/media/media/image17_1_js.png) button.

### Sharing dashboards

The dashboard can be shared with other Energy Logserver users as well
as on any page - by placing a snippet of code. Provided that it can
retrieve information from Energy Logserver.

To do this, create a new dashboard or open the saved dashboard and click on "Share" at the top of the page. A window
will appear with the generated two URLs. The content of the first one "Embaded iframe"
is used to provide the dashboard in the page code, and the second "Link" is a link
that can be passed on to another user. There are two options for each,
the first is to shorten the length of the link, and the second is to copy to the clipboard the content of the given bar.

![](/media/media/image37.png)

### Dashboard drill down

In the discovery tab search for a message of Your interest

![](/media/media/image125.png)

----------

Save Your search

Check Your „Shared link” and copy it

![](/media/media/image127.png)
![](/media/media/image128.png)

**! ATTENTION !** Do not copy `„?_g=()”` at the end.

----------

Select Alerting module

![](/media/media/image129.png)

----------

Once Alert is created use `ANY` frame to add the following directives:

```yaml
Use_kibana4_dashboard: paste Your „shared link” here
```

`use_kibana_dashboard:` - The name of a Kibana dashboard to link to. Instead of generating a dashboard from a template, Alert can use an existing dashboard. It will set the time range on the dashboard to around the match time, upload it as a temporary dashboard, add a filter to the query_key of the alert if applicable, and put the URL to the dashboard in the alert. (Optional, string, no default).

----------

```yaml
Kibana4_start_timedelta
```

`kibana4_start_timedelta:` Defaults to 10 minutes. This option allows you to specify the start time for the generated kibana4 dashboard. This value is added in front of the event. For example,

```yaml
kibana4_start_timedelta: minutes: 2
```

----------

```yaml
Kibana4_end_timedelta
```

`kibana4_end_timedelta:` Defaults to 10 minutes. This option allows you to specify the end time for the generated kibana4 dashboard. This value is added to the back of the event. For example,

```yaml
kibana4_end_timedelta: minutes: 2
```

----------
Sample:
![](/media/media/image130.png)

----------
Search for triggered alerts in the Discovery tab.

Use alert* search pattern.

![](/media/media/image131.png)

Refresh the alert that should contain url for the dashboard.
Once available, the kibana_dashboard field can be exposed to dashboards giving You a real drill-down feature.

## Reports

### CSV Report

To export data to CSV Report click the ***Reports*** icon, you immediately go
to the first tab - ***Export Data***

In this tab, we have the opportunity to specify the source from which
we want to export. It can be an index pattern. After selecting it,
we confirm the selection with the Submit button, and a report is
created at the moment. The symbol
![](/media/media/image40.png)can refresh the list of reports and see
what its status is.

![](/media/media/image41_js.png)

We can also create a report by pointing to a specific index from the
drop-down list of indexes.

![](/media/media/image42_js.png)

We can also check which fields are to be included in the report. The
selection is confirmed by the Submit button.

![](/media/media/image43_js.png)

When the process of generating the report (Status: Completed) is
finished, we can download it (Download button) or delete it (Delete
button). The downloaded report in the form of a \*.csv file can be
opened in the browser or saved to the disk.

![](/media/media/image44_js.png)

In this tab, the downloaded data has a format that we can import into
other systems for further analysis.

### PDF Report

In the Export Dashboard tab, we can create graphic reports in PDF files.
To create such a report, just from the drop-down list of previously
created and saved Dashboards, indicate the one we are interested in,
and then confirm the selection with the Submit button. A newly
created export with the Processing status will appear on the list
under Dashboard Name.
When the processing is completed, the Status changes to Complete and it
will be possible to download the report.

![](/media/media/image45.png)

By clicking the Download button, the report is downloaded to the disk
or we can open it in the PDF file browser. There is also to option
of deleting the report with the Delete button.

![](/media/media/image46.png)

Below is an example report from the Dashboard template generated and
downloaded as a PDF file.

![](/media/media/image47.png)

### PDF report from the table visualization

Data from a table visualization can be exported as a PDF report.

To export a table visualization data, follow these steps:

1. Go to the 'Report' module and then to the 'Report Export' tab,
2. Add the new task name in the 'Task Name' field,
3. Toggle the switch 'Enable Data Table Export':

   ![](/media/media/image215.png)

4. Select the table from the 'Table Visualization' list,
5. Select the time range for which the report is to be prepared,
6. You can select a logo from the 'Logo' list,
7. You can add a report title using the 'Title' field,
8. You can add a report comment using the 'Comments' field,
9. Select the 'Submit' button to start creating the report,
10. You can follow the progress in the 'Task List' tab,
11. After completing the task, the status will change to 'Complete' and you can download the PDF report via 'Action' -> 'Download':

    ![](/media/media/image216.png)

### Scheduler Report (Schedule Export Dashboard) ##

In the Report selection, we have the option of setting the Scheduler
which from the Dashboard template can generate a report at time intervals.
To do this, go to the Schedule Export Dashboard tab.

![](/media/media/image48_js.png)

Scheduler Report (Schedule Export Dashboard)

In this tab mark the saved Dashboard.

![](/media/media/image49_js.png)

*Note: The default time period of the dashboard is last 15 minutes.*

*Please refer to **Discovery > Time settings and refresh** to change the time period of your dashboard.*

In the Email Topic field, enter the Message title, in the Email field
enter the email address to which the report should be sent. From the drop-down list choose at what frequency you want the report to be generated and sent.
The action configured in this way is confirmed with the Submit button.

![](/media/media/image50_js.png)

The defined action goes to the list and will generate a report to the
e-mail address, with the cycle we set, until we cannot cancel it with
the Cancel button.

![](/media/media/image51_js.png)

## User roles and object management

### Users, roles, and settings

Energy Logserver allows to you manage users and permission for
indexes and methods used by them. To do this click the "Config" button from the main menu bar.

![](/media/media/image38_js.png)

A new window will appear with three main tabs: „User Management",
„Settings" and „License Info".

From the „User Management" level we have access to the following
possibilities: Creating a user in „Create User", displaying users in
„User List", creating new roles in „Create Role" and displaying
existing roles in „List Role".

### Creating a User (Create User)

#### Creating user

To create a new user click on the Config icon and you immediately
enter the administration panel, where the first tab is to create
a new user (**Create User**).

![](/media/media/image52_js.png)

In the wizard that opens, we enter a unique username (Username field), and password for the user (field Password) and assign a role (field Role). In this field, we have the option of assigning more than one role.
Until we select a role in the Roles field, the Default Role field
remains empty. When we mark several roles, these roles appear in
the Default Role field. In this field, we have the opportunity to
indicate which role for a new user will be the default role with
which the user will be associated in the first place when logging in.
The default role field has one more important task - it binds all
users with the field/role set in one group. When one of the users
of this group creates the Visualization or the Dashboard it will be available
to other users from this role(group). Creating the account is confirmed
with the Submit button.

### User's modification and deletion, (User List)

Once we have created users, we can display their list. We do it in the next tab (**User List**).

![](/media/media/image53_js.png)

In this view, we get a list of user accounts with assigned roles and we
have two buttons: Delete and Update. The first of these is the ability to delete a user account. Under the Update button is a drop-down menu in
which we can change the previous password to a new one (New password),
change the password (Re-enter New Password), change the previously
assigned roles (Roles), to other (we can take the role assigned
earlier and give a new one, extend user permissions with new roles).
The introduced changes are confirmed with the Submit button.

We can also see the current user settings and clicking the Update button
collapses the previously expanded menu.

### Create, modify, and delete a role (Create Role), (Role List)

In the Create Role tab, we can define a new role with permissions that
we assign to a pattern or several index patterns.

![](/media/media/image54_js.png)

For example, we use the syslog2\* index pattern. We give this name
in the Paths field. We can provide one or more index patterns, their
names should be separated by a comma. In the next Methods field, we
select one or many methods that will be assigned to the role. Available
methods:

- PUT - sends data to the server
- POST - sends a request to the server for a change
- DELETE - deletes the index/document
- GET - gets information about the index /document
- HEAD - is used to check if the index /document exists

In the role field, enter the unique name of the role. We confirm the addition of a new role with the Submit button. To see if a new role has been added,
go to the net Role List tab.

![](/media/media/image55_js.png)

As we can see, the new role has been added to the list. With the
Delete button we have the option of deleting it, while under the
Update button, we have a drop-down menu thanks to which we can add or
remove an index pattern and add or remove a method. When we want to
confirm the changes, we choose the Submit button. Pressing the Update
button again will close the menu.

Fresh installation of the application has sewn solid roles, which grant users special rights:

- admin - this role gives unlimited permissions to administer/manage
the application
- alert - a role for users who want to see the Alert module
- kibana - a role for users who want to see the application GUI
- Intelligence - a role for users who are to see the Intelligence moduleObject access permissions (Objects permissions)

In the User Manager tab, we can parameterize access to the newly
created role as well as existing roles. In this tab, we can indicate
to which object in the application the role has access.

Example:

In the Role List tab, we have a role called **sys2**, it refers
to all index patterns beginning with syslog\* and the methods get,
post, delete, put and head are assigned.

![](/media/media/image56_js.png)

When we go to the Object permission tab, we have the option to choose
the sys2 role in the drop-down list choose a role:

![](/media/media/image57_js.png)

After selecting, we can see that we already have access to the objects:
two index patterns syslog2\* and Energy Logserver-\* and on a dashboard Windows Events.
There are also appropriate read or update permissions.

![](/media/media/image58_js.png)

From the list, we have the opportunity to choose another object that we
can add to the role. We have the ability to quickly find this object
in the search engine (Find) and narrow the object class in
the drop-down field "Select object type". The object type is associated with saved previous documents in the sections Dashboard, Index pattern,
Search, and Visualization.
By buttons, ![](/media/media/image59.png) we have the ability to add or remove or
object, and the Save button to save the selection.

### Default user and passwords

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-tysj{text-align:left;vertical-align:top}
.tg .tg-qahb{border-color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-i91a{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-ie02{border-color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-qahb">Address</th>
    <th class="tg-qahb">User</th>
    <th class="tg-qahb">Password</th>
    <th class="tg-qahb">Role</th>
    <th class="tg-qahb">Description</th>
    <th class="tg-qahb">Usage</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-i91a"><a href="https://localhost:5601/" target="_blank" rel="noopener noreferrer"><span style="text-decoration:none">https://localhost:5601</span></a></td>
    <td class="tg-ie02">logserver</td>
    <td class="tg-ie02">logserver</td>
    <td class="tg-ie02">logserver</td>
    <td class="tg-ie02">A built-in superuser account</td>
    <td class="tg-ie02"></td>
  </tr>
  <tr>
    <td class="tg-ie02"></td>
    <td class="tg-ie02">alert</td>
    <td class="tg-ie02">alert</td>
    <td class="tg-ie02">alert</td>
    <td class="tg-ie02">A built-in account for the Alert module</td>
    <td class="tg-ie02"></td>
  </tr>
  <tr>
    <td class="tg-ie02"></td>
    <td class="tg-ie02">intelligence</td>
    <td class="tg-ie02">intelligece</td>
    <td class="tg-ie02">intelligence</td>
    <td class="tg-ie02">A built-in account for the Intelligence module</td>
    <td class="tg-ie02">authorizing communication with elasticsearch server</td>
  </tr>
  <tr>
    <td class="tg-ie02"></td>
    <td class="tg-ie02">scheduler</td>
    <td class="tg-ie02">scheduler</td>
    <td class="tg-ie02">scheduler</td>
    <td class="tg-ie02">A built-in account for the Scheduler module</td>
    <td class="tg-ie02"></td>
  </tr>
  <tr>
    <td class="tg-ie02"></td>
    <td class="tg-ie02">logstash</td>
    <td class="tg-ie02">logstash</td>
    <td class="tg-ie02">logstash</td>
    <td class="tg-ie02">A built-in account for authorized comuunication form Logstash</td>
    <td class="tg-ie02"></td>
  </tr>
  <tr>
    <td class="tg-ie02"></td>
    <td class="tg-ie02">cerebro</td>
    <td class="tg-ie02"></td>
    <td class="tg-ie02">system acconut only</td>
    <td class="tg-ie02">A built-in account for authorized comuunication from Cerebro moudule</td>
    <td class="tg-ie02"></td>
  </tr>
</tbody>
</table>

### Changing the password for the system account

1. Account **Logserver**

    - Update */etc/kibana/kibana.yml*Update password in _/_opt/license-service/license-service.conf* file:

    ```bash
    elasticsearch_connection:
    hosts: ["10.4.3.185:9200"]

    username: logserver
    password: "new_logserver_password"

    https: true
    ```

    - Update the password in the *curator* configuration file: */usr/share/kibana/curator/curator.yml*

    ```yml
    http_auth: logserver:"new_logserver_password
    ```

2. Account **Intelligence**

   - Update */opt/ai/bin/conf.cfg*

     ```bash
     vi /opt/ai/bin/conf.cfg
     password=new_intelligence_password
     ```

3. Account **Alert**

   - Update file */opt/alert/config.yaml*

     ```yaml
     vi /opt/alert/config.yaml
     es_password: alert
     ```

4. Account **Scheduler**

   - Update */etc/kibana/kibana.yml*

     ```yml
     vi /etc/kibana/kibana.yml
     elastscheduler.password: "new_scheduler_password"
     ```

5. Account **Logstash**

   - Update the Logstash pipeline configuration files (*.conf) in the output sections:

     ```bash
     vi /etc/logstash/conf.d/*/*.conf
     output {
      elasticsearch {
        hosts => ["localhost:9200"]
        index => "syslog-%{+YYYY.MM}"
        user => "logstash"
        password => "new_password"
      }
     }
     ```

6. Account **License**

   - Update file **/opt/license-service/license-service.conf**

     ```bash
     elasticsearch_connection:
       hosts: ["127.0.0.1:9200"]

       username: license
       password: "new_license_password"
     ```

### Module Access

You can restrict access to specific modules for a user role. For example: the user can only use the Discovery, Alert, and Cerebro modules, the other modules should be inaccessible to the user.

You can do this by editing the roles in the `Role List` and selecting the application from the `Apps` list. After saving, the user has access only to specific modules.

![](/media/media/image165.png)

### Manage API keys

The system allows you to manage, create, and delete API access keys from the level of the GUI management application.

Examples of implementation:

1. From the main menu select the "Dev Tools" button:

   ![](/media/media/image213.png)

2. List of active keys:

   ![](/media/media/image209.png)

3. Details of a single key:

   ![](/media/media/image210.png)

4. Create a new key:

   ![](/media/media/image211.png)

5. Deleting the key:

   ![](/media/media/image212.png)

### Separate data from one index to different user groups

We can Separate data from one index to different user groups using aliases. For example, in one index we have several tags:

![](https://user-images.githubusercontent.com/42172770/209846991-ca27566d-1a57-4d45-b5ae-24ce24ed5c84.png)

To separate the data, you must first set up an alias on the appropriate tag.

![](https://user-images.githubusercontent.com/42172770/209850716-104762f8-4cb6-45dc-b651-287eacbf92d8.png)

Then assume a pattern index on the above alias.
Finally, we can assign the appropriate role to the new index pattern.

![](https://user-images.githubusercontent.com/42172770/209851010-2dc583de-889b-4baf-bdc9-21cbaba820eb.png)

## Settings

### General Settings

The Settings tab is used to set the audit on different activities or events
and consists of several fields:

![](/media/media/image60_js.png)

- **Time Out in minutes** field - this field defines the time after how
    many minutes the application will automatically log you off
- **Delete Application Tokens (in days)** - in this field, we specify
    after what time the data from the audit should be deleted
- **Delete Audit Data (in days)** field - in this field, we specify after
    what time the data from the audit should be deleted
- The next fields are checkboxes in which we specify what kind of events
  are to be logged (saved) in the audit index. The events that can be
  monitored are: logging (Login), logging out (Logout), creating a
  user (Create User), deleting a user (Delete User), updating user
  (Update User), creating a role (Create Role), deleting a role
  (Delete Role), update of the role (Update Role), start of export
  (Export Start), delete of export (Export Delete), queries (Queries),
  result of the query (Content), if attempt was made to perform a
  series of operation (Bulk)
- **Delete Exported CSVs (in days)** field - in this field, we specify
    after which time exported files with CSV extension have to be removed
- **Delete Exported PDFs (in days)** field - in this field, we specify
    after which time exported files with PDF extension have to be removed

Each field is assigned the "Submit" button thanks to which we can confirm the changes.

### License (License Info)

The License Information tab consists of several non-editable information fields.

Also, if you are logged in as an administrator you will be able to upload new license from here.

![](/media/media/image61_js.png)

These fields contain information:

- Company - who owns the license, in this case, Foo Bar.
- Issued on - license creation date
- Expiration date - when the license will expire
- Days left - how many days left before it will expire
- Data nodes in cluster - how many nodes we can put in one cluster - in this case, 10
- SIEM Plan enabled - is SIEM Plan covered by the license
- Network Probes - count of NetworkProbes covered by the license
- No of documents - license can be limited by docs count
- Indices - license can be limited by index pattern names
- Version - version of the product

#### Renew license

To change the Energy Logserver license files on a running system, use the "Upload new license" option at the top of the "License" tab.

1. Select the provided license files, e.g.: es_123.info, es_123.license.
2. Click upload.
3. Files will be uploaded and verified. New license information will appear.
4. Verify new license information and click "Submit" when ready.
5. It will install itself in the cluster - no need to manually put it on all nodes.

### Special accounts

At the first installation of the Energy Logserver application, apart
from the administrative account (logserver), special applications are
created in the application: alert, intelligence, and scheduler.

![](/media/media/image62_js.png)

- **Alert Account** - this account is connected to the Alert Module
which is designed to track events written to the index for the
previously defined parameters. If these are met the information
action is started (more on the action in the Alert section)
- **Intelligence Account** - this account is related to the module
of artificial intelligence which is designed to track events and learn
the network based on previously defined rules artificial intelligence
based on one of the available algorithms (more on operation in the
Intelligence chapter)
- **Scheduler Account** - the scheduler module is associated with this
account, which corresponds to, among others for generating reports

## Backup/Restore

### Backing up

The backup bash script is located on the hosts with Elasticsearch in the location: ```/usr/share/elasticsearch/utils/configuration-backup.sh```.

The script is responsible for backing up the basic data in the Logserver system (these data are the system indexes found in Elasticsearch of those starting with a dot  '.'  in the name),  the configuration of the entire cluster, the set of templates used in the cluster and all the components.

These components include the Logstash configuration located in ```/etc/logstash``` and the Kibana configuration located in ```/etc/kibana```.

All data is stored in the ```/tmp``` folder and then packaged using the ```/usr/bin/tar``` utility to ```tar.gz``` format with the exact date and time of execution in the target location, then the files from ```/tmp``` are deleted.

crontab
It is recommended to configure ```crontab```.

- Before executing the following commands, you need to create a crontab file, set the path to backup, and direct them there.

In the below example, the task was configured on hosts with the Elasticsearch module on the root.

```bash
# crontab -l #Printing the Crontab file for the currently logged in user
0 1 * * * /bin/bash /usr/share/elasticsearch/utils/configuration-backup.sh
```

- The client-node host saves the backup in the /archive/configuration-backup/ folder.
- Receiver-node hosts save the backup in the /root/backup/ folder.

### Restoration from backup

To restore the data, extract the contents of the created archive, e.g.

```bash
# tar -xzf /archive/configuration-backup/backup_name-000000-00000.tar.gz -C /tmp/restore
```

Then display the contents and select the files to restore (this will look similar to the following):

```bash
# ls -al /tmp/restore/00000-11111/
drwxr-xr-x 2 root root    11111 01-08 10:29 .
drwxr-xr-x 3 root root     2222 01-08 10:41 ..
-rw-r--r-- 1 root root  3333333 01-08 10:28 .file1.json
-rw-r--r-- 1 root root     4444 01-08 10:28 .file_number2.json
-rw-r--r-- 1 root root     5555 01-08 10:29 .file3.json
-rw-r--r-- 1 root root      666 01-08 10:29 .file4.json
-rw-r--r-- 1 root root     7777 01-08 10:29 .file5.json
-rw-r--r-- 1 root root       87 01-08 10:29 .file6.json
-rw-r--r-- 1 root root        1 01-08 10:29  file6.json
-rw-r--r-- 1 root root       11 01-08 10:29 .file7.json
-rw-r--r-- 1 root root     1234 01-08 10:29  file8.tar.gz
-rw-r--r-- 1 root root     0000 01-08 10:29 .file9.json
```

To restore any of the system indexes, e.g. ```.security```, execute the commands:

```bash
# /usr/share/kibana/elasticdump/elasticdump  --output="http://logserver:password@127.0.0.1:9200/.kibana" --input="/root/restore/20210108-102848/.security.json" –type=data
# /usr/share/kibana/elasticdump/elasticdump  --output="http://logserver:password@127.0.0.1:9200/.kibana" --input="/root/restore/20210108-102848/.security_mapping.json" --type=mapping
```

To restore any of the configurations e.g. ```kibana/logstash/elastic/wazuh```, follow the steps below:

```bash
# systemctl stop kibana
# tar -xvf /tmp/restore/20210108-102848/kibana_conf.tar.gz -C / --overwrite
```

```bash
# systemctl start kibana
```

To restore any of the templates, perform the following steps for each template:

- Select from the ```templates.json``` file the template you are interested in, omitting its name
- Move it to a new ```json``` file, e.g. ```test.json```
- Load by specifying the name of the target template in the link

```bash
# curl -s -XPUT -H 'Content-Type: application/json' -u logserver '127.0.0.1:9200/_template/test -d@/root/restore/20210108-102848/test.json
```

To restore the cluster settings, execute the following command:

```bash
# curl -s -XPUT -H 'Content-Type: application/json' -u logserver '127.0.0.1:9200/_cluster/settings' -d@/root/restore/20210108-102848/cluster_settings.json
```
## Audit actions

### AUTHORIZATION PLUGIN

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>

<table class="tg">
<thead>
<tr data-sourcepos="3:1-3:37">
<th data-sourcepos="3:2-3:14">ACTION TYPE</th>
<th data-sourcepos="3:16-3:21">PATH</th>
<th data-sourcepos="3:23-3:36">FROM REQUEST</th>
</tr>
</thead>
<tbody>
<tr data-sourcepos="5:1-5:78">
<td data-sourcepos="5:2-5:32">USER_[CREATE|UPDATE|DELETE]</td>
<td data-sourcepos="5:34-5:54">_logserver/accounts</td>
<td data-sourcepos="5:56-5:77">whole body with diff</td>
</tr>
<tr data-sourcepos="6:1-6:81">
<td data-sourcepos="6:2-6:32">ROLE_[CREATE|UPDATE|DELETE]</td>
<td data-sourcepos="6:34-6:57">_logserver/constraints</td>
<td data-sourcepos="6:59-6:80">whole body with diff</td>
</tr>
<tr data-sourcepos="7:1-7:40">
<td data-sourcepos="7:2-7:7">BULK</td>
<td data-sourcepos="7:9-7:15">_bulk</td>
<td data-sourcepos="7:17-7:39">whole body if enabled</td>
</tr>
<tr data-sourcepos="8:1-8:38">
<td data-sourcepos="8:2-8:8">QUERY</td>
<td data-sourcepos="8:10-8:13">*</td>
<td data-sourcepos="8:15-8:37">whole body if enabled</td>
</tr>
</tr>
<tr data-sourcepos="7:1-7:40">
<td data-sourcepos="7:2-7:7">OBJECTS</td>
<td data-sourcepos="7:9-7:15">.kibana</td>
<td data-sourcepos="7:17-7:39">whole body if enabled</td>
</tr>
</tbody>
</table>

<h5 dir="auto" data-sourcepos="10:1-10:33">Paths excluded from auditing</h5>

<ul dir="auto" data-sourcepos="12:1-17:0">
<li data-sourcepos="12:1-12:5"><code data-sourcepos="12:4-12:4">/</code></li>
<li data-sourcepos="13:1-13:12"><code data-sourcepos="13:4-13:11">/_nodes*</code></li>
<li data-sourcepos="14:1-14:12"><code data-sourcepos="14:4-14:11">/_stats*</code></li>
<li data-sourcepos="16:1-17:0"><code data-sourcepos="16:4-16:16">/.auth</code></li>
<li data-sourcepos="16:1-17:0"><code data-sourcepos="16:4-16:16">/.authconfig*</code></li>
</ul>

### CONFIG

<table class="tg">
<thead>
<tr data-sourcepos="20:1-20:37">
<th data-sourcepos="20:2-20:14">ACTION TYPE</th>
<th data-sourcepos="20:16-20:21">PATH</th>
<th data-sourcepos="20:23-20:36">FROM REQUEST</th>
</tr>
</thead>
<tbody>
<tr data-sourcepos="22:1-22:66">
<td data-sourcepos="22:2-22:17">TOKENS DELETED</td>
<td data-sourcepos="22:19-22:57">post:/api/setting/job/deletealltokens</td>
<td data-sourcepos="22:59-22:65">empty</td>
</tr>
<tr data-sourcepos="23:1-23:71">
<td data-sourcepos="23:2-23:23">SETTINGS TOKENDELETE</td>
<td data-sourcepos="23:25-23:54">put:/api/setting/tokendelete</td>
<td data-sourcepos="23:56-23:70">payload.value</td>
</tr>
<tr data-sourcepos="24:1-24:59">
<td data-sourcepos="24:2-24:19">SETTINGS TIMEOUT</td>
<td data-sourcepos="24:21-24:42">put:/api/setting/ttl</td>
<td data-sourcepos="24:44-24:58">payload.value</td>
</tr>
<tr data-sourcepos="25:1-25:79">
<td data-sourcepos="25:2-25:27">SETTINGS AUDIT SELECTION</td>
<td data-sourcepos="25:29-25:61">put:/api/setting/auditselection</td>
<td data-sourcepos="25:63-25:78">payload.value1</td>
</tr>
<tr data-sourcepos="26:1-26:72">
<td data-sourcepos="26:2-26:27">SETTINGS AUDIT EXCLUSION</td>
<td data-sourcepos="26:29-26:61">put:/api/setting/auditexclusion</td>
<td data-sourcepos="26:63-26:71">payload</td>
</tr>
<tr data-sourcepos="27:1-27:90">
<td data-sourcepos="27:2-27:32">SETTINGS ALERT EXCLUDE FIELDS</td>
<td data-sourcepos="27:34-27:72">put:/api/setting/alert_exclude_fields</td>
<td data-sourcepos="27:74-27:89">payload.value1</td>
</tr>
<tr data-sourcepos="28:1-28:82">
<td data-sourcepos="28:2-28:24">SETTINGS AUTH DOMAINS</td>
<td data-sourcepos="28:26-28:56">put:/api/setting/auth_domains</td>
<td data-sourcepos="28:58-28:81">payload.default_domain</td>
</tr>
</tbody>
</table>


### REPORTS

<table class="tg">
<thead>
<tr data-sourcepos="32:1-32:37">
<th data-sourcepos="32:2-32:14">ACTION TYPE</th>
<th data-sourcepos="32:16-32:21">PATH</th>
<th data-sourcepos="32:23-32:36">FROM REQUEST</th>
</tr>
</thead>
<tbody>
<tr data-sourcepos="34:1-34:74">
<td data-sourcepos="34:2-34:22">DATA EXPORT CREATED</td>
<td data-sourcepos="34:24-34:54">post:/api/reports/data/export</td>
<td data-sourcepos="34:56-34:73">payload.taskName</td>
</tr>
<tr data-sourcepos="35:1-35:84">
<td data-sourcepos="35:2-35:29">MANUAL DATA EXPORT CREATED</td>
<td data-sourcepos="35:31-35:68">post:/api/reports/data/export_manual</td>
<td data-sourcepos="35:70-35:83">payload.user</td>
</tr>
<tr data-sourcepos="36:1-36:72">
<td data-sourcepos="36:2-36:21">DATA EXPORT EDITED</td>
<td data-sourcepos="36:23-36:52">put:/api/reports/data/export</td>
<td data-sourcepos="36:54-36:71">payload.taskName</td>
</tr>
<tr data-sourcepos="37:1-37:91">
<td data-sourcepos="37:2-37:34">DASHBOARD REPORT EXPORT CREATED</td>
<td data-sourcepos="37:36-37:71">post:/api/reports/dashboard/export</td>
<td data-sourcepos="37:73-37:90">payload.taskName</td>
</tr>
<tr data-sourcepos="38:1-38:89">
<td data-sourcepos="38:2-38:33">DASHBOARD REPORT EXPORT EDITED</td>
<td data-sourcepos="38:35-38:69">put:/api/reports/dashboard/export</td>
<td data-sourcepos="38:71-38:88">payload.taskName</td>
</tr>
<tr data-sourcepos="39:1-39:88">
<td data-sourcepos="39:2-39:35">DATA TABLE REPORT EXPORT CREATED</td>
<td data-sourcepos="39:37-39:68">post:/api/reports/table/export</td>
<td data-sourcepos="39:70-39:87">payload.taskName</td>
</tr>
<tr data-sourcepos="40:1-40:86">
<td data-sourcepos="40:2-40:34">DATA TABLE REPORT EXPORT EDITED</td>
<td data-sourcepos="40:36-40:66">put:/api/reports/table/export</td>
<td data-sourcepos="40:68-40:85">payload.taskName</td>
</tr>
<tr data-sourcepos="41:1-41:75">
<td data-sourcepos="41:2-41:25">SCHEDULED TASK ENABLED</td>
<td data-sourcepos="41:27-41:61">put:/api/reports/scheduler/enable</td>
<td data-sourcepos="41:63-41:74">payload.id</td>
</tr>
<tr data-sourcepos="42:1-42:77">
<td data-sourcepos="42:2-42:26">SCHEDULED TASK DISABLED</td>
<td data-sourcepos="42:28-42:63">put:/api/reports/scheduler/disable</td>
<td data-sourcepos="42:65-42:76">payload.id</td>
</tr>
<tr data-sourcepos="43:1-43:54">
<td data-sourcepos="43:2-43:16">TASKS DELETED</td>
<td data-sourcepos="43:18-43:38">delete:/api/reports</td>
<td data-sourcepos="43:40-43:53">payload.objs</td>
</tr>
<tr data-sourcepos="44:1-44:76">
<td data-sourcepos="44:2-44:22">SETTINGS PDF_EXPIRY</td>
<td data-sourcepos="44:24-44:55">post:/api/reports/settings/pdf</td>
<td data-sourcepos="44:57-44:75">payload.pdfExpiry</td>
</tr>
<tr data-sourcepos="45:1-45:76">
<td data-sourcepos="45:2-45:22">SETTINGS CSV_EXPIRY</td>
<td data-sourcepos="45:24-45:55">post:/api/reports/settings/csv</td>
<td data-sourcepos="45:57-45:75">payload.csvExpiry</td>
</tr>
<tr data-sourcepos="46:1-46:76">
<td data-sourcepos="46:2-46:21">REPORT UPLOAD LOGO</td>
<td data-sourcepos="46:23-46:56">post:/api/reports/settings/logos</td>
<td data-sourcepos="46:58-46:75">payload.fileName</td>
</tr>
<tr data-sourcepos="47:1-47:62">
<td data-sourcepos="47:2-47:20">ONGOING TASK STOP</td>
<td data-sourcepos="47:22-47:45">post:/api/reports/stop</td>
<td data-sourcepos="47:47-47:61">params.taskId</td>
</tr>
</tbody>
</table>


### INDEX MANAGEMENT

<table class="tg">
<thead>
<tr data-sourcepos="51:1-51:37">
<th data-sourcepos="51:2-51:14">ACTION TYPE</th>
<th data-sourcepos="51:16-51:21">PATH</th>
<th data-sourcepos="51:23-51:36">FROM REQUEST</th>
</tr>
</thead>
<tbody>
<tr data-sourcepos="53:1-53:69">
<td data-sourcepos="53:2-53:17">ACTION CREATED</td>
<td data-sourcepos="53:19-53:53">post:/api/index_management/action</td>
<td data-sourcepos="53:55-53:68">payload.name</td>
</tr>
<tr data-sourcepos="54:1-54:67">
<td data-sourcepos="54:2-54:16">ACTION EDITED</td>
<td data-sourcepos="54:18-54:51">put:/api/index_management/action</td>
<td data-sourcepos="54:53-54:66">payload.name</td>
</tr>
<tr data-sourcepos="55:1-55:80">
<td data-sourcepos="55:2-55:19">ACTION START NOW</td>
<td data-sourcepos="55:21-55:66">post:/api/index_management/action/run_action</td>
<td data-sourcepos="55:68-55:79">payload.id</td>
</tr>
<tr data-sourcepos="56:1-56:70">
<td data-sourcepos="56:2-56:17">ACTION DELETED</td>
<td data-sourcepos="56:19-56:55">delete:/api/index_management/action</td>
<td data-sourcepos="56:57-56:69">params.name</td>
</tr>
<tr data-sourcepos="57:1-57:109">
<td data-sourcepos="57:2-57:34">SYSTEM INDEX ROLLOVER CONFIGURE</td>
<td data-sourcepos="57:36-57:89">post:/api/index_management/settings/rollover/.agents</td>
<td data-sourcepos="57:91-57:108">params.indexName</td>
</tr>
<tr data-sourcepos="58:1-58:108">
<td data-sourcepos="58:2-58:34">SYSTEM INDEX ROLLOVER CONFIGURE</td>
<td data-sourcepos="58:36-58:88">post:/api/index_management/settings/rollover/alerts</td>
<td data-sourcepos="58:90-58:107">params.indexName</td>
</tr>
<tr data-sourcepos="59:1-59:107">
<td data-sourcepos="59:2-59:34">SYSTEM INDEX ROLLOVER CONFIGURE</td>
<td data-sourcepos="59:36-59:87">post:/api/index_management/settings/rollover/audit</td>
<td data-sourcepos="59:89-59:106">params.indexName</td>
</tr>
</tbody>
</table>


### ARCHIVE

<table class="tg">
<thead>
<tr data-sourcepos="63:1-63:37">
<th data-sourcepos="63:2-63:14">ACTION TYPE</th>
<th data-sourcepos="63:16-63:21">PATH</th>
<th data-sourcepos="63:23-63:36">FROM REQUEST</th>
</tr>
</thead>
<tbody>
<tr data-sourcepos="65:1-65:71">
<td data-sourcepos="65:2-65:24">ARCHIVAL TASK CREATED</td>
<td data-sourcepos="65:26-65:57">post:/api/archive/archive_task</td>
<td data-sourcepos="65:59-65:70">payload.id</td>
</tr>
<tr data-sourcepos="66:1-66:73">
<td data-sourcepos="66:2-66:24">ARCHIVAL TASK UPDATED</td>
<td data-sourcepos="66:26-66:56">put:/api/archive/archive_task</td>
<td data-sourcepos="66:58-66:72">params.taskId</td>
</tr>
<tr data-sourcepos="67:1-67:80">
<td data-sourcepos="67:2-67:26">ARCHIVAL TASK START NOW</td>
<td data-sourcepos="67:28-67:63">post:/api/archive/archive_task/run</td>
<td data-sourcepos="67:65-67:79">params.taskId</td>
</tr>
<tr data-sourcepos="68:1-68:60">
<td data-sourcepos="68:2-68:16">TASKS DELETED</td>
<td data-sourcepos="68:18-68:44">delete:/api/archive/tasks</td>
<td data-sourcepos="68:46-68:59">payload.objs</td>
</tr>
<tr data-sourcepos="69:1-69:80">
<td data-sourcepos="69:2-69:22">SEARCH TASK CREATED</td>
<td data-sourcepos="69:24-69:58">post:/api/archive/search_task/run</td>
<td data-sourcepos="69:60-69:79">payload.searchtext</td>
</tr>
<tr data-sourcepos="70:1-70:88">
<td data-sourcepos="70:2-70:23">RESTORE TASK CREATED</td>
<td data-sourcepos="70:25-70:60">post:/api/archive/restore_task/run</td>
<td data-sourcepos="70:62-70:87">payload.destinationIndex</td>
</tr>
</tbody>
</table>


### ALERTS

<table class="tg">
<thead>
<tr data-sourcepos="74:1-74:37">
<th data-sourcepos="74:2-74:14">ACTION TYPE</th>
<th data-sourcepos="74:16-74:21">PATH</th>
<th data-sourcepos="74:23-74:36">FROM REQUEST</th>
</tr>
</thead>
<tbody>
<tr data-sourcepos="76:1-76:75">
<td data-sourcepos="76:2-76:21">ALERT RULE CREATED</td>
<td data-sourcepos="76:23-76:50">post:/api/alerts/alertrule</td>
<td data-sourcepos="76:52-76:74">payload.alertrulename</td>
</tr>
<tr data-sourcepos="77:1-77:73">
<td data-sourcepos="77:2-77:20">ALERT RULE EDITED</td>
<td data-sourcepos="77:22-77:48">put:/api/alerts/alertrule</td>
<td data-sourcepos="77:50-77:72">payload.alertrulename</td>
</tr>
<tr data-sourcepos="78:1-78:73">
<td data-sourcepos="78:2-78:22">ALERT RULE RAN ONCE</td>
<td data-sourcepos="78:24-78:59">post:/api/alerts/alertrule/runonce</td>
<td data-sourcepos="78:61-78:72">payload.id</td>
</tr>
<tr data-sourcepos="79:1-79:65">
<td data-sourcepos="79:2-79:21">ALERT RULES SAVED</td>
<td data-sourcepos="79:23-79:52">post:/api/alerts/alertrule/saverules</td>
<td data-sourcepos="79:54-79:64">empty</td>
</tr>
<tr data-sourcepos="79:1-79:65">
<td data-sourcepos="79:2-79:21">ALERT RULE DELETED</td>
<td data-sourcepos="79:23-79:52">delete:/api/alerts/alertrule</td>
<td data-sourcepos="79:54-79:64">params.id</td>
</tr>
<tr data-sourcepos="80:1-80:57">
<td data-sourcepos="80:2-80:22">ALERT GROUP CREATED</td>
<td data-sourcepos="80:24-80:48">post:/api/alerts/groups</td>
<td data-sourcepos="80:50-80:56">empty</td>
</tr>
<tr data-sourcepos="81:1-81:65">
<td data-sourcepos="81:2-81:22">ALERT GROUP RENAMED</td>
<td data-sourcepos="81:24-81:47">put:/api/alerts/groups</td>
<td data-sourcepos="81:49-81:64">payload.rename</td>
</tr>
<tr data-sourcepos="82:1-82:71">
<td data-sourcepos="82:2-82:22">ALERT GROUP DELETED</td>
<td data-sourcepos="82:24-82:50">delete:/api/alerts/groups</td>
<td data-sourcepos="82:52-82:70">payload.groupName</td>
</tr>
<tr data-sourcepos="83:1-83:63">
<td data-sourcepos="83:2-83:23">ALERT ADDED TO GROUP</td>
<td data-sourcepos="83:25-83:54">put:/api/alerts/updatealerts</td>
<td data-sourcepos="83:56-83:62">empty</td>
</tr>
<tr data-sourcepos="84:1-84:85">
<td data-sourcepos="84:2-84:22">ALERT CHANGED ROLES</td>
<td data-sourcepos="84:24-84:63">put:/api/alerts/alertrules/changeroles</td>
<td data-sourcepos="84:65-84:84">payload.alertsList</td>
</tr>
<tr data-sourcepos="85:1-85:101">
<td data-sourcepos="85:2-85:32">ALERT MANUAL INCIDENT CREATED</td>
<td data-sourcepos="85:34-85:75">post:/api/alerts/incidents/create_manual</td>
<td data-sourcepos="85:77-85:100">payload.data.rule_name</td>
</tr>
<tr data-sourcepos="86:1-86:90">
<td data-sourcepos="86:2-86:33">ALERT RULE [enabled|disabled]</td>
<td data-sourcepos="86:35-86:68">put:/api/alerts/alertrule/switch</td>
<td data-sourcepos="86:70-86:89">payload.alertsList</td>
</tr>
<tr data-sourcepos="87:1-87:90">
<td data-sourcepos="87:2-87:29">ALERT RULE INCIDENT EDITED</td>
<td data-sourcepos="87:31-87:57">put:/api/alerts/incidents</td>
<td data-sourcepos="87:59-87:89">payload.id + <code data-sourcepos="87:74-87:87">dynamic values</code>
</td>
</tr>
</tbody>
</table>


### SYNC

<table class="tg">
<thead>
<tr data-sourcepos="91:1-91:37">
<th data-sourcepos="91:2-91:14">ACTION TYPE</th>
<th data-sourcepos="91:16-91:21">PATH</th>
<th data-sourcepos="91:23-91:36">FROM REQUEST</th>
</tr>
</thead>
<tbody>
<tr data-sourcepos="93:1-93:71">
<td data-sourcepos="93:2-93:23">SYNC PROFILE CREATED</td>
<td data-sourcepos="93:25-93:55">post:/api/sync/clusterprofile</td>
<td data-sourcepos="93:57-93:70">payload.host</td>
</tr>
<tr data-sourcepos="94:1-94:68">
<td data-sourcepos="94:2-94:20">SYNC SYNCHRONISED</td>
<td data-sourcepos="94:22-94:45">put:/api/sync/syncTask</td>
<td data-sourcepos="94:47-94:67">payload.destination</td>
</tr>
<tr data-sourcepos="95:1-95:63">
<td data-sourcepos="95:2-95:14">SYNC COPIED</td>
<td data-sourcepos="95:16-95:40">post:/api/sync/copyTask</td>
<td data-sourcepos="95:42-95:62">payload.destination</td>
</tr>
<tr data-sourcepos="96:1-96:70">
<td data-sourcepos="96:2-96:23">SYNC PROFILE DELETED</td>
<td data-sourcepos="96:25-96:56">post:/api/sync/syncTask/delete</td>
<td data-sourcepos="96:58-96:69">payload.id</td>
</tr>
<tr data-sourcepos="97:1-97:56">
<td data-sourcepos="97:2-97:17">SYNC JOB RUNED</td>
<td data-sourcepos="97:19-97:42">post:/api/sync/runTask</td>
<td data-sourcepos="97:44-97:55">payload.id</td>
</tr>
</tbody>
</table>


### AGENTS

<table class="tg">
<thead>
<tr data-sourcepos="101:1-101:37">
<th data-sourcepos="101:2-101:14">ACTION TYPE</th>
<th data-sourcepos="101:16-101:21">PATH</th>
<th data-sourcepos="101:23-101:36">FROM REQUEST</th>
</tr>
</thead>
<tbody>
<tr data-sourcepos="103:1-103:69">
<td data-sourcepos="103:2-103:24">AGENTS AGENT RELOADED</td>
<td data-sourcepos="103:26-103:56">post:/api/agents/reloadagents</td>
<td data-sourcepos="103:58-103:68">params.id</td>
</tr>
<tr data-sourcepos="104:1-104:80">
<td data-sourcepos="104:2-104:30">AGENTS MASTERAGENT RELOADED</td>
<td data-sourcepos="104:32-104:67">post:/api/agents/reloadmasteragent</td>
<td data-sourcepos="104:69-104:79">params.id</td>
</tr>
<tr data-sourcepos="105:1-105:52">
<td data-sourcepos="105:2-105:17">AGENTS DELETED</td>
<td data-sourcepos="105:19-105:38">delete:/api/agents</td>
<td data-sourcepos="105:40-105:51">params.uid</td>
</tr>
<tr data-sourcepos="106:1-106:77">
<td data-sourcepos="106:2-106:22">AGENTS FILE CREATED</td>
<td data-sourcepos="106:24-106:56">post:/api/agents/templates/file</td>
<td data-sourcepos="106:58-106:76">payload.file.name</td>
</tr>
<tr data-sourcepos="107:1-107:58">
<td data-sourcepos="107:2-107:22">AGENTS FILE DELETED</td>
<td data-sourcepos="107:24-107:49">delete:/api/agents/files</td>
<td data-sourcepos="107:51-107:57">empty</td>
</tr>
<tr data-sourcepos="108:1-108:61">
<td data-sourcepos="108:2-108:21">AGENTS FILE EDITED</td>
<td data-sourcepos="108:23-108:45">put:/api/agents/files</td>
<td data-sourcepos="108:47-108:60">payload.name</td>
</tr>
<tr data-sourcepos="109:1-109:80">
<td data-sourcepos="109:2-109:26">AGENTS TEMPLATE CREATED</td>
<td data-sourcepos="109:28-109:55">post:/api/agents/templates</td>
<td data-sourcepos="109:57-109:79">payload.template.name</td>
</tr>
<tr data-sourcepos="110:1-110:78">
<td data-sourcepos="110:2-110:25">AGENTS TEMPLATE EDITED</td>
<td data-sourcepos="110:27-110:53">put:/api/agents/templates</td>
<td data-sourcepos="110:55-110:77">payload.template.name</td>
</tr>
<tr data-sourcepos="111:1-111:78">
<td data-sourcepos="111:2-111:26">AGENTS TEMPLATE DELETED</td>
<td data-sourcepos="111:28-111:57">delete:/api/agents/templates</td>
<td data-sourcepos="111:59-111:77">payload.params.id</td>
</tr>
<tr data-sourcepos="112:1-112:104">
<td data-sourcepos="112:2-112:44">AGENTS BEATS [started|restarted|stoped]</td>
<td data-sourcepos="112:46-112:74">post:/api/agents/manage/<code data-sourcepos="112:72-112:72">*</code>
</td>
<td data-sourcepos="112:76-112:103">[params.beatname|payload]</td>
</tr>
</tbody>
</table>


### INTELLIGENCE

<table class="tg">
<thead>
<tr data-sourcepos="116:1-116:37">
<th data-sourcepos="116:2-116:14">ACTION TYPE</th>
<th data-sourcepos="116:16-116:21">PATH</th>
<th data-sourcepos="116:23-116:36">FROM REQUEST</th>
</tr>
</thead>
<tbody>
<tr data-sourcepos="118:1-118:103">
<td data-sourcepos="118:2-118:27">INTELLIGENCE RULE STOPED</td>
<td data-sourcepos="118:29-118:85">get:/api/intelligence/intelligence_airules_set_stoprule</td>
<td data-sourcepos="118:87-118:102">query.rule_uid</td>
</tr>
<tr data-sourcepos="119:1-119:105">
<td data-sourcepos="119:2-119:28">INTELLIGENCE RULE STARTED</td>
<td data-sourcepos="119:30-119:87">get:/api/intelligence/intelligence_airules_set_startrule</td>
<td data-sourcepos="119:89-119:104">query.rule_uid</td>
</tr>
<tr data-sourcepos="120:1-120:106">
<td data-sourcepos="120:2-120:28">INTELLIGENCE RULE DELETED</td>
<td data-sourcepos="120:30-120:88">get:/api/intelligence/intelligence_airules_set_deleterule</td>
<td data-sourcepos="120:90-120:105">query.rule_uid</td>
</tr>
<tr data-sourcepos="121:1-121:121">
<td data-sourcepos="121:2-121:38">INTELLIGENCE RULE [created|edited]</td>
<td data-sourcepos="121:40-121:102">get:/api/intelligence/intelligence_modelcreation_set_formdata</td>
<td data-sourcepos="121:104-121:120">query.rule_name</td>
</tr>
</tbody>
</table>


### NETWORK-PROBE

<table class="tg">
<thead>
<tr data-sourcepos="125:1-125:37">
<th data-sourcepos="125:2-125:14">ACTION TYPE</th>
<th data-sourcepos="125:16-125:21">PATH</th>
<th data-sourcepos="125:23-125:36">FROM REQUEST</th>
</tr>
</thead>
<tbody>
<tr data-sourcepos="127:1-127:82">
<td data-sourcepos="127:2-127:29">NETWORK-PROBE FILE CREATED</td>
<td data-sourcepos="127:31-127:61">post:/api/network-probe/files</td>
<td data-sourcepos="127:63-127:81">payload.file.path</td>
</tr>
<tr data-sourcepos="128:1-128:83">
<td data-sourcepos="128:2-128:29">NETWORK-PROBE FILE DELETED</td>
<td data-sourcepos="128:31-128:63">delete:/api/network-probe/files</td>
<td data-sourcepos="128:65-128:82">payload.filePath</td>
</tr>
<tr data-sourcepos="129:1-129:94">
<td data-sourcepos="129:2-129:34">NETWORK-PROBE FILE REREGISTERED</td>
<td data-sourcepos="129:36-129:75">post:/api/network-probe/files/register</td>
<td data-sourcepos="129:77-129:93">payload.host.ip</td>
</tr>
<tr data-sourcepos="130:1-130:115">
<td data-sourcepos="130:2-130:54">NETWORK PROBE SERVICES [stoped|started|restarted]</td>
<td data-sourcepos="130:56-130:89">post:/api/network-probe/services</td>
<td data-sourcepos="130:91-130:114">payload.services.names</td>
</tr>
<tr data-sourcepos="131:1-131:126">
<td data-sourcepos="131:2-131:34">NETWORK-PROBE PIPELINES ENABLED</td>
<td data-sourcepos="131:36-131:87">post:/api/network-probe/{probeId}/pipelines/enable</td>
<td data-sourcepos="131:89-131:125">params.hostId, payload.pipelinesIds</td>
</tr>
<tr data-sourcepos="132:1-132:128">
<td data-sourcepos="132:2-132:35">NETWORK-PROBE PIPELINES DISABLED</td>
<td data-sourcepos="132:37-132:89">post:/api/network-probe/{probeId}/pipelines/disable</td>
<td data-sourcepos="132:91-132:127">params.hostId, payload.pipelinesIds</td>
</tr>
<tr data-sourcepos="133:1-133:87">
<td data-sourcepos="133:2-133:35">NETWORK-PROBE PIPELINES RELOADED</td>
<td data-sourcepos="133:37-133:78">post:/api/network-probe/pipelines/reload</td>
<td data-sourcepos="133:80-133:86">empty</td>
</tr>
</tbody>
</table>


### ELASTSCHEDULER

<table class="tg">
<thead>
<tr data-sourcepos="137:1-137:37">
<th data-sourcepos="137:2-137:14">ACTION TYPE</th>
<th data-sourcepos="137:16-137:21">PATH</th>
<th data-sourcepos="137:23-137:36">FROM REQUEST</th>
</tr>
</thead>
<tbody>
<tr data-sourcepos="139:1-139:124">
<td data-sourcepos="139:2-139:69">[<code data-sourcepos="139:5-139:11">ARCHIVE</code>|<code data-sourcepos="139:15-139:30">INDEX_MANAGEMENT</code>|<code data-sourcepos="139:34-139:37">SYNC</code>] ACTION [enabled|disabled]</td>
<td data-sourcepos="139:71-139:108">put:/api/elastscheduler/schedulerjob</td>
<td data-sourcepos="139:110-139:123">payload.name</td>
</tr>
<tr data-sourcepos="140:1-140:94">
<td data-sourcepos="140:2-140:39">SCHEDULER ACTION [enabled|disabled]</td>
<td data-sourcepos="140:41-140:78">put:/api/elastscheduler/schedulerjob</td>
<td data-sourcepos="140:80-140:93">payload.name</td>
</tr>
</tbody>
</table></div>

## Index management

**Note** \
**Before using the *Index Management* module is necessary to set an appropriate password for the *Log Server* user in the following file: ```/usr/share/kibana/curator/curator.yml```***

The Index Management module allows you to manage indexes and perform activities such as:

 - Closing indexes,
 - Delete indexes,
 - Performing a merge operation for index,
 - Shrink index shards,
 - Index rollover.

The *Index Management* module is accessible through the main menu tab.

The main module window allows you to create new *Create Task* tasks, view and manage created tasks, that is:

 - Update,
 - Custom update,
 - Delete,
 - Start now,
 - Disable / Enable.

![](/media/media/image227.png)

**Note** ***Use the `Help` button***

![](/media/media/image229.png)

***By using the `Help` button you can get a detailed description of the current action***s

![](/media/media/image228.png)

### Close action

This action closes the selected indices and optionally deletes associated aliases beforehand.

Settings required:

- Action Name
- Schedule Cron Pattern - it sets when the task is to be executed, to decode cron format use the online tool: [https://crontab.guru](https://crontab.guru),
- Pattern filter kind  - it sets the index filtertype for the task,
- Pattern filter value - it sets the value for the index filter,
- Index age - it sets the index age for the task.

Optional settings:

 - Timeout override
 - Ignore Empty List
 - Continue if exception
 - Closed indices filter
 - Empty indices filter

![](/media/media/image221.png)

### Delete action

This action deletes the selected indices.

Settings required:

- Action Name
- Schedule Cron Pattern - it sets when the task is to be executed, to decode cron format use the online tool: [https://crontab.guru](https://crontab.guru)/,
- Pattern filter kind  - it sets the index filtertype for the task,
- Pattern filter value - it sets the value for the index filter,
- Index age - it sets the index age for the task.

Optional settings:

 - Delete Aliases
 - Skip Flush
 - Ignore Empty List
 - Ignore Sync Failures

![](/media/media/image222.png)

### Force Merge action

This action performs a Force Merge on the selected indices, merging them in the specific number of segments per shard.

Settings required:

- Action Name
- Schedule Cron Pattern - it sets when the task is to be executed, to decode cron format use the online tool: [https://crontab.guru](https://crontab.guru)/,
- Max Segments - it sets the number of segments for the shard,
- Pattern filter kind  - it sets the index filtertype for the task,
- Pattern filter value - it sets the value for the index filter,
- Index age - it sets the index age for the task.

Optional settings:

 - Ignore Empty List
 - Ignore Sync Failures

![](/media/media/image223.png)

### Shrink action

Shrinking an index is a good way to reduce the total shard count in your cluster.

Several conditions need to be met in order for index shrinking to take place:

 - The index must be marked as read-only
 - A (primary or replica) copy of every shard in the index must be relocated to the same node
 - The cluster must have health green
 - The target index must not exist
 - The number of primary shards in the target index must be a factor of the number of primary shards in the source index.
 - The source index must have more primary shards than the target index.
 - The index must not contain more than 2,147,483,519 documents in total across all shards that will be shrunk into a single shard on the target index as this is the maximum number of docs that can fit into a single shard.
 - The node handling the shrink process must have sufficient free disk space to accommodate a second copy of the existing index.

The task will try to meet these conditions. If it is unable to meet them all, it will not perform a shrink operation.

Settings required:

- Action Name
- Schedule Cron Pattern - it sets when the task is to be executed, to decode cron format use the online tool: [https://crontab.guru](https://crontab.guru)/,
- Number of primary shards in the target index - it sets the number of shared for the target index,
- Pattern filter kind  - it sets the index filtertype for the task,
- Pattern filter value - it sets the value for the index filter,
- Index age - it sets the index age for the task.

Optional settings:

 - Ignore Empty List
 - Continue if exception
 - Delete source index after operation
 - Closed indices filter
 - Empty indices filter

![](/media/media/image224.png)

### Rollover action

This action uses the Elasticsearch Rollover API to create a new index if any of the described conditions are met.

Settings required:

- Action Name
- Schedule Cron Pattern - it sets when the task is to be executed, to decode cron format use the online tool: [https://crontab.guru](https://crontab.guru)/,
- Alias Name - it sets an alias for the index,
- Set max age (hours) - it sets an age for the index after then index will rollover,
- Set max docs - it sets a number of documents for the index after which the index will rollover,
- Set max size (GiB) - it sets index size in GB after which the index will rollover.

Optional settings:

 - New index name (optional)

![](/media/media/image225.png)

### Index rollover

Using the rollover function, you can make changes to removing documents from the *audit*, *.agents*, and *alert\** indexes.

You can configure the rollover by going to the *Config* module, then clicking the *Settings* tab, going to the *Index rollover settings* section, and clicking the *Configure* button:

![](/media/media/image167.png)

You can set the following retention parameters for the above indexes:

- Maximum size (GB);
- Maximum age (h);
- Maximum number of documents.

### Custom action

Additionally, the module allows you to define your own actions in line with the Curator documentation: https://www.elastic.co/guide/en/elasticsearch/client/curator/current/actions.html

To create a Custom action, select *Custom* from *Select Action*, enter a name in the *Action Name* field, and set the schedule in the *Schedule Cron Pattern* field. In the edit field, enter the definition of a custom action:

![](/media/media/image226.png)

Custom Action examples:

#### Open index

```yaml
actions:
  1:
    action: open
    description: >-
      Open indices older than 30 days but younger than 60 days (based on index
      name), for logstash- prefixed indices.
    options:
      timeout_override:
      continue_if_exception: False
      disable_action: True
    filters:
    - filtertype: pattern
      kind: prefix
      value: logstash-
      exclude:
    - filtertype: age
      source: name
      direction: older
      timestring: '%Y.%m.%d'
      unit: days
      unit_count: 30
      exclude:
    - filtertype: age
      source: name
      direction: younger
      timestring: '%Y.%m.%d'
      unit: days
      unit_count: 60
      exclude:

```

#### Replica reduce

```yaml
actions:
  1:
    action: replicas
    description: >-
      Reduce the replica count to 0 for logstash- prefixed indices older than
      10 days (based on index creation_date)
    options:
      count: 0
      wait_for_completion: False
      timeout_override:
      continue_if_exception: False
      disable_action: True
    filters:
    - filtertype: pattern
      kind: prefix
      value: logstash-
      exclude:
    - filtertype: age
      source: creation_date
      direction: older
      unit: days
      unit_count: 10
      exclude:
```

#### Index allocation

```yaml
actions:
  1:
    action: allocation
    description: >-
      Apply shard allocation routing to 'require' 'tag=cold' for hot/cold node
      setup for logstash- indices older than 3 days, based on index_creation
      date
    options:
      key: tag
      value: cold
      allocation_type: require
      disable_action: True
    filters:
    - filtertype: pattern
      kind: prefix
      value: logstash-
    - filtertype: age
      source: creation_date
      direction: older
      unit: days
      unit_count: 3

```

#### Cluster routing

```yaml
actions:
  1:
    action: cluster_routing
    description: >-
      Disable shard routing for the entire cluster.
    options:
      routing_type: allocation
      value: none
      setting: enable
      wait_for_completion: True
      disable_action: True
  2:
    action: (any other action details go here)
    ...
  3:
    action: cluster_routing
    description: >-
      Re-enable shard routing for the entire cluster.
    options:
      routing_type: allocation
      value: all
      setting: enable
      wait_for_completion: True
      disable_action: True
```

### Preinstalled actions

#### Close-Daily

This action closes the selected indices older than 93 days and optionally deletes associated aliases beforehand. For example, if it is today 21 December this action will close or optionally delete every index older than 30 September of the same year, action starts every day at 01:00 AM.

`Action type`:   CLOSE \
`Action name`:   Close-Daily \
`Action Description (optional)`:   Close daily indices older than 90 days \
`Schedule Cron Pattern` :   0 1 \* \* \* \
`Delete Aliases`:   enabled \
`Skip Flush`:   disabled \
`Ignore Empty List`:   enabled \
`Ignore Sync Failures`:   enabled \
`Pattern filter kind`:   Timestring \
`Pattern filter value`:   %Y.%m$ \
`Index age`:   93 days \
`Empty indices filter`:   disable

#### Close-Monthly

This action closes the selected indices older than 93 days (3 months)and optionally deletes associated aliases beforehand. If it today is 21 December, this action will close or optionally delete every index older than Oktober the same year, the action starts every day at 01:00 AM.

`Action type`:    CLOSE \
`Action name`:     Close-Daily \
`Action Description (optional)`:     Close daily indices older than 93 days \
`Schedule Cron Pattern`:    0 1 * * * \
`Delete Aliases`:     enabled \
`Skip Flush`:    disabled \
`Ignore Empty List`:   enabled \
`Ignore Sync Failures`:    enabled \
`Pattern filter kind`:    Timestring \
`Pattern filter value`:   %Y.%m$ \
`Index age`:     93 days \
`Empty indices filter`:    disable

#### Disable-Refresh-Older-Than-Days

This action disables the daily refresh of indices older than 2 days. the action is performed daily at 01:00.

`Action type`: CUSTOM \
`Action name`: Disable-Refresh-Older-Than-Days \
`Schedule Cron Pattern`:    0 1 * * *

`YAML`:

```yaml
actions:
  '1':
    action: index_settings
    description: Disable refresh for older daily indices
    options:
      index_settings:
        index:
          refresh_interval: -1
      ignore_unavailable: False
      ignore_empty_list: true
      preserve_existing: False
    filters:
      - filtertype: pattern
        kind: timestring
        value: '%Y.%m.%d$'
      - filtertype: age
        source: creation_date
        direction: older
        unit: days
        unit_count: 2
```

#### Disable-Refresh-Older-Than-Month

This action forces the daily merge of indices older than one month. The action is performed daily at 01:00.

`Action type`: CUSTOM \
`Action name`: Disable-Refresh-Older-Than-Month \
`Schedule Cron Pattern`:    0 1 * * *

`YAML`:

```yaml
actions:
  '1':
    action: index_settings
    description: Disable refresh for older monthly indices
    options:
      index_settings:
        index:
          refresh_interval: -1
      ignore_unavailable: False
      ignore_empty_list: true
      preserve_existing: False
    filters:
      - filtertype: pattern
        kind: timestring
        value: '%Y.%m$'
      - filtertype: age
        source: creation_date
        direction: older
        unit: days
        unit_count: 32
```

#### Force-Merge-Older-Than-Days

This action forces the daily merge of indices older than two days. The action is performed daily at 01:00.

`Action type`: CUSTOM \
`Action name`: Force-Merge-Older-Than-Days \
`Schedule Cron Pattern`:    0 1 * * *

`YAML`:

```yaml
actions:
  '1':
    action: forcemerge
    description: Force merge on older daily indices
    options:
      max_num_segments: 1
      ignore_empty_list: true
      continue_if_exception: false
      delay: 60
    filters:
      - filtertype: pattern
        kind: timestring
        value: '%Y.%m.%d$'
      - filtertype: age
        source: creation_date
        direction: older
        unit: days
        unit_count: 2
      - filtertype: forcemerged
        max_num_segments: 1
        exclude: True
```

#### Force-Merge-Older-Than-Months

This action forces the daily merge of indices older than one month. The action is performed daily at 01:00.

`Action type`: CUSTOM \
`Action name`: Force-Merge-Older-Than-Months \
`Schedule Cron Pattern`:    0 1 * * *

`YAML`:

```yaml
actions:
  '1':
    action: forcemerge
    description: Force merge on older monthly indices
    options:
      max_num_segments: 1
      ignore_empty_list: true
      continue_if_exception: false
      delay: 60
    filters:
      - filtertype: pattern
        kind: timestring
        value: '%Y.%m$'
      - filtertype: age
        source: creation_date
        direction: older
        unit: days
        unit_count: 32
      - filtertype: forcemerged
        max_num_segments: 1
        exclude: True
```

#### Logtrail-default-delete

This action leaves only two last indices from each logtrail rollover index ( allows for up to 10GB of data). The action is performed daily at 03:30.

`Action type`:   CUSTOM \
`Action name`:   Logtrail-default-delete \
`Schedule Cron Pattern`:   30 3 * * *

`YAML`:

```yaml
actions:
  '1':
    action: delete_indices
    description: >-
      Leave only two last indices from each logtrail rollover index - allows for up to
      10GB data.
    options:
      ignore_empty_list: true
      continue_if_exception: true
    filters:
      - filtertype: count
        count: 2
        pattern: '^logtrail-(.*?)-\d{4}.\d{2}.\d{2}-\d+$'
        reverse: true


```

#### Logtrail-default-rollover

This action rollover default Logtrail indices. The action is performed every 5 minutes.

`Action type`:   CUSTOM \
`Action name`:   Logtrail-default-rollover \
`Schedule Cron Pattern`:   5 * * * *

`YAML`:

```yaml
actions:
  '1':
    action: rollover
    description: >-
      This action works on default logtrail indices. It is recommended to enable
      it.
    options:
      name: logtrail-alert
      conditions:
        max_size: 5GB
      continue_if_exception: true
      allow_ilm_indices: true
  '2':
    action: rollover
    description: >-
      This action works on default logtrail indices. It is recommended to enable
      it.
    options:
      name: logtrail-elasticsearch
      conditions:
        max_size: 5GB
      continue_if_exception: true
      allow_ilm_indices: true
  '3':
    action: rollover
    description: >-
      This action works on default logtrail indices. It is recommended to enable
      it.
    options:
      name: logtrail-kibana
      conditions:
        max_size: 5GB
      continue_if_exception: true
      allow_ilm_indices: true
  '4':
    action: rollover
    description: >-
      This action works on default logtrail indices. It is recommended to enable
      it.
    options:
      name: logtrail-logstash
      conditions:
        max_size: 5GB
      continue_if_exception: true
      allow_ilm_indices: true
```


## Task Management

Energy Logserver provides the ability to manage tasks. Table with running tasks is located in `Task Management` section.

![](/media/media/task_management1.png)

![](/media/media/task_management2.png)

### Long Running Query

If query is cancellable trash icon is available in Actions column. (Note: Not every query can be canceled)

![](/media/media/task_management3.png)

### Searchbar and filtering

It is possible to search for running task using searchbar. There are provided four types of filtering:

- `Cancellable` - It filters only cancellable tasks.  
- `Parent` - This option filters only parent tasks.
- `Action` - It filters by action ( Sample action: `indices:data/write/bulk`).
- `Running time in seconds` - When checked, only shows tasks that take longer than a specified number of seconds.

### Task Details

Expanding the details column provides more information about a given task. (Note: Depending on the type of task, different information may be provided.)

![](/media/media/task_management4.png)


## Empowered AI

`Empowered AI` is a module of Energy Logserver containing mathematical algorithms for data science.

It is licenced extention for SIEM deplyment. Main purpose of the `Empowered AI` is to help SOC teams see that data which are difficult to detect with regular approach. Advance mathematical sorting, grouping, forecastig enriched with statistics create a new outlook of security posture.

`Empowered AI` is an ongoing project. Our team of mathematicians, data scientists and security analysts continue their work addressing more and more new usecases.

### AI Rules

In the `Empowered AI`  section you will find a summary of the existing rules. At the top, you'll find the total number of rules and the number of scheduled and unscheduled rules. Here is the search field and buttons `Refresh rules list`  and `Create New Rule`  Below is the table. It contains `AI Rule Name`, `Search/Index Name`  -  data source, `Last Executed`  - date, `Last Modified` - date, selected `Use Case`,  `Schedule`  - scheduling frequency, `Status`  and `Action`  icons.

![](/media/media/okno.png)

#### Status

The rule has one of the following statuses:

- Waiting to start - `Run once` rule starts by clicking symbol play.
- Scheduled - the scheduled rule starts automatically.
- Scoring
- Building
- Finished - click on the `AI Rule Name`  to get the forecast results preview `AI Rules>Performance`.
- Error -  check error details in the results preview  `Performance>AI Rule Configuration>Exceptions`.

#### Actions

Icons of actions:

 - Play – run or rerun the rule,
 - Stop – unschedule periodic rule, after this action rule type changes to Run Once,
 - Pencil - edit the rule's configuration,
 - Bin – delete the rule.

#### Prepare your data set

Save your `Discover`  search so you can use it the same way as in visualizations and dashboards.

#### Create New Rule

To create a rule choose ``Empowered AI`>AI Rules>Create New Rule`. In pop-up form `Select Use Case`. The `Empowered AI` module contains AI models for various use cases: `Forecasting`, `Anomaly Detection - Number`, `Anomaly Detection - Text`, `Clustering` and `Relationship Mining`.

![](/media/media/wybor.png)

#### Performance

To see the result of the finished rule click on the link in the column `AI Rule Name`. Here we have `AI Rule Configuration` and `Model Performance`.

 ![](/media/media/result.png)

In `AI Rule Configuration` you will find detailed configuration parameters and information about the training data set. Exception details will also appear here in case of misconfiguration. `Model Performance` is the presentation of data and analysis results. Depending on the use case, these are charts, relationship visualizations, and tables.

### Forecasting

Predicting future conditions is a crucial aspect of decision-making in any organization. To anticipate upcoming events, historical data analysis is indispensable. Energy Logserver `Empowered AI` Module suggests utilizing the XGBoost algorithm, also known as eXtreme Gradient Boosting, for forecasting your environmental variables in the near future.

XGBoost is an advanced machine learning algorithm that excels at handling datasets with multiple variables. This algorithm can accurately model complex relationships within data, enabling precise predictions of future events. XGBoost is a popular choice in the field of Data Science, particularly for solving regression and classification problems, thanks to its efficiency and effectiveness.

#### Create a rule

To create a rule choose `Empowered AI`>`AI Rules`>`Create New Rule`. In pop-up form `Select Use Case>Forecasting` and insert the rule's name.

 ![](/media/media/nazwa_i_dane.png)

#### Choose data

`Choose Data Source`  is a drop-down list with your saved data, choose one of them. After loading the source, we can select `Field to Analyse`  - the id-field to be predicted. The system default loads headers of the appropriate data type for the specified use case. You can also choose the checkbox displaying all the fields. The proper mapping is necessary for appropriate header recognition. As numerical data, you can also use the number of documents instead of field values. To do that, choose the checkbox. `Multiply by Field`  allows you to obtain separate forecasts e.g., for several (or all) hosts, users and domains, in one rule.

 ![](/media/media/multiply.png)

#### Scheduler options

In this field, you can choose the frequency at which the rule runs `Run Once` or `Scheduled`.

##### Run Once

Range of dates you choose from the interactive calendars, click on icons.
`Build Time Frame` is a piece of data used to create and train the model. More training data allows the algorithm to obtain more accurate signal patterns and trend information. If there is too little and incomplete data, the forecast may not be accurate.
`Start Date` is the starting point of predictions.

 ![](/media/media/agregacja.png)

##### Scheduled

Scheduled rules require dates to be a relative distance from now. You choose number and time unit: minutes, hours, days, weeks, months. `Build Time Frame Offset`  is historical data used to build the model.  `Period: time selection`   is time distance before end point `TO: now - time selection` of the data set. `Start Date Offset  is the starting point of forecast. It must be set inside the build time frame offset.

![](/media/media/scheduled.png)

#### Data Aggregation and Forecast Time Frame

The data set is divided into small intervals specified in the `Data Aggregation> 30 min | 1 h | 2 h | 4 h | 8 h | 12 h | 1 d`  parameter. The algorithm uses this unit as the training and reporting frequency. `Forecast Time Frame> 4 h | 8 h | 12 h | 1 d | 2 d | 3 d | 1 w` is the period of the requested forecast. A shorter time gives a better estimation. Value of forecast time frame must be a multiplicity of time data aggregation.

#### Launch

You can find the newly created rule in the table with the `Waiting to start` status. Click `Play` and wait for a moment. Refresh the rules list. If it has the status `Finished`, click on the rule's name to see the results.

 ![](/media/media/finished.png)

#### Results

![](/media/media/result.png)

#### Difference Multi Pattern - alert rule

Users of SIEM Plan can leverage Empowered AI in alert rules. For forecasting, a special rule called Multi Pattern Difference has been created. In the form  `Create Alert Rule`, we compare two patterns, index_name-* and index_name-forecast-*, along with the fields used in the forecast, `field_name` and `ai.field_name`. It's crucial to note that the `agg_min` value should not be lower than the aggregation window used in the forecast; it must be a multiple thereof.
Fill in the remaining fields following the convention used for other alert rules.

![](/media/media/multi_difference_alert1.png)

### Default AI Forecasting Rules

In today's rapidly evolving world of technology, the ability to predict and respond to potential IT threats and challenges is crucial for maintaining operational continuity and system security. Our new functionality, **Default Forecasting Rules** within the *Empowered AI* module, has been designed to meet these challenges by offering advanced analysis and forecasting capabilities in the context of syslog data.

The goal of our functionality is simple yet ambitious: to automatically deploy a set of default forecasting rules for the syslog index right after the system starts up. This enables users to immediately make use of advanced analytical tools that help in identifying and responding to data anomalies, potential security threats, and other significant patterns that may impact the system and organizational operations.

By using **Default Forecasting Rules**, users can:

- **Quickly start analyzing data**: Default rules eliminate the need for manual system configuration, allowing users to focus on the analysis and interpretation of data.
- **Increase the effectiveness of threat detection**: Applying advanced AI algorithms and machine learning in forecasting allows for faster and more precise identification of potential threats.
- **Improve operational efficiency**: Automating the forecasting process saves time and resources while increasing overall operational efficiency.

Our functionality is designed with ease of use and accessibility in mind, ensuring that organizations of any size or industry can leverage the power of predictive analytics to optimize their IT operations.

### Step-by-Step Guide: How to Use Default Forecasting Rules in the Empowered AI Module

This guide shows how to quickly and easily start using default forecasting rules in our Empowered AI module. By following these simple steps, you will be able to effectively utilize the power of AI for data analysis and forecasting.

#### Prerequisites

Ensure you are logged into the application and have the appropriate permissions to use the Empowered AI module.

#### Step 1: Go to the Empowered AI Module in the Application

Find and open the Empowered AI module in the application. You can do this by selecting the appropriate option in the main menu.

![GoToEmpoweredAIModule](/media/media/go_to_empowered_ai.png)

#### Step 2: Select One of the Default Forecasting Rules

Upon entering the Empowered AI module, you will see a list of available forecasting rules. Select the one that best fits your needs by clicking on it.

![SelectForecastingRule](/media/media/select_default_rule.png)

#### Step 3: Run Forecasting Rule

With the selected rule, click the "run" button to start the data analysis process. This may take some time, depending on the amount of data to be processed.

![LaunchForecasting](/media/media/run_rule.png)

#### Step 4: Check the Results

After forecasting is complete, the results will be displayed in the module. Review them to understand potential patterns and dependencies in the data.

![CheckForecastingResults](/media/media/check_results.png)

#### FAQ

**Q: How often can I run forecasting?**  
A: Forecasting can be run as often as needed. However, keep in mind that each forecasting run is a computational process and may take some time.

**Q: Can I modify the default forecasting rules?**  
A: Yes, default rules can be modified.

#### Troubleshooting

- **Problem: Forecasting is not launching.**  
Solution: Ensure you have the appropriate permissions and that all required data is correctly loaded into the system.

- **Problem: Forecasting results seem to be inaccurate.**  
Solution: Check if the selected forecasting rule is suitable for the type and character of your data. Consider modifying the rule for better alignment.

## Archive

The Archive module allows you to create compressed data files ([zstd](https://github.com/facebook/zstd)) from Elasticsearch indices. The archive checks the age of each document in the index and if it is older than defined in the job, it is copied to the archive file.

### Configuration

#### Enabling module

To configure the module edit the `kibana.yml` configuration file end set path to the archive directory - location where the archive files will be stored:

```bash
vim /etc/kibana/kibana.yml
```

remove the comment from the following line and set the correct path to the archive directory:

```vim
archive.archivefolderpath: '/var/lib/elastic_archive_test'
```

Archives will be saved inside above directory in the subdirectories that describes year and month of its creation. For example:

```bash
/var/lib/elastic_archive_test
├── 2022
│   └── 08
│       ├── enc3_2022-08-15.json.zstd
│       └── skimmer-2022.08_2022-08-06.json.zstd
└── 2023
    ├── 05
    │   ├── enc1_2023-05-25.json.zstd
    │   ├── enc2_2023-05-25.json.zstd
    │   └── skimmer-2023.05_2023-05-25.json.zstd
    └── 07
        └── skimmer-2023.07_2023-07-30.json.zstd
```

### Archive Task

#### Create Archive task

1. From the main navigation go to the "Archive" module.

2. On the "Archive" tab select "Create Task" and define the following parameters:

   - `Index pattern` - for the indices that will be archived, for example, `syslog*`
   - `Timestamp Field` - time field of the indices (default **@timestamp**)
   - `Older than (days)` - number of days after which documents will be archived
   - `Field names filter` - filter fields that should be archived
   - `Encrypt archives` - after enabling encryption, prompt with two password fields will be shown.

   - `Schedule task` (crontab format) - the work schedule of the ordered task.

   ![](/media/media/04_archive_create-archive-task.png)

#### Task List

In the `Task List`, you can follow the current status of ordered tasks. You can modify the task scheduler or delete a single or many tasks at once.

![](/media/media/04_archive_archive-task-list.png)

If the archiving task finds an existing archive file that matches the data being archived, it will check the number of documents in the archive and the number of documents in the index. If there is a difference in the number of documents then new documents will be added to the archive file.

To show more details of the task, click on the details cell of the desired row.

### Archive Search

The Archive Search module can search archive files for the specific content and back results in the `Task List`

#### Create Search task

1. From the main navigation go to the `Archive` module.
2. On the `Search` tab select `Create Task` and define the following parameters:

   - `Select range of listed archives` - files that matches selected range will be displayed in the list (default **last 14 days**)
   - `Search text` - field for entering the text to be searched
   - `File name` - list of archive files that will be searched
   - `Enable searching in encrypted archives` - enable option to search in encrypted archives

![](/media/media/04_archive_create-search-task.png)

The table footer shows the total number of found files for the specified date range

#### Task list

The searching process can take a long time. On the `Task List`, you can follow the status of the searching process. Also, you can view results and delete tasks.

![](/media/media/04_archive_search-task-list.png)

### Archive Restore

The Archive Restore module moves data from the archive to the Elasticsearch index and make it online.

#### Create Restore task

1. From the main navigation go to the `Archive` module.

2. On the `Restore` tab select `Create Task` and define the following parameters:

  - `Select range of listed archives` - files that matches selected range will be displayed in the list (default **last 14 days**)
  - `Destination index` - If a destination index does not exist it will be created. If exists data will be appended
  - `File name` - list of archive files that will be recovered to Elasticsearch index
  - `Enable restoring from encrypted archives` - enable option to restore data from encrypted archives

![](/media/media/04_archive_create-restore-task.png)

The table footer shows the total number of found files for the specified date range.

#### Task List

The process will index data back into Elasticsearch. Depend on archive size the process can take long time. On the `Task List` you can follow the status of the recovery process. Also you can view result and delete tasks.

![](/media/media/04_archive_restore-task-list.png)

### Search/Restore task with archives without metadata

When creating Search or Restore tasks, during selection of archives to use, some warnings could be seen. Following screenshot presents list of archives with enabled filter that shows only archives with warnings:

- `missing metadata`
- `missing archive file`

![](/media/media/04_archive_archives-list.png)

When particular archive's metadata could not be found following icon will be displayed:
![](/media/media/04_archive_missing-metadata-icon.png)

That archive can be used for task creation, but there are some issues to keep in mind:

  - encryption status of the archive without metadata cannot be established (can be either encrypted or not)
  - when task has enabled encryption handling (e.g. `Enable restoring from encrypted archives` or  `Enable searching in encrypted archives`), archives will be decrypted with provided password. If archive was not decrypted, an error is expected
  - when archive is potentially encrypted and password is not provided, an error is expected.

On the other hand, when metadata is present, but archive itself could not be located, following icon will be displayed: ![](/media/media/04_archive_missing-archive-icon.png)

That archive cannot be used for task creation and so cannot be selected.


### Archive Directory Structure

New archives will be created in the configured archive.archivefolderpath (kibana.yml) in a systematic order. They can be found under a path based on the date the archive was created: /$archivefolderpath/$year/$month. This method of storing archives ensures better readability and significantly simplifies viewing large numbers of files.
The final directory is determined by the last segment of the archive name, which contains the archive creation date. For example, assuming that the root archivefolderpath is set to /download, archive sample-archive_2023-11-01.json.zstd will be saved to the /download/2023/11/ automatically created directory.
Archives once saved to the root directory will be displayed normally in the GUI and will be accessible in the same way as those saved in a sorted manner.

### Archives Checksum Verification

Archives checksum verification feature has been integrated into the `Create Task` section, enhancing the functionality of both the `Search` and `Restore` tabs. This feature adds an extra layer of confidence in the accuracy and reliability of the stored files.

#### Starting Verification

To start the verification process navigate to one of the mentioned tabs. Select archives that will be checked and move them to the right-side table. Below picture presents the button that will be activated, as soon as any complete archives (without any warning) will be selected in the right table. Archives without metadata cannot be utilized due to the lack of necessary details.

![](/media/media/04_archive_checksum-button-disabled.png)

In order to optimize resource utilization and enhance the overall efficiency, a double selection mechanism has been implemented for the file checksum verification, acknowledging the resource-intensive nature of this feature. This ensures, that only desired files will be processed.

![](/media/media/04_archive_checksum-button-enabled.png)

Above picture presents correctly selected archives and a situation when verification process can be started by clicking the `Verify Checksums` button. Following modal will be displayed.

![](/media/media/04_archive_checksum-modal-start.png)

Showcased modal displays previously selected files and some of its details, such as its size and result of verification. Hovering over the result dot provide users with additional information about the result, eg. current status of the verification or possible error.

To start verification, simply click the `Verify` button in the bottom right corner.
After verification has been started, the loading progress bar will be displayed, indicating that the process is running. It is worth mentioning that neither this modal nor the page should be closed or reloaded as the verification process will stop immediately.

The verification can be either stopped or cancelled, by clicking one of the two buttons.

![](/media/media/04_archive_checksum-modal-stop.png)

#### Verification Result

After some time, when the verification is concluded, the final results will be displayed. The verification result is shown in the left bottom corner and is symbolized by one of the displayed colors:
- `green` - all of the archives have compliant checksums
- `yellow` - indicates that some of the archives passed the verification, while others did not
- `red` -  signifies that all of the selected archives failed the verification process

##### When all files are okay:

![](/media/media/04_archive_checksum-modal-success.png)

##### When results are partially correct:

![](/media/media/04_archive_checksum-modal-partially.png)

##### When all files are failed:

![](/media/media/04_archive_checksum-modal-failed.png)

As mentioned before, there is an option to hover over the color dot that indicates the verification result of the file. Below picture shows the reason of failed verification of particular file.

![](/media/media/04_archive_checksum-modal-partially-description.png)

### Identifying progress of archivisation/restoration process

The `/usr/share/kibana/data/archive/tasks` directory contains metadata files, that indicates the current status of the task. That files contains informations about all indices, that:

  - are about to be processed (**"Waiting"** status)
  - are processing (**"Running"** status)
  - were processed (**"Complete"** status)

If everything went according to the plan and the process has successfully finished, that metadata file will be removed. However, when some index cannot be processed or something unexpected happened, there will be **"Error"** status, with detailed message in the "error" field and metadata will remain in the system.

The above described situation is reflected in the GUI by the **Status** column in the Task List tables.

Moreover, in the metadata files can be found current process id (`pid`), total documents count and encryption details.

#### Uncompleted Tasks removal

1. List archive folder and find filename generated by uncompleted task.

    ```bash
    ls -la /archivefolderpath/
    -rw-r--r--. 1 kibana kibana          13 Mar 21 10:07 prd-srv-win-ad-2022.12.
    21_2022-12-21.json.zstd
    ```

1. Find document in `.archive` index using filename from previous step

    `curl -s -k -X GET -ulogserver:... http://127.0.0.1:9200/.archive/_search?size=10000 |jq '.'| grep -B4 "prd-srv-win-ad-2022.12.21"`

1. Write down it's ID

    ```json
    "_id": "Q8teA4cBj_ghAWXFcMJA",
          "_score": 1.0,
          "_source": {
            "date": "2023-03-21T08:52:13.502Z",
            "filename": "prd-srv-win-ad-2022.12.21_2022-12-21.json.zstd",
    ```

1. Remove documen using saved ID

    ```bash
    curl -s -k -X DELETE -ulogserver:... http://127.0.0.1:9200/.archive/_doc/Q8teA4cBj_ghAWXFcMJA
    ```

### Command Line tools

Archive files can be handled by the following commands `zstd`, `zstdcat`, `zstdgrep`, `zstdless`, `zstdmt`.

#### zstd

The command for decompress `*.zstd` the Archive files, for example:

```bash
zstd -d winlogbeat-2020.10_2020-10-23.json.zstd -o
 winlogbeat-2020.10_2020-10-23.json
```

#### zstdcat

The command for concatenate  `*.zstd` Archive files and print content on the standard output, for example:

```bash
zstdcat winlogbeat-2020.10_2020-10-23.json.zstd
```

#### zstdgrep

The command for print lines matching a pattern from `*.zstd` Archive files, for example:

```bash
zstdgrep "optima" winlogbeat-2020.10_2020-10-23.json.zstd
```

Above example is searching documents contain the "optima" phrase in winlogbeat-2020.10_2020-10-23.json.zstd archive file.

#### zstdless

The command for viewing Archive `* .zstd` files, for example:

```bash
zstdless winlogbeat-2020.10_2020-10-23.json.zstd
```

#### zstdmt

The command for compress and decompress Archive `*.zdtd` file useing multiple CPU core (default is 1), for example:

```bash
zstdmt -d winlogbeat-2020.10_2020-10-23.json.zstd -o winlogbeat-2020.10_2020-10-23.json
```

## E-doc

**E-doc** is one of the most powerful and extensible Wiki-like software. The **Energy Logserver** have integration plugin with **E-doc**, which allows you to access **E-doc** directly from the Energy Logserver GUI. Additionally, Energy Logserver provides access management to the E-doc content.

### Login to E-doc

Access to the **E-doc** is from the main **Energy Logserver** GUI window via the **E-doc** button located at the top of the window:

![](/media/media/image168.png)

### Creating a public site

There are several ways to create a public site:

- by clicking the **New Page** icon on the existing page;
- by clicking on a link of a non-existent site;
- by entering the path in the browser's address bar to a non-existent site;
- by duplicating an existing site;

1. Create a site by clicking the **New Page** icon on an existing page

   - On the opened page, click the **New Page** button in the menu at the top of the opened website:

     ![](/media/media/image169.png)

   - A new page location selection window will appear, where in the **Virtual Folders** panel you can select where the new page will be saved.

   - In the text field at the bottom of the window, the **new-page** string is entered by default, specifying the address of the page being created:

     ![](/media/media/image170.png)

   - After clicking on the ***SELECT*** button at the bottom of the window, a window will appear with the option to select the editor type of the newly created site:

     ![](/media/media/image171.png)

   - After selecting the site editor (in this case, the ***Visual Editor*** editor has been selected), a window with site properties will appear where you can set the site title (change the default page title), set a short site description, change the path to the site and optionally add tags to the site:

     ![](/media/media/image172.png)

   - A public site should be placed in the path ***/public*** which is available for the **Guest** group and have the ***public-pages*** tag assigned. The ***public-pages*** tag mark sites are accessible to the "Guest" group.

   - After completing the site with content, save it by clicking on the **Create** button
     located in the menu at the top of the new site editor:

     ![](/media/media/image173.png)

   - After the site is successfully created, the browser will open the newly created site.

2. Create a site by typing a nonexistent path into the browser's address bar

   - In the address bar of the browser, enter the address of non-existent websites, e.g. by adding ***/en/public/test-page*** to the end of the domain name:

     ![](/media/media/image174.png)

   - The browser will display the information ***This page does not exists yet.***, Below there will be a button to create a ***CREATE PAGE*** page (if you have permission to create a site at the given address):

     ![](/media/media/image175.png)

   - After clicking the ***CREATE PAGE*** button, a window with site properties will appear where you can set the site title (change the default page title), set a short site description, change the path to the site and optionally add tags to the site:

     ![](/media/media/image176.png)

   - A public site should be placed in the path ***/public*** which is available for the **Guest** group and have the ***public-pages*** tag assigned. The ***public-pages*** tag mark sites are accessible to the ***Guest*** group.

   - After completing the site with content, save it by clicking on the **Create** button
     located in the menu at the top of the new site editor:

     ![](/media/media/image176.png)

   - After the site is successfully created, the browser will open the newly created site.

3. Create a site by duplicating an existing site

   - On the open page, click the ***Page Actions*** button in the menu at the top of the open site:

     ![](/media/media/image178.png)

   - The list of actions that can be performed on the currently open site will appear:

     ![](/media/media/image179.png)

   - From the expanded list of actions, click on the ***Duplicate*** item, then a new page location selection window will appear, where in the ***Virtual Folders*** panel you can indicate where the new page will be saved. In the text field at the bottom of the window, the string ***public/new-page*** is entered (by default), specifying the address of the page being created:

     ![](/media/media/image180.png)

   - After clicking the ***SELECT*** button, a window with site properties will appear where you can set the site title (change the title of the duplicated page), set a short site description (change the description of the duplicated site), change the path to the site and optionally add tags to the site:

     ![](/media/media/image181.png)

   - A public site should be placed in the path ***/public*** which is available for the **Guest** group and have the ***public-pages*** tag assigned. The ***public-pages*** tag mark sites are accessible to the ***Guest*** group.

   - After completing the site with content, save it by clicking on the **Create** button
     located in the menu at the top of the new site editor:

     ![](/media/media/image176.png)

   - After the site is successfully created, the browser will open the newly created site.

### Creating a site with the permissions of a given group

To create sites with the permissions of a given group, do the following:

1. Check the permissions of the group to which the user belongs. To do this, click on the ***Account*** button in the top right menu in E-doc:

   ![](/media/media/image195.png)

2. After clicking on the ***Account*** button, a menu with a list of actions to be performed on your own account will be displayed:

   ![](/media/media/image196.png)

3. From the expanded list of actions, click on the ***Profiles*** item, then the profile of the currently logged in user will be displayed. The ***Groups*** tile will display the groups to which the currently logged in user belongs:

   ![](/media/media/image197.png)

4. Then create the site in the path, putting the name of the group to which the user belongs. In this case it will be putting your site in the path starting with ***/demo***(preceded by an abbreviation of the language name):

   ![](/media/media/image198.png)

5. Click the ***SELECT*** button at the bottom of the window, a new window will appear with the option to select the editor type for the newly created site:

   ![](/media/media/image199.png)

6. After selecting the site editor (for example ***Visual Editor***), a window with site properties will appear where you can set the site title (change the default page title), set a short site description, change the path to the site and optionally add tags to the site:

   ![](/media/media/image200.png)

7. After completing the site with content, save it by clicking the ***Create*** button in the menu at the top of the new site editor

   ![](/media/media/image201.png)

8. After the site is successfully created, the browser will open the newly created site.

### Content management

#### Text formatting features

- change the text size;
- changing the font type;
- bold;
- italics;
- stress;
- strikethrough;
- subscript;
- superscript;
- align (left, right, center, justify);
- numbered list;
- bulleted list;
- to-do list;
- inserting special characters;
- inserting tables;
- inserting text blocks E-doc also offers non-text insertion.

#### Insert Links

- To insert links, click in the site editor on the ***Link*** icon on the editor icon bar:

![](/media/media/image182.png)

- After clicking on the icon, a text field will appear to enter the website address:

  ![](/media/media/image183.png)

- Then click the ***Save*** button (green sign next to the text field), then the address to the external site will appear on the current site:

  ![](/media/media/image184.png)

#### Insert images

- To insert images, click in the site editor on the ***Insert Assets*** icon on the editor icon bar:

  ![](/media/media/image185.png)

- After clicking on the icon, the window for upload images will appear:

  ![](/media/media/image186.png)

- To upload the image, click the ***Browse*** button (or from the file manager, drag and drop the file to the ***Browse or Drop files here ...*** area) then the added file will appear on the list, its name will be on a gray background:

  ![](/media/media/image187.png)

- Click the ***UPLOAD*** button to send files to the editor, after the upload is completed, you will see information about the status of the operation performed:

  ![](/media/media/image188.png)

- After uploading, the image file will also appear in the window where you can select images to insert:

  ![](/media/media/image189.png)

- Click on the file name and then the ***INSERT*** button to make the image appear on the edited site:

  ![](/media/media/image190.png)

- After completing the site with content, save it by clicking the ***CREATE*** button in the menu at the top of the editor of the new site:

  ![](/media/media/image191.png)

- or the ***SAVE*** button in the case of editing an existing site:

  ![](/media/media/image192.png)

- After the site is successfully created, the browser will open the newly created site.

#### Create a "tree" of documents

***E-doc*** does not offer a document tree structure directly. Creating a structure (tree) of documents is done automatically by grouping sites according to the paths in which they are available.

1. To create document structures (trees), create sites with the following paths:

   ```markdown
   /en/linux/1-introduction
   /en/linux/2-installation
   /en/linux/3-configuration
   /en/linux/4-administration
   /en/linux/5-summary
   ```

2. The items in the menu are sorted alphabetically, so the site titles should begin with a number followed by a dot followed by the name of the site, for example:

   - for the site in the path ***/en/linux/1-introduction*** you should set the title ***1.Introduction***;
   - for the site in the path ***/en/linux/2-installation*** you should set the title ***2.Installation***;
   - for the site in the path ***/en/linux/3-configuration*** you should set the title ***3.Configuration***;
   - for the site in the path ***/en/linux/4-administration*** you should set the title ***4.Administration***;
   - for the site in the path ***/en/linux/5-summary*** you should set the title ***5.Summary***

3. In this way, you can create a structure (tree) of documents relating to one topic:

   ![](/media/media/image193.png)

4. You can create a document with chapters in a similar way. To do this, create sites with the following paths:

   ```e-doc
   /en/elaboration/1-introduction
   /en/elaboration/2-chapter-1
   /en/elaboration/2-chapter-1
   /en/elaboration/2-chapter-1
   /en/elaboration/3-summary
   ```

5. The menu items are in alphabetical order. Site titles should begin with a number followed by a period followed by a name that identifies the site's content:

   - for the site in the path ***/en/elaboration/1-introduction*** you should set the title ***1. Introduction***
   - for the site in the path ***/en/elaboration/2-chapter-1*** you should set the title ***2. Chapter 1***
   - for the site in the path ***/en/elaboration/2-chapter-2*** you should set the title ***2. Chapter 2***
   - for the site in the path ***/en/elaboration/2-chapter-3*** the title should be set to ***2. Chapter 3***
   - for the site in the path ***/en/elaboration/3-summary*** you should set the title ***3. Summary***

6. In this way, you can create a structure (tree) of documents related to one document:

   ![](/media/media/image194.png)

#### Embed allow iframes

**iFrames** - an element to the HTML language that allows an HTML document to be embedded within another HTML document.

For enable iframes in pages:

1. With top menu select `Administration` \
   ![](/media/media/04_wiki_embed_01.png)

2. Now select on left side menu `Rendering` \
   ![](/media/media/04_wiki_embed_02.png)

3. In `Pipeline` medu select `html->html` \
   ![](/media/media/04_wiki_embed_03.png)

4. Then select `Security` \
   ![](media/media/04_wiki_embed_04.png)

5. Next enable option `Allow iframes` \
   ![](/media/media/04_wiki_embed_05.png)

6. `Apply` changes \
   ![](/media/media/04_wiki_embed_06.png)

**Now is possible embed iframes in page HTML code.**

Example of usage:

- Use iframe tag in page html code. \
  ![](/media/media/04_wiki_embed_eou_01.png)

- Result: \
  ![](/media/media/04_wiki_embed_eou_02.png)

#### Conver Pages

It's possible convert page between `Visoal Editor`, `MarkDown` and `Raw HTML`.

Example of usage:

- Create or edit page content in `Visual Editor` \
  ![](/media/media/04_wiki_convert_01.png)

- Click on the `save` button and later click `close` button '\
  ![](/media/media/04_wiki_convert_02.png)

- Select `Page Action` and `Convert` \
  ![](/media/media/04_wiki_convert_03.png)

- Choose destination format \
  ![](/media/media/04_wiki_convert_04.png)

- The content in `Raw HTML format: \
  ![](/media/media/04_wiki_convert_05.png)

## CMDB

This module is a tool used to store information about hardware and sofrware assets, its database store information regarding the relationships among its assets.Is a means of understanding the critical assets and their relationships, such as information systyems upstream sources or dependencies of assets. Data coming with indexes wazuh, winlogbeat,syslog and filebeat.

Module CMDB have two tabs:

### Infrastructure tab

1. Get documents button - which get all matching data. \
   ![](/media/media/04_cmdb_infra_tab_01.png)

2. Search by parameters. \
   ![](/media/media/04_cmdb_infra_tab_02.png)

3. Select query filters - filter data by fields example name or IP. \
   ![](/media/media/04_cmdb_infra_tab_03.png)

4. Add new source

   - For add new element click `Add new source` button. \
   ![](/media/media/04_cmdb_infra_tab_04.png)

   Complete a form:

      - name (required)
      - ip (optional)
      - risk_group (optional)
      - lastKeepAlive (optional)
      - risk_score (optional)
      - siem_id (optional)
      - status (optional)
   Click `Save` \
   ![](/media/media/04_cmdb_infra_tab_05.png)

5. Update multiple element

   - Select multiple items which you needed change \
   ![](/media/media/04_cmdb_infra_tab_06.png)
   - Select fields for changes (in all selected items)
   - Write new value (for all selected items)
   - Click `Update` button \
   ![](/media/media/04_cmdb_infra_tab_07.png)

6. Update single element

   - Select `Update` icon on element \
   ![](/media/media/04_cmdb_infra_tab_08.png)
   - Change value/values and click `Update` \
   ![](/media/media/04_cmdb_infra_tab_09.png)

### Relations Tab

1. Expand details \
   ![](/media/media/04_cmdb_infra_tab_10.png)

2. Edit relation for source

   - Click update icon. \
   ![](/media/media/04_cmdb_infra_tab_11.png)
   - Add new destination for selected source and click `update` \
   ![](/media/media/04_cmdb_infra_tab_12.png)
   - Delete select destination for delete and click delete destination, confirm with `Update` button \
   ![](/media/media/04_cmdb_infra_tab_13.png)

3. Create relation

   - Click `Add new relations` \
   ![](/media/media/04_cmdb_infra_tab_14.png)
   - Select source and one or more destination, next confirm with `Save` button. \
   ![](/media/media/04_cmdb_infra_tab_15.png)

4. Delete relation

   - Select delete relation icon \
   ![](/media/media/04_cmdb_infra_tab_16.png)
   - Confirm delete relation \
   ![](/media/media/04_cmdb_infra_tab_17.png)

### Integration with network_visualization

1. Select visualize module \
![](/media/media/04_cmdb_integra_net_vis_01.png)

2. Click create visualization button \
![](/media/media/04_cmdb_integra_net_vis_02.png)

3. Select Network type \
![](/media/media/04_cmdb_integra_net_vis_03.png)

4. Select `cmdb_relations` source \
![](/media/media/04_cmdb_integra_net_vis_04.png)

5. At Buckets menu click `Add`, \
![](/media/media/04_cmdb_integra_net_vis_05.png)

   - First bucket **Node**
      - Aggregation: Terms
      - Field: source
   - Second bucket **Node**
      - Sub aggregation: Terms
      - Field: destination

   - Third bucket **Node Color**
      - Sub aggregation: Terms
      - Field: source_risk_group

    ![](/media/media/04_cmdb_integra_net_vis_06.png)

6. Select `option` button and matk the checkbox `Redirect to CMDB` \
![](/media/media/04_cmdb_integra_net_vis_07.png)

7. Now if click on some source icon, browser will redirect you to CMDB module with all information for this source. \
![](/media/media/04_cmdb_integra_net_vis_08.png)

## Cerebro - Cluster Health

Cerebro is the Elasticsearch administration tool that allows you to perform the following tasks:

- monitoring and management of indexing nodes, indexes and shards:

![](/media/media/image217.png)

- monitoring and management of index snapshoots :

![](/media/media/image220.png)

- informing about problems with indexes and shards:

![](/media/media/image219.png)

Access to the `Cluster` module is possible through the button in the upper right corner of the main window.

![](/media/media/image230.png)

To configure cerebro see to *Configuration* section.

## Elasticdump

Elasticdump is a tool for moving and saving indices.

### Location

```bash
/usr/share/kibana/elasticdump/elasticdump
```

### Examples of use

#### Copy an index from production to staging with analyzer and mapping

```bash
elasticdump \
  --input=http://production.es.com:9200/my_index \
  --output=http://staging.es.com:9200/my_index \
  --type=analyzer
elasticdump \
  --input=http://production.es.com:9200/my_index \
  --output=http://staging.es.com:9200/my_index \
  --type=mapping
elasticdump \
  --input=http://production.es.com:9200/my_index \
  --output=http://staging.es.com:9200/my_index \
  --type=data
```

#### Backup index data to a file:

```bash
elasticdump \
  --input=http://production.es.com:9200/my_index \
  --output=/data/my_index_mapping.json \
  --type=mapping
elasticdump \
  --input=http://production.es.com:9200/my_index \
  --output=/data/my_index.json \
  --type=data
```

#### Backup and index to a gzip using stdout

```bash
elasticdump \
  --input=http://production.es.com:9200/my_index \
  --output=$ \
  | gzip > /data/my_index.json.gz
```

#### Backup the results of a query to a file

```bash
elasticdump \
  --input=http://production.es.com:9200/my_index \
  --output=query.json \
  --searchBody="{\"query\":{\"term\":{\"username\": \"admin\"}}}"
```

#### Copy a single shard data

```bash
elasticdump \
  --input=http://es.com:9200/api \
  --output=http://es.com:9200/api2 \
  --params="{\"preference\":\"_shards:0\"}"
```

#### Backup aliases to a file

```bash
elasticdump \
  --input=http://es.com:9200/index-name/alias-filter \
  --output=alias.json \
 ```
#### Copy a single type:

```bash
elasticdump \
  --input=http://es.com:9200/api/search \
  --input-index=my_index/my_type \
  --output=http://es.com:9200/api/search \
  --output-index=my_index \
  --type=mapping
```

### Usage

```bash
elasticdump --input SOURCE --output DESTINATION [OPTIONS]
```

### All parameters

```bash

--input
                    Source location (required)
--input-index
                    Source index and type
                    (default: all, example: index/type)
--output
                    Destination location (required)
--output-index
                    Destination index and type
                    (default: all, example: index/type)
--overwrite
                    Overwrite output file if it exists
                    (default: false)
--limit
                    How many objects to move in batch per operation
                    limit is approximate for file streams
                    (default: 100)

--size
                    How many objects to retrieve
                    (default: -1 -> no limit)

--concurrency
                    How many concurrent request is sent to a specified transport
                    (default: 1)

--concurrencyInterval
                    The length of time in milliseconds before the interval count resets. Must be finite.
                    (default: 5000)

--intervalCap
                    The max number of transport request in the given interval of time.
                    (default: 5)

--carryoverConcurrencyCount
                    Whether the task must finish in the given concurrencyInterval
                    (intervalCap will reset to the default whether the request is completed or not)
                    or will be carried over into the next interval count,
                    which will effectively reduce the number of new requests created in the next interval
                    i.e. intervalCap -= <num of carried over requests>
                    (default: true)

--throttleInterval
                    The length of time in milliseconds to delay between getting data from an inputTransport and sending it to an outputTransport
                    (default: 1)

--debug
                    Display the elasticsearch commands being used
                    (default: false)

--quiet
                    Suppress all messages except for errors
                    (default: false)

--type
                    What are we exporting?
                    (default: data, options: [settings, analyzer, data, mapping, alias, template, component_template, index_template])
--filterSystemTemplates
                    Whether to remove metrics-*-* and logs-*-* system templates
                    (default: true])
--templateRegex
                    Regex used to filter templates before passing to the output transport
                    (default: (metrics|logs|\\..+)(-.+)?)
--delete
                    Delete documents one-by-one from the input as they are
                    moved.  Will not delete the source index
                    (default: false)
--headers
                    Add custom headers to Elastisearch requests (helpful when
                    your Elasticsearch instance sits behind a proxy)
                    (default: '{"User-Agent": "elasticdump"}')
--params
                    Add custom parameters to Elastisearch requests uri. Helpful when you for example
                    want to use elasticsearch preference
                    (default: null)
--searchBody
                    Preform a partial extract based on search results
                    (when ES is the input, default values are
                      if ES > 5
                        `'{"query": { "match_all": {} }, "stored_fields": ["*"], "_source": true }'`
                      else
                        `'{"query": { "match_all": {} }, "fields": ["*"], "_source": true }'`
--searchWithTemplate
                    Enable to use Search Template when using --searchBody
                    If using Search Template then searchBody has to consist of "id" field and "params" objects
                    If "size" field is defined within Search Template, it will be overridden by --size parameter
                    See https://www.elastic.co/guide/en/elasticsearch/reference/current/search-template.html for
                    further information
                    (default: false)
--sourceOnly
                    Output only the json contained within the document _source
                    Normal: {"_index":"","_type":"","_id":"", "_source":{SOURCE}}
                    sourceOnly: {SOURCE}
                    (default: false)
--ignore-errors
                    Will continue the read/write loop on write error
                    (default: false)
--scrollId
                    The last scroll Id returned from elasticsearch.
                    This will allow dumps to be resumed used the last scroll Id &
                    `scrollTime` has not expired.
--scrollTime
                    Time the nodes will hold the requested search in order.
                    (default: 10m)
--maxSockets
                    How many simultaneous HTTP requests can we process make?
                    (default:
                      5 [node <= v0.10.x] /
                      Infinity [node >= v0.11.x] )
--timeout
                    Integer containing the number of milliseconds to wait for
                    a request to respond before aborting the request. Passed
                    directly to the request library. Mostly used when you don't
                    care too much if you lose some data when importing
                    but rather have speed.
--offset
                    Integer containing the number of rows you wish to skip
                    ahead from the input transport.  When importing a large
                    index, things can go wrong, be it connectivity, crashes,
                    someone forgetting to `screen`, etc.  This allows you
                    to start the dump again from the last known line written
                    (as logged by the `offset` in the output).  Please be
                    advised that since no sorting is specified when the
                    dump is initially created, there's no real way to
                    guarantee that the skipped rows have already been
                    written/parsed.  This is more of an option for when
                    you want to get most data as possible in the index
                    without concern for losing some rows in the process,
                    similar to the `timeout` option.
                    (default: 0)
--noRefresh
                    Disable input index refresh.
                    Positive:
                      1. Much increase index speed
                      2. Much less hardware requirements
                    Negative:
                      1. Recently added data may not be indexed
                    Recommended to use with big data indexing,
                    where speed and system health in a higher priority
                    than recently added data.
--inputTransport
                    Provide a custom js file to use as the input transport
--outputTransport
                    Provide a custom js file to use as the output transport
--toLog
                    When using a custom outputTransport, should log lines
                    be appended to the output stream?
                    (default: true, except for `$`)
--awsChain
                    Use [standard](https://aws.amazon.com/blogs/security/a-new-and-standardized-way-to-manage-credentials-in-the-aws-sdks/) location and ordering for resolving credentials including environment variables, config files, EC2 and ECS metadata locations
                    _Recommended option for use with AWS_
--awsAccessKeyId
--awsSecretAccessKey
                    When using Amazon Elasticsearch Service protected by
                    AWS Identity and Access Management (IAM), provide
                    your Access Key ID and Secret Access Key
--awsIniFileProfile
                    Alternative to --awsAccessKeyId and --awsSecretAccessKey,
                    loads credentials from a specified profile in aws ini file.
                    For greater flexibility, consider using --awsChain
                    and setting AWS_PROFILE and AWS_CONFIG_FILE
                    environment variables to override defaults if needed
--awsService
                    Sets the AWS service that the signature will be generated for
                    (default: calculated from hostname or host)
--awsRegion
                    Sets the AWS region that the signature will be generated for
                    (default: calculated from hostname or host)
--awsUrlRegex
                    Regular expression that defined valied AWS urls that should be signed
                    (default: ^https?:\\.*.amazonaws.com.*$)
--transform
                    A javascript, which will be called to modify documents
                    before writing it to destination. global variable 'doc'
                    is available.
                    Example script for computing a new field 'f2' as doubled
                    value of field 'f1':
                        doc._source["f2"] = doc._source.f1 * 2;

--httpAuthFile
                    When using http auth provide credentials in ini file in form
                    `user=<username>
                    password=<password>`

--support-big-int
                    Support big integer numbers
--retryAttempts
                    Integer indicating the number of times a request should be automatically re-attempted before failing
                    when a connection fails with one of the following errors `ECONNRESET`, `ENOTFOUND`, `ESOCKETTIMEDOUT`,
                    ETIMEDOUT`, `ECONNREFUSED`, `EHOSTUNREACH`, `EPIPE`, `EAI_AGAIN`
                    (default: 0)

--retryDelay
                    Integer indicating the back-off/break period between retry attempts (milliseconds)
                    (default : 5000)
--parseExtraFields
                    Comma-separated list of meta-fields to be parsed
--maxRows
                    supports file splitting.  Files are split by the number of rows specified
--fileSize
                    supports file splitting.  This value must be a string supported by the **bytes** module.
                    The following abbreviations must be used to signify size in terms of units
                    b for bytes
                    kb for kilobytes
                    mb for megabytes
                    gb for gigabytes
                    tb for terabytes

                    e.g. 10mb / 1gb / 1tb
                    Partitioning helps to alleviate overflow/out of memory exceptions by efficiently segmenting files
                    into smaller chunks that then be merged if needs be.
--fsCompress
                    gzip data before sending output to file.
                    On import the command is used to inflate a gzipped file
--s3AccessKeyId
                    AWS access key ID
--s3SecretAccessKey
                    AWS secret access key
--s3Region
                    AWS region
--s3Endpoint
                    AWS endpoint can be used for AWS compatible backends such as
                    OpenStack Swift and OpenStack Ceph
--s3SSLEnabled
                    Use SSL to connect to AWS [default true]

--s3ForcePathStyle  Force path style URLs for S3 objects [default false]

--s3Compress
                    gzip data before sending to s3
--s3ServerSideEncryption
                    Enables encrypted uploads
--s3SSEKMSKeyId
                    KMS Id to be used with aws:kms uploads
--s3ACL
                    S3 ACL: private | public-read | public-read-write | authenticated-read | aws-exec-read |
                    bucket-owner-read | bucket-owner-full-control [default private]
--retryDelayBase
                    The base number of milliseconds to use in the exponential backoff for operation retries. (s3)
--customBackoff
                    Activate custom customBackoff function. (s3)
--tlsAuth
                    Enable TLS X509 client authentication
--cert, --input-cert, --output-cert
                    Client certificate file. Use --cert if source and destination are identical.
                    Otherwise, use the one prefixed with --input or --output as needed.
--key, --input-key, --output-key
                    Private key file. Use --key if source and destination are identical.
                    Otherwise, use the one prefixed with --input or --output as needed.
--pass, --input-pass, --output-pass
                    Pass phrase for the private key. Use --pass if source and destination are identical.
                    Otherwise, use the one prefixed with --input or --output as needed.
--ca, --input-ca, --output-ca
                    CA certificate. Use --ca if source and destination are identical.
                    Otherwise, use the one prefixed with --input or --output as needed.
--inputSocksProxy, --outputSocksProxy
                    Socks5 host address
--inputSocksPort, --outputSocksPort
                    Socks5 host port
--handleVersion
                    Tells elastisearch transport to handle the `_version` field if present in the dataset
                    (default : false)
--versionType
                    Elasticsearch versioning types. Should be `internal`, `external`, `external_gte`, `force`.
                    NB : Type validation is handle by the bulk endpoint and not elasticsearch-dump
--csvDelimiter
                    The delimiter that will separate columns.
                    (default : ',')
--csvFirstRowAsHeaders
                    If set to true the first row will be treated as the headers.
                    (default : true)
--csvRenameHeaders
                    If you want the first line of the file to be removed and replaced by the one provided in the `csvCustomHeaders` option
                    (default : true)
--csvCustomHeaders  A comma-seperated listed of values that will be used as headers for your data. This param must
                    be used in conjunction with `csvRenameHeaders`
                    (default : null)
--csvWriteHeaders   Determines if headers should be written to the csv file.
                    (default : true)
--csvIgnoreEmpty
                    Set to true to ignore empty rows.
                    (default : false)
--csvSkipLines
                    If number is > 0 the specified number of lines will be skipped.
                    (default : 0)
--csvSkipRows
                    If number is > 0 then the specified number of parsed rows will be skipped
                    (default : 0)
--csvTrim
                    Set to true to trim all white space from columns.
                    (default : false)
--csvRTrim
                    Set to true to right trim all columns.
                    (default : false)
--csvLTrim
                    Set to true to left trim all columns.
                    (default : false)
--csvHandleNestedData
                    Set to true to handle nested JSON/CSV data.
                    NB : This is a very optioninated implementaton !
                    (default : false)
--csvIdColumn
                    Name of the column to extract the record identifier (id) from
                    When exporting to CSV this column can be used to override the default id (@id) column name
                    (default : null)
--csvIndexColumn
                    Name of the column to extract the record index from
                    When exporting to CSV this column can be used to override the default index (@index) column name
                    (default : null)
--csvTypeColumn
                    Name of the column to extract the record type from
                    When exporting to CSV this column can be used to override the default type (@type) column name
                    (default : null)
--help
                    This page

```

### Elasticsearch's Scroll API

Elasticsearch provides a scroll API to fetch all documents of an index starting from (and keeping) a consistent snapshot in time, which we use under the hood. This method is safe to use for large exports since it will maintain the result set in cache for the given period of time.

NOTE: only works for --output

### Bypassing self-sign certificate errors

Set the environment NODE_TLS_REJECT_UNAUTHORIZED=0 before running elasticdump

### An alternative method of passing environment variables before execution

NB : This only works with linux shells

NODE_TLS_REJECT_UNAUTHORIZED=0 elasticdump --input="https://localhost:9200" --output myfile

## Curator - Elasticsearch index management tool

Curator is a tool that allows you to perform index management tasks, such as:

- Close Indices
- Delete Indices
- Delete Snapshots
- Forcemerge segments
- Changing Index Settings
- Open Indices
- Reindex data

And other.

### Curator installation

Curator is delivered with the client node installer.

### Curator configuration

Create directory for configuration:

```bash
mkdir /etc/curator
```

Create directory for Curator logs file:

```bash
mkdir /var/log/curator
```

### Running Curator

The curator executable is located in the directory:

```bash
/usr/share/kibana/curator/bin/curator
```

Curator requires two parameters:

- config - path to configuration file for Curator
- path to action file for Curator

Example running command:

```bash
/usr/share/kibana/curator/bin/curator --config /etc/curator/curator.conf /etc/curator/close_indices.yml
```

### Sample configuration file

----------

Remember, leave a key empty if there is no value.  None will be a string, not a Python "NoneType"

```bash
client:
  hosts:
    - 127.0.0.1
  port: 9200
#  url_prefix:
#  use_ssl: False
#  certificate:
  client_cert:
  client_key:
  ssl_no_validate: False
  http_auth: $user:$passowrd
  timeout: 30
  master_only: True

logging:
  loglevel: INFO
  logfile: /var/log/curator/curator.log
  logformat: default
  blacklist: ['elasticsearch', 'urllib3']
```

### Sample action file

- close indices

  ```yaml
  actions:
    1:
      action: close
      description: >-
        Close indices older than 30 days (based on index name), for logstash-
        prefixed indices.
      options:
        delete_aliases: False
        timeout_override:
        continue_if_exception: False
        disable_action: True
      filters:
      - filtertype: pattern
        kind: prefix
        value: logstash-
        exclude:
      - filtertype: age
        source: name
        direction: older
        timestring: '%Y.%m.%d'
        unit: days
        unit_count: 30
        exclude:
  ```

- delete indices

  ```yaml
  actions:
    1:
      action: delete_indices
      description: >-
        Delete indices older than 45 days (based on index name), for logstash-
        prefixed indices. Ignore the error if the filter does not result in an
        actionable list of indices (ignore_empty_list) and exit cleanly.
      options:
        ignore_empty_list: True
        timeout_override:
        continue_if_exception: False
        disable_action: True
      filters:
      - filtertype: pattern
        kind: prefix
        value: logstash-
        exclude:
      - filtertype: age
        source: name
        direction: older
        timestring: '%Y.%m.%d'
        unit: days
        unit_count: 45
        exclude:
  ```

- forcemerge segments

  ```yaml
  actions:
    1:
      action: forcemerge
      description: >-
        forceMerge logstash- prefixed indices older than 2 days (based on index
        creation_date) to 2 segments per shard.  Delay 120 seconds between each
        forceMerge operation to allow the cluster to quiesce.
        This action will ignore indices already forceMerged to the same or fewer
        number of segments per shard, so the 'forcemerged' filter is unneeded.
      options:
        max_num_segments: 2
        delay: 120
        timeout_override:
        continue_if_exception: False
        disable_action: True
      filters:
      - filtertype: pattern
        kind: prefix
        value: logstash-
        exclude:
      - filtertype: age
        source: creation_date
        direction: older
        unit: days
        unit_count: 2
        exclude:
  ```

- open indices

  ```yaml
  actions:
    1:
      action: open
      description: >-
        Open indices older than 30 days but younger than 60 days (based on index
        name), for logstash- prefixed indices.
      options:
        timeout_override:
        continue_if_exception: False
        disable_action: True
      filters:
      - filtertype: pattern
        kind: prefix
        value: logstash-
        exclude:
      - filtertype: age
        source: name
        direction: older
        timestring: '%Y.%m.%d'
        unit: days
        unit_count: 30
        exclude:
      - filtertype: age
        source: name
        direction: younger
        timestring: '%Y.%m.%d'
        unit: days
        unit_count: 60
        exclude:
  ```

- replica reduce

  ```yaml
  actions:
    1:
      action: replicas
      description: >-
        Reduce the replica count to 0 for logstash- prefixed indices older than
        10 days (based on index creation_date)
      options:
        count: 0
        wait_for_completion: False
        timeout_override:
        continue_if_exception: False
        disable_action: True
      filters:
      - filtertype: pattern
        kind: prefix
        value: logstash-
        exclude:
      - filtertype: age
        source: creation_date
        direction: older
        unit: days
        unit_count: 10
        exclude:
  ```

## Cross-cluster Search

**Cross-cluster search** lets you run a single search request against one or more remote clusters. For example, you can use a cross-cluster search to filter and analyze log data stored on clusters in different data centers.

### Configuration

1. Use `_cluster` API to add least one remote cluster:

   ```bash
   curl -u user:password -X PUT "localhost:9200/_cluster/settings?pretty" -H 'Content-Type: application/json' -d'
   {
     "persistent": {
       "cluster": {
         "remote": {
           "cluster_one": {
             "seeds": [
               "192.168.0.1:9300"
             ]
           },
           "cluster_two": {
             "seeds": [
               "192.168.0.2:9300"
             ]
           }
         }
       }
     }
   }'
   ```

2. To search data in index `twitter` located on the `cluster_one` use following command:

   ```bash
   curl -u user:password -X GET "localhost:9200/cluster_one:twitter/_search?pretty" -H 'Content-Type: application/json' -d'
   {
     "query": {
       "match": {
         "user": "kimchy"
       }
     }
   }'
   ```

3. To search data in index `twitter` located on multiple clusters, use following command:

   ```bash
   curl -u user:password -X GET "localhost:9200/twitter,cluster_one:twitter,cluster_two:twitter/_search?pretty" -H 'Content-Type: application/json' -d'
   {
     "query": {
       "match": {
         "user": "kimchy"
       }
     }
   }'
   ```

4. Configure index pattern in Kibana GUI to discover data from multiple clusters:

   ```bash
   cluster_one:logstash-*,cluster_two:logstash-*
   ```

   ![](/media/media/image133.png)

### Security

Cross-cluster search uses the Elasticsearch transport layer (default 9300/tcp port) to exchange data.  To secure the transmission, encryption must be enabled for the transport layer.

Configuration is in the `/etc/elasticsearch/elastisearch.yml` file:

```bash
# Transport layer encryption
logserverguard.ssl.transport.enabled: true
logserverguard.ssl.transport.pemcert_filepath: "/etc/elasticsearch/ssl/certificate.crt"
logserverguard.ssl.transport.pemkey_filepath: "/etc/elasticsearch/ssl/certificate.key"
logserverguard.ssl.transport.pemkey_password: ""
logserverguard.ssl.transport.pemtrustedcas_filepath: "/etc/elasticsearch/ssl/rootCA.crt"

logserverguard.ssl.transport.enforce_hostname_verification: false
logserverguard.ssl.transport.resolve_hostname: false

```

 Encryption must be enabled on each cluster.

## Sync/Copy

The Sync/Copy module allows you to synchronize or copy data between two Elasticsearch clusters.
You can copy or synchronize selected indexes or indicate index pattern.

### Configuration

Before starting Sync/Copy, complete the source and target cluster data in the `Profile` and `Create profile`tab:

- Protocol - http or https;
- Host - IP address ingest node;
- Port - communication port (default 9200);
- Username - username that has permission to get data and save data to the cluster;
- Password - password of the above user
- Cluster name

![](/media/media/image134.png)

You can view or delete the profile in the `Profile List` tab.

### Synchronize data

To perform data synchronization, follow the instructions:

- go to the `Sync` tab;
- select `Source Profile`
- select `Destination Profile`
- enter the index pattern name in `Index pattern to sync`
- or use switch `Toggle to select between Index pattern or name` and enter indices name.
- to create synchronization task, press `Submit` button

![](/media/media/image135.png)

### Copy data

To perform data copy, follow the instructions:

- go to the `Copy` tab;
- select `Source Profile`
- select `Destination Profile`
- enter the index pattern name in `Index pattern to sync`
- or use switch `Toggle to select between Index pattern or name` and enter indices name.
- to start copying data press the `Submit` button

![](/media/media/image136.png)

### Running Sync/Copy

Prepared Copy/Sync tasks can be run on demand or according to a set schedule.
To do this, go to the `Jobs` tab. With each task you will find the `Action` button that allows:

- running the task;
- scheduling task in Cron format;
- deleting task;
- download task logs.

![](/media/media/image137.png)

## XLSX Import

The XLSX Import module allow to import your `xlsx` and `csv` file to indices.

### Importing steps

1. Go to XLSX Import module and select your file and sheet:

   ![](/media/media/image138.png)

2. After the data has been successfully loaded, you will see a preview of your data at the bottom of the window.

3. Press `Next` button.

4. In the next step, enter the index name in the `Index name` field, you can also change the pattern for the document ID and select the columns that the import will skip.

   ![](/media/media/image139.png)

5. Select the `Configure your own mapping` for every field. You can choose the type and apply more options with the advanced JSON.
   The list of parameters can be found here, https://www.elastic.co/guide/en/elasticsearch/reference/7.x/mapping-params.html

6. After the import configuration is complete, select the `Import` button to start the import process.

7. After the import process is completed, a summary will be displayed. Now you can create a new index pattern to view your data in the Discovery module.

   ![](/media/media/image140.png)

## Logtrail

LogTrail module allow to view, analyze, search and tail log events from multiple indices in realtime. Main features of this module are:

- View, analyze and search log events from a centralized interface
- Clean & simple devops friendly interface
- Live tail
- Filter aggregated logs by hosts and program
- Quickly seek to logs based on time
- Supports highlighting of search matches
- Supports multiple Elasticsearch index patterns each with different  schemas
- Can be extended by adding additional fields to log event
- Color coding of messages based on field values

Default Logtrail configuration, keeps track of event logs for Elasticsearch, Logstash, Kibana and Alert processes.
The module allows you to track events from any index stored in Elasticsearch.

### Configuration

The LogTrail module uses the Logstash pipeline to retrieve data from any of the event log files and save its contents to the Elasticsearch index.

### Logstash configuration

Example for the file `/var/log/messages`

1. Add the Logstash configuration file in the correct pipline (default is "logtrail"):

    ```bash
    vi /etc/logstash/conf.d/logtrail/messages.conf
    ```

    ```bash
    input {
        file {
            path => "/var/log/messages"
            start_position => beginning
            tags => "logtrail_messages"
        }
    }
    filter {
            if "logtrail_messages" in [tags] {
                    grok {
                            match => {
                                    #"message" => "%{SYSLOGTIMESTAMP:syslog_timestamp} %{SYSLOGHOST:hostname} %{DATA:program}(?:\[%{POSINT:pid}\])?: %{GREEDYDATA:syslog_message}"
    # If syslog is format is "<%PRI%><%syslogfacility%>%TIMESTAMP% %HOSTNAME% %syslogtag%%msg:::sp-if-no-1st-sp%%msg:::drop-last-lf%\n"
                                    "message" => "<?%{NONNEGINT:priority}><%{NONNEGINT:facility}>%{SYSLOGTIMESTAMP:syslog_timestamp} %{SYSLOGHOST:hostname} %{DATA:program}(?:\[%{POSINT:pid}\])?: %{GREEDYDATA:syslog_message}"
                                    }
                            }
                    date {
                            match => [ "syslog_timestamp", "MMM  d HH:mm:ss", "MMM dd HH:mm:ss" ]
                    }
                    ruby {
                            code =>  "event.set('level',event.get('priority').to_i - ( event.get('facility').to_i * 8 ))"
                    }
            }
    }
    output {
        if "logtrail_messages" in [tags] {
            elasticsearch {
                hosts => "http://localhost:9200"
                index => "logtrail-messages-%{+YYYY.MM}"
                user => "logstash"
                password => "logstash"
            }
        }
    }
    ```

2. Restart the Logstash service

   ```bahs
   systemctl restart logstash
   ```

### Kibana configuration

1. Set up a new pattern index `logtrail-messages*`  in the Energy Logserver configuration. The procedure is described in the chapter [First login](/02-00-00-Data_source_and_application_management/02-00-00-Data_source_and_application_management.md).

2. Add a new configuration section in the LogTrail configuration file:

   ```bash
   vi /usr/share/kibana/plugins/logtrail/logtrail.json
   ```

   ```bash
   {
     "index_patterns" : [
       {
         "es": {
           "default_index": "logstash-message-*",
           "allow_url_parameter": false
         },
         "tail_interval_in_seconds": 10,
         "es_index_time_offset_in_seconds": 0,
         "display_timezone": "Etc/UTC",
         "display_timestamp_format": "MMM DD HH:mm:ss",
         "max_buckets": 500,
         "default_time_range_in_days" : 0,
         "max_hosts": 100,
         "max_events_to_keep_in_viewer": 5000,
         "fields" : {
           "mapping" : {
               "timestamp" : "@timestamp",
               "display_timestamp" : "@timestamp",
               "hostname" : "hostname",
               "program": "program",
               "message": "syslog_message"
           },
           "message_format": "{{{syslog_message}}}"
         },
         "color_mapping" : {
           "field": "level",
           "mapping" : {
             "0": "#ff0000",
             "1": "#ff3232",
             "2": "#ff4c4c",
             "3": "#ff7f24",
             "4": "#ffb90f",
             "5": "#a2cd5a"
           }
         }
       }
     ]
   }

   ```

3. Restate the Kibana service

   ```bash
   systemctl restart kibana
   ```

### Using Logtrail

To access of the LogTrail module, click the tile icon from the main menu bar and then go to the „LogTrail” icon.

![](/media/media/image144.png)

The main module window contains the content of messages that are automatically updated.

![](/media/media/image145.png)

Below is the search and options bar.

![](/media/media/image146.png)

It allows you to search for event logs, define the systems from which events will be displayed, define the time range for events and define the index pattern.

## Logstash #

The Energy Logserver use Logstash service to dynamically unify data
from disparate sources and normalize the data into destination of your
choose. A Logstash pipeline has two required elements, *input* and *output*,
and one optional element *filter*. The input plugins consume data from a source, the filter plugins modify the data as you specify, and the output plugins write the data to a destination.
The default location of the Logstash plugin files is: */etc/logstash/conf.d/*. This location contain following Energy Logserver

Energy Logserver default plugins:

- `01-input-beats.conf`
- `01-input-syslog.conf`
- `01-input-snmp.conf`
- `01-input-http.conf`
- `01-input-file.conf`
- `01-input-database.conf`
- `020-filter-beats-syslog.conf`
- `020-filter-network.conf`
- `099-filter-geoip.conf`
- `100-output-elasticsearch.conf`
- `naemon_beat.example`
- `perflogs.example`

### Logstash - Input "beats" ##

This plugin wait for receiving data from remote beats services. It use tcp
/5044 port for communication:

```bash
                input {
                        beats {
                                port => 5044
                        }
                }
```

### Getting data from share folder

Using beats, you can reading data from FTP, SFTP, SMB share.
Connection to remote resources should be done as follows:

#### Input - FTP server

- Installation

  ```bash
  yum install curlftpfs
  ```

- Create mount ftp directory

  ```bash
  mkdir /mnt/my_ftp
  ```

- Use `curlftpfs` to mount your remote ftp site. Suppose my access credentials are as follows:

  ```bash
  urlftpfs ftp-user:ftp-pass@my-ftp-location.local /mnt/my_ftp/
  ```

#### Input - SFTP server

- Install the required packages

  ```bash
  yum install sshfs
  ```

- Add user

  ```bash
  sudo adduser yourusername fuse
  ```

- Create local folder

  ```bash
  mkdir ~/Desktop/sftp
  ```

- Mount remote folder to local:

  ```bash
  sshfs HOSTuser@remote.host.or.ip:/host/dir/to/mount ~/Desktop/sftp
  ```

#### Input - SMB/CIFS server

- Create local folder

  ```bash
  mkdir ~/Desktop/smb
  ```

- Mount remote folder to local:

  ```bash
  mount -t smbfs //remoate.host.or.ip/freigabe /mnt -o username=testuser
  ```

  or

  ```bash
  mount -t cifs //remoate.host.or.ip/freigabe /mnt -o username=testuser
  ```

### Logstash - Input "network" ##

This plugin read events over a TCP or UDP socket assigns the appropriate tags:

```bash
input {
       tcp {
               port => 5514
               type => "network"
               tags => [ "LAN", "TCP" ]
       }
       udp {
               port => 5514
               type => "network"
               tags => [ "LAN", "UDP" ]
       }
}
```

To redirect the default syslog port (514/TCP/UDP) to the dedicated collector port, follow these steps:

```bash
firewall-cmd --add-forward-port=port=514:proto=udp:toport=5514:toaddr=127.0.0.1 --permanent
firewall-cmd --add-forward-port=port=514:proto=tcp:toport=5514:toaddr=127.0.0.1 --permanent
firewall-cmd --reload
systemctl restart firewalld
```

### Logstash - Input SNMP

The SNMP input polls network devices using Simple Network Management Protocol (SNMP) to gather information related to the current state of the devices operation:

```bash
input {
  snmp {
    get => ["1.3.6.1.2.1.1.1.0"]
    hosts => [{host => "udp:127.0.0.1/161" community => "public" version => "2c"  retries => 2  timeout => 1000}]
  }
}
```

### Logstash - Input HTTP / HTTPS

Using this input you can receive single or multiline events over http(s). Applications can send an HTTP request to the endpoint started by this input and Logstash will convert it into an event for subsequent processing. Sample definition:

```bash
input {
  http {
    host => "0.0.0.0"
    port => "8080"
  }
}
```

Events are by default sent in plain text. You can enable encryption by setting ssl to true and configuring the ssl_certificate and ssl_key options:

```bash
input {
  http {
    host => "0.0.0.0"
    port => "8080"
    ssl => "true"
    ssl_certificate => "path_to_certificate_file"
    ssl_key => "path_to_key_file"
  }
}
```

### Logstash - Input Relp

#### Installation

For plugins not bundled by default, it is easy to install by running bin/logstash-plugin install logstash-input-relp.

#### Description

Read RELP events over a TCP socket.

This protocol implements application-level acknowledgments to help protect against message loss.

Message acks only function as far as messages being put into the queue for filters; anything lost after that point will not be retransmitted.

#### Relp input configuration options

This plugin supports the following configuration options plus the Common Options described later.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-9odp{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:bottom}
.tg .tg-pjk6{border-color:inherit;color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg" style="undefined;table-layout: fixed; width: 690px">
<colgroup>
<col style="width: 41px">
<col style="width: 192px">
<col style="width: 358px">
<col style="width: 99px">
</colgroup>
<thead>
  <tr>
    <th class="tg-9odp">Nr.</th>
    <th class="tg-9odp">Setting</th>
    <th class="tg-9odp">Input type</th>
    <th class="tg-9odp">Required</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pjk6">1</td>
    <td class="tg-pjk6">host</td>
    <td class="tg-pjk6">string</td>
    <td class="tg-pjk6">No</td>
  </tr>
  <tr>
    <td class="tg-pjk6">2</td>
    <td class="tg-pjk6">port</td>
    <td class="tg-pjk6">number</td>
    <td class="tg-pjk6">Yes</td>
  </tr>
  <tr>
    <td class="tg-pjk6">3</td>
    <td class="tg-pjk6">ssl_cacert</td>
    <td class="tg-pjk6">a valid filesystem path</td>
    <td class="tg-pjk6">No</td>
  </tr>
  <tr>
    <td class="tg-pjk6">4</td>
    <td class="tg-pjk6">ssl_cert</td>
    <td class="tg-pjk6">a valid filesystem path</td>
    <td class="tg-pjk6">No</td>
  </tr>
  <tr>
    <td class="tg-pjk6">5</td>
    <td class="tg-pjk6">ssl_enable</td>
    <td class="tg-pjk6">boolean</td>
    <td class="tg-pjk6">No</td>
  </tr>
  <tr>
    <td class="tg-pjk6">6</td>
    <td class="tg-pjk6">ssl_key</td>
    <td class="tg-pjk6">a valid filesystem path</td>
    <td class="tg-pjk6">No</td>
  </tr>
  <tr>
    <td class="tg-pjk6">7</td>
    <td class="tg-pjk6">ssl_key_passphrase</td>
    <td class="tg-pjk6">password</td>
    <td class="tg-pjk6">No</td>
  </tr>
  <tr>
    <td class="tg-pjk6">8</td>
    <td class="tg-pjk6">ssl_verify</td>
    <td class="tg-pjk6">string</td>
    <td class="tg-pjk6">boolean</td>
  </tr>
</tbody>
</table>

```host``` - The address to listen on.

```port``` - The port to listen on.

```ssl_cacert``` - The SSL CA certificate, chainfile or CA path. The system CA path is automatically included.

```ssl_cert``` - SSL certificate path

```ssl_enable``` - Enable SSL (must be set for other ssl_ options to take effect).

```ssl_key``` - SSL key path

```ssl_key_passphrase``` - SSL key passphrase

```ssl_verify``` - Verify the identity of the other end of the SSL connection against the CA. For input, sets the field sslsubject to that of the client certificate.

Common Options
The following configuration options are supported by all input plugins:

<table border="1" class="colwidths-given docutils" id="id1">
<colgroup>
<col width="2%" />
<col width="30%" />
<col width="50%" />
<col width="18%" />

</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Setting</th>
<th class="head">Input type</th>
<th class="head">Required</th>
</tr>
</thead>
<tbody valign="top">

<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last">add_field</p>
</td>
<td><p class="first last">hash</p>
</td>
<td><p class="first last">No</p>
</td>
</tr>

<tr class="row-even"><td><p class="first last">2</p>
</td>
<td><p class="first last">codec</p>
</td>
<td><p class="first last">codec</p>
</td>
<td><p class="first last">No</p>
</td>
</tr>

<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last">enable_metric</p>
</td>
<td><p class="first last">boolean</p>
</td>
<td><p class="first last">No</p>
</td>
</tr>

<tr class="row-even"><td><p class="first last">4</p>
</td>
<td><p class="first last">id</p>
</td>
<td><p class="first last">string</p>
</td>
<td><p class="first last">No</p>
</td>
</tr>

<tr class="row-even"><td><p class="first last">5</p>
</td>
<td><p class="first last">tags</p>
</td>
<td><p class="first last">array</p>
</td>
<td><p class="first last">No</p>
</td>
</tr>

<tr class="row-even"><td><p class="first last">6</p>
</td>
<td><p class="first last">type</p>
</td>
<td><p class="first last">string</p>
</td>
<td><p class="first last">No</p>
</td>
</tr>

</td>
</tr>

</tbody>
</table>

```add_field``` - Add a field to an event

```codec``` - The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

```enable_metric``` - Disable or enable metric logging for this specific plugin instance by default we record all the metrics we can, but you can disable metrics collection for a specific plugin.

```id``` - Add a unique ID to the plugin configuration. If no ID is specified, Logstash will generate one. It is strongly recommended to set this ID in your configuration. This is particularly useful when you have two or more plugins of the same type, for example, if you have 2 relp inputs. Adding a named ID in this case will help in monitoring Logstash when using the monitoring APIs.

```bash
input {
  relp {
    id => "my_plugin_id"
  }
}
```

```tags``` - add any number of arbitrary tags to your event.

```type``` - Add a type field to all events handled by this input.

Types are used mainly for filter activation.

The type is stored as part of the event itself, so you can also use the type to search for it in Kibana.

If you try to set a type on an event that already has one (for example when you send an event from a shipper to an indexer) then a new input will not override the existing type. A type set at the shipper stays with that event for its life even when sent to another Logstash server.

### Logstash - Input Kafka

This input will read events from a Kafka topic.

Sample definition:

```bash
input {
  kafka {
    bootstrap_servers => "10.0.0.1:9092"
    consumer_threads => 3

    topics => ["example"]
    codec => json
    client_id => "hostname"
    group_id => "logstash"
    max_partition_fetch_bytes => "30000000"
    max_poll_records => "1000"

    fetch_max_bytes => "72428800"
    fetch_min_bytes => "1000000"

    fetch_max_wait_ms => "800"

    check_crcs => false

  }
}
```

```bootstrap_servers``` - A list of URLs of Kafka instances to use for establishing the initial connection to the cluster. This list should be in the form of host1:port1,host2:port2 These urls are just used for the initial connection to discover the full cluster membership (which may change dynamically) so this list need not contain the full set of servers (you may want more than one, though, in case a server is down).

```consumer_threads``` - Ideally you should have as many threads as the number of partitions for a perfect balance — more threads than partitions means that some threads will be idle

```topics``` - A list of topics to subscribe to, defaults to ["logstash"].

```codec``` - The codec used for input data. Input codecs are a convenient method for decoding your data before it enters the input, without needing a separate filter in your Logstash pipeline.

```client_id``` - The id string to pass to the server when making requests. The purpose of this is to be able to track the source of requests beyond just ip/port by allowing a logical application name to be included.

```group_id``` - The identifier of the group this consumer belongs to. Consumer group is a single logical subscriber that happens to be made up of multiple processors. Messages in a topic will be distributed to all Logstash instances with the same group_id.

```max_partition_fetch_bytes``` - The maximum amount of data per-partition the server will return. The maximum total memory used for a request will be #partitions * max.partition.fetch.bytes. This size must be at least as large as the maximum message size the server allows or else it is possible for the producer to send messages larger than the consumer can fetch. If that happens, the consumer can get stuck trying to fetch a large message on a certain partition.

```max_poll_records``` - The maximum number of records returned in a single call to poll().

```fetch_max_bytes``` - The maximum amount of data the server should return for a fetch request. This is not an absolute maximum, if the first message in the first non-empty partition of the fetch is larger than this value, the message will still be returned to ensure that the consumer can make progress.

```fetch_min_bytes``` - The minimum amount of data the server should return for a fetch request. If insufficient data is available the request will wait for that much data to accumulate before answering the request.

```fetch_max_wait_ms``` - The maximum amount of time the server will block before answering the fetch request if there isn’t sufficient data to immediately satisfy fetch_min_bytes. This should be less than or equal to the timeout used in poll_timeout_ms.

```check_crcs``` - Automatically check the CRC32 of the records consumed. This ensures no on-the-wire or on-disk corruption to the messages occurred. This check adds some overhead, so it may be disabled in cases seeking extreme performance.

### Logstash - Input File

This plugin stream events from files, normally by tailing them in a manner similar to tail -0F but optionally reading them from the beginning. Sample definition:

```bash
file {
    path => "/tmp/access_log"
    start_position => "beginning"
}
```

### Logstash - Input database

This plugin can read data in any database with a JDBC interface into Logstash. You can periodically schedule ingestion using a cron syntax (see schedule setting) or run the query one time to load data into Logstash. Each row in the resultset becomes a single event. Columns in the resultset are converted into fields in the event.

#### Logasth input - MySQL

Download jdbc driver: [https://dev.mysql.com/downloads/connector/j/](https://dev.mysql.com/downloads/connector/j/)

Sample definition:

```bash
input {
  jdbc {
    jdbc_driver_library => "mysql-connector-java-5.1.36-bin.jar"
    jdbc_driver_class => "com.mysql.jdbc.Driver"
    jdbc_connection_string => "jdbc:mysql://localhost:3306/mydb"
    jdbc_user => "mysql"
    jdbc_password => "mysql"
    parameters => { "favorite_artist" => "Beethoven" }
    schedule => "* * * * *"
    statement => "SELECT * from songs where artist = :favorite_artist"
  }
}
```

#### Logasth input - MSSQL

Download jdbc driver: [https://docs.microsoft.com/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server?view=sql-server-ver15](https://docs.microsoft.com/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server?view=sql-server-ver15)

Sample definition:

```bash
input {
  jdbc {
    jdbc_driver_library => "./mssql-jdbc-6.2.2.jre8.jar"
    jdbc_driver_class => "com.microsoft.sqlserver.jdbc.SQLServerDriver"
    jdbc_connection_string => "jdbc:sqlserver://VB201001000;databaseName=Database;"
    jdbc_user => "mssql"
    jdbc_password => "mssql"
    jdbc_default_timezone => "UTC"
    statement_filepath => "/usr/share/logstash/plugin/query"
    schedule => "*/5 * * * *"
    sql_log_level => "warn"
    record_last_run => "false"
    clean_run => "true"
  }
}
```

#### Logstash input - Oracle

Download jdbc driver: [https://www.oracle.com/database/technologies/appdev/jdbc-downloads.html](https://www.oracle.com/database/technologies/appdev/jdbc-downloads.html)

Sample definition:

```bash
input {
  jdbc {
    jdbc_driver_library => "./ojdbc8.jar"
    jdbc_driver_class => "oracle.jdbc.driver.OracleDriver"
    jdbc_connection_string => "jdbc:oracle:thin:@hostname:PORT/SERVICE"
    jdbc_user => "oracle"
    jdbc_password => "oracle"
    parameters => { "favorite_artist" => "Beethoven" }
    schedule => "* * * * *"
    statement => "SELECT * from songs where artist = :favorite_artist"
  }
}
```

#### Logstash input - PostgreSQL

Download jdbc driver: [https://jdbc.postgresql.org/download.html](https://jdbc.postgresql.org/download.html)

Sample definition:

```bash
input {
    jdbc {
        jdbc_driver_library => "D:/postgresql-42.2.5.jar"
        jdbc_driver_class => "org.postgresql.Driver"
        jdbc_connection_string => "jdbc:postgresql://127.0.0.1:57610/mydb"
        jdbc_user => "myuser"
        jdbc_password => "mypw"
        statement => "select * from mytable"
    }
}
```

### Logstash - Input CEF

The common event format (CEF) is a standard for the interoperability of event or log generating devices and applications. The standard defines a syntax for log records. It comprises of a standard prefix and a variable extension that is formatted as key-value pairs.

```bash
input {
  tcp {
    codec => cef { delimiter => "\r\n" }
    port => 12345
  }
}
```

This setting allows the following character sequences to have special meaning:

- `\r` (backslash "r") - means carriage return (ASCII 0x0D)
- `\n` (backslash "n") - means newline (ASCII 0x0A)

### Logstash - Input OPSEC

FW1-LogGrabber is a Linux command-line tool to grab logfiles from remote Checkpoint devices. It makes extensive use of OPSEC Log Export APIs (LEA) from Checkpoint's [OPSEC SDK 6.0 for Linux 50](http://supportcontent.checkpoint.com/file_download?id=48148).

#### Build FW1-LogGrabber

FW1-LogGrabber v2.0 and above can be built on Linux x86/amd64 platforms only.

If you are interested in other platforms please check [FW1-LogGrabber v1.11.1 website](https://sourceforge.net/projects/fw1-loggrabber/files/fw1-loggrabber/1.11.1/)

#### Download dependencies

FW1-LogGrabber uses API-functions from Checkpoint's [OPSEC SDK 6.0 for Linux 50](http://supportcontent.checkpoint.com/file_download?id=48148).

You must take care of downloading the Checkpoint OPSEC SDK and extracting it inside the `OPSEC_SDK` folder.

You also need to install some required 32-bit libraries.

If you are using **Debian or Ubuntu**, please run:

```bash
sudo apt-get install gcc-multilib g++-multilib libelf-dev:i386 libpam0g:i386 zlib1g-dev:i386
```

If you are using **CentOS or RHEL**, please run:

```bash
sudo yum install gcc gcc-c++ make glibc-devel.i686 elfutils-libelf-devel.i686 zlib-devel.i686 libstdc++-devel.i686 pam-devel.i686
```

#### Compile source code

Building should be as simple as running GNU Make in the project root folder:

```bash
make
```

If the build process complains, you might need to tweak some variables inside the `Makefile` (e.g. `CC`, `LD` and `OPSEC_PKG_DIR`) according to your environment.

#### Install FW1-LogGrabber

To install FW1-LogGrabber into its default location `/usr/local/fw1-loggrabber` (defined by `INSTALL_DIR` variable), please run

```bash
sudo make install
```

#### Set environment variables

FW1-LogGraber makes use of two environment variables, which should be defined in the shell configuration files.

- `LOGGRABBER_CONFIG_PATH` defines a directory containing configuration files (`fw1-loggrabber.conf`, `lea.conf`). If the variable is not defined, the program expects to find these files in the current directory.
- `LOGGRABBER_TEMP_PATH` defines a directory where FW1-LogGrabber will store temporary files. If the variable is not defined, the program stores these files in the current directory.

Since the binary is dynamically linked to Checkpoint OPSEC libraries, please also add `/usr/local/fw1-loggrabber/lib` to `LD_LIBRARY_PATH` or to your dynamic linker configuration with

```bash
sudo echo /usr/local/fw1-loggrabber/lib > /etc/ld.so.conf.d/fw1-loggrabber.conf
sudo ldconfig
```

#### Configuration files

#### lea.conf file

Starting with version 1.11, FW1-LogGrabber uses the default connection configuration procedure for OPSEC applications. This includes server, port and authentication settings. From now on, all this parameters can only be configured using the configuration file `lea.conf` (see `--leaconfigfile` option to use a different LEA configuration file) and not using the command-line as before.

- `lea_server ip <IP address>` specifies the IP address of the FW1 management station, to which FW1-LogGrabber should connect to.

- `lea_server port <port number>` is the port on the FW1 management station to which FW1-LogGrabber should connect to (for unauthenticated connections only).

- `lea_server auth_port <port number>` is the port to be used for authenticated connection to your FW1 management station.

- `lea_server auth_type <authentication mechanism>` you can use this parameter to specify the authentication mechanism to be used (default is `sslca`); valid values are `sslca`, `sslca_clear`, `sslca_comp`, `sslca_rc4`, `sslca_rc4_comp`, `asym_sslca`, `asym_sslca_comp`, `asym_sslca_rc4`, `asym_sslca_rc4_comp`, `ssl`, `ssl_opsec`, `ssl_clear`, `ssl_clear_opsec`, `fwn1` and `auth_opsec`.

- `opsec_sslca_file <p12-file>` specify the location of the PKCS#12 certificate, when using authenticated connections.

- `opsec_sic_name <LEA client SIC name>` is the SIC name of the LEA client for authenticated connections.

- `lea_server opsec_entity_sic_name <LEA server SIC name>` is the SIC name of your FW1 management station when using authenticated connections.

#### fw1-loggrabber.conf file

This paragraph deals with the options that can be set within the configuration file. The default configuration file is `fw1-loggrabber.conf` (see `--configfile` option to use a different configuration file). The precedence of given options is as follows: command line, configuration file, default value. E.g. if you set the resolve-mode to be used in the configuration file, this can be overwritten by command line option `--noresolve`; only if an option isn't set neither on command line nor in the configuration file, the default value will be used.

- `DEBUG_LEVEL=<0-3>` sets the debug level to the specified value; zero means no output of debug information, and further levels will cause output of program specific as well as OPSEC specific debug information.

- `FW1_LOGFILE=<name of log file>` specifies the name of the FW1 logfile to be read; this can be either done exactly or using only a part of the filename; if no exact match can be found in the list of logfiles returned by the FW-1 management station, all logfiles which contain the specified string are processed; if this parameter is omitted, the default logfile `fw.log` will be processed.

- `FW1_OUTPUT=<files|logs>` specifies whether FW1-LogGrabber should only display the available logfiles (`files`) on the FW11 server or display the content of these logfiles (`logs`).

- `FW1_TYPE=<ng|2000>` choose which version of FW1 to connect to; for Checkpoint FW-1 5.0 you have to specify `NG` and for Checkpoint FW-1 4.1 you have to specify `2000`.

- `FW1_MODE=<audit|normal>` specifies whether to display `audit` logs, which contain administrative actions, or `normal` security logs, which contain data about dropped and accepted connections.

- `MODE=<online|online-resume|offline>` when using online mode, FW1-LogGrabber starts retrieving logging data from the end of the specified logfile and displays all future log entries (mainly used for continuously processing); the online-resume mode is similar to the online mode, but if FW1-LogGrabber is stopped and started again, it resumes processing from where it was stopped; if you instead choose the offline mode, FW1-LogGrabber quits after having displayed the last log entry.

- `RESOLVE_MODE=<yes|no>` with this option (enabled by default), IP addresses will be resolved to names using FW1 name resolving behaviour; this resolving mechanism will not cause the machine running FW1-LogGrabber to initiate DNS requests, but the name resolution will be done directly on the FW1 machine; if you disable resolving mode, IP addresses will be displayed in log output instead of names.

- `RECORD_SEPARATOR=<char>` can be used to change the default record separator `|` (pipe) into another character; if you choose a character which is contained in some log data, the occurrence within the logdata will be escaped by a backslash.

- `LOGGING_CONFIGURATION=<screen|file|syslog>` can be used for redirecting logging output to other destinations than the default destination `STDOUT`; currently it is possible to redirect output to a file or to the syslog daemon.

- `OUTPUT_FILE_PREFIX=<prefix of output file>` when using file output, this parameter defines a prefix for the output filename; default value is simply `fw1-loggrabber`.

- `OUTPUT_FILE_ROTATESIZE=<rotatesize in bytes>` when using file output, this parameter specifies the maximum size of the output files, before they will be rotated with suffix `-YYYY-MM-DD-hhmmss[-x].log`; default value is 1048576 bytes, which equals 1 MB; setting a zero value disables file rotation.

- `SYSLOG_FACILITY=<USER|LOCAL0|...|LOCAL7>` when using syslog output, this parameter sets the syslog facility to be used.

- `FW1_FILTER_RULE="<filterexpression1>[;<filterexpression2>]"` defines filters for `normal` log mode; you can find a more detailed description of filter rules, along with some examples, [in a separate chapter below](#filtering).

- `AUDIT_FILTER_RULE="<filterexpression1>[;<filterexpression2>]"` defines filters for `audit` log mode; you can find a more detailed description of filter rules, along with some examples, [in a separate chapter below](#filtering).

#### Command line options

In the following section, all available command line options are described in detail. Most of the options can also be configured using the file `fw1-loggrabber.conf` (see `--configfile` option to use a different configuration file). The precedence of given options is as follows: command line, configuration file, default value. E.g. if you set the resolve-mode to be used in the configuration file, this can be overwritten by command line option `--noresolve`; only if an option isn't set neither on command line nor in the configuration file, the default value will be used.

#### Help

Use `--help` to display basic help and usage information.

#### Debug level

The `--debuglevel` option sets the debug level to the specified value. A zero debug level means no output of debug information, while further levels will cause output of program specific as well as OPSEC specific debug
information.

#### Location of configuration files

The `-c <configfilename>` or `--configfile <configfilename>` options allow to specify a non-default configuration file, in which most of the command line options can be configured, as well as other options which are not available as command line parameters.

If this parameter is omitted, the file `fw1-loggrabber.conf` inside `$LOGGRABBER_CONFIG_PATH` will be used. [See above](#fw1-loggrabberconf-file) for a description of all available configuration file options.

Using `-l <leaconfigfilename>` or `--leaconfigfile <leaconfigfilename>` instead, it's possible to use a non-default LEA configuration file. In this file, all connection parameters such as FW1 server, port, authentication method as well as SIC names have to be configured, as usual procedure for OPSEC applications.

If this parameter is omitted, the file `lea.conf` inside `$LOGGRABBER_CONFIG_PATH` will be used. [See above](#leaconf-file) for a description of all available LEA configuration file options.

#### Remote log files

With `-f <logfilename|pattern|ALL>` or `--logfile <logfilename|pattern|ALL>` you can specify the name of the remote FW1 logfile to be read.

This can be either done exactly or using only a part of the filename. If no exact match can be found in the list of logfiles returned by the FW1 management station, all logfiles which contain the specified string are processed.

A special case is the usage of `ALL` instead of a logfile name or pattern. In that case all logfiles that are available on the management station, will be processed. If this parameter is omitted, only the default logfile `fw.log` will be processed.

The first example displays the logfile `2003-03-27_213652.log`, while the second one processes all logfiles which contain `2003-03` in their filename.

```bash
--logfile 2003-03-27_213652.log
--logfile 2003-03
```

The default behaviour of FW1-LogGrabber is to display the content of the logfiles and not just their names. This can be explicitely specified using the `--showlogs` option.

The option `--showfiles` can be used instead to simply show the available logfiles on the FW1 management station. After the names of the logfiles have been displayed, FW1-LogGrabber quits.

#### Name resolving behaviour

Using the `--resolve` option, IP addresses will be resolved to names using FW1 name resolving behaviour. This resolving mechanism will not cause the machine running FW1-LogGrabber to initiate DNS requests, but the name resolution will be done directly on the FW1 machine.

This is the default behavior of FW1-LogGrabber which can be disabled by using `--no-resolve`. That option will cause IP addresses to be displayed in log output instead of names.

#### Checkpoint firewall version

The default FW1 version, for which this tool is being developed, is Checkpoint FW1 5.0 (NG) and above. If no other version is explicitly specified, the default version is `--ng`.

The option `--2000` has to be used if you want to connect to older Checkpoint FW1 4.1 (2000) firewalls. You should keep in mind that some options are not available for non-NG firewalls; these include `--auth`, `--showfiles`, `--auditlog` and some more.

#### Online and Online-Resume modes

Using `--online` mode, FW1-LogGrabber starts output of logging data at the end of the specified logfile (or `fw.log` if no logfile name has been specified). This mode is mainly used for continuously processing FW1 log data and continues to display log entries also after scheduled and manual log switches. If you use `--logfile` to specify another logfile to be processed, you have to consider that no data will be shown, if the file isn't active anymore.

The `--online-resume` mode is similar to the above online mode, but starts output of logging data at the last known processed position (which is stored inside a cursor).

In contrast to online mode, when using `--offline` mode FW1-LogGrabber quits after having displayed the last log entry. This is the default behavior and is mainly used for analysis of historic log data.

#### Audit and normal logs

Using the `--auditlog` mode, the content of the audit logfile (`fw.adtlog`) can be displayed. This includes administrator actions and uses different fields than normal log data.

The default `--normallog` mode of FW1-LogGrabber processes normal FW1 logfiles. In contrast to the `--auditlog` option, no administrative actions are displayed in this mode, but all regular log data is.

#### Filtering

Filter rules provide the possibility to display only log entries that match a given set of rules. There can be specified one or more filter rules using one or multiple `--filter` arguments on the command line.

All individual filter rules are related by OR. That means a log entry will be displayed if at least one of the filter rules matches. You can specify multiple argument values by separating the values by `,` (comma).

Within one filter rule, there can be specified multiple arguments that have to be separated by `;` (semi-colon). All these arguments are related by AND. That means a filter rule matches a given log entry only, if all of the filter arguments match.

If you specify `!=` instead of `=` between the name and value of the filter argument, you can negate the name/value pair.

For arguments that expect IP addresses, you can specify either a single IP address, multiple IP addresses separated by `,` (comma), or a network address with netmask (e.g. `10.0.0.0/255.0.0.0`). Currently, it is not possible to specify a network address and a single IP address within the same filter argument.

#### Supported filter arguments

Normal mode:

```bash
action=<ctl|accept|drop|reject|encrypt|decrypt|keyinst>
dst=<IP address>
endtime=<YYYYMMDDhhmmss>
orig=<IP address>
product=<VPN-1 & FireWall-1|SmartDefense>
proto=<icmp|tcp|udp>
rule=<rulenumber|startrule-endrule>
service=<portnumber|startport-endport>
src=<IP address>
starttime=<YYYYMMDDhhmmss>
```

Audit mode:

```bash
action=<ctl|accept|drop|reject|encrypt|decrypt|keyinst>
administrator=<string>
endtime=<YYYYMMDDhhmmss>
orig=<IP address>
product=<SmartDashboard|Policy Editor|SmartView Tracker|SmartView Status|SmartView Monitor|System Monitor|cpstat_monitor|SmartUpdate|CPMI Client>
starttime=<YYYYMMDDhhmmss>
```

#### Example filters

Display all dropped connections:

```bash
--filter "action=drop"
```

Display all dropped and rejected connections:

```bash
--filter "action=drop,reject"
--filter "action!=accept"
```

Display all log entries generated by rules 20 to 23:

```bash
--filter "rule=20,21,22,23"
--filter "rule=20-23"
```

Display all log entries generated by rules 20 to 23, 30 or 40 to 42:

```bash
--filter "rule=20-23,30,40-42"
```

Display all log entries to `10.1.1.1` and `10.1.1.2`:

```bash
--filter "dst=10.1.1.1,10.1.1.2"
```

Display all log entries from `192.168.1.0/255.255.255.0`:

```bash
--filter "src=192.168.1.0/255.255.255.0"
```

Display all log entries starting from `2004/03/02 14:00:00`:

```bash
--filter "starttime=20040302140000"
```

#### Checkpoint device configuration

Modify `$FWDIR/conf/fwopsec.conf` and define the port to be used for authenticated LEA connections (e.g. 18184):

```bash
lea_server port 0
lea_server auth_port 18184
lea_server auth_type sslca
```

Restart in order to activate changes:

```bash
cpstop; cpstart
```

Create a new OPSEC Application Object with the following details:

```bash
Name: e.g. myleaclient
Vendor: User Defined
Server Entities: None
Client Entities: LEA
```

Initialize Secure Internal Communication (SIC) for recently created OPSEC Application Object and enter (and remember) the activation key (e.g. `def456`).

Write down the DN of the recently created OPSEC Application Object; this is your Client Distinguished Name, which you need later on.

Open the object of your FW1 management server and write down the DN of that object; this is the Server Distinguished Name, which you will need later on.

Add a rule to the policy to allow the port defined above as well as port 18210/tcp (FW1_ica_pull) in order to allow pulling of PKCS#12 certificate by the FW1-LogGrabber machine from the FW1 management server. Port 18210/tcp can be shut down after the communication between FW1-LogGrabber and the FW1 management server has been established successfully.

Finally, install the policy.

#### FW1-LogGrabber configuration

Modify `$LOGGRABBER_CONFIG_PATH/lea.conf` and define the IP address of your FW1 management station (e.g. `10.1.1.1`) as well as port (e.g. `18184`), authentication type and SIC names for authenticated LEA
connections. You can get the SIC names from the object properties of your LEA client object, respectively the
Management Station object (see above for details about Client DN and Server DN).

```bash
lea_server ip 10.1.1.1
lea_server auth_port 18184
lea_server auth_type sslca
opsec_sslca_file opsec.p12
opsec_sic_name "CN=myleaclient,O=cpmodule..gysidy"
lea_server opsec_entity_sic_name "cn=cp_mgmt,o=cpmodule..gysidy"
```

Get the tool `opsec_pull_cert` either from `opsec-tools.tar.gz` from the project home page or directly from the OPSEC SDK. This tool is needed to establish the Secure Internal Communication (SIC) between FW1-LogGrabber and the FW1 management server.

Get the clients certificate from the management station (e.g. `10.1.1.1`). The activation key has to be the same as specified before in the firewall policy. After that, copy the resulting PKCS#12 file (default name `opsec.p12`) to your FW1-LogGrabber directory.

```bash
opsec_pull_cert -h 10.1.1.1 -n myleaclient -p def456
```

#### Authenticated SSL OPSEC connections

#### Checkpoint device configuration

Modify `$FWDIR/conf/fwopsec.conf` and define the port to be used for authenticated LEA connections (e.g. 18184):

```bash
lea_server port 0
lea_server auth_port 18184
lea_server auth_type ssl_opsec
```

Restart in order to activate changes:

```bash
cpstop; cpstart
```

Set a password (e.g. `abc123`) for the LEA client (e.g. `10.1.1.2`):

```bash
fw putkey -ssl -p abc123 10.1.1.2
```

Create a new OPSEC Application Object with the following details:

```bash
Name: e.g. myleaclient
Vendor: User Defined
Server Entities: None
Client Entities: LEA
```

Initialize Secure Internal Communication (SIC) for recently created OPSEC Application Object and enter (and remember) the activation key (e.g. `def456`).

Write down the DN of the recently created OPSEC Application Object; this is your Client Distinguished Name, which you need later on.

Open the object of your FW1 management server and write down the DN of that object; this is the Server Distinguished Name, which you will need later on.

Add a rule to the policy to allow the port defined above as well as port 18210/tcp (FW1_ica_pull) in order to allow pulling of PKCS#12 certificate from the FW1-LogGrabber machine to the FW1 management server. The port 18210/tcp can be shut down after the communication between FW1-LogGrabber and the FW1 management server has
been established successfully.

Finally, install the policy.

#### FW1-LogGrabber configuration

Modify `$LOGGRABBER_CONFIG_PATH/lea.conf` and define the IP address of your FW1 management station (e.g. `10.1.1.1`) as well as port (e.g. `18184`), authentication type and SIC names for authenticated LEA connections. The SIC names you can get from the object properties of your LEA client object respectively the Management Station object (see above for details about Client DN and Server DN).

```bash
lea_server ip 10.1.1.1
lea_server auth_port 18184
lea_server auth_type ssl_opsec
opsec_sslca_file opsec.p12
opsec_sic_name "CN=myleaclient,O=cpmodule..gysidy"
lea_server opsec_entity_sic_name "cn=cp_mgmt,o=cpmodule..gysidy"
```

Set password for the connection to the LEA server. The password has to be the same as specified on the LEA server.

```bash
opsec_putkey -ssl -p abc123 10.1.1.1
```

Get the tool `opsec_pull_cert` either from `opsec-tools.tar.gz` from the project home page or directly from the OPSEC SDK. This tool is needed to establish the Secure Internal Communication (SIC) between FW1-LogGrabber and the FW1 management server.

Get the clients certificate from the management station (e.g. `10.1.1.1`). The activation key has to be the same as specified before in the firewall policy.

```bash
opsec_pull_cert -h 10.1.1.1 -n myleaclient -p def456
```

#### Authenticated OPSEC connections

#### Checkpoint device configuration

Modify `$FWDIR/conf/fwopsec.conf` and define the port to be used for authenticated LEA connections (e.g. 18184):

```bash
lea_server port 0
lea_server auth_port 18184
lea_server auth_type auth_opsec
```

Restart in order to activate changes

```bash
fwstop; fwstart
```

Set a password (e.g. `abc123`) for the LEA client (e.g. `10.1.1.2`).

```bash
fw putkey -opsec -p abc123 10.1.1.2
```

Add a rule to the policy to allow the port defined above from the FW1-LogGrabber machine to the FW1 management
server.

Finally, install the policy.

#### FW1-LogGrabber configuration

Modify `$LOGGRABBER_CONFIG_PATH/lea.conf` and define the IP address of your FW1 management station (e.g. `10.1.1.1`) as well as the port (e.g. 18184) and authentication type for authenticated LEA connections:

```bash
lea_server ip 10.1.1.1
lea_server auth_port 18184
lea_server auth_type auth_opsec
```

Set password for the connection to the LEA server. The password has to be the same as specified on the LEA server.

```bash
opsec_putkey -p abc123 10.1.1.1
```

#### Unauthenticated connections

#### Checkpoint device configuration

Modify `$FWDIR/conf/fwopsec.conf` and define the port to be used for unauthenticated LEA connections (e.g. 50001):

```bash
lea_server port 50001
lea_server auth_port 0
```

Restart in order to activate changes:

```bash
fwstop; fwstart  # for 4.1
cpstop; cpstart  # for NG
```

Add a rule to the policy to allow the port defined above from the FW1-LogGrabber machine to the FW1 management
server.

Finally, install the policy.

#### FW1-LogGrabber configuration

Modify `$LOGGRABBER_CONFIG_PATH/lea.conf` and define the IP address of your FW1 management station (e.g. `10.1.1.1`) and port (e.g. `50001`) for unauthenticated LEA connections:

```bash
lea_server ip 10.1.1.1
lea_server port 50001
```

### Logstash - Input SDEE

This [Logstash](https://github.com/elasticsearch/logstash) input plugin allows you to call a Cisco SDEE/CIDEE HTTP API, decode the output of it into event(s), and send them on their merry way. The idea behind this plugins came from a need to gather events from Cisco security devices and feed them to ELK stack

#### Download

Only support for Logstash core 5.6.4.

Download link: https://rubygems.org/gems/logstash-input-sdee

#### Installation

```bash
gem install logstash-input-sdee-0.7.8.gem
```

#### Configuration

You need to import host SSL certificate in Java trust store to be able to connect to Cisco IPS device.

- Get server certificate from IPS device:

  ```bash
  echo | openssl s_client -connect ciscoips:443 2>&1 | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > cert.pem
  ```

- Import it into Java ca certs:

  ```bash
  $JAVA_HOME/bin/keytool -keystore $JAVA_HOME/lib/security/cacerts -importcert -alias ciscoips -file cert.pem
  ```

- Verify if import was successful:

  ```bash
  $JAVA_HOME/bin/keytool -keystore $JAVA_HOME/lib/security/cacerts -list
  ```

- Setup the Logstash input config with SSL connection:

  ```bash
  input {
    sdee {
      interval => 60
      http => {
        truststore_password => "changeit"
        url => "https://10.0.2.1"
        auth => {
          user => "cisco"
          password => "p@ssw0rd"
        }
      }
    }
  }
  ```

### Logstash - Input XML

To download xml files via Logstash use input "file", and set the location of the files in the configuration file:

```bash
file {
       path => [ "/etc/logstash/files/*.xml" ]
       mode => "read"
  }
```

The XML filter takes a field that contains XML and expands it into an actual datastructure.

```bash
filter {
      xml {
        source => "message"
      }
    }
```

More configuration options you can find: https://www.elastic.co/guide/en/logstash/6.8/plugins-filters-xml.html#plugins-filters-xml-options

### Logstash - Input WMI

The Logstash input **wmi** allow to collect data from WMI query. This is useful for collecting performance metrics and other data which is accessible via WMI on a Windows host.

#### Installation

For plugins not bundled by default, it is easy to install by running:

`/usr/share/logstash/bin/logstash-plugin install logstash-input-wmi`

#### Configuration

Configuration example:

```ruby
input {
      wmi {
        query => "select * from Win32_Process"
        interval => 10
      }
      wmi {
        query => "select PercentProcessorTime from Win32_PerfFormattedData_PerfOS_Processor where name = '_Total'"
      }
      wmi { # Connect to a remote host
        query => "select * from Win32_Process"
        host => "MyRemoteHost"
        user => "mydomain\myuser"
        password => "Password"
      }
    }
```

More about parameters: [https://www.elastic.co/guide/en/logstash/6.8/plugins-inputs-wmi.html#plugins-inputs-wmi-options](https://www.elastic.co/guide/en/logstash/6.8/plugins-inputs-wmi.html#plugins-inputs-wmi-options)

### Logstash - Filter "beats syslog" ##

This filter processing an event data with syslog type:

```bash
filter {
  if [type] == "syslog" {
    grok {
      match => {
        "message" => [
          # auth: ssh|sudo|su

          "%{SYSLOGTIMESTAMP:[system][auth][timestamp]} %{SYSLOGHOST:[system][auth][hostname]} sshd(?:\[%{POSINT:[system][auth][pid]}\])?: %{DATA:[system][auth][ssh][event]} %{DATA:[system][auth][ssh][method]} for (invalid user )?%{DATA:[system][auth][user]} from %{IPORHOST:[system][auth][ssh][ip]} port %{NUMBER:[system][auth][ssh][port]} ssh2(: %{GREEDYDATA:[system][auth][ssh][signature]})?",

          "%{SYSLOGTIMESTAMP:[system][auth][timestamp]} %{SYSLOGHOST:[system][auth][hostname]} sshd(?:\[%{POSINT:[system][auth][pid]}\])?: %{DATA:[system][auth][ssh][event]} user %{DATA:[system][auth][user]} from %{IPORHOST:[system][auth][ssh][ip]}",

          "%{SYSLOGTIMESTAMP:[system][auth][timestamp]} %{SYSLOGHOST:[system][auth][hostname]} sshd(?:\[%{POSINT:[system][auth][pid]}\])?: Did not receive identification string from %{IPORHOST:[system][auth][ssh][dropped_ip]}",

          "%{SYSLOGTIMESTAMP:[system][auth][timestamp]} %{SYSLOGHOST:[system][auth][hostname]} sudo(?:\[%{POSINT:[system][auth][pid]}\])?: \s*%{DATA:[system][auth][user]} :( %{DATA:[system][auth][sudo][error]} ;)? TTY=%{DATA:[system][auth][sudo][tty]} ; PWD=%{DATA:[system][auth][sudo][pwd]} ; USER=%{DATA:[system][auth][sudo][user]} ; COMMAND=%{GREEDYDATA:[system][auth][sudo][command]}",

          "%{SYSLOGTIMESTAMP:[system][auth][timestamp]} %{SYSLOGHOST:[system][auth][hostname]} %{DATA:[system][auth][program]}(?:\[%{POSINT:[system][auth][pid]}\])?: %{GREEDYMULTILINE:[system][auth][message]}",

          # add/remove user or group
          "%{SYSLOGTIMESTAMP:[system][auth][timestamp]} %{SYSLOGHOST:[system][auth][hostname]} groupadd(?:\[%{POSINT:[system][auth][pid]}\])?: new group: name=%{DATA:system.auth.groupadd.name}, GID=%{NUMBER:system.auth.groupadd.gid}",

          "%{SYSLOGTIMESTAMP:[system][auth][timestamp]} %{SYSLOGHOST:[system][auth][hostname]} userdel(?:\[%{POSINT:[system][auth][pid]}\])?: removed group '%{DATA:[system][auth][groupdel][name]}' owned by '%{DATA:[system][auth][group][owner]}'",

          "%{SYSLOGTIMESTAMP:[system][auth][timestamp]} %{SYSLOGHOST:[system][auth][hostname]} useradd(?:\[%{POSINT:[system][auth][pid]}\])?: new user: name=%{DATA:[system][auth][user][add][name]}, UID=%{NUMBER:[system][auth][user][add][uid]}, GID=%{NUMBER:[system][auth][user][add][gid]}, home=%{DATA:[system][auth][user][add][home]}, shell=%{DATA:[system][auth][user][add][shell]}$",

          "%{SYSLOGTIMESTAMP:[system][auth][timestamp]} %{SYSLOGHOST:[system][auth][hostname]} userdel(?:\[%{POSINT:[system][auth][pid]}\])?: delete user '%{WORD:[system][auth][user][del][name]}'$",

          "%{SYSLOGTIMESTAMP:[system][auth][timestamp]} %{SYSLOGHOST:[system][auth][hostname]} usermod(?:\[%{POSINT:[system][auth][pid]}\])?: add '%{WORD:[system][auth][user][name]}' to group '%{WORD:[system][auth][user][memberof]}'",

          # yum install/erase/update package
         "%{SYSLOGTIMESTAMP:[system][auth][timestamp]} %{DATA:[system][package][action]}: %{NOTSPACE:[system][package][name]}"
        ]
      }
      pattern_definitions => {
        "GREEDYMULTILINE"=> "(.|\n)*"
      }
    }

    date {
      match => [ "[system][auth][timestamp]", "MMM  d HH:mm:ss", "MMM dd HH:mm:ss" ]
      target => "[system][auth][timestamp]"
    }

    mutate {
      convert => { "[system][auth][pid]" => "integer" }
      convert => { "[system][auth][groupadd][gid]" => "integer" }
      convert => { "[system][auth][user][add][uid]" => "integer" }
      convert => { "[system][auth][user][add][gid]" => "integer" }
    }
  }
}
```

### Logstash - Filter "network" ##

This filter processing event data with network type:

```bash
filter {
  if [type] == "network" {
    grok {
      named_captures_only => true
      match => {
        "message" => [

          # Cisco Firewall
          "%{SYSLOG5424PRI}%{NUMBER:log_sequence#}:%{SPACE}%{IPORHOST:device_ip}: (?:.)?%{CISCOTIMESTAMP:log_data} CET: %%{CISCO_REASON:facility}-%{INT:severity_level}-%{CISCO_REASON:facility_mnemonic}:%{SPACE}%{GREEDYDATA:event_message}",

          # Cisco Routers
          "%{SYSLOG5424PRI}%{NUMBER:log_sequence#}:%{SPACE}%{IPORHOST:device_ip}: (?:.)?%{CISCOTIMESTAMP:log_data} CET: %%{CISCO_REASON:facility}-%{INT:severity_level}-%{CISCO_REASON:facility_mnemonic}:%{SPACE}%{GREEDYDATA:event_message}",

          # Cisco Switches
          "%{SYSLOG5424PRI}%{NUMBER:log_sequence#}:%{SPACE}%{IPORHOST:device_ip}: (?:.)?%{CISCOTIMESTAMP:log_data} CET: %%{CISCO_REASON:facility}-%{INT:severity_level}-%{CISCO_REASON:facility_mnemonic}:%{SPACE}%{GREEDYDATA:event_message}",
          "%{SYSLOG5424PRI}%{NUMBER:log_sequence#}:%{SPACE}(?:.)?%{CISCOTIMESTAMP:log_data} CET: %%{CISCO_REASON:facility}-%{INT:severity_level}-%{CISCO_REASON:facility_mnemonic}:%{SPACE}%{GREEDYDATA:event_message}",

          # HP switches
          "%{SYSLOG5424PRI}%{SPACE}%{CISCOTIMESTAMP:log_data} %{IPORHOST:device_ip} %{CISCO_REASON:facility}:%{SPACE}%{GREEDYDATA:event_message}"
        ]

      }
    }

    syslog_pri { }

    if [severity_level] {
      translate {
        dictionary_path => "/etc/logstash/dictionaries/cisco_syslog_severity.yml"
        field => "severity_level"
        destination => "severity_level_descr"
      }
    }

    if [facility] {
      translate {
        dictionary_path => "/etc/logstash/dictionaries/cisco_syslog_facility.yml"
        field => "facility"
        destination => "facility_full_descr"
      }
    }

    #ACL
    if [event_message] =~ /(\d+.\d+.\d+.\d+)/ {
      grok {
        match => {
          "event_message" => [
            "list %{NOTSPACE:[acl][name]} %{WORD:[acl][action]} %{WORD:[acl][proto]} %{IP:[src][ip]}.*%{IP:[dst][ip]}",
            "list %{NOTSPACE:[acl][name]} %{WORD:[acl][action]} %{IP:[src][ip]}",
            "^list %{NOTSPACE:[acl][name]} %{WORD:[acl][action]} %{WORD:[acl][proto]} %{IP:[src][ip]}.*%{IP:[dst][ip]}"
          ]
        }
      }
    }

    if [src][ip] {

      cidr {
        address => [ "%{[src][ip]}" ]
        network => [ "0.0.0.0/32", "10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16", "fc00::/7", "127.0.0.0/8", "::1/128", "169.254.0.0/16", "fe80::/10","224.0.0.0/4", "ff00::/8","255.255.255.255/32"  ]
        add_field => { "[src][locality]" => "private" }
      }

      if ![src][locality] {
        mutate {
          add_field => { "[src][locality]" => "public" }
        }
      }
    }


    if [dst][ip] {
      cidr {
        address => [ "%{[dst][ip]}" ]
        network => [ "0.0.0.0/32", "10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16", "fc00::/7", "127.0.0.0/8", "::1/128", "169.254.0.0/16", "fe80::/10","224.0.0.0/4", "ff00::/8","255.255.255.255/32" ]
        add_field => { "[dst][locality]" => "private" }
      }

      if ![dst][locality] {
        mutate {
          add_field => { "[dst][locality]" => "public" }
        }
      }
    }

    # date format
    date {
      match => [ "log_data", "MMM dd HH:mm:ss", "MMM  dd HH:mm:ss","MMM dd HH:mm:ss.SSS", "MMM  dd HH:mm:ss.SSS", "ISO8601" ]
      target => "log_data"
    }

  }
}
```

### Logstash - Filter "geoip" ##

This filter processing an events data with IP address and check localization:

```bash
filter {
  if [src][locality] == "public" {

    geoip {
      source => "[src][ip]"
      target => "[src][geoip]"
      database => "/etc/logstash/geoipdb/GeoLite2-City.mmdb"
      fields => [ "city_name", "country_name", "continent_code", "country_code2", "location" ]
      remove_field => [ "[src][geoip][ip]" ]
    }

    geoip {
      source => "[src][ip]"
      target => "[src][geoip]"
      database => "/etc/logstash/geoipdb/GeoLite2-ASN.mmdb"
      remove_field => [ "[src][geoip][ip]" ]
    }

  }

  if [dst][locality] == "public" {

    geoip {
      source => "[dst][ip]"
      target => "[dst][geoip]"
      database => "/etc/logstash/geoipdb/GeoLite2-City.mmdb"
      fields => [ "city_name", "country_name", "continent_code", "country_code2", "location" ]
      remove_field =>  [ "[dst][geoip][ip]" ]
    }

    geoip {
      source => "[dst][ip]"
      target => "[dst][geoip]"
      database => "/etc/logstash/geoipdb/GeoLite2-ASN.mmdb"
      remove_field => [ "[dst][geoip][ip]" ]
    }
  }

}
```

### Logstash - avoiding duplicate documents

To avoid duplicating the same documents, e.g. if the collector receives the entire event log file on restart, prepare the Logstash filter as follows:

1. Use the **fingerprint** Logstash filter to create consistent hashes of one or more fields whose values are unique for the document and store the result in a new field, for example:

   ```bash
   fingerprint {
                           source => [ "log_name", "record_number" ]
                           target => "generated_id"
                           method => "SHA1"
                   }

   ```

   - source - The name(s) of the source field(s) whose contents will be used to create the fingerprint
   - target - The name of the field where the generated fingerprint will be stored. Any current contents of that field will be overwritten.
   - method - If set to `SHA1`, `SHA256`, `SHA384`, `SHA512`, or `MD5` and a key is set, the cryptographic hash function with the same name will be used to generate the fingerprint. When a key set, the keyed-hash (HMAC) digest function will be used.

2. In the **elasticsearch** output set the **document_id** as the value of the **generated_id** field:

   ```bash
   elasticsearch {
                   hosts => ["http://localhost:9200"]
                   user => "logserver"
                   password => "logserver"
                   index => "syslog_wec-%{+YYYY.MM.dd}"
                   document_id => "%{generated_id}"
           }
   ```

   - document_id - The document ID for the index. Useful for overwriting existing entries in Elasticsearch with the same ID.

Documents having the same document_id will be indexed only once.

### Logstash data enrichment

It is possible to enrich the events that go to the logstash filters with additional fields, the values of which come from the following sources:

- databases, using the `jdbc` plugin;
- Active Directory or OpenLdap, using the `logstash-filter-ldap` plugin;
- dictionary files, using the `translate` plugin;
- external systems using their API, e.g. OP5 Monitor/Nagios

#### Filter `jdbc`

This filter executes a SQL query and store the result set in the field specified as `target`. It will cache the results locally in an LRU cache with expiry.

For example, you can load a row based on an id in the event:

```bahs
filter {
  jdbc_streaming {
    jdbc_driver_library => "/path/to/mysql-connector-java-5.1.34-bin.jar"
    jdbc_driver_class => "com.mysql.jdbc.Driver"
    jdbc_connection_string => "jdbc:mysql://localhost:3306/mydatabase"
    jdbc_user => "me"
    jdbc_password => "secret"
    statement => "select * from WORLD.COUNTRY WHERE Code = :code"
    parameters => { "code" => "country_code"}
    target => "country_details"
  }
}
```

More about `jdbc` plugin parameters: [https://www.elastic.co/guide/en/logstash/6.8/plugins-filters-jdbc_streaming.html](https://www.elastic.co/guide/en/logstash/6.8/plugins-filters-jdbc_streaming.html#plugins-filters-jdbc_streaming-prepared_statements)

#### Filter `logstash-filter-ldap`

#### Download and installation

[https://github.com/Transrian/logstash-filter-ldap](https://github.com/Transrian/logstash-filter-ldap)

#### Configuration

The **logstash-filter-ldap** filter will add fields queried from a ldap server to the event.
The fields will be stored in a variable called **target**, that you can modify in the configuration file.

If an error occurs during the process tha **tags** array of the event is updated with either:

- **LDAP_ERROR** tag: Problem while connecting to the server: bad *host, port, username, password, or search_dn* -> Check the error message and your configuration.
- **LDAP_NOT_FOUND** tag: Object wasn't found.

If error logging is enabled a field called **error** will also be added to the event.
It will contain more details about the problem.

#### Input event

```ruby
{
    "@timestamp" => 2018-02-25T10:04:22.338Z,
    "@version" => "1",
    "myUid" => "u501565"
}
```

#### Logstash filter

```ruby
filter {
  ldap {
    identifier_value => "%{myUid}"
    host => "my_ldap_server.com"
    ldap_port => "389"
    username => "<connect_username>"
    password => "<connect_password>"
    search_dn => "<user_search_pattern>"
  }
}
```

#### Output event

```ruby
{
    "@timestamp" => 2018-02-25T10:04:22.338Z,
    "@version" => "1",
    "myUid" => "u501565",
    "ldap" => {
        "givenName" => "VALENTIN",
        "sn" => "BOURDIER"
    }
}
```

#### Parameters available

Here is a list of all parameters, with their default value, if any, and their description.

|      Option name      | Type    | Required | Default value  | Description                                                  | Example                                   |
| :-------------------: | ------- | -------- | -------------- | ------------------------------------------------------------ | ----------------------------------------- |
|   identifier_value    | string  | yes      | n/a            | Identifier of the value to search. If identifier type is uid, then the value should be the uid to search for. | "123456"                                  |
|    identifier_key     | string  | no       | "uid"          | Type of the identifier to search                             | "uid"                                     |
|    identifier_type    | string  | no       | "posixAccount" | Object class of the object to search                         | "person"                                  |
|       search_dn       | string  | yes      | n/a            | Domain name in which search inside the ldap database (usually your userdn or groupdn) | "dc=example,dc=org"                       |
|      attributes       | array   | no       | []             | List of attributes to get. If not set, all attributes available will be get | ['givenName', 'sn']                       |
|        target         | string  | no       | "ldap"         | Name of the variable you want the result being stocked in    | "myCustomVariableName"                    |
|         host          | string  | yes      | n/a            | LDAP server host adress                                      | "ldapserveur.com"                         |
|       ldap_port       | number  | no       | 389            | LDAP server port for non-ssl connection                      | 400                                       |
|      ldaps_port       | number  | no       | 636            | LDAP server port for ssl connection                          | 401                                       |
|        use_ssl        | boolean | no       | false          | Enable or not ssl connection for LDAP  server. Set-up the good ldap(s)_port depending on that | true                                      |
| enable_error_logging  | boolean | no       | false          | When there is a problem with the connection with the LDAP database, write reason in the event | true                                      |
|   no_tag_on_failure   | boolean | no       | false          | No tags are added when an error (wrong credentials, bad server, ..) occur | true                                      |
|       username        | string  | no       | n/a            | Username to use for search in the database                   | "cn=SearchUser,ou=person,o=domain"        |
|       password        | string  | no       | n/a            | Password of the account linked to previous username          | "123456"                                  |
|       use_cache       | boolean | no       | true           | Choose to enable or not use of buffer                        | false                                     |
|      cache_type       | string  | no       | "memory"       | Type of buffer to use. Currently, only one is available, "memory" buffer | "memory"                                  |
| cache_memory_duration | number  | no       | 300            | Cache duration (in s) before refreshing values of it         | 3600                                      |
|   cache_memory_size   | number  | no       | 20000          | Number of object max that the buffer can contains            | 100                                       |
|  disk_cache_filepath  | string  | no       | nil            | Where the cache will periodically be dumped                  | "/tmp/my-memory-backup"                   |
|  disk_cache_schedule  | string  | no       | 10m            | Cron period of when the dump of the cache should occured. See [here](https://github.com/floraison/fugit) for the syntax. | "10m", "1h", "every day at five", "3h10m" |

#### Buffer

Like all filters, this filter treat only 1 event at a time.
This can lead to some slowing down of the pipeline speed due to the network round-trip time, and high network I/O.

A buffer can be set to mitigate this.

Currently, there is only one basic **"memory"** buffer.

You can enable / disable use of buffer with the option **use_cache**.

#### Memory Buffer

This buffer **store** data fetched from the LDAP server **in RAM**, and can be configured with two parameters:

- *cache_memory_duration*: duration (in s) before a cache entry is refreshed if hit.
- *cache_memory_size*: number of tuple (identifier, attributes) that the buffer can contains.

Older cache values than your TTL will be removed from cache.

#### Persistant cache buffer

For the only buffer for now, you will be able to save it to disk periodically.

Some specificities :

  - for *the memory cache*, TTL will be reset

Two parameters are required:

  - *disk_cache_filepath*: path on disk of this backup
  - *disk_cache_schedule*: schedule (every X time unit) of this backup. Please check [here](https://github.com/floraison/fugit) for the syntax of this parameter.

#### Filter `translate`

A general search and replace tool that uses a configured hash and/or a file to determine replacement values. Currently supported are YAML, JSON, and CSV files. Each dictionary item is a key value pair.

You can specify dictionary entries in one of two ways:

- The dictionary configuration item can contain a hash representing the mapping.

```ruby
filter {
      translate {
        field => "[http_status]"
        destination => "[http_status_description]"
        dictionary => {
          "100" => "Continue"
          "101" => "Switching Protocols"
          "200" => "OK"
          "500" => "Server Error"
        }
        fallback => "I'm a teapot"
      }
    }
```

- An external file (readable by logstash) may be specified in the `dictionary_path` configuration item:

```ruby
filter {
  translate {
    dictionary_path => "/etc/logstash/lists/instance_cpu.yml"
    field => "InstanceType"
    destination => "InstanceCPUCount"
    refresh_behaviour => "replace"
  }
}
```

​Sample dictionary file:

```yml
"c4.4xlarge": "16"
"c5.xlarge": "4"
"m1.medium": "1"
"m3.large": "2"
"m3.medium": "1"
"m4.2xlarge": "8"
"m4.large": "2"
"m4.xlarge": "4"
"m5a.xlarge": "4"
"m5d.xlarge": "4"
"m5.large": "2"
"m5.xlarge": "4"
"r3.2xlarge": "8"
"r3.xlarge": "4"
"r4.xlarge": "4"
"r5.2xlarge": "8"
"r5.xlarge": "4"
"t2.large": "2"
"t2.medium": "2"
"t2.micro": "1"
"t2.nano": "1"
"t2.small": "1"
"t2.xlarge": "4"
"t3.medium": "2"
```

#### External API

A simple filter that checks if an IP (from **PublicIpAddress** field) address exists in an external system. The result is written to the **op5exists** field. Then, using a grok filter, the number of occurrences is decoded and put into the **op5count** field.

```ruby
ruby {
  code => '
    checkip = event.get("PublicIpAddress")
    output=`curl -s -k -u monitor:monitor "https://192.168.1.1/api/filter/count?query=%5Bhosts%5D%28address%20~~%20%22# {checkip}%22%20%29" 2>&1`
    event.set("op5exists", "#{output}")
  '
}
grok {
  match => { "op5exists" => [ ".*\:%{NUMBER:op5count}" ] }
}
```

#### Mathematical calculations

Using Logstash filters, you can perform mathematical calculations for field values and save the results to a new field.

Application example:

```bash
filter {
   ruby { code => 'event.set("someField", event.get("field1") + event.get("field2"))' }
}
```

### Logstash - Output to Elasticsearch

This output plugin sends all data to the local Elasticsearch instance and create indexes:

```bash
output {
  elasticsearch {
    hosts => [ "127.0.0.1:9200" ]
    index => "%{type}-%{+YYYY.MM.dd}"
    user => "logstash"
    password => "logstash"
  }
}
```

### Logstash plugin for "naemon beat"

This Logstash plugin has example of complete configuration for integration with *naemon* application:

```bash
input {
    beats {
        port => FILEBEAT_PORT
        type => "naemon"
    }
}

filter {
    if [type] == "naemon" {
        grok {
            patterns_dir => [ "/etc/logstash/patterns" ]
            match => { "message" => "%{NAEMONLOGLINE}" }
            remove_field => [ "message" ]
        }
        date {
            match => [ "naemon_epoch", "UNIX" ]
            target => "@timestamp"
            remove_field => [ "naemon_epoch" ]
        }
    }
}

output {
  # Single index
#    if [type] == "naemon" {
#        elasticsearch {
#            hosts => ["ELASTICSEARCH_HOST:ES_PORT"]
#            index => "naemon-%{+YYYY.MM.dd}"
#        }
#    }

  # Separate indexes
  if [type] == "naemon" {
    if "_grokparsefailure" in [tags] {
      elasticsearch {
        hosts => ["ELASTICSEARCH_HOST:ES_PORT"]
        index => "naemongrokfailure"
      }
    }
    else {
      elasticsearch {
        hosts => ["ELASTICSEARCH_HOST:ES_PORT"]
        index => "naemon-%{+YYYY.MM.dd}"
      }
    }
  }
}
```

### Logstash plugin for "perflog"

This Logstash plugin has an example of a complete configuration for integration with perflog:

```bash
input {
  tcp {
    port => 6868
    host => "0.0.0.0"
    type => "perflogs"
  }
}

filter {
  if [type] == "perflogs" {
    grok {
      break_on_match => "true"
      match => {
        "message" => [
          "DATATYPE::%{WORD:datatype}\tTIMET::%{NUMBER:timestamp}\tHOSTNAME::%{DATA:hostname}\tSERVICEDESC::%{DATA:servicedescription}\tSERVICEPERFDATA::%{DATA:performance}\tSERVICECHECKCOMMAND::.*?HOSTSTATE::%{WORD:hoststate}\tHOSTSTATETYPE::.*?SERVICESTATE::%{WORD:servicestate}\tSERVICESTATETYPE::%{WORD:servicestatetype}",
          "DATATYPE::%{WORD:datatype}\tTIMET::%{NUMBER:timestamp}\tHOSTNAME::%{DATA:hostname}\tHOSTPERFDATA::%{DATA:performance}\tHOSTCHECKCOMMAND::.*?HOSTSTATE::%{WORD:hoststate}\tHOSTSTATETYPE::%{WORD:hoststatetype}"
        ]
      }
      remove_field => [ "message" ]
    }
    kv {
      source => "performance"
      field_split => "\t"
      remove_char_key => "\.\'"
      trim_key => " "
      target => "perf_data"
      remove_field => [ "performance" ]
      allow_duplicate_values => "false"
      transform_key => "lowercase"
    }
    date {
      match => [ "timestamp", "UNIX" ]
      target => "@timestamp"
      remove_field => [ "timestamp" ]
    }
  }
}

output {
  if [type] == "perflogs" {
    elasticsearch {
      hosts => ["127.0.0.1:9200"]
      index => "perflogs-%{+YYYY.MM.dd}"
    }
  }
}
```

### Logstash plugin for LDAP data enrichement

1. Download logstash plugin with dependencies ![logstash-filter-ldap-0.2.4.zip](/files/logstash-filter-ldap-0.2.4.zip) and upload files to your server.

2. Unzip file.

3. Install logstash plugin.

    ```/usr/share/logstash/bin/logstash-plugin install /directory/to/file/logstash-filter-ldap-0.2.4.gem```

4. Create new file in beats pipeline. To do this, go to beats folder (/etc/logstash/conf.d/beats) and create new config file, for example ```031-filter-ldap-enrichement.conf```

5. Below is an example of the contents of the configuration file:

    ```bash
    filter {
      ldap {
        identifier_value => "%{[winlog][event_data][TargetUserName]}"
        identifier_key => "sAMAccountName"
        identifier_type => "person"
        host => "10.0.0.1"
        ldap_port => "389"
        username => "user"
        password => "pass"
        search_dn => "OU=example,DC=example"
        enable_error_logging => true
        attributes => ['sAMAccountType','lastLogon','badPasswordTime']
      }
    }
    ```

6. Fields description

    ```bash
    identifier_value - Identifier of the value to search. If identifier type is uid, then the value should be the uid to search for.
    identifier_key - Type of the identifier to search.
    identifier_type - Object class of the object to search.
    host - LDAP server host adress.
    ldap_port - LDAP server port for non-ssl connection.
    username - Username to use for search in the database.
    password - Password of the account linked to previous username.
    search_dn - Domain name in which search inside the ldap database (usually your userdn or groupdn).
    enable_error_logging - When there is a problem with the connection with the LDAP database, write reason in the event.
    attributes - List of attributes to get. If not set, all attributes available will be get.
    ```

### Single password in all Logstash outputs

You can set passwords and other Logstash pipeline settings as environment variables. This can be useful if the password was changed for the `logastash` user and it must be to update in the configuration files.

Configuration steps:

1. Create the service file:

    ```bash
    mkdir –p /etc/systemd/system/logstash.service.d
    vi /etc/systemd/system/logstash.service.d/logstash.conf

    [Service]
    Environment="ELASTICSEARCH_ES_USER=logserver"
    Environment="ELASTICSEARCH_ES_PASSWD=logserver"
    ```

1. Reload systemctl daemon:

    ```bash
    systemctl daemon-reload
    ```

1. Sample definition of Logstash output pipline seciotn:

    ```bash
    output  {
      elasticsearch {
        index => "test-%{+YYYY.MM.dd}"
        user => "${ELASTICSEARCH_ES_USER:elastic}"
        password => "${ELASTICSEARCH_ES_PASSWD:changeme}"
      }
    }
    ```

### Multiline codec

The original goal of this codec was to allow joining of multiline messages from files into a single event. For example, joining Java exception and stacktrace messages into a single event.

```conf
    input {
      stdin {
        codec => multiline {
          pattern => "pattern, a regexp"
          negate => "true" or "false"
          what => "previous" or "next"
        }
      }
    }
```

```conf
    input {
      file {
        path => "/var/log/someapp.log"
        codec => multiline {
          # Grok pattern names are valid! :)
          pattern => "^%{TIMESTAMP_ISO8601} "
          negate => true
          what => "previous"
        }
      }
    }
```

## SQL

Energy Logserver SQL lets you write queries in SQL rather than the Query domain-specific language (DSL)

### SIEM Examples
Use SQL query to get security related data:

#### Example 1: Check number of failed login attemps

Query:

```sql

SELECT COUNT(sys.client.ip) AS failed_login_attempts FROM syslog-2024.02.23 sys
WHERE postfix_message = "SASL LOGIN authentication failed: UGFzc3dvcmQ6"
```

Result:

```
	failed_login_attempts
1	1329
```

#### Example 2: Gather host data from different sources in one place using *JOIN*

Query:

```sql
SELECT syslog.host.ip, syslog.host.name, zeek.server_addr, zeek.mac
FROM syslog-2024.02.23 syslog JOIN stream-zeek-2024.02.23 zeek ON zeek.server_addr = syslog.host.ip
```
Result:

```
	syslog.host.ip	syslog.host.name	zeek.server_addr	zeek.mac
	192.168.10.1	   example-hostname-1	192.168.10.1	bc:24:11:0g:f9:28
	192.168.10.1	   example-hostname-1	192.168.10.1	bc:24:11:0g:f9:28
	192.168.10.2	   example-hostname-2	192.168.10.2	bs:12:18:0g:f2:66
	192.168.10.1	   example-hostname-1	192.168.10.1	bc:24:11:0g:f9:28
	192.168.10.1	   example-hostname-1	192.168.10.1	bc:24:11:0g:f9:28
```

#### Example 3: See MAC addresses and their assigned IP addresses:

Query:

```

POST /_plugins/_sql
{
  "query" : "SELECT mac, client_addr FROM stream-zeek-2024.02.20 WHERE netflow.zeek.type ='dhcp'"
}
```

Result:

```json
{
  "schema": [
    {
      "name": "mac",
      "type": "keyword"
    },
    {
      "name": "client_addr",
      "type": "keyword"
    }
  ],
  "total": 3369,
  "datarows": [
    [
      "cs:96:d5:98:55:72",
      "10.7.7.2"
    ],
    [
      "bw:85:58:6a:b7:5a",
      "10.7.7.232"
    ],
    [
      "bc:34:11:0d:s9:88",
      "192.168.10.200"
    ]
    ]
    }
```

#### Example 4: Check total number of warnings from *syslog*:

Query:

```sql

SELECT COUNT(sys.syslog_severity_code) AS warnings_total FROM syslog-2024.02.23 sys
WHERE syslog_severity = "warning"

```
Result:

```
warnings_total
429822
```

#### Example 5: Check number of failed login attemps for every client:

Query:

```sql
SELECT sys.client.ip, COUNT(*) AS failed_login_attempts FROM syslog-2024.02.23 sys
WHERE  postfix_message = "SASL LOGIN authentication failed: CGZFzc3evxmQ6"
GROUP BY sys.client.ip
```

Result:

```
client.ip	failed_login_attempts
144.220.71.224	3
127.174.131.70	2
146.114.84.226	3
142.169.105.19	5
142.180.112.241	3
155.211.74.18	1
```


### SQL/PPL API

Use the SQL and PPL API to send queries to the SQL plugin. Use the `_sql` endpoint to send queries in SQL, and the `_ppl` endpoint to send queries in PPL. For both of these, you can also use the `_explain` endpoint to translate your query into  Domain-specific language (DSL) or to troubleshoot errors.

#### Query API

Sends an SQL/PPL query to the SQL plugin. You can pass the format for the response as a query parameter.

##### Query parameters

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b"> Parameter </th>
    <th class="tg-ua3b"> Data Type </th>
    <th class="tg-ua3b"> Description </th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2"><a href="https://kb.energylogserver.com/en/latest/04-User_Manual/04-User_Manual.md#response-formats" target="_blank" rel="noopener noreferrer"><span style="text-decoration:none"> format </span></a></td>
    <td class="tg-pnl2"> String </td>
    <td class="tg-pnl2"> The format for the response. The _sql endpoint supports jdbc, csv, raw, and json formats. The _ppl endpoint supports jdbc, csv, and raw formats. Default is jdbc. </td>
  </tr>
  <tr>
    <td class="tg-pnl2"> sanitize </td>
    <td class="tg-pnl2"> Boolean </td>
    <td class="tg-pnl2"> Specifies whether to escape special characters in the results. See <a href="https://kb.energylogserver.com/en/latest/04-User_Manual/04-User_Manual.md#response-formats" target="_blank" rel="noopener noreferrer"><span style="text-decoration:none">Response formats</span></a> for more information. Default is true. </td>
  </tr>
</tbody>
</table>

##### Request fields

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b"> Field </th>
    <th class="tg-ua3b"> Data Type </th>
    <th class="tg-ua3b"> Description </th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2"> query </td>
    <td class="tg-pnl2"> String </td>
    <td class="tg-pnl2"> The query to be executed. Required. </td>
  </tr>
  <tr>
    <td class="tg-pnl2"> <a href="https://kb.energylogserver.com/en/latest/04-User_Manual/04-User_Manual.md#filtering-results" target="_blank" rel="noopener noreferrer"><span style="text-decoration:none">filter</span></a> </td>
    <td class="tg-pnl2"> JSON object </td>
    <td class="tg-pnl2"> The filter for the results. Optional. </td>
  </tr>
  <tr>
    <td class="tg-pnl2"> <a href="https://kb.energylogserver.com/en/latest/04-User_Manual/04-User_Manual.md#paginating-results" target="_blank" rel="noopener noreferrer"><span style="text-decoration:none">fetch_size</span></a> </td>
    <td class="tg-pnl2">integer</td>
    <td class="tg-pnl2">The number of results to return in one response. Used for paginating results. Default is 1,000. Optional. Only supported for the `jdbc` response format.</td>
  </tr>
</tbody>
</table>

###### Example request

```json
POST /_plugins/_sql
{
  "query" : "SELECT * FROM accounts"
}
```

###### Example response

The response contains the schema and the results:

```json
{
  "schema": [
    {
      "name": "account_number",
      "type": "long"
    },
    {
      "name": "firstname",
      "type": "text"
    },
    {
      "name": "address",
      "type": "text"
    },
    {
      "name": "balance",
      "type": "long"
    },
    {
      "name": "gender",
      "type": "text"
    },
    {
      "name": "city",
      "type": "text"
    },
    {
      "name": "employer",
      "type": "text"
    },
    {
      "name": "state",
      "type": "text"
    },
    {
      "name": "age",
      "type": "long"
    },
    {
      "name": "email",
      "type": "text"
    },
    {
      "name": "lastname",
      "type": "text"
    }
  ],
  "datarows": [
    [
      1,
      "Amber",
      "880 Holmes Lane",
      39225,
      "M",
      "Brogan",
      "Pyrami",
      "IL",
      32,
      "amberduke@pyrami.com",
      "Duke"
    ],
    [
      6,
      "Hattie",
      "671 Bristol Street",
      5686,
      "M",
      "Dante",
      "Netagy",
      "TN",
      36,
      "hattiebond@netagy.com",
      "Bond"
    ],
    [
      13,
      "Nanette",
      "789 Madison Street",
      32838,
      "F",
      "Nogal",
      "Quility",
      "VA",
      28,
      "nanettebates@quility.com",
      "Bates"
    ],
    [
      18,
      "Dale",
      "467 Hutchinson Court",
      4180,
      "M",
      "Orick",
      null,
      "MD",
      33,
      "daleadams@boink.com",
      "Adams"
    ]
  ],
  "total": 4,
  "size": 4,
  "status": 200
}
```

##### Response fields

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-022u{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Field</th>
    <th class="tg-ua3b">Data Type</th>
    <th class="tg-ua3b">Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-022u">schema</td>
    <td class="tg-022u">Array</td>
    <td class="tg-022u">Specifies the field names and types for all fields.</td>
  </tr>
  <tr>
    <td class="tg-022u">data_rows</td>
    <td class="tg-022u">2D array</td>
    <td class="tg-022u">An array of results. Each result represents one matching row (document).</td>
  </tr>
  <tr>
    <td class="tg-022u">total</td>
    <td class="tg-022u">Integer</td>
    <td class="tg-022u">The total number of rows (documents) in the index.</td>
  </tr>
  <tr>
    <td class="tg-022u">size</td>
    <td class="tg-022u">Integer</td>
    <td class="tg-022u">The number of results to return in one response.</td>
  </tr>
  <tr>
    <td class="tg-022u">status</td>
    <td class="tg-022u">String</td>
    <td class="tg-022u">The HTTP response status Energy Logserver returns after running the query.</td>
  </tr>
</tbody>
</table>

#### Explain API

The SQL plugin has an `explain` feature that shows how a query is executed against Energy Logserver, which is useful for debugging and development. A POST request to the `_plugins/_sql/_explain` or `_plugins/_ppl/_explain` endpoint returns Domain-specific language (DSL) in JSON format, explaining the query.
You can execute the explain API operation either in command line using `curl` or in the Dashboards console, like in the example below.

##### Sample explain request for an SQL query

```json
POST _plugins/_sql/_explain
{
  "query": "SELECT firstname, lastname FROM accounts WHERE age > 20"
}
```

##### Sample SQL query explain response

```json
{
  "root": {
    "name": "ProjectOperator",
    "description": {
      "fields": "[firstname, lastname]"
    },
    "children": [
      {
        "name": "OpenSearchIndexScan",
        "description": {
          "request": """OpenSearchQueryRequest(indexName=accounts, sourceBuilder={"from":0,"size":200,"timeout":"1m","query":{"range":{"age":{"from":20,"to":null,"include_lower":false,"include_upper":true,"boost":1.0}}},"_source":{"includes":["firstname","lastname"],"excludes":[]},"sort":[{"_doc":{"order":"asc"}}]}, searchDone=false)"""
        },
        "children": []
      }
    ]
  }
}
```

##### Sample explain request for a PPL query

```json
POST _plugins/_ppl/_explain
{
  "query" : "source=accounts | fields firstname, lastname"
}
```

##### Sample PPL query explain response

```json
{
  "root": {
    "name": "ProjectOperator",
    "description": {
      "fields": "[firstname, lastname]"
    },
    "children": [
      {
        "name": "OpenSearchIndexScan",
        "description": {
          "request": """OpenSearchQueryRequest(indexName=accounts, sourceBuilder={"from":0,"size":200,"timeout":"1m","_source":{"includes":["firstname","lastname"],"excludes":[]}}, searchDone=false)"""
        },
        "children": []
      }
    ]
  }
}
```

For queries that require post-processing, the `explain` response includes a query plan in addition to the Energy Logserver DSL. For those queries that don't require post processing, you can see a complete DSL.

#### Paginating results

To get back a paginated response, use the `fetch_size` parameter. The value of `fetch_size` should be greater than 0. The default value is 1,000. A value of 0 will fall back to a non-paginated response.

The `fetch_size` parameter is only supported for the `jdbc` response format.
{: .note }

##### Example

The following request contains an SQL query and specifies to return five results at a time:

```json
POST _plugins/_sql/
{
  "fetch_size" : 5,
  "query" : "SELECT firstname, lastname FROM accounts WHERE age > 20 ORDER BY state ASC"
}
```

The response contains all the fields that a query without `fetch_size` would contain, and a `cursor` field that is used to retrieve subsequent pages of results:

```json
{
  "schema": [
    {
      "name": "firstname",
      "type": "text"
    },
    {
      "name": "lastname",
      "type": "text"
    }
  ],
  "cursor": "d:eyJhIjp7fSwicyI6IkRYRjFaWEo1UVc1a1JtVjBZMmdCQUFBQUFBQUFBQU1XZWpkdFRFRkZUMlpTZEZkeFdsWnJkRlZoYnpaeVVRPT0iLCJjIjpbeyJuYW1lIjoiZmlyc3RuYW1lIiwidHlwZSI6InRleHQifSx7Im5hbWUiOiJsYXN0bmFtZSIsInR5cGUiOiJ0ZXh0In1dLCJmIjo1LCJpIjoiYWNjb3VudHMiLCJsIjo5NTF9",
  "total": 956,
  "datarows": [
    [
      "Cherry",
      "Carey"
    ],
    [
      "Lindsey",
      "Hawkins"
    ],
    [
      "Sargent",
      "Powers"
    ],
    [
      "Campos",
      "Olsen"
    ],
    [
      "Savannah",
      "Kirby"
    ]
  ],
  "size": 5,
  "status": 200
}
```

To fetch subsequent pages, use the `cursor` from the previous response:

```json
POST /_plugins/_sql
{
   "cursor": "d:eyJhIjp7fSwicyI6IkRYRjFaWEo1UVc1a1JtVjBZMmdCQUFBQUFBQUFBQU1XZWpkdFRFRkZUMlpTZEZkeFdsWnJkRlZoYnpaeVVRPT0iLCJjIjpbeyJuYW1lIjoiZmlyc3RuYW1lIiwidHlwZSI6InRleHQifSx7Im5hbWUiOiJsYXN0bmFtZSIsInR5cGUiOiJ0ZXh0In1dLCJmIjo1LCJpIjoiYWNjb3VudHMiLCJsIjo5NTF9"
}
```

The next response contains only the `datarows` of the results and a new `cursor`.

```json
{
  "cursor": "d:eyJhIjp7fSwicyI6IkRYRjFaWEo1UVc1a1JtVjBZMmdCQUFBQUFBQUFBQU1XZWpkdFRFRkZUMlpTZEZkeFdsWnJkRlZoYnpaeVVRPT0iLCJjIjpbeyJuYW1lIjoiZmlyc3RuYW1lIiwidHlwZSI6InRleHQifSx7Im5hbWUiOiJsYXN0bmFtZSIsInR5cGUiOiJ0ZXh0In1dLCJmIjo1LCJpIjoiYWNjb3VudHMabcde12345",
  "datarows": [
    [
      "Abbey",
      "Karen"
    ],
    [
      "Chen",
      "Ken"
    ],
    [
      "Ani",
      "Jade"
    ],
    [
      "Peng",
      "Hu"
    ],
    [
      "John",
      "Doe"
    ]
  ]
}
```

The `datarows` can have more than the `fetch_size` number of records in case nested fields are flattened.

The last page of results has only `datarows` and no `cursor`. The `cursor` context is automatically cleared on the last page.

To explicitly clear the cursor context, use the `_plugins/_sql/close` endpoint operation:

```json
POST /_plugins/_sql/close
{
   "cursor": "d:eyJhIjp7fSwicyI6IkRYRjFaWEo1UVc1a1JtVjBZMmdCQUFBQUFBQUFBQU1XZWpkdFRFRkZUMlpTZEZkeFdsWnJkRlZoYnpaeVVRPT0iLCJjIjpbeyJuYW1lIjoiZmlyc3RuYW1lIiwidHlwZSI6InRleHQifSx7Im5hbWUiOiJsYXN0bmFtZSIsInR5cGUiOiJ0ZXh0In1dLCJmIjo1LCJpIjoiYWNjb3VudHMiLCJsIjo5NTF9"
}'
```

The response is an acknowledgement from Energy Logserver:

```json
{"succeeded":true}
```

#### Filtering results

You can use the `filter` parameter to add more conditions to the Energy Logserver DSL directly.

The following SQL query returns the names and account balances of all customers. The results are then filtered to contain only those customers with less than $10,000 balance.

```json
POST /_plugins/_sql/
{
  "query" : "SELECT firstname, lastname, balance FROM accounts",
  "filter" : {
    "range" : {
      "balance" : {
        "lt" : 10000
      }
    }
  }
}
```

The response contains the matching results:

```json
{
  "schema": [
    {
      "name": "firstname",
      "type": "text"
    },
    {
      "name": "lastname",
      "type": "text"
    },
    {
      "name": "balance",
      "type": "long"
    }
  ],
  "total": 2,
  "datarows": [
    [
      "Hattie",
      "Bond",
      5686
    ],
    [
      "Dale",
      "Adams",
      4180
    ]
  ],
  "size": 2,
  "status": 200
}
```

You can use the Explain API to see how this query is executed against Energy Logserver:

```json
POST /_plugins/_sql/_explain
{
  "query" : "SELECT firstname, lastname, balance FROM accounts",
  "filter" : {
    "range" : {
      "balance" : {
        "lt" : 10000
      }
    }
  }
}'
```

The response contains the Boolean query in Energy Logserver DSL that corresponds to the query above:

```json
{
  "from": 0,
  "size": 200,
  "query": {
    "bool": {
      "filter": [{
        "bool": {
          "filter": [{
            "range": {
              "balance": {
                "from": null,
                "to": 10000,
                "include_lower": true,
                "include_upper": false,
                "boost": 1.0
              }
            }
          }],
          "adjust_pure_negative": true,
          "boost": 1.0
        }
      }],
      "adjust_pure_negative": true,
      "boost": 1.0
    }
  },
  "_source": {
    "includes": [
      "firstname",
      "lastname",
      "balance"
    ],
    "excludes": []
  }
}
```

#### Using parameters

You can use the `parameters` field to pass parameter values to a prepared SQL query.

The following explain operation uses an SQL query with an `age` parameter:

```json
POST /_plugins/_sql/_explain
{
  "query": "SELECT * FROM accounts WHERE age = ?",
  "parameters": [{
    "type": "integer",
    "value": 30
  }]
}
```

The response contains the Boolean query in Energy Logserver DSL that corresponds to the SQL query above:

```json
{
  "from": 0,
  "size": 200,
  "query": {
    "bool": {
      "filter": [{
        "bool": {
          "must": [{
            "term": {
              "age": {
                "value": 30,
                "boost": 1.0
              }
            }
          }],
          "adjust_pure_negative": true,
          "boost": 1.0
        }
      }],
      "adjust_pure_negative": true,
      "boost": 1.0
    }
  }
}

```

### Response formats

The SQL plugin provides the `jdbc`, `csv`, `raw`, and `json` response formats that are useful for different purposes. The `jdbc` format is widely used because it provides the schema information and adds more functionality, such as pagination. Besides the JDBC driver, various clients can benefit from a detailed and well-formatted response.

#### JDBC format

By default, the SQL plugin returns the response in the standard JDBC format. This format is provided for the JDBC driver and clients that need both the schema and the result set to be well formatted.

##### Example request

The following query does not specify the response format, so the format is set to `jdbc`:

```json
POST _plugins/_sql
{
  "query" : "SELECT firstname, lastname, age FROM accounts ORDER BY age LIMIT 2"
}
```

##### Example response

In the response, the `schema` contains the field names and types, and the `datarows` field contains the result set:

```json
{
  "schema": [{
      "name": "firstname",
      "type": "text"
    },
    {
      "name": "lastname",
      "type": "text"
    },
    {
      "name": "age",
      "type": "long"
    }
  ],
  "total": 4,
  "datarows": [
    [
      "Nanette",
      "Bates",
      28
    ],
    [
      "Amber",
      "Duke",
      32
    ]
  ],
  "size": 2,
  "status": 200
}
```

If an error of any type occurs, Energy Logserver returns the error message.

The following query searches for a non-existent field `unknown`:

```json
POST /_plugins/_sql
{
  "query" : "SELECT unknown FROM accounts"
}
```

The response contains the error message and the cause of the error:

```json
{
  "error": {
    "reason": "Invalid SQL query",
    "details": "Field [unknown] cannot be found or used here.",
    "type": "SemanticAnalysisException"
  },
  "status": 400
}
```

#### Energy Logserver DSL JSON format

If you set the format to `json`, the original Energy Logserver response is returned in JSON format. Because this is the native response from Energy Logserver, extra effort is needed to parse and interpret it.

##### Example request

The following query sets the response format to `json`:

```json
POST _plugins/_sql?format=json
{
  "query" : "SELECT firstname, lastname, age FROM accounts ORDER BY age LIMIT 2"
}
```

##### Example response

The response is the original response from Energy Logserver:

```json
{
  "_shards": {
    "total": 5,
    "failed": 0,
    "successful": 5,
    "skipped": 0
  },
  "hits": {
    "hits": [{
        "_index": "accounts",
        "_type": "account",
        "_source": {
          "firstname": "Nanette",
          "age": 28,
          "lastname": "Bates"
        },
        "_id": "13",
        "sort": [
          28
        ],
        "_score": null
      },
      {
        "_index": "accounts",
        "_type": "account",
        "_source": {
          "firstname": "Amber",
          "age": 32,
          "lastname": "Duke"
        },
        "_id": "1",
        "sort": [
          32
        ],
        "_score": null
      }
    ],
    "total": {
      "value": 4,
      "relation": "eq"
    },
    "max_score": null
  },
  "took": 100,
  "timed_out": false
}
```

#### CSV format

You can also specify to return results in CSV format.

##### Example request

```json
POST /_plugins/_sql?format=csv
{
  "query" : "SELECT firstname, lastname, age FROM accounts ORDER BY age"
}
```

##### Example response

```text
firstname,lastname,age
Nanette,Bates,28
Amber,Duke,32
Dale,Adams,33
Hattie,Bond,36
```

##### Sanitizing results in CSV format

By default, Energy Logserver sanitizes header cells (field names) and data cells (field contents) according to the following rules:

- If a cell starts with `+`, `-`, `=` , or `@`, the sanitizer inserts a single quote (`'`) at the start of the cell.
- If a cell contains one or more commas (`,`), the sanitizer surrounds the cell with double quotes (`"`).

##### Example

The following query indexes a document with cells that either start with special characters or contain commas:

```json
PUT /userdata/_doc/1?refresh=true
{
  "+firstname": "-Hattie",
  "=lastname": "@Bond",
  "address": "671 Bristol Street, Dente, TN"
}
```

You can use the query below to request results in CSV format:

```json
POST /_plugins/_sql?format=csv
{
  "query" : "SELECT * FROM userdata"
}
```

In the response, cells that start with special characters are prefixed with `'`. The cell that has commas is surrounded with quotation marks:

```text
'+firstname,'=lastname,address
'Hattie,'@Bond,"671 Bristol Street, Dente, TN"
```

To skip sanitizing, set the `sanitize` query parameter to false:

```json
POST /_plugins/_sql?format=csvandsanitize=false
{
  "query" : "SELECT * FROM userdata"
}
```

The response contains the results in the original CSV format:

```text
=lastname,address,+firstname
@Bond,"671 Bristol Street, Dente, TN",-Hattie
```

#### Raw format

You can use the raw format to pipe the results to other command line tools for post-processing.

##### Example request

```json
POST /_plugins/_sql?format=raw
{
  "query" : "SELECT firstname, lastname, age FROM accounts ORDER BY age"
}
```

##### Example response

```text
Nanette|Bates|28
Amber|Duke|32
Dale|Adams|33
Hattie|Bond|36
```

By default, Energy Logserver sanitizes results in `raw` format according to the following rule:

- If a data cell contains one or more pipe characters (`|`), the sanitizer surrounds the cell with double quotes.

##### Example

The following query indexes a document with pipe characters (`|`) in its fields:

```json
PUT /userdata/_doc/1?refresh=true
{
  "+firstname": "|Hattie",
  "=lastname": "Bond|",
  "|address": "671 Bristol Street| Dente| TN"
}
```

You can use the query below to request results in `raw` format:

```json
POST /_plugins/_sql?format=raw
{
  "query" : "SELECT * FROM userdata"
}
```

The query returns cells with the `|` character surrounded by quotation marks:

```text
"|address"|=lastname|+firstname
"671 Bristol Street| Dente| TN"|"Bond|"|"|Hattie"
```

### SQL

SQL in Energy Logserver bridges the gap between traditional relational database concepts and the flexibility of Energy Logserver’s document-oriented data storage. This integration gives you the ability to use your SQL knowledge to query, analyze, and extract insights from your  data.

**SQL and Energy Logserver terminology**

Here’s how core SQL concepts map to Energy Logserver:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">SQL</th>
    <th class="tg-ua3b">Energy Logserver</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">Table</td>
    <td class="tg-pnl2">Index</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Row</td>
    <td class="tg-pnl2">Document</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Column</td>
    <td class="tg-pnl2">Field</td>
  </tr>
</tbody>
</table>

**REST API**

To use the SQL plugin with your own applications, send requests to the `_plugins/_sql` endpoint:

```json
POST _plugins/_sql
{
  "query": "SELECT * FROM my-index LIMIT 50"
}
```

You can query multiple indexes by using a comma-separated list:

```json
POST _plugins/_sql
{
  "query": "SELECT * FROM my-index1,myindex2,myindex3 LIMIT 50"
}
```

You can also specify an index pattern with a wildcard expression:

```json
POST _plugins/_sql
{
  "query": "SELECT * FROM my-index* LIMIT 50"
}
```

To run the above query in the command line, use the curl command:

```bash
curl -XPOST https://localhost:9200/_plugins/_sql -u 'admin:admin' -k -H 'Content-Type: application/json' -d '{"query": "SELECT * FROM my-index* LIMIT 50"}'
```

You can specify the [response format](#response-formats) as JDBC, standard Energy Logserver JSON, CSV, or raw. By default, queries return data in JDBC format. The following query sets the format to JSON:

```json
POST _plugins/_sql?format=json
{
  "query": "SELECT * FROM my-index LIMIT 50"
}
```

See the rest of this guide for more information about request parameters, settings, supported operations, and tools.

#### Basic queries

Use the `SELECT` clause, along with `FROM`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, and `LIMIT` to search and aggregate data.

Among these clauses, `SELECT` and `FROM` are required, as they specify which fields to retrieve and which indexes to retrieve them from. All other clauses are optional. Use them according to your needs.

##### Syntax

The complete syntax for searching and aggregating data is as follows:

```sql
SELECT [DISTINCT] (* | expression) [[AS] alias] [, ...]
FROM index_name
[WHERE predicates]
[GROUP BY expression [, ...]
 [HAVING predicates]]
[ORDER BY expression [IS [NOT] NULL] [ASC | DESC] [, ...]]
[LIMIT [offset, ] size]
```

##### Fundamentals

Apart from the predefined keywords of SQL, the most basic elements are literal and identifiers.
A literal is a numeric, string, date or boolean constant. An identifier is an Energy Logserver index or field name.
With arithmetic operators and SQL functions, use literals and identifiers to build complex expressions.

Rule `expressionAtom`:

![expressionAtom](/media/media/expressionAtom.png)

The expression in turn can be combined into a predicate with logical operator. Use a predicate in the `WHERE` and `HAVING` clause to filter out data by specific conditions.

Rule `expression`:

![expression](/media/media/expression.png)

Rule `predicate`:

![expression](/media/media/predicate.png)

##### Execution Order

These SQL clauses execute in an order different from how they appear:

```sql
FROM index
 WHERE predicates
  GROUP BY expressions
   HAVING predicates
    SELECT expressions
     ORDER BY expressions
      LIMIT size
```

##### Select

Specify the fields to be retrieved.

###### Syntax

Rule `selectElements`:

![selectElements](/media/media/selectElements.png)

Rule `selectElement`:

![selectElements](/media/media/selectElement.png)

*Example 1*: Use `*` to retrieve all fields in an index:

```sql
SELECT *
FROM accounts
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-9iv7{color:inherit;text-align:left;vertical-align:top}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-37zg{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-9iv7{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">firstname</th>
    <th class="tg-37zg">gender</th>
    <th class="tg-37zg">city</th>
    <th class="tg-37zg">balance</th>
    <th class="tg-37zg">employer</th>
    <th class="tg-37zg">state</th>
    <th class="tg-37zg">email</th>
    <th class="tg-37zg">address</th>
    <th class="tg-37zg">lastname</th>
    <th class="tg-37zg">age</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-9iv7">1</td>
    <td class="tg-9iv7">Amber</td>
    <td class="tg-9iv7">M</td>
    <td class="tg-9iv7">Brogan</td>
    <td class="tg-9iv7">39225</td>
    <td class="tg-9iv7">Pyrami</td>
    <td class="tg-9iv7">IL</td>
    <td class="tg-9iv7">amberduke@pyrami.com</td>
    <td class="tg-9iv7">880 Holmes Lane</td>
    <td class="tg-9iv7">Duke</td>
    <td class="tg-9iv7">32</td>
  </tr>
  <tr>
    <td class="tg-9iv7">16</td>
    <td class="tg-9iv7">Hattie</td>
    <td class="tg-9iv7">M</td>
    <td class="tg-9iv7">Dante</td>
    <td class="tg-9iv7">5686</td>
    <td class="tg-9iv7">Netagy</td>
    <td class="tg-9iv7">TN</td>
    <td class="tg-9iv7">hattiebond@netagy.com</td>
    <td class="tg-9iv7">671 Bristol Street</td>
    <td class="tg-9iv7">Bond</td>
    <td class="tg-9iv7">36</td>
  </tr>
  <tr>
    <td class="tg-9iv7">13</td>
    <td class="tg-9iv7">Nanette</td>
    <td class="tg-9iv7">F</td>
    <td class="tg-9iv7">Nogal</td>
    <td class="tg-9iv7">32838</td>
    <td class="tg-9iv7">Quility</td>
    <td class="tg-9iv7">VA</td>
    <td class="tg-9iv7">nanettebates@quility.com</td>
    <td class="tg-9iv7">789 Madison Street</td>
    <td class="tg-9iv7">Bates</td>
    <td class="tg-9iv7">28</td>
  </tr>
  <tr>
    <td class="tg-9iv7">18</td>
    <td class="tg-9iv7">Dale</td>
    <td class="tg-9iv7">M</td>
    <td class="tg-9iv7">Orick</td>
    <td class="tg-9iv7">4180</td>
    <td class="tg-9iv7"></td>
    <td class="tg-9iv7">MD</td>
    <td class="tg-9iv7">daleadams@boink.com</td>
    <td class="tg-9iv7">467 Hutchinson Court</td>
    <td class="tg-9iv7">Adams</td>
    <td class="tg-9iv7">33</td>
  </tr>
</tbody>
</table>

*Example 2*: Use field name(s) to retrieve only specific fields:

```sql
SELECT firstname, lastname
FROM accounts
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">firstname</th>
    <th class="tg-ua3b">lastname</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">Amber</td>
    <td class="tg-pnl2">Duke</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Hattie</td>
    <td class="tg-pnl2">Bond</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Nanette</td>
    <td class="tg-pnl2">Bates</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Dale</td>
    <td class="tg-pnl2">Adams</td>
  </tr>
</tbody>
</table>

*Example 3*: Use field aliases instead of field names. Field aliases are used to make field names more readable:

```sql
SELECT account_number AS num
FROM accounts
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">num</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
  </tr>
  <tr>
    <td class="tg-pnl2">18</td>
  </tr>
</tbody>
</table>

*Example 4*: Use the `DISTINCT` clause to get back only unique field values. You can specify one or more field names:

```sql
SELECT DISTINCT age
FROM accounts
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">age</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">28</td>
  </tr>
  <tr>
    <td class="tg-pnl2">32</td>
  </tr>
  <tr>
    <td class="tg-pnl2">33</td>
  </tr>
  <tr>
    <td class="tg-pnl2">36</td>
  </tr>
</tbody>
</table>

##### From

Specify the index that you want search.
You can specify subqueries within the `FROM` clause.

###### Syntax

Rule `tableName`:

![tableName](/media/media/tableName.png)

*Example 1*: Use index aliases to query across indexes.
In this sample query, `acc` is an alias for the `accounts` index:

```sql
SELECT account_number, accounts.age
FROM accounts
```

or

```sql
SELECT account_number, acc.age
FROM accounts acc
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">age</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">32</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">36</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">28</td>
  </tr>
  <tr>
    <td class="tg-pnl2">18</td>
    <td class="tg-pnl2">33</td>
  </tr>
</tbody>
</table>

*Example 2*: Use index patterns to query indexes that match a specific pattern:

```sql
SELECT account_number
FROM account*
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
  </tr>
  <tr>
    <td class="tg-pnl2">18</td>
  </tr>
</tbody>
</table>

##### Where

Specify a condition to filter the results.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Operators</th>
    <th class="tg-ua3b">Behavior</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">=</td>
    <td class="tg-pnl2">Equal to.</td>
  </tr>
  <tr>
    <td class="tg-pnl2"><></td>
    <td class="tg-pnl2">Not equal to.</td>
  </tr>
  <tr>
    <td class="tg-pnl2">></td>
    <td class="tg-pnl2">Greater than.</td>
  </tr>
  <tr>
    <td class="tg-pnl2"><</td>
    <td class="tg-pnl2">Less than.</td>
  </tr>
  <tr>
    <td class="tg-pnl2">>=</td>
    <td class="tg-pnl2">Greater than or equal to.</td>
  </tr>
  <tr>
    <td class="tg-pnl2"><=</td>
    <td class="tg-pnl2">Less than or equal to.</td>
  </tr>
  <tr>
    <td class="tg-pnl2">IN</td>
    <td class="tg-pnl2">Specify multiple `OR` operators.</td>
  </tr>
  <tr>
    <td class="tg-pnl2">BETWEEN</td>
    <td class="tg-pnl2">Similar to a range query.</td>
  </tr>
  <tr>
    <td class="tg-pnl2">LIKE</td>
    <td class="tg-pnl2">Use for full-text search. For more information about full-text queries.</td>
  </tr>
  <tr>
    <td class="tg-pnl2">IS NULL</td>
    <td class="tg-pnl2">Check if the field value is `NULL`.</td>
  </tr>
  <tr>
    <td class="tg-pnl2">IS NOT NULL</td>
    <td class="tg-pnl2">Check if the field value is `NOT NULL`.</td>
  </tr>
</tbody>
</table>

Combine comparison operators (`=`, `<>`, `>`, `>=`, `<`, `<=`) with boolean operators `NOT`, `AND`, or `OR` to build more complex expressions.

*Example 1*: Use comparison operators for numbers, strings, or dates:

```sql
SELECT account_number
FROM accounts
WHERE account_number = 1
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
  </tr>
</tbody>
</table>

*Example 2*: Energy Logserver allows for flexible schema，so documents in an index may have different fields. Use `IS NULL` or `IS NOT NULL` to retrieve only missing fields or existing fields. Energy Logserver does not differentiate between missing fields and fields explicitly set to `NULL`:

```sql
SELECT account_number, employer
FROM accounts
WHERE employer IS NULL
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">employer</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">18</td>
    <td class="tg-pnl2"> </td>
  </tr>
</tbody>
</table>

*Example 3*: Deletes a document that satisfies the predicates in the `WHERE` clause:

```sql
DELETE FROM accounts
WHERE age > 30
```

##### Group By

Group documents with the same field value into buckets.

*Example 1*: Group by fields:

```sql
SELECT age
FROM accounts
GROUP BY age
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">id</th>
    <th class="tg-ua3b">age</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">0</td>
    <td class="tg-pnl2">28</td>
  </tr>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">32</td>
  </tr>
  <tr>
    <td class="tg-pnl2">2</td>
    <td class="tg-pnl2">33</td>
  </tr>
  <tr>
    <td class="tg-pnl2">3</td>
    <td class="tg-pnl2">36</td>
  </tr>
</tbody>
</table>

*Example 2*: Group by field alias:

```sql
SELECT account_number AS num
FROM accounts
GROUP BY num
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">id</th>
    <th class="tg-ua3b">num</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">0</td>
    <td class="tg-pnl2">1</td>
  </tr>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">6</td>
  </tr>
  <tr>
    <td class="tg-pnl2">2</td>
    <td class="tg-pnl2">13</td>
  </tr>
  <tr>
    <td class="tg-pnl2">3</td>
    <td class="tg-pnl2">18</td>
  </tr>
</tbody>
</table>

*Example 4*: Use scalar functions in the `GROUP BY` clause:

```sql
SELECT ABS(age) AS a
FROM accounts
GROUP BY ABS(age)
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">id</th>
    <th class="tg-ua3b">a</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">0</td>
    <td class="tg-pnl2">28.0</td>
  </tr>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">32.0</td>
  </tr>
  <tr>
    <td class="tg-pnl2">2</td>
    <td class="tg-pnl2">33.0</td>
  </tr>
  <tr>
    <td class="tg-pnl2">3</td>
    <td class="tg-pnl2">36.0</td>
  </tr>
</tbody>
</table>

##### Having

Use the `HAVING` clause to aggregate inside each bucket based on aggregation functions (`COUNT`, `AVG`, `SUM`, `MIN`, and `MAX`).
The `HAVING` clause filters results from the `GROUP BY` clause:

*Example 1*:

```sql
SELECT age, MAX(balance)
FROM accounts
GROUP BY age HAVING MIN(balance) > 10000
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">id</th>
    <th class="tg-ua3b">age</th>
    <th class="tg-ua3b">MAX (balance)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">0</td>
    <td class="tg-pnl2">28</td>
    <td class="tg-pnl2">32838</td>
  </tr>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">32</td>
    <td class="tg-pnl2">39225</td>
  </tr>
</tbody>
</table>

##### Order By

Use the `ORDER BY` clause to sort results into your desired order.

*Example 1*: Use `ORDER BY` to sort by ascending or descending order. Besides regular field names, using `ordinal`, `alias`, or `scalar` functions are supported:

```sql
SELECT account_number
FROM accounts
ORDER BY account_number DESC
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">18</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
  </tr>
  <tr>
    <td class="tg-pnl2">1</td>
  </tr>
</tbody>
</table>

*Example 2*: Specify if documents with missing fields are to be put at the beginning or at the end of the results. The default behavior of Energy Logserver is to return nulls or missing fields at the end. To push them before non-nulls, use the `IS NOT NULL` operator:

```sql
SELECT employer
FROM accounts
ORDER BY employer IS NOT NULL
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">employer</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2"> </td>
  </tr>
  <tr>
    <td class="tg-pnl2">Netagy</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Pyrami</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Quility</td>
  </tr>
</tbody>
</table>

##### Limit

Specify the maximum number of documents that you want to retrieve. Used to prevent fetching large amounts of data into memory.

*Example 1*: If you pass in a single argument, it's mapped to the `size` parameter in Energy Logserver and the `from` parameter is set to 0.

```sql
SELECT account_number
FROM accounts
ORDER BY account_number LIMIT 1
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
  </tr>
</tbody>
</table>

*Example 2*: If you pass in two arguments, the first is mapped to the `from` parameter and the second to the `size` parameter in Energy Logserver. You can use this for simple pagination for small indexes, as it's inefficient for large indexes.
Use `ORDER BY` to ensure the same order between pages:

```sql
SELECT account_number
FROM accounts
ORDER BY account_number LIMIT 1, 1
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">6</td>
  </tr>
</tbody>
</table>

#### Complex queries

Besides simple SFW (`SELECT-FROM-WHERE`) queries, the SQL plugin supports complex queries such as subquery, join, union, and minus. These queries operate on more than one Energy Logserver index. To examine how these queries execute behind the scenes, use the `explain` operation.

##### Joins

Energy Logserver SQL supports inner joins, cross joins, and left outer joins.

###### Constraints

Joins have a number of constraints:

1. You can only join two indexes.
1. You must use aliases for indexes (for example, `people p`).
1. Within an ON clause, you can only use AND conditions.
1. In a WHERE statement, don't combine trees that contain multiple indexes. For example, the following statement works:

   ```sql
   WHERE (a.type1 > 3 OR a.type1 < 0) AND (b.type2 > 4 OR b.type2 < -1)
   ```

   The following statement does not:

   ```sql
   WHERE (a.type1 > 3 OR b.type2 < 0) AND (a.type1 > 4 OR b.type2 < -1)
   ```

1. You can't use GROUP BY or ORDER BY for results.
1. LIMIT with OFFSET (e.g. `LIMIT 25 OFFSET 25`) is not supported.

###### Description

The `JOIN` clause combines columns from one or more indexes using values common to each.

###### Syntax

Rule `tableSource`:

![tableSource](/media/media/tableSource.png)

Rule `joinPart`:

![joinPart](/media/media/joinPart.png)

###### Example 1: Inner join

Inner join creates a new result set by combining columns of two indexes based on your join predicates. It iterates the two indexes and compares each document to find the ones that satisfy the join predicates. You can optionally precede the `JOIN` clause with an `INNER` keyword.

The join predicate(s) is specified by the ON clause.

SQL query:

```sql
SELECT
  a.account_number, a.firstname, a.lastname,
  e.id, e.name
FROM accounts a
JOIN employees_nested e
 ON a.account_number = e.id
```

Explain:

The `explain` output is complicated, because a `JOIN` clause is associated with two Energy Logserver DSL queries that execute in separate query planner frameworks. You can interpret it by examining the `Physical Plan` and `Logical Plan` objects.

```json
{
  "Physical Plan" : {
    "Project [ columns=[a.account_number, a.firstname, a.lastname, e.name, e.id] ]" : {
      "Top [ count=200 ]" : {
        "BlockHashJoin[ conditions=( a.account_number = e.id ), type=JOIN, blockSize=[FixedBlockSize with size=10000] ]" : {
          "Scroll [ employees_nested as e, pageSize=10000 ]" : {
            "request" : {
              "size" : 200,
              "from" : 0,
              "_source" : {
                "excludes" : [ ],
                "includes" : [
                  "id",
                  "name"
                ]
              }
            }
          },
          "Scroll [ accounts as a, pageSize=10000 ]" : {
            "request" : {
              "size" : 200,
              "from" : 0,
              "_source" : {
                "excludes" : [ ],
                "includes" : [
                  "account_number",
                  "firstname",
                  "lastname"
                ]
              }
            }
          },
          "useTermsFilterOptimization" : false
        }
      }
    }
  },
  "description" : "Hash Join algorithm builds hash table based on result of first query, and then probes hash table to find matched rows for each row returned by second query",
  "Logical Plan" : {
    "Project [ columns=[a.account_number, a.firstname, a.lastname, e.name, e.id] ]" : {
      "Top [ count=200 ]" : {
        "Join [ conditions=( a.account_number = e.id ) type=JOIN ]" : {
          "Group" : [
            {
              "Project [ columns=[a.account_number, a.firstname, a.lastname] ]" : {
                "TableScan" : {
                  "tableAlias" : "a",
                  "tableName" : "accounts"
                }
              }
            },
            {
              "Project [ columns=[e.name, e.id] ]" : {
                "TableScan" : {
                  "tableAlias" : "e",
                  "tableName" : "employees_nested"
                }
              }
            }
          ]
        }
      }
    }
  }
}
```

Result set:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">a.account_number</th>
    <th class="tg-ua3b">a.firstname</th>
    <th class="tg-ua3b">a.lastname</th>
    <th class="tg-ua3b">e.id</th>
    <th class="tg-ua3b">e.name</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">Hattie</td>
    <td class="tg-pnl2">Bond</td>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">Jane Smith</td>
  </tr>
</tbody>
</table>

###### Example 2: Cross join

Cross join, also known as cartesian join, combines each document from the first index with each document from the second.
The result set is the the cartesian product of documents of both indexes.
This operation is similar to the inner join without the `ON` clause that specifies the join condition.

It's risky to perform cross join on two indexes of large or even medium size. It might trigger a circuit breaker that terminates the query to avoid running out of memory.
{: .warning }

SQL query:

```sql
SELECT
  a.account_number, a.firstname, a.lastname,
  e.id, e.name
FROM accounts a
JOIN employees_nested e
```

Result set:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">a.account_number</th>
    <th class="tg-ua3b">a.firstname</th>
    <th class="tg-ua3b">a.lastname</th>
    <th class="tg-ua3b">e.id</th>
    <th class="tg-ua3b">e.name</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">Amber</td>
    <td class="tg-pnl2">Duke</td>
    <td class="tg-pnl2">3</td>
    <td class="tg-pnl2">Bob Smith</td>
  </tr>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">Amber</td>
    <td class="tg-pnl2">Duke</td>
    <td class="tg-pnl2">4</td>
    <td class="tg-pnl2">Susan Smith</td>
  </tr>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">Amber</td>
    <td class="tg-pnl2">Duke</td>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">Jane Smith</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">Hattie</td>
    <td class="tg-pnl2">Bond</td>
    <td class="tg-pnl2">3</td>
    <td class="tg-pnl2">Bob Smith</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">Hattie</td>
    <td class="tg-pnl2">Bond</td>
    <td class="tg-pnl2">4</td>
    <td class="tg-pnl2">Susan Smith</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">Hattie</td>
    <td class="tg-pnl2">Bond</td>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">Jane Smith</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">Nanette</td>
    <td class="tg-pnl2">Bates</td>
    <td class="tg-pnl2">3</td>
    <td class="tg-pnl2">Bob Smith</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">Nanette</td>
    <td class="tg-pnl2">Bates</td>
    <td class="tg-pnl2">4</td>
    <td class="tg-pnl2">Susan Smith</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">Nanette</td>
    <td class="tg-pnl2">Bates</td>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">Jane Smith</td>
  </tr>
  <tr>
    <td class="tg-pnl2">18</td>
    <td class="tg-pnl2">Dale</td>
    <td class="tg-pnl2">Adams</td>
    <td class="tg-pnl2">3</td>
    <td class="tg-pnl2">Bob Smith</td>
  </tr>
  <tr>
    <td class="tg-pnl2">18</td>
    <td class="tg-pnl2">Dale</td>
    <td class="tg-pnl2">Adams</td>
    <td class="tg-pnl2">4</td>
    <td class="tg-pnl2">Susan Smith</td>
  </tr>
  <tr>
    <td class="tg-pnl2">18</td>
    <td class="tg-pnl2">Dale</td>
    <td class="tg-pnl2">Adams</td>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">Jane Smith</td>
  </tr>
</tbody>
</table>

###### Example 3: Left outer join

Use left outer join to retain rows from the first index if it does not satisfy the join predicate. The keyword `OUTER` is optional.

SQL query:

```sql
SELECT
  a.account_number, a.firstname, a.lastname,
  e.id, e.name
FROM accounts a
LEFT JOIN employees_nested e
 ON a.account_number = e.id
```

Result set:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">a.account_number</th>
    <th class="tg-ua3b">a.firstname</th>
    <th class="tg-ua3b">a.lastname</th>
    <th class="tg-ua3b">e.id</th>
    <th class="tg-ua3b">e.name</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">Amber</td>
    <td class="tg-pnl2">Duke</td>
    <td class="tg-pnl2">null</td>
    <td class="tg-pnl2">null</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">Hattie</td>
    <td class="tg-pnl2">Bond</td>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">Jane Smith</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">Nanette</td>
    <td class="tg-pnl2">Bates</td>
    <td class="tg-pnl2">null</td>
    <td class="tg-pnl2">null</td>
  </tr>
  <tr>
    <td class="tg-pnl2">18</td>
    <td class="tg-pnl2">Dale</td>
    <td class="tg-pnl2">Adams</td>
    <td class="tg-pnl2">null</td>
    <td class="tg-pnl2">null</td>
  </tr>
</tbody>
</table>

##### Subquery

A subquery is a complete `SELECT` statement used within another statement and enclosed in parenthesis.
From the explain output, you can see that some subqueries are actually transformed to an equivalent join query to execute.

###### Example 1: Table subquery

SQL query:

```sql
SELECT a1.firstname, a1.lastname, a1.balance
FROM accounts a1
WHERE a1.account_number IN (
  SELECT a2.account_number
  FROM accounts a2
  WHERE a2.balance > 10000
)
```

Explain:

```json
{
  "Physical Plan" : {
    "Project [ columns=[a1.balance, a1.firstname, a1.lastname] ]" : {
      "Top [ count=200 ]" : {
        "BlockHashJoin[ conditions=( a1.account_number = a2.account_number ), type=JOIN, blockSize=[FixedBlockSize with size=10000] ]" : {
          "Scroll [ accounts as a2, pageSize=10000 ]" : {
            "request" : {
              "size" : 200,
              "query" : {
                "bool" : {
                  "filter" : [
                    {
                      "bool" : {
                        "adjust_pure_negative" : true,
                        "must" : [
                          {
                            "bool" : {
                              "adjust_pure_negative" : true,
                              "must" : [
                                {
                                  "bool" : {
                                    "adjust_pure_negative" : true,
                                    "must_not" : [
                                      {
                                        "bool" : {
                                          "adjust_pure_negative" : true,
                                          "must_not" : [
                                            {
                                              "exists" : {
                                                "field" : "account_number",
                                                "boost" : 1
                                              }
                                            }
                                          ],
                                          "boost" : 1
                                        }
                                      }
                                    ],
                                    "boost" : 1
                                  }
                                },
                                {
                                  "range" : {
                                    "balance" : {
                                      "include_lower" : false,
                                      "include_upper" : true,
                                      "from" : 10000,
                                      "boost" : 1,
                                      "to" : null
                                    }
                                  }
                                }
                              ],
                              "boost" : 1
                            }
                          }
                        ],
                        "boost" : 1
                      }
                    }
                  ],
                  "adjust_pure_negative" : true,
                  "boost" : 1
                }
              },
              "from" : 0
            }
          },
          "Scroll [ accounts as a1, pageSize=10000 ]" : {
            "request" : {
              "size" : 200,
              "from" : 0,
              "_source" : {
                "excludes" : [ ],
                "includes" : [
                  "firstname",
                  "lastname",
                  "balance",
                  "account_number"
                ]
              }
            }
          },
          "useTermsFilterOptimization" : false
        }
      }
    }
  },
  "description" : "Hash Join algorithm builds hash table based on result of first query, and then probes hash table to find matched rows for each row returned by second query",
  "Logical Plan" : {
    "Project [ columns=[a1.balance, a1.firstname, a1.lastname] ]" : {
      "Top [ count=200 ]" : {
        "Join [ conditions=( a1.account_number = a2.account_number ) type=JOIN ]" : {
          "Group" : [
            {
              "Project [ columns=[a1.balance, a1.firstname, a1.lastname, a1.account_number] ]" : {
                "TableScan" : {
                  "tableAlias" : "a1",
                  "tableName" : "accounts"
                }
              }
            },
            {
              "Project [ columns=[a2.account_number] ]" : {
                "Filter [ conditions=[AND ( AND account_number ISN null, AND balance GT 10000 ) ] ]" : {
                  "TableScan" : {
                    "tableAlias" : "a2",
                    "tableName" : "accounts"
                  }
                }
              }
            }
          ]
        }
      }
    }
  }
}
```

Result set:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">a1.firstname</th>
    <th class="tg-ua3b">a1.lastname</th>
    <th class="tg-ua3b">a1.balance</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">Amber</td>
    <td class="tg-pnl2">Duke</td>
    <td class="tg-pnl2">39225</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Nanette</td>
    <td class="tg-pnl2">Bates</td>
    <td class="tg-pnl2">32838</td>
  </tr>
</tbody>
</table>

###### Example 2: From subquery

SQL query:

```sql
SELECT a.f, a.l, a.a
FROM (
  SELECT firstname AS f, lastname AS l, age AS a
  FROM accounts
  WHERE age > 30
) AS a
```

Explain:

```json
{
  "from" : 0,
  "size" : 200,
  "query" : {
    "bool" : {
      "filter" : [
        {
          "bool" : {
            "must" : [
              {
                "range" : {
                  "age" : {
                    "from" : 30,
                    "to" : null,
                    "include_lower" : false,
                    "include_upper" : true,
                    "boost" : 1.0
                  }
                }
              }
            ],
            "adjust_pure_negative" : true,
            "boost" : 1.0
          }
        }
      ],
      "adjust_pure_negative" : true,
      "boost" : 1.0
    }
  },
  "_source" : {
    "includes" : [
      "firstname",
      "lastname",
      "age"
    ],
    "excludes" : [ ]
  }
}
```

Result set:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">f</th>
    <th class="tg-ua3b">l</th>
    <th class="tg-ua3b">a</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">Amber</td>
    <td class="tg-pnl2">Duke</td>
    <td class="tg-pnl2">32</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Dale</td>
    <td class="tg-pnl2">Adams</td>
    <td class="tg-pnl2">33</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Hattie</td>
    <td class="tg-pnl2">Bond</td>
    <td class="tg-pnl2">36</td>
  </tr>
</tbody>
</table>

#### Functions

The SQL language supports all SQL plugin [common functions](https://opensearch.org/docs/latest/search-plugins/sql/functions/), including [relevance search](https://opensearch.org/docs/latest/search-plugins/sql/full-text/), but also introduces a few function synonyms, which are available in SQL only.
These synonyms are provided by the `V1` engine. For more information, see [Limitations](https://opensearch.org/docs/latest/search-plugins/sql/limitation).

##### Match query

The `MATCHQUERY` and `MATCH_QUERY` functions are synonyms for the [`MATCH`](https://opensearch.org/docs/latest/search-plugins/sql/full-text#match) relevance function. They don't accept additional arguments but provide an alternate syntax.

###### Syntax

To use `matchquery` or `match_query`, pass in your search query and the field name that you want to search against:

```sql
match_query(field_expression, query_expression[, option=<option_value>]*)
matchquery(field_expression, query_expression[, option=<option_value>]*)
field_expression = match_query(query_expression[, option=<option_value>]*)
field_expression = matchquery(query_expression[, option=<option_value>]*)
```

You can specify the following options in any order:

- `analyzer`
- `boost`

###### Example

You can use `MATCHQUERY` to replace `MATCH`:

```sql
SELECT account_number, address
FROM accounts
WHERE MATCHQUERY(address, 'Holmes')
```

Alternatively, you can use `MATCH_QUERY` to replace `MATCH`:

```sql
SELECT account_number, address
FROM accounts
WHERE address = MATCH_QUERY('Holmes')
```

The results contain documents in which the address contains "Holmes":

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">address</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">880 Holmes Lane</td>
  </tr>
</tbody>
</table>

##### Multi-match

There are three synonyms for `MULTI_MATCH`, each with a slightly different syntax. They accept a query string and a fields list with weights. They can also accept additional optional parameters.

###### Syntax

```sql
multimatch('query'=query_expression[, 'fields'=field_expression][, option=<option_value>]*)
multi_match('query'=query_expression[, 'fields'=field_expression][, option=<option_value>]*)
multimatchquery('query'=query_expression[, 'fields'=field_expression][, option=<option_value>]*)
```

The `fields` parameter is optional and can contain a single field or a comma-separated list (whitespace characters are not allowed). The weight for each field is optional and is specified after the field name. It should be delimited by the `caret` character -- `^` -- without whitespace.

###### Example

The following queries show the `fields` parameter of a multi-match query with a single field and a field list:

```sql
multi_match('fields' = "Tags^2,Title^3.4,Body,Comments^0.3", ...)
multi_match('fields' = "Title", ...)
```

You can specify the following options in any order:

- `analyzer`
- `boost`
- `slop`
- `type`
- `tie_breaker`
- `operator`

##### Query string

The `QUERY` function is a synonym for 'QUERY_STRING`.

###### Syntax

```sql
query('query'=query_expression[, 'fields'=field_expression][, option=<option_value>]*)
```

The `fields` parameter is optional and can contain a single field or a comma-separated list (whitespace characters are not allowed). The weight for each field is optional and is specified after the field name. It should be delimited by the `caret` character -- `^` -- without whitespace.

###### Example

The following queries show the `fields` parameter of a multi-match query with a single field and a field list:

```sql
query('fields' = "Tags^2,Title^3.4,Body,Comments^0.3", ...)
query('fields' = "Tags", ...)
```

You can specify the following options in any order:

- `analyzer`
- `boost`
- `slop`
- `default_field`

###### Example of using `query_string` in SQL and PPL queries:

The following is a sample REST API search request in Energy Logserver DSL.

```json
GET accounts/_search
{
  "query": {
    "query_string": {
      "query": "Lane Street",
      "fields": [ "address" ],
    }
  }
}
```

The request above is equivalent to the following `query` function:

```sql
SELECT account_number, address
FROM accounts
WHERE query('address:Lane OR address:Street')
```

The results contain addresses that contain "Lane" or "Street":

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">address</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">880 Holmes Lane</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">671 Bristol Street</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">789 Madison Street</td>
  </tr>
</tbody>
</table>

##### Match phrase

The `MATCHPHRASEQUERY` function is a synonym for `MATCH_PHRASE`.

###### Syntax

```sql
matchphrasequery(query_expression, field_expression[, option=<option_value>]*)
```

You can specify the following options in any order:

- `analyzer`
- `boost`
- `slop`

##### Score query

To return a relevance score along with every matching document, use the `SCORE`, `SCOREQUERY`, or `SCORE_QUERY` functions.

###### Syntax

The `SCORE` function expects two arguments. The first argument is the [`MATCH_QUERY`](#match-query) expression. The second argument is an optional floating-point number to boost the score (the default value is 1.0):

```sql
SCORE(match_query_expression, score)
SCOREQUERY(match_query_expression, score)
SCORE_QUERY(match_query_expression, score)
```

###### Example

The following example uses the `SCORE` function to boost the documents' scores:

```sql
SELECT account_number, address, _score
FROM accounts
WHERE SCORE(MATCH_QUERY(address, 'Lane'), 0.5) OR
  SCORE(MATCH_QUERY(address, 'Street'), 100)
ORDER BY _score
```

The results contain matches with corresponding scores:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">address</th>
    <th class="tg-ua3b">score</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">880 Holmes Lane</td>
    <td class="tg-pnl2">0.5</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">671 Bristol Street</td>
    <td class="tg-pnl2">100</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">789 Madison Street</td>
    <td class="tg-pnl2">100</td>
  </tr>
</tbody>
</table>

##### Wildcard query

To search documents by a given wildcard, use the `WILDCARDQUERY` or `WILDCARD_QUERY` functions.

###### Syntax

```sql
wildcardquery(field_expression, query_expression[, boost=<value>])
wildcard_query(field_expression, query_expression[, boost=<value>])
```

###### Example

The following example uses a wildcard query:

```sql
SELECT account_number, address
FROM accounts
WHERE wildcard_query(address, '*Holmes*');
```

The results contain documents that match the wildcard expression:

| account_number | address
:--- | :---
1 | 880 Holmes Lane

#### JSON Support

SQL plugin supports JSON by following [PartiQL](https://partiql.org/) specification, a SQL-compatible query language that lets you query semi-structured and nested data for any data format. The SQL plugin only supports a subset of the PartiQL specification.

##### Querying nested collection

PartiQL extends SQL to allow you to query and unnest nested collections. In Energy Logserver, this is very useful to query a JSON index with nested objects or fields.

To follow along, use the `bulk` operation to index some sample data:

```json
POST employees_nested/_bulk?refresh
{"index":{"_id":"1"}}
{"id":3,"name":"Bob Smith","title":null,"projects":[{"name":"SQL Spectrum querying","started_year":1990},{"name":"SQL security","started_year":1999},{"name":"Energy Logserver security","started_year":2015}]}
{"index":{"_id":"2"}}
{"id":4,"name":"Susan Smith","title":"Dev Mgr","projects":[]}
{"index":{"_id":"3"}}
{"id":6,"name":"Jane Smith","title":"Software Eng 2","projects":[{"name":"SQL security","started_year":1998},{"name":"Hello security","started_year":2015,"address":[{"city":"Dallas","state":"TX"}]}]}
```

###### Example 1: Unnesting a nested collection

This example finds the nested document (`projects`) with a field value (`name`) that satisfies the predicate (contains `security`). Because each parent document can have more than one nested documents, the nested document that matches is flattened. In other words, the final result is the cartesian product between the parent and nested documents.

```sql
SELECT e.name AS employeeName,
       p.name AS projectName
FROM employees_nested AS e,
       e.projects AS p
WHERE p.name LIKE '%security%'
```

Explain:

```json
{
  "from" : 0,
  "size" : 200,
  "query" : {
    "bool" : {
      "filter" : [
        {
          "bool" : {
            "must" : [
              {
                "nested" : {
                  "query" : {
                    "wildcard" : {
                      "projects.name" : {
                        "wildcard" : "*security*",
                        "boost" : 1.0
                      }
                    }
                  },
                  "path" : "projects",
                  "ignore_unmapped" : false,
                  "score_mode" : "none",
                  "boost" : 1.0,
                  "inner_hits" : {
                    "ignore_unmapped" : false,
                    "from" : 0,
                    "size" : 3,
                    "version" : false,
                    "seq_no_primary_term" : false,
                    "explain" : false,
                    "track_scores" : false,
                    "_source" : {
                      "includes" : [
                        "projects.name"
                      ],
                      "excludes" : [ ]
                    }
                  }
                }
              }
            ],
            "adjust_pure_negative" : true,
            "boost" : 1.0
          }
        }
      ],
      "adjust_pure_negative" : true,
      "boost" : 1.0
    }
  },
  "_source" : {
    "includes" : [
      "name"
    ],
    "excludes" : [ ]
  }
}
```

Result set:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">employeeName</th>
    <th class="tg-ua3b">projectName</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">Bob Smith</td>
    <td class="tg-pnl2">Energy Logserver Security</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Bob Smith</td>
    <td class="tg-pnl2">SQL security</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Jane Smith</td>
    <td class="tg-pnl2">Hello security</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Jane Smith</td>
    <td class="tg-pnl2">SQL security</td>
  </tr>
</tbody>
</table>

###### Example 2: Unnesting in existential subquery

To unnest a nested collection in a subquery to check if it satisfies a condition:

```sql
SELECT e.name AS employeeName
FROM employees_nested AS e
WHERE EXISTS (
    SELECT *
    FROM e.projects AS p
    WHERE p.name LIKE '%security%'
)
```

Explain:

```json
{
  "from" : 0,
  "size" : 200,
  "query" : {
    "bool" : {
      "filter" : [
        {
          "bool" : {
            "must" : [
              {
                "nested" : {
                  "query" : {
                    "bool" : {
                      "must" : [
                        {
                          "bool" : {
                            "must" : [
                              {
                                "bool" : {
                                  "must_not" : [
                                    {
                                      "bool" : {
                                        "must_not" : [
                                          {
                                            "exists" : {
                                              "field" : "projects",
                                              "boost" : 1.0
                                            }
                                          }
                                        ],
                                        "adjust_pure_negative" : true,
                                        "boost" : 1.0
                                      }
                                    }
                                  ],
                                  "adjust_pure_negative" : true,
                                  "boost" : 1.0
                                }
                              },
                              {
                                "wildcard" : {
                                  "projects.name" : {
                                    "wildcard" : "*security*",
                                    "boost" : 1.0
                                  }
                                }
                              }
                            ],
                            "adjust_pure_negative" : true,
                            "boost" : 1.0
                          }
                        }
                      ],
                      "adjust_pure_negative" : true,
                      "boost" : 1.0
                    }
                  },
                  "path" : "projects",
                  "ignore_unmapped" : false,
                  "score_mode" : "none",
                  "boost" : 1.0
                }
              }
            ],
            "adjust_pure_negative" : true,
            "boost" : 1.0
          }
        }
      ],
      "adjust_pure_negative" : true,
      "boost" : 1.0
    }
  },
  "_source" : {
    "includes" : [
      "name"
    ],
    "excludes" : [ ]
  }
}
```

Result set:

| employeeName |
:--- | :---
Bob Smith |
Jane Smith |

#### Metadata queries

To see basic metadata about your indexes, use the `SHOW` and `DESCRIBE` commands.

##### Syntax

Rule `showStatement`:

![showStatement](/media/media/showStatement.png)

Rule `showFilter`:

![showFilter](/media/media/showFilter.png)

##### Example 1: See metadata for indexes

To see metadata for indexes that match a specific pattern, use the `SHOW` command.
Use the wildcard `%` to match all indexes:

```sql
SHOW TABLES LIKE %
```

| TABLE_CAT | TABLE_SCHEM | TABLE_NAME | TABLE_TYPE | REMARKS | TYPE_CAT | TYPE_SCHEM | TYPE_NAME | SELF_REFERENCING_COL_NAME | REF_GENERATION
:--- | :---
docker-cluster | null | accounts | BASE TABLE | null | null | null | null | null | null
docker-cluster  | null | employees_nested | BASE TABLE | null | null | null | null | null | null

##### Example 2: See metadata for a specific index

To see metadata for an index name with a prefix of `acc`:

```sql
SHOW TABLES LIKE acc%
```

| TABLE_CAT | TABLE_SCHEM | TABLE_NAME | TABLE_TYPE | REMARKS | TYPE_CAT | TYPE_SCHEM | TYPE_NAME | SELF_REFERENCING_COL_NAME | REF_GENERATION
:--- | :---
docker-cluster | null | accounts | BASE TABLE | null | null | null | null | null | null

##### Example 3: See metadata for fields

To see metadata for field names that match a specific pattern, use the `DESCRIBE` command:

```sql
DESCRIBE TABLES LIKE accounts
```

| TABLE_CAT | TABLE_SCHEM | TABLE_NAME | COLUMN_NAME | DATA_TYPE | TYPE_NAME | COLUMN_SIZE | BUFFER_LENGTH | DECIMAL_DIGITS | NUM_PREC_RADIX | NULLABLE | REMARKS | COLUMN_DEF | SQL_DATA_TYPE | SQL_DATETIME_SUB | CHAR_OCTET_LENGTH | ORDINAL_POSITION | IS_NULLABLE | SCOPE_CATALOG | SCOPE_SCHEMA | SCOPE_TABLE | SOURCE_DATA_TYPE | IS_AUTOINCREMENT | IS_GENERATEDCOLUMN
:--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---
docker-cluster | null | accounts | account_number | null | long | null | null | null | 10 | 2 | null | null | null | null | null | 1 |  | null | null | null | null | NO |
docker-cluster | null | accounts | firstname | null | text | null | null | null | 10 | 2 | null | null | null | null | null | 2 |  | null | null | null | null | NO |
docker-cluster | null | accounts | address | null | text | null | null | null | 10 | 2 | null | null | null | null | null | 3 |  | null | null | null | null | NO |
docker-cluster | null | accounts | balance | null | long | null | null | null | 10 | 2 | null | null | null | null | null | 4 |  | null | null | null | null | NO |
docker-cluster | null | accounts | gender | null | text | null | null | null | 10 | 2 | null | null | null | null | null | 5 |  | null | null | null | null | NO |
docker-cluster | null | accounts | city | null | text | null | null | null | 10 | 2 | null | null | null | null | null | 6 |  | null | null | null | null | NO |
docker-cluster | null | accounts | employer | null | text | null | null | null | 10 | 2 | null | null | null | null | null | 7 |  | null | null | null | null | NO |
docker-cluster | null | accounts | state | null | text | null | null | null | 10 | 2 | null | null | null | null | null | 8 |  | null | null | null | null | NO |
docker-cluster | null | accounts | age | null | long | null | null | null | 10 | 2 | null | null | null | null | null | 9 |  | null | null | null | null | NO |
docker-cluster | null | accounts | email | null | text | null | null | null | 10 | 2 | null | null | null | null | null | 10 |  | null | null | null | null | NO |
docker-cluster | null | accounts | lastname | null | text | null | null | null | 10 | 2 | null | null | null | null | null | 11 |  | null | null | null | null | NO |

#### Aggregate functions

Aggregate functions operate on subsets defined by the `GROUP BY` clause. In the absence of a `GROUP BY` clause, aggregate functions operate on all elements of the result set. You can use aggregate functions in the `GROUP BY`, `SELECT`, and `HAVING` clauses.

Energy Logserver supports the following aggregate functions.

Function | Description
:--- | :---
`AVG` | Returns the average of the results.
`COUNT` | Returns the number of results.
`SUM` | Returns the sum of the results.
`MIN` | Returns the minimum of the results.
`MAX` | Returns the maximum of the results.
`VAR_POP` or `VARIANCE` | Returns the population variance of the results after discarding nulls. Returns 0 when there is only one row of results.
`VAR_SAMP` | Returns the sample variance of the results after discarding nulls. Returns null when there is only one row of results.
`STD` or `STDDEV` | Returns the sample standard deviation of the results. Returns 0 when there is only one row of results.
`STDDEV_POP` | Returns the population standard deviation of the results. Returns 0 when there is only one row of results.
`STDDEV_SAMP` | Returns the sample standard deviation of the results. Returns null when there is only one row of results.

The examples below reference an `employees` table. You can try out the examples by indexing the following documents into Energy Logserver using the bulk index operation:

```json
PUT employees/_bulk?refresh
{"index":{"_id":"1"}}
{"employee_id": 1, "department":1, "firstname":"Amber", "lastname":"Duke", "sales":1356, "sale_date":"2020-01-23"}
{"index":{"_id":"2"}}
{"employee_id": 1, "department":1, "firstname":"Amber", "lastname":"Duke", "sales":39224, "sale_date":"2021-01-06"}
{"index":{"_id":"6"}}
{"employee_id":6, "department":1, "firstname":"Hattie", "lastname":"Bond", "sales":5686, "sale_date":"2021-06-07"}
{"index":{"_id":"7"}}
{"employee_id":6, "department":1, "firstname":"Hattie", "lastname":"Bond", "sales":12432, "sale_date":"2022-05-18"}
{"index":{"_id":"13"}}
{"employee_id":13,"department":2, "firstname":"Nanette", "lastname":"Bates", "sales":32838, "sale_date":"2022-04-11"}
{"index":{"_id":"18"}}
{"employee_id":18,"department":2, "firstname":"Dale", "lastname":"Adams", "sales":4180, "sale_date":"2022-11-05"}
```

##### GROUP BY

The `GROUP BY` clause defines subsets of a result set. Aggregate functions operate on these subsets and return one result row for each subset.

You can use an identifier, ordinal, or expression in the `GROUP BY` clause.

###### Using an identifier in GROUP BY

You can specify the field name (column name) to aggregate on in the `GROUP BY` clause. For example, the following query returns the department numbers and the total sales for each department:

```sql
SELECT department, sum(sales)
FROM employees
GROUP BY department;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">department</th>
    <th class="tg-ua3b">sum(sales)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">58700<</td>
  </tr>
  <tr>
    <td class="tg-pnl2">2</td>
    <td class="tg-pnl2">37018</td>
  </tr>
</tbody>
</table>

###### Using an ordinal in GROUP BY

You can specify the column number to aggregate on in the `GROUP BY` clause. The column number is determined by the column position in the `SELECT` clause. For example, the following query is equivalent to the query above. It returns the department numbers and the total sales for each department. It groups the results by the first column of the result set, which is `department`:

```sql
SELECT department, sum(sales)
FROM employees
GROUP BY 1;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">department</th>
    <th class="tg-ua3b">sum(sales)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">58700</td>
  </tr>
  <tr>
    <td class="tg-pnl2">2</td>
    <td class="tg-pnl2">37018</td>
  </tr>
</tbody>
</table>

###### Using an expression in GROUP BY

You can use an expression in the `GROUP BY` clause. For example, the following query returns the average sales for each year:

```sql
SELECT year(sale_date), avg(sales)
FROM employees
GROUP BY year(sale_date);
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">year(start_date)</th>
    <th class="tg-ua3b">avg(sales)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">2020 </td>
    <td class="tg-pnl2">1356.0</td>
  </tr>
  <tr>
    <td class="tg-pnl2">2021</td>
    <td class="tg-pnl2">22455.0</td>
  </tr>
  <tr>
    <td class="tg-pnl2">2022</td>
    <td class="tg-pnl2">16484.0</td>
  </tr>
</tbody>
</table>

##### SELECT

You can use aggregate expressions in the `SELECT` clause either directly or as part of a larger expression. In addition, you can use expressions as arguments of aggregate functions.

###### Using aggregate expressions directly in SELECT

The following query returns the average sales for each department:

```sql
SELECT department, avg(sales)
FROM employees
GROUP BY department;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">department</th>
    <th class="tg-ua3b">avg(sales)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">14675.0</td>
  </tr>
  <tr>
    <td class="tg-pnl2">2</td>
    <td class="tg-pnl2">18509.0</td>
  </tr>
</tbody>
</table>

###### Using aggregate expressions as part of larger expressions in SELECT

The following query calculates the average commission for the employees of each department as 5% of the average sales:

```sql
SELECT department, avg(sales) * 0.05 as avg_commission
FROM employees
GROUP BY department;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">department</th>
    <th class="tg-ua3b">avg_commission</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">733.75</td>
  </tr>
  <tr>
    <td class="tg-pnl2">2</td>
    <td class="tg-pnl2">925.45</td>
  </tr>
</tbody>
</table>

###### Using expressions as arguments to aggregate functions

The following query calculates the average commission amount for each department. First it calculates the commission amount for each `sales` value as 5% of the `sales`. Then it determines the average of all commission values:

```sql
SELECT department, avg(sales * 0.05) as avg_commission
FROM employees
GROUP BY department;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">department</th>
    <th class="tg-ua3b">avg_commission</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">733.75</td>
  </tr>
  <tr>
    <td class="tg-pnl2">2</td>
    <td class="tg-pnl2">925.45</td>
  </tr>
</tbody>
</table>

##### COUNT

The `COUNT` function accepts arguments, such as `*`, or literals, such as `1`.
The following table describes how various forms of the `COUNT` function operate.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Function type</th>
    <th class="tg-ua3b">Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">COUNT(field)</td>
    <td class="tg-pnl2">Counts the number of rows where the value of the given field (or expression) is not null.</td>
  </tr>
  <tr>
    <td class="tg-pnl2">COUNT(*)</td>
    <td class="tg-pnl2">Counts the total number of rows in a table.</td>
  </tr>
  <tr>
    <td class="tg-pnl2">COUNT(1) [same as COUNT(*)]</td>
    <td class="tg-pnl2">Counts any non-null literal.</td>
  </tr>
</tbody>
</table>

For example, the following query returns the count of sales for each year:

```sql
SELECT year(sale_date), count(sales)
FROM employees
GROUP BY year(sale_date);
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">year(sale_date)</th>
    <th class="tg-ua3b">count(sales)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">2020</td>
    <td class="tg-pnl2">1</td>
  </tr>
  <tr>
    <td class="tg-pnl2">2021</td>
    <td class="tg-pnl2">2</td>
  </tr>
  <tr>
    <td class="tg-pnl2">2022</td>
    <td class="tg-pnl2">3</td>
  </tr>
</tbody>
</table>

##### HAVING

Both `WHERE` and `HAVING` are used to filter results. The `WHERE` filter is applied before the `GROUP BY` phase, so you cannot use aggregate functions in a `WHERE` clause. However, you can use the `WHERE` clause to limit the rows to which the aggregate is then applied.

The `HAVING` filter is applied after the `GROUP BY` phase, so you can use the `HAVING` clause to limit the groups that are included in the results.

###### HAVING with GROUP BY

You can use aggregate expressions or their aliases defined in a `SELECT` clause in a `HAVING` condition.

The following query uses an aggregate expression in the `HAVING` clause. It returns the number of sales for each employee who made more than one sale:

```sql
SELECT employee_id, count(sales)
FROM employees
GROUP BY employee_id
HAVING count(sales) > 1;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">employee_id</th>
    <th class="tg-ua3b">count(sales)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">2</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">2</td>
  </tr>
</tbody>
</table>

The aggregations in a `HAVING` clause do not have to be the same as the aggregations in a `SELECT` list. The following query uses the `count` function in the `HAVING` clause but the `sum` function in the `SELECT` clause. It returns the total sales amount for each employee who made more than one sale:

```sql
SELECT employee_id, sum(sales)
FROM employees
GROUP BY employee_id
HAVING count(sales) > 1;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">employee_id</th>
    <th class="tg-ua3b">sum (sales)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">40580</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">18120</td>
  </tr>
</tbody>
</table>

As an extension of the SQL standard, you are not restricted to using only identifiers in the `GROUP BY` clause. The following query uses an alias in the `GROUP BY` clause and is equivalent to the previous query:

```sql
SELECT employee_id as id, sum(sales)
FROM employees
GROUP BY id
HAVING count(sales) > 1;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">id</th>
    <th class="tg-ua3b">sum (sales)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">40580</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">18120</td>
  </tr>
</tbody>
</table>

You can also use an alias for an aggregate expression in the `HAVING` clause. The following query returns the total sales for each department where sales exceed $40,000:

```sql
SELECT department, sum(sales) as total
FROM employees
GROUP BY department
HAVING total > 40000;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">department</th>
    <th class="tg-ua3b">total</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">58700</td>
  </tr>
</tbody>
</table>

If an identifier is ambiguous (for example, present both as a `SELECT` alias and as an index field), the preference is given to the alias. In the following query the identifier is replaced with the expression aliased in the `SELECT` clause:

```sql
SELECT department, sum(sales) as sales
FROM employees
GROUP BY department
HAVING sales > 40000;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">department</th>
    <th class="tg-ua3b">sales</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">58700</td>
  </tr>
</tbody>
</table>

###### HAVING without GROUP BY

You can use a `HAVING` clause without a `GROUP BY` clause. In this case, the whole set of data is to be considered one group. The following query will return `True` if there is more than one value in the `department` column:

```sql
SELECT 'True' as more_than_one_department FROM employees HAVING min(department) < max(department);
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">more_than_one_department</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">True</td>
  </tr>
</tbody>
</table>

If all employees in the employee table belonged to the same department, the result would contain zero rows:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">more_than_one_department</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2"></td>
  </tr>
</tbody>
</table>

#### Delete

The `DELETE` statement deletes documents that satisfy the predicates in the `WHERE` clause.
If you don't specify the `WHERE` clause, all documents are deleted.

##### Setting

The `DELETE` statement is disabled by default. To enable the `DELETE` functionality in SQL, you need to update the configuration by sending the following request:

```json
PUT _plugins/_query/settings
{
  "transient": {
    "plugins.sql.delete.enabled": "true"
  }
}
```

##### Syntax

Rule `singleDeleteStatement`:

![singleDeleteStatement](/media/media/singleDeleteStatement.png)

##### Example

SQL query:

```sql
DELETE FROM accounts
WHERE age > 30
```

Explain:

```json
{
  "size" : 1000,
  "query" : {
    "bool" : {
      "must" : [
        {
          "range" : {
            "age" : {
              "from" : 30,
              "to" : null,
              "include_lower" : false,
              "include_upper" : true,
              "boost" : 1.0
            }
          }
        }
      ],
      "adjust_pure_negative" : true,
      "boost" : 1.0
    }
  },
  "_source" : false
}
```

Result set:

```json
{
  "schema" : [
    {
      "name" : "deleted_rows",
      "type" : "long"
    }
  ],
  "total" : 1,
  "datarows" : [
    [
      3
    ]
  ],
  "size" : 1,
  "status" : 200
}
```

The `datarows` field shows the number of documents deleted.

### PPL - Piped Processing Language

Piped Processing Language (PPL) is a query language that lets you use pipe (`|`) syntax to explore, discover, and query data stored in Energy Logserver.

To quickly get up and running with PPL, use **SQL** in Energy Logserver Dashboards.

The PPL syntax consists of commands delimited by the pipe character (`|`) where data flows from left to right through each pipeline.

```sql
search command | command 1 | command 2 ...
```

You can only use read-only commands like `search`, `where`, `fields`, `rename`, `dedup`, `stats`, `sort`, `eval`, `head`, `top`, and `rare`.

#### Quick start

To get started with PPL, choose **Dev Tools** in Energy Logserver Dashboards and use the `bulk` operation to index some sample data:

```json
PUT accounts/_bulk?refresh
{"index":{"_id":"1"}}
{"account_number":1,"balance":39225,"firstname":"Amber","lastname":"Duke","age":32,"gender":"M","address":"880 Holmes Lane","employer":"Pyrami","email":"amberduke@pyrami.com","city":"Brogan","state":"IL"}
{"index":{"_id":"6"}}
{"account_number":6,"balance":5686,"firstname":"Hattie","lastname":"Bond","age":36,"gender":"M","address":"671 Bristol Street","employer":"Netagy","email":"hattiebond@netagy.com","city":"Dante","state":"TN"}
{"index":{"_id":"13"}}
{"account_number":13,"balance":32838,"firstname":"Nanette","lastname":"Bates","age":28,"gender":"F","address":"789 Madison Street","employer":"Quility","city":"Nogal","state":"VA"}
{"index":{"_id":"18"}}
{"account_number":18,"balance":4180,"firstname":"Dale","lastname":"Adams","age":33,"gender":"M","address":"467 Hutchinson Court","email":"daleadams@boink.com","city":"Orick","state":"MD"}
```

Go to **SQL** and select **PPL**.

The following example returns `firstname` and `lastname` fields for documents in an `accounts` index with `age` greater than 18:

```sql
search source=accounts
| where age > 18
| fields firstname, lastname
```

#### Example response

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">firstname</th>
    <th class="tg-ua3b">lastname</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">Amber</td>
    <td class="tg-pnl2">Duke</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Hattie</td>
    <td class="tg-pnl2">Bond</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Nanette</td>
    <td class="tg-pnl2">Bates</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Dale</td>
    <td class="tg-pnl2">Adams</td>
  </tr>
</tbody>
</table>

![PPL query workbench](/media/media/ppl.png)

#### PPL syntax

Every PPL query starts with the `search` command. It specifies the index to search and retrieve documents from. Subsequent commands can follow in any order.

Currently, `PPL` supports only one `search` command, which can be omitted to simplify the query.
{ : .note}

##### Syntax

```sql
search source=<index> [boolean-expression]
source=<index> [boolean-expression]
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Field</th>
    <th class="tg-ua3b">Description</th>
    <th class="tg-ua3b">Required</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">search</td>
    <td class="tg-pnl2">Specifies search keywords.</td>
    <td class="tg-pnl2">Yes</td>
  </tr>
  <tr>
    <td class="tg-pnl2">index</td>
    <td class="tg-pnl2">Specifies which index to query from.</td>
    <td class="tg-pnl2">No</td>
  </tr>
  <tr>
    <td class="tg-pnl2">bool-expression</td>
    <td class="tg-pnl2">Specifies an expression that evaluates to a Boolean value.</td>
    <td class="tg-pnl2">No</td>
  </tr>
</tbody>
</table>

##### Examples

**Example 1: Search through accounts index**

In the following example, the `search` command refers to an `accounts` index as the source and uses `fields` and `where` commands for the conditions:

```sql
search source=accounts
| where age > 18
| fields firstname, lastname
```

In the following examples, angle brackets `< >` enclose required arguments and square brackets `[ ]` enclose optional arguments.

**Example 2: Get all documents**

To get all documents from the `accounts` index, specify it as the `source`:

```sql
search source=accounts;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">firstname</th>
    <th class="tg-ua3b">address</th>
    <th class="tg-ua3b">balance</th>
    <th class="tg-ua3b">gender</th>
    <th class="tg-ua3b">city</th>
    <th class="tg-ua3b">employer</th>
    <th class="tg-ua3b">state</th>
    <th class="tg-ua3b">age</th>
    <th class="tg-ua3b">email</th>
    <th class="tg-ua3b">lastname</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">Amber </td>
    <td class="tg-pnl2">880 Holmes Lane</td>
    <td class="tg-pnl2">39225</td>
    <td class="tg-pnl2">M</td>
    <td class="tg-pnl2">Brogan</td>
    <td class="tg-pnl2">Pyrami</td>
    <td class="tg-pnl2">IL</td>
    <td class="tg-pnl2">32</td>
    <td class="tg-pnl2">amberduke@pyrami.com </td>
    <td class="tg-pnl2">Duke</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">Hattie</td>
    <td class="tg-pnl2">671 Bristol Street</td>
    <td class="tg-pnl2">5686</td>
    <td class="tg-pnl2">M</td>
    <td class="tg-pnl2">Dante</td>
    <td class="tg-pnl2">Netagy</td>
    <td class="tg-pnl2">TN</td>
    <td class="tg-pnl2">36 </td>
    <td class="tg-pnl2">hattiebond@netagy.com</td>
    <td class="tg-pnl2">Bond</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">Nanette</td>
    <td class="tg-pnl2">789 Madison Street</td>
    <td class="tg-pnl2">32838</td>
    <td class="tg-pnl2">F</td>
    <td class="tg-pnl2">Nogal</td>
    <td class="tg-pnl2">Quility</td>
    <td class="tg-pnl2">VA</td>
    <td class="tg-pnl2">28</td>
    <td class="tg-pnl2">null</td>
    <td class="tg-pnl2">Bates</td>
  </tr>
  <tr>
    <td class="tg-pnl2">18</td>
    <td class="tg-pnl2">Dale </td>
    <td class="tg-pnl2">467 Hutchinson Court</td>
    <td class="tg-pnl2">4180</td>
    <td class="tg-pnl2">M</td>
    <td class="tg-pnl2">Orick</td>
    <td class="tg-pnl2">null</td>
    <td class="tg-pnl2">MD</td>
    <td class="tg-pnl2">33</td>
    <td class="tg-pnl2">daleadams@boink.com</td>
    <td class="tg-pnl2">Adams</td>
  </tr>
</tbody>
</table>

**Example 3: Get documents that match a condition**

To get all documents from the `accounts` index that either have `account_number` equal to 1 or have `gender` as `F`, use the following query:

```sql
search source=accounts account_number=1 or gender=\"F\";
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">firstname</th>
    <th class="tg-ua3b">address</th>
    <th class="tg-ua3b">balance</th>
    <th class="tg-ua3b">gender</th>
    <th class="tg-ua3b">city</th>
    <th class="tg-ua3b">employer</th>
    <th class="tg-ua3b">state</th>
    <th class="tg-ua3b">age</th>
    <th class="tg-ua3b">email</th>
    <th class="tg-ua3b">lastname</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">Amber</td>
    <td class="tg-pnl2">880 Holmes Lane</td>
    <td class="tg-pnl2">39225</td>
    <td class="tg-pnl2">M</td>
    <td class="tg-pnl2">Brogan</td>
    <td class="tg-pnl2">Pyrami</td>
    <td class="tg-pnl2">IL</td>
    <td class="tg-pnl2">32</td>
    <td class="tg-pnl2">amberduke@pyrami.com</td>
    <td class="tg-pnl2">Duke</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">Nanette</td>
    <td class="tg-pnl2">789 Madison Street</td>
    <td class="tg-pnl2">32838</td>
    <td class="tg-pnl2">F</td>
    <td class="tg-pnl2">Nogal</td>
    <td class="tg-pnl2">Quility</td>
    <td class="tg-pnl2">VA</td>
    <td class="tg-pnl2">28</td>
    <td class="tg-pnl2">null</td>
    <td class="tg-pnl2">Bates</td>
  </tr>
</tbody>
</table>

#### Commands

`PPL` supports all [`SQL` common](#functions) functions, including [relevance search](#full-text-search), but also introduces few more functions (called `commands`) which are available in `PPL` only.

##### dedup

The `dedup` (data deduplication) command removes duplicate documents defined by a field from the search result.

###### Syntax

```sql
dedup [int] <field-list> [keepempty=<bool>] [consecutive=<bool>]
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Field</th>
    <th class="tg-ua3b">Description</th>
    <th class="tg-ua3b">Type</th>
    <th class="tg-ua3b">Required</th>
    <th class="tg-ua3b">Default</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">int</td>
    <td class="tg-pnl2"> Retain the specified number of duplicate events for each combination. The number must be greater than 0. If you do not specify a number, only the first occurring event is kept and all other duplicates are removed from the results.</td>
    <td class="tg-pnl2">string</td>
    <td class="tg-pnl2">No</td>
    <td class="tg-pnl2">1</td>
  </tr>
  <tr>
    <td class="tg-pnl2">keepempty</td>
    <td class="tg-pnl2">If true, keep the document if any field in the field list has a null value or a field missing.</td>
    <td class="tg-pnl2">nested list of objects</td>
    <td class="tg-pnl2">No</td>
    <td class="tg-pnl2">False</td>
  </tr>
  <tr>
    <td class="tg-pnl2">consecutive</td>
    <td class="tg-pnl2">If true, remove only consecutive events with duplicate combinations of values.</td>
    <td class="tg-pnl2">Boolean</td>
    <td class="tg-pnl2">No</td>
    <td class="tg-pnl2">False</td>
  </tr>
  <tr>
    <td class="tg-pnl2">field-list</td>
    <td class="tg-pnl2">Specify a comma-delimited field list. At least one field is required.</td>
    <td class="tg-pnl2">String or comma-separated list of strings</td>
    <td class="tg-pnl2">Yes</td>
    <td class="tg-pnl2">-</td>
  </tr>
</tbody>
</table>

**Example 1: Dedup by one field**

To remove duplicate documents with the same gender:

```sql
search source=accounts | dedup gender | fields account_number, gender;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">gender</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">M</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">F</td>
  </tr>
</tbody>
</table>

**Example 2: Keep two duplicate documents**

To keep two duplicate documents with the same gender:

```sql
search source=accounts | dedup 2 gender | fields account_number, gender;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">gender</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">M</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">M</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">F</td>
  </tr>
</tbody>
</table>

**Example 3: Keep or ignore an empty field by default**

To keep two duplicate documents with a `null` field value:

```sql
search source=accounts | dedup email keepempty=true | fields account_number, email;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">email</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">amberduke@pyrami.com</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">hattiebond@netagy.com</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">null</td>
  </tr>
  <tr>
    <td class="tg-pnl2">18</td>
    <td class="tg-pnl2">daleadams@boink.com</td>
  </tr>
</tbody>
</table>

To remove duplicate documents with the `null` field value:

```sql
search source=accounts | dedup email | fields account_number, email;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">email</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">amberduke@pyrami.com</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">hattiebond@netagy.com</td>
  </tr>
  <tr>
    <td class="tg-pnl2">18</td>
    <td class="tg-pnl2">daleadams@boink.com</td>
  </tr>
</tbody>
</table>

**Example 4: Dedup of consecutive documents**

To remove duplicates of consecutive documents:

```sql
search source=accounts | dedup gender consecutive=true | fields account_number, gender;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">gender</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">M</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">F</td>
  </tr>
  <tr>
    <td class="tg-pnl2">18</td>
    <td class="tg-pnl2">M</td>
  </tr>
</tbody>
</table>

###### Limitations

The `dedup` command is not rewritten to Energy Logserver DSL, it is only executed on the coordination node.

##### eval

The `eval` command evaluates an expression and appends its result to the search result.

###### Syntax

```sql
eval <field>=<expression> ["," <field>=<expression> ]...
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Field</th>
    <th class="tg-ua3b">Description</th>
    <th class="tg-ua3b">Required</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">field</td>
    <td class="tg-pnl2">If a field name does not exist, a new field is added. If the field name already exists, it's overwritten.</td>
    <td class="tg-pnl2">Yes</td>
  </tr>
  <tr>
    <td class="tg-pnl2">expression</td>
    <td class="tg-pnl2">Specify any supported expression.</td>
    <td class="tg-pnl2">Yes</td>
  </tr>
</tbody>
</table>

**Example 1: Create a new field**

To create a new `doubleAge` field for each document. `doubleAge` is the result of `age` multiplied by 2:

```sql
search source=accounts | eval doubleAge = age * 2 | fields age, doubleAge;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">age | doubleAge</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">32</td>
    <td class="tg-pnl2">64</td>
  </tr>
  <tr>
    <td class="tg-pnl2">36</td>
    <td class="tg-pnl2">72</td>
  </tr>
  <tr>
    <td class="tg-pnl2">28</td>
    <td class="tg-pnl2">56</td>
  </tr>
  <tr>
    <td class="tg-pnl2">33</td>
    <td class="tg-pnl2">66</td>
  </tr>
</tbody>
</table>

*Example 2*: Overwrite the existing field

To overwrite the `age` field with `age` plus 1:

```sql
search source=accounts | eval age = age + 1 | fields age;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">age</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">33</td>
  </tr>
  <tr>
    <td class="tg-pnl2">37</td>
  </tr>
  <tr>
    <td class="tg-pnl2">29</td>
  </tr>
  <tr>
    <td class="tg-pnl2">34</td>
  </tr>
</tbody>
</table>

**Example 3: Create a new field with a field defined with the `eval` command**

To create a new field `ddAge`. `ddAge` is the result of `doubleAge` multiplied by 2, where `doubleAge` is defined in the `eval` command:

```sql
search source=accounts | eval doubleAge = age * 2, ddAge = doubleAge * 2 | fields age, doubleAge, ddAge;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">age</th>
    <th class="tg-ua3b">doubleAge</th>
    <th class="tg-ua3b">ddAge</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">32</td>
    <td class="tg-pnl2">64</td>
    <td class="tg-pnl2">128</td>
  </tr>
  <tr>
    <td class="tg-pnl2">36</td>
    <td class="tg-pnl2">72</td>
    <td class="tg-pnl2">144</td>
  </tr>
  <tr>
    <td class="tg-pnl2">28</td>
    <td class="tg-pnl2">56</td>
    <td class="tg-pnl2">112</td>
  </tr>
  <tr>
    <td class="tg-pnl2">33</td>
    <td class="tg-pnl2">66</td>
    <td class="tg-pnl2">132</td>
  </tr>
</tbody>
</table>

##### Limitation

The ``eval`` command is not rewritten to Energy Logserver DSL, it is only executed on the coordination node.

#### fields

Use the `fields` command to keep or remove fields from a search result.

##### Syntax

```sql
fields [+|-] <field-list>
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Field</th>
    <th class="tg-ua3b">Description</th>
    <th class="tg-ua3b">Required</th>
    <th class="tg-ua3b">Default</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">index</td>
    <td class="tg-pnl2">Plus (+) keeps only fields specified in the field list. Minus (-) removes all fields specified in the field list.</td>
    <td class="tg-pnl2">No</td>
    <td class="tg-pnl2">+</td>
  </tr>
  <tr>
    <td class="tg-pnl2">field list</td>
    <td class="tg-pnl2">Specify a comma-delimited list of fields.</td>
    <td class="tg-pnl2">Yes</td>
    <td class="tg-pnl2">No default</td>
  </tr>
</tbody>
</table>

**Example 1: Select specified fields from result**

To get `account_number`, `firstname`, and `lastname` fields from a search result:

```sql
search source=accounts | fields account_number, firstname, lastname;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">firstname </th>
    <th class="tg-ua3b">lastname</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">Amber</td>
    <td class="tg-pnl2">Duke</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">Hattie</td>
    <td class="tg-pnl2">Bond</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">Nanette</td>
    <td class="tg-pnl2">Bates</td>
  </tr>
  <tr>
    <td class="tg-pnl2">18</td>
    <td class="tg-pnl2">Dale</td>
    <td class="tg-pnl2">Adams</td>
  </tr>
</tbody>
</table>

**Example 2: Remove specified fields from a search result**

To remove the `account_number` field from the search results:

```sql
search source=accounts | fields account_number, firstname, lastname | fields - account_number;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">firstname</th>
    <th class="tg-ua3b">lastname</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">Amber</td>
    <td class="tg-pnl2">Duke</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Hattie</td>
    <td class="tg-pnl2">Bond</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Nanette</td>
    <td class="tg-pnl2">Bates</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Dale</td>
    <td class="tg-pnl2">Adams</td>
  </tr>
</tbody>
</table>

#### parse

Use the `parse` command to parse a text field using regular expression and append the result to the search result.

##### Syntax

```sql
parse <field> <regular-expression>
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Field</th>
    <th class="tg-ua3b">Description</th>
    <th class="tg-ua3b">Required</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">field</td>
    <td class="tg-pnl2">A text field.</td>
    <td class="tg-pnl2">Yes</td>
  </tr>
  <tr>
    <td class="tg-pnl2">regular-expression</td>
    <td class="tg-pnl2">The regular expression used to extract new fields from the given test field. If a new field name exists, it will replace the original field.</td>
    <td class="tg-pnl2">Yes</td>
  </tr>
</tbody>
</table>

The regular expression is used to match the whole text field of each document with Java regex engine. Each named capture group in the expression will become a new ``STRING`` field.

**Example 1: Create new field**

The example shows how to create new field `host` for each document. `host` will be the hostname after `@` in `email` field. Parsing a null field will return an empty string.

```sql
os> source=accounts | parse email '.+@(?<host>.+)' | fields email, host ;
fetched rows / total rows = 4/4
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">email</th>
    <th class="tg-ua3b">host</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">amberduke@pyrami.com</td>
    <td class="tg-pnl2">pyrami.com</td>
  </tr>
  <tr>
    <td class="tg-pnl2">hattiebond@netagy.com</td>
    <td class="tg-pnl2">netagy.com</td>
  </tr>
  <tr>
    <td class="tg-pnl2">null</td>
    <td class="tg-pnl2">null</td>
  </tr>
  <tr>
    <td class="tg-pnl2">daleadams@boink.com  </td>
    <td class="tg-pnl2">boink.com</td>
  </tr>
</tbody>
</table>

**Example 2: Override the existing field**

The example shows how to override the existing address field with street number removed.

```sql
os> source=accounts | parse address '\d+ (?<address>.+)' | fields address ;
fetched rows / total rows = 4/4
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">address</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">Holmes Lane</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Bristol Street</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Madison Street</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Hutchinson Court</td>
  </tr>
</tbody>
</table>

**Example 3: Filter and sort be casted parsed field**

The example shows how to sort street numbers that are higher than 500 in address field.

```sql
os> source=accounts | parse address '(?<streetNumber>\d+) (?<street>.+)' | where cast(streetNumber as int) > 500 | sort num(streetNumber) | fields streetNumber, street ;
fetched rows / total rows = 3/3
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">streetNumber</th>
    <th class="tg-ua3b">street</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">671</td>
    <td class="tg-pnl2">Bristol Street</td>
  </tr>
  <tr>
    <td class="tg-pnl2">789</td>
    <td class="tg-pnl2">Madison Street</td>
  </tr>
  <tr>
    <td class="tg-pnl2">880</td>
    <td class="tg-pnl2">Holmes Lane</td>
  </tr>
</tbody>
</table>

##### Limitations

A few limitations exist when using the parse command:

- Fields defined by parse cannot be parsed again. For example, `source=accounts | parse address '\d+ (?<street>.+)' | parse street '\w+ (?<road>\w+)' ;` will fail to return any expressions.
- Fields defined by parse cannot be overridden with other commands. For example, when entering `source=accounts | parse address '\d+ (?<street>.+)' | eval street='1' | where street='1' ;` `where` will not match any documents since `street` cannot be overridden.
- The text field used by parse cannot be overridden. For example, when entering `source=accounts | parse address '\d+ (?<street>.+)' | eval address='1' ;` `street` will not be parse since address is overridden.
- Fields defined by parse cannot be filtered/sorted after using them in the `stats` command. For example, `source=accounts | parse email '.+@(?<host>.+)' | stats avg(age) by host | where host=pyrami.com ;` `where` will not parse the domain listed.

#### rename

Use the `rename` command to rename one or more fields in the search result.

##### Syntax

```sql
rename <source-field> AS <target-field>["," <source-field> AS <target-field>]...
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Field</th>
    <th class="tg-ua3b">Description</th>
    <th class="tg-ua3b">Required</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">source-field</td>
    <td class="tg-pnl2">The name of the field that you want to rename.</td>
    <td class="tg-pnl2">Yes</td>
  </tr>
  <tr>
    <td class="tg-pnl2">target-field</td>
    <td class="tg-pnl2">The name you want to rename to.</td>
    <td class="tg-pnl2">Yes</td>
  </tr>
</tbody>
</table>

**Example 1: Rename one field**

Rename the `account_number` field as `an`:

```sql
search source=accounts | rename account_number as an | fields an;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">an</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
  </tr>
  <tr>
    <td class="tg-pnl2">18</td>
  </tr>
</tbody>
</table>

**Example 2: Rename multiple fields**

Rename the `account_number` field as `an` and `employer` as `emp`:

```sql
search source=accounts | rename account_number as an, employer as emp | fields an, emp;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">an  </th>
    <th class="tg-ua3b">emp</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">Pyrami</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">Netagy</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">Quility</td>
  </tr>
  <tr>
    <td class="tg-pnl2">18</td>
    <td class="tg-pnl2">null</td>
  </tr>
</tbody>
</table>

##### Limitations

The `rename` command is not rewritten to Energy Logserver DSL, it is only executed on the coordination node.

#### sort

Use the `sort` command to sort search results by a specified field.

##### Syntax

```sql
sort [count] <[+|-] sort-field>...
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Field</th>
    <th class="tg-ua3b">Description</th>
    <th class="tg-ua3b">Required</th>
    <th class="tg-ua3b">Default</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">count</td>
    <td class="tg-pnl2">The maximum number results to return from the sorted result. If count=0, all results are returned.</td>
    <td class="tg-pnl2">No</td>
    <td class="tg-pnl2">1000</td>
  </tr>
  <tr>
    <td class="tg-pnl2">[+|-]</td>
    <td class="tg-pnl2">Use plus [+] to sort by ascending order and minus [-] to sort by descending order.</td>
    <td class="tg-pnl2">No</td>
    <td class="tg-pnl2">Ascending order</td>
  </tr>
  <tr>
    <td class="tg-pnl2">sort-field</td>
    <td class="tg-pnl2">Specify the field that you want to sort by.</td>
    <td class="tg-pnl2">Yes</td>
    <td class="tg-pnl2">-</td>
  </tr>
</tbody>
</table>

**Example 1: Sort by one field**

To sort all documents by the `age` field in ascending order:

```sql
search source=accounts | sort age | fields account_number, age;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">age</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">28</td>
  </tr>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">32</td>
  </tr>
  <tr>
    <td class="tg-pnl2">18</td>
    <td class="tg-pnl2">33</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">36</td>
  </tr>
</tbody>
</table>

**Example 2: Sort by one field and return all results**

To sort all documents by the `age` field in ascending order and specify count as 0 to get back all results:

```sql
search source=accounts | sort 0 age | fields account_number, age;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">age</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">28</td>
  </tr>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">32</td>
  </tr>
  <tr>
    <td class="tg-pnl2">18</td>
    <td class="tg-pnl2">33</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">36</td>
  </tr>
</tbody>
</table>

**Example 3: Sort by one field in descending order**

To sort all documents by the `age` field in descending order:

```sql
search source=accounts | sort - age | fields account_number, age;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">age</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">36</td>
  </tr>
  <tr>
    <td class="tg-pnl2">18</td>
    <td class="tg-pnl2">33</td>
  </tr>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">32</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">28</td>
  </tr>
</tbody>
</table>

**Example 4: Specify the number of sorted documents to return**

To sort all documents by the `age` field in ascending order and specify count as 2 to get back two results:

```sql
search source=accounts | sort 2 age | fields account_number, age;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">age</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">28</td>
  </tr>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">32</td>
  </tr>
</tbody>
</table>

**Example 5: Sort by multiple fields**

To sort all documents by the `gender` field in ascending order and `age` field in descending order:

```sql
search source=accounts | sort + gender, - age | fields account_number, gender, age;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">gender</th>
    <th class="tg-ua3b">age</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">F</td>
    <td class="tg-pnl2">28</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">M</td>
    <td class="tg-pnl2">36</td>
  </tr>
  <tr>
    <td class="tg-pnl2">18</td>
    <td class="tg-pnl2">M</td>
    <td class="tg-pnl2">33</td>
  </tr>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">M</td>
    <td class="tg-pnl2">32</td>
  </tr>
</tbody>
</table>

#### stats

Use the `stats` command to aggregate from search results.

The following table lists the aggregation functions and also indicates how each one handles null or missing values:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Function</th>
    <th class="tg-ua3b">NULL</th>
    <th class="tg-ua3b">MISSING</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">COUNT</td>
    <td class="tg-pnl2">Not counted</td>
    <td class="tg-pnl2">Not counted</td>
  </tr>
  <tr>
    <td class="tg-pnl2">SUM</td>
    <td class="tg-pnl2">Ignore</td>
    <td class="tg-pnl2">Ignore</td>
  </tr>
  <tr>
    <td class="tg-pnl2">AVG</td>
    <td class="tg-pnl2">Ignore</td>
    <td class="tg-pnl2">Ignore</td>
  </tr>
  <tr>
    <td class="tg-pnl2">MAX</td>
    <td class="tg-pnl2">Ignore</td>
    <td class="tg-pnl2">Ignore</td>
  </tr>
  <tr>
    <td class="tg-pnl2">MIN</td>
    <td class="tg-pnl2">Ignore</td>
    <td class="tg-pnl2">Ignore</td>
  </tr>
</tbody>
</table>

##### Syntax

```bash
stats <aggregation>... [by-clause]...
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Field</th>
    <th class="tg-ua3b">Description</th>
    <th class="tg-ua3b">Required</th>
    <th class="tg-ua3b">Default</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">aggregation</td>
    <td class="tg-pnl2">Specify a statistical aggregation function. The argument of this function must be a field.</td>
    <td class="tg-pnl2">Yes</td>
    <td class="tg-pnl2">1000</td>
  </tr>
  <tr>
    <td class="tg-pnl2">by-clause</td>
    <td class="tg-pnl2">Specify one or more fields to group the results by. If not specified, the <i>stats</i> command returns only one row, which is the aggregation over the entire result set.</td>
    <td class="tg-pnl2">No</td>
    <td class="tg-pnl2">-</td>
  </tr>
</tbody>
</table>

**Example 1: Calculate the average value of a field**

To calculate the average `age` of all documents:

```sql
search source=accounts | stats avg(age);
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">avg(age)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">32.25</td>
  </tr>
</tbody>
</table>

**Example 2: Calculate the average value of a field by group**

To calculate the average age grouped by gender:

```sql
search source=accounts | stats avg(age) by gender;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">gender</th>
    <th class="tg-ua3b">avg(age)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">F</td>
    <td class="tg-pnl2">28.0</td>
  </tr>
  <tr>
    <td class="tg-pnl2">M</td>
    <td class="tg-pnl2">33.666666666666664</td>
  </tr>
</tbody>
</table>

**Example 3: Calculate the average and sum of a field by group**

To calculate the average and sum of age grouped by gender:

```sql
search source=accounts | stats avg(age), sum(age) by gender;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">gender</th>
    <th class="tg-ua3b">avg(age)</th>
    <th class="tg-ua3b">sum(age)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">F</td>
    <td class="tg-pnl2">28</td>
    <td class="tg-pnl2">28</td>
  </tr>
  <tr>
    <td class="tg-pnl2">M</td>
    <td class="tg-pnl2">33.666666666666664</td>
    <td class="tg-pnl2">101</td>
  </tr>
</tbody>
</table>

**Example 4: Calculate the maximum value of a field**

To calculate the maximum age:

```sql
search source=accounts | stats max(age);
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">max(age)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">36</td>
  </tr>
</tbody>
</table>

**Example 5: Calculate the maximum and minimum value of a field by group**

To calculate the maximum and minimum age values grouped by gender:

```sql
search source=accounts | stats max(age), min(age) by gender;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">gender</th>
    <th class="tg-ua3b">min(age)</th>
    <th class="tg-ua3b">max(age)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">F</td>
    <td class="tg-pnl2">28</td>
    <td class="tg-pnl2">28</td>
  </tr>
  <tr>
    <td class="tg-pnl2">M</td>
    <td class="tg-pnl2">32</td>
    <td class="tg-pnl2">36</td>
  </tr>
</tbody>
</table>

#### where

Use the `where` command with a bool expression to filter the search result. The `where` command only returns the result when the bool expression evaluates to true.

##### Syntax

```sql
where <boolean-expression>
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Field</th>
    <th class="tg-ua3b">Description</th>
    <th class="tg-ua3b">Required</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">bool-expression</td>
    <td class="tg-pnl2">An expression that evaluates to a boolean value.</td>
    <td class="tg-pnl2">No</td>
  </tr>
</tbody>
</table>

**Example: Filter result set with a condition**

To get all documents from the `accounts` index where `account_number` is 1 or gender is `F`:

```sql
search source=accounts | where account_number=1 or gender=\"F\" | fields account_number, gender;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">gender</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">M</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">F</td>
  </tr>
</tbody>
</table>

#### head

Use the `head` command to return the first N number of results in a specified search order.

##### Syntax

```sql
head [N]
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Field</th>
    <th class="tg-ua3b">Description</th>
    <th class="tg-ua3b">Required</th>
    <th class="tg-ua3b">Default</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">N</td>
    <td class="tg-pnl2">Specify the number of results to return.</td>
    <td class="tg-pnl2">No</td>
    <td class="tg-pnl2">10</td>
  </tr>
</tbody>
</table>

**Example 1: Get the first 10 results**

To get the first 10 results:

```sql
search source=accounts | fields firstname, age | head;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">firstname</th>
    <th class="tg-ua3b">age</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">Amber</td>
    <td class="tg-pnl2">32</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Hattie</td>
    <td class="tg-pnl2">36</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Nanette</td>
    <td class="tg-pnl2">28</td>
  </tr>
</tbody>
</table>

**Example 2: Get the first N results**

To get the first two results:

```sql
search source=accounts | fields firstname, age | head 2;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">firstname</th>
    <th class="tg-ua3b">age</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">Amber</td>
    <td class="tg-pnl2">32</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Hattie</td>
    <td class="tg-pnl2">36</td>
  </tr>
</tbody>
</table>

##### Limitations

The `head` command is not rewritten to Energy Logserver DSL, it is only executed on the coordination node.

#### rare

Use the `rare` command to find the least common values of all fields in a field list.
A maximum of 10 results are returned for each distinct set of values of the group-by fields.

##### Syntax

```sql
rare <field-list> [by-clause]
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Field</th>
    <th class="tg-ua3b">Description</th>
    <th class="tg-ua3b">Required</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">field-list</td>
    <td class="tg-pnl2">Specify a comma-delimited list of field names.</td>
    <td class="tg-pnl2">No
`by-clause`</td>
    <td class="tg-pnl2">Specify one or more fields to group the results by.</td>
    <td class="tg-pnl2">No</td>
  </tr>
</tbody>
</table>

**Example 1: Find the least common values in a field**

To find the least common values of gender:

```sql
search source=accounts | rare gender;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">gender</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">F</td>
  </tr>
  <tr>
    <td class="tg-pnl2">M</td>
  </tr>
</tbody>
</table>

**Example 2: Find the least common values grouped by gender**

To find the least common age grouped by gender:

```sql
search source=accounts | rare age by gender;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">gender</th>
    <th class="tg-ua3b">age</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">F</td>
    <td class="tg-pnl2">28</td>
  </tr>
  <tr>
    <td class="tg-pnl2">M</td>
    <td class="tg-pnl2">32</td>
  </tr>
  <tr>
    <td class="tg-pnl2">M</td>
    <td class="tg-pnl2">33</td>
  </tr>
</tbody>
</table>

##### Limitations

The `rare` command is not rewritten to Energy Logserver DSL, it is only executed on the coordination node.

#### top

Use the `top` command to find the most common values of all fields in the field list.

##### Syntax

```sql
top [N] <field-list> [by-clause]
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Field</th>
    <th class="tg-ua3b">Description</th>
    <th class="tg-ua3b">Default</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">N</td>
    <td class="tg-pnl2">Specify the number of results to return.</td>
    <td class="tg-pnl2">10</td>
  </tr>
  <tr>
    <td class="tg-pnl2">field-list</td>
    <td class="tg-pnl2">Specify a comma-delimited list of field names.</td>
    <td class="tg-pnl2">-</td>
  </tr>
  <tr>
    <td class="tg-pnl2">by-clause</td>
    <td class="tg-pnl2">Specify one or more fields to group the results by.</td>
    <td class="tg-pnl2">-</td>
  </tr>
</tbody>
</table>

**Example 1: Find the most common values in a field**

To find the most common genders:

```sql
search source=accounts | top gender;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">gender</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">M</td>
  </tr>
  <tr>
    <td class="tg-pnl2">F</td>
  </tr>
</tbody>
</table>

**Example 2: Find the most common value in a field**

To find the most common gender:

```sql
search source=accounts | top 1 gender;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">gender</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">M</td>
  </tr>
</tbody>
</table>

**Example 3: Find the most common values grouped by gender**

To find the most common age grouped by gender:

```sql
search source=accounts | top 1 age by gender;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">gender</th>
    <th class="tg-ua3b">age</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">F</td>
    <td class="tg-pnl2">28</td>
  </tr>
  <tr>
    <td class="tg-pnl2">M</td>
    <td class="tg-pnl2">32</td>
  </tr>
</tbody>
</table>

##### Limitations

The `top` command is not rewritten to Energy Logserver DSL, it is only executed on the coordination node.

### Identifiers

An identifier is an ID to name your database objects, such as index names, field names, aliases, and so on.
Energy Logserver supports two types of identifiers: regular identifiers and delimited identifiers.

#### Regular identifiers

A regular identifier is a string of characters that starts with an ASCII letter (lower or upper case).
The next character can either be a letter, digit, or underscore (_). It can't be a reserved keyword.
Whitespace and other special characters are also not allowed.

Energy Logserver supports the following regular identifiers:

1. Identifiers prefixed by a dot `.` sign. Use to hide an index. For example `.opensearch-dashboards`.
1. Identifiers prefixed by an `@` sign. Use for meta fields generated by Logstash ingestion.
1. Identifiers with hyphen `-` in the middle. Use for index names with date information.
1. Identifiers with star `*` present. Use for wildcard match of index patterns.

For regular identifiers, you can use the name without any back tick or escape characters.
In this example, `source`, `fields`, `account_number`, `firstname`, and `lastname` are all identifiers. Out of these, the `source` field is a reserved identifier.

```sql
SELECT account_number, firstname, lastname FROM accounts;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">firstname</th>
    <th class="tg-ua3b">lastname</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">Amber</td>
    <td class="tg-pnl2">Duke</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">Hattie</td>
    <td class="tg-pnl2">Bond</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">Nanette</td>
    <td class="tg-pnl2">Bates</td>
  </tr>
  <tr>
    <td class="tg-pnl2">18</td>
    <td class="tg-pnl2">Dale</td>
    <td class="tg-pnl2">Adams</td>
  </tr>
</tbody>
</table>

#### Delimited identifiers

A delimited identifier can contain special characters not allowed by a regular identifier.
You must enclose delimited identifiers with back ticks (\`\`). Back ticks differentiate the identifier from special characters.

If the index name includes a dot (`.`), for example, `log-2021.01.11`, use delimited identifiers with back ticks to escape it \``log-2021.01.11`\`.

Typical examples of using delimited identifiers:

1. Identifiers with reserved keywords.
1. Identifiers with a `.` present. Similarly, `-` to include date information.
1. Identifiers with other special characters. For example, Unicode characters.

To quote an index name with back ticks:

```sql
source=`accounts` | fields `account_number`;
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
  </tr>
  <tr>
    <td class="tg-pnl2">18</td>
  </tr>
</tbody>
</table>

#### Case sensitivity

Identifiers are case sensitive. They must be exactly the same as what's stored in Energy Logserver.

For example, if you run `source=Accounts`, you'll get an index not found exception because the actual index name is in lower case.

### Data types

The following table shows the data types supported by the SQL plugin and how each one maps to SQL and Energy Logserver data types:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Energy Logserver SQL Type</th>
    <th class="tg-ua3b">Energy Logserver Type</th>
    <th class="tg-ua3b">SQL Type</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">boolean</td>
    <td class="tg-pnl2">boolean</td>
    <td class="tg-pnl2">BOOLEAN</td>
  </tr>
  <tr>
    <td class="tg-pnl2">byte</td>
    <td class="tg-pnl2">byte</td>
    <td class="tg-pnl2">TINYINT</td>
  </tr>
  <tr>
    <td class="tg-pnl2">short</td>
    <td class="tg-pnl2">byte</td>
    <td class="tg-pnl2">SMALLINT</td>
  </tr>
  <tr>
    <td class="tg-pnl2">integer</td>
    <td class="tg-pnl2">integer</td>
    <td class="tg-pnl2">INTEGER</td>
  </tr>
  <tr>
    <td class="tg-pnl2">long</td>
    <td class="tg-pnl2">long</td>
    <td class="tg-pnl2">BIGINT</td>
  </tr>
  <tr>
    <td class="tg-pnl2">float</td>
    <td class="tg-pnl2">float</td>
    <td class="tg-pnl2">REAL</td>
  </tr>
  <tr>
    <td class="tg-pnl2">half_float</td>
    <td class="tg-pnl2">float</td>
    <td class="tg-pnl2">FLOAT</td>
  </tr>
  <tr>
    <td class="tg-pnl2">scaled_float</td>
    <td class="tg-pnl2">float</td>
    <td class="tg-pnl2">DOUBLE</td>
  </tr>
  <tr>
    <td class="tg-pnl2">double</td>
    <td class="tg-pnl2">double</td>
    <td class="tg-pnl2">DOUBLE</td>
  </tr>
  <tr>
    <td class="tg-pnl2">keyword</td>
    <td class="tg-pnl2">string</td>
    <td class="tg-pnl2">VARCHAR</td>
  </tr>
  <tr>
    <td class="tg-pnl2">text</td>
    <td class="tg-pnl2">text</td>
    <td class="tg-pnl2">VARCHAR</td>
  </tr>
  <tr>
    <td class="tg-pnl2">date</td>
    <td class="tg-pnl2">timestamp</td>
    <td class="tg-pnl2">TIMESTAMP</td>
  </tr>
  <tr>
    <td class="tg-pnl2">date_nanos</td>
    <td class="tg-pnl2">timestamp</td>
    <td class="tg-pnl2">TIMESTAMP</td>
  </tr>
  <tr>
    <td class="tg-pnl2">ip</td>
    <td class="tg-pnl2">ip</td>
    <td class="tg-pnl2">VARCHAR</td>
  </tr>
  <tr>
    <td class="tg-pnl2">date</td>
    <td class="tg-pnl2">timestamp</td>
    <td class="tg-pnl2">TIMESTAMP</td>
  </tr>
  <tr>
    <td class="tg-pnl2">binary</td>
    <td class="tg-pnl2">binary</td>
    <td class="tg-pnl2">VARBINARY</td>
  </tr>
  <tr>
    <td class="tg-pnl2">object</td>
    <td class="tg-pnl2">struct</td>
    <td class="tg-pnl2">STRUCT</td>
  </tr>
  <tr>
    <td class="tg-pnl2">nested</td>
    <td class="tg-pnl2">array</td>
    <td class="tg-pnl2">STRUCT</td>
  </tr>
</tbody>
</table>

In addition to this list, the SQL plugin also supports the `datetime` type, though it doesn't have a corresponding mapping with Energy Logserver or SQL.
To use a function without a corresponding mapping, you must explicitly convert the data type to one that does.

#### Date and time types

The date and time types represent a time period: `DATE`, `TIME`, `DATETIME`, `TIMESTAMP`, and `INTERVAL`. By default, the Energy Logserver DSL uses the `date` type as the only date-time related type that contains all information of an absolute time point.

To integrate with SQL, each type other than the `timestamp` type holds part of the time period information. Some functions might have restrictions for the input argument type.

#### Date

The `date` type represents the calendar date regardless of the time zone. A given date value is a 24-hour period, but this period varies in different timezones and might have flexible hours during daylight saving programs. The `date` type doesn't contain time information and it only supports a range of `1000-01-01` to `9999-12-31`.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Type</th>
    <th class="tg-ua3b">Syntax</th>
    <th class="tg-ua3b">Range</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">date</td>
    <td class="tg-pnl2">yyyy-MM-dd</td>
    <td class="tg-pnl2">0001-01-01 to 9999-12-31</td>
  </tr>
</tbody>
</table>

#### Time

The `time` type represents the time of a clock regardless of its timezone. The `time` type doesn't contain date information.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Type</th>
    <th class="tg-ua3b">Syntax</th>
    <th class="tg-ua3b">Range</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">time</td>
    <td class="tg-pnl2">hh:mm:ss[.fraction]</td>
    <td class="tg-pnl2">00:00:00.0000000000 to 23:59:59.9999999999</td>
  </tr>
</tbody>
</table>

#### Datetime

The `datetime` type is a combination of date and time. It doesn't contain timezone information. For an absolute time point that contains date, time, and timezone information, see [Timestamp](#timestamp).

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Type</th>
    <th class="tg-ua3b">Syntax</th>
    <th class="tg-ua3b">Range</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">datetime</td>
    <td class="tg-pnl2">yyyy-MM-dd hh:mm:ss[.fraction]</td>
    <td class="tg-pnl2">0001-01-01 00:00:00.0000000000 to 9999-12-31 23:59:59.9999999999</td>
  </tr>
</tbody>
</table>

#### Timestamp

The `timestamp` type is an absolute instance independent of timezone or convention. For example, for a given point of time, if you change the timestamp to a different timezone, its value changes accordingly.

The `timestamp` type is stored differently from the other types. It's converted from its current timezone to UTC for storage and converted back to its set timezone from UTC when it's retrieved.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Type</th>
    <th class="tg-ua3b">Syntax</th>
    <th class="tg-ua3b">Range</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">timestamp</td>
    <td class="tg-pnl2">yyyy-MM-dd hh:mm:ss[.fraction]</td>
    <td class="tg-pnl2">0001-01-01 00:00:01.9999999999 UTC to 9999-12-31 23:59:59.9999999999</td>
  </tr>
</tbody>
</table>

#### Interval

The `interval` type represents a temporal duration or a period.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Type</th>
    <th class="tg-ua3b">Syntax</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">interval</td>
    <td class="tg-pnl2">INTERVAL expr unit</td>
  </tr>
</tbody>
</table>

The `expr` unit is any expression that eventually iterates to a quantity value. It represents a unit for interpreting the quantity, including `MICROSECOND`, `SECOND`, `MINUTE`, `HOUR`, `DAY`, `WEEK`, `MONTH`, `QUARTER`, and `YEAR`. The `INTERVAL` keyword and the unit specifier are not case sensitive.

The `interval` type has two classes of intervals: year-week intervals and day-time intervals.

- Year-week intervals store years, quarters, months, and weeks.
- Day-time intervals store days, hours, minutes, seconds, and microseconds.

#### Convert between date and time types

Apart from the `interval` type, all date and time types can be converted to each other. The conversion might alter the value or cause some information loss. For example, when extracting the `time` value from a `datetime` value, or converting a `date` value to a `datetime` value, and so on.

The SQL plugin supports the following conversion rules for each of the types:

**Convert from date**

- Because the `date` value doesn't have any time information, conversion to the `time` type isn't useful and always returns a zero time value of `00:00:00`.
- Converting from `date` to `datetime` has a data fill-up due to the lack of time information. It attaches the time `00:00:00` to the original date by default and forms a `datetime` instance. For example, conversion of `2020-08-17` to a `datetime` type is `2020-08-17 00:00:00`.
- Converting to `timestamp` type alternates both the `time` value and the `timezone` information. It attaches the zero time value `00:00:00` and the session timezone (UTC by default) to the date. For example, conversion of `2020-08-17` to a `datetime` type with a session timezone UTC is `2020-08-17 00:00:00 UTC`.

**Convert from time**

- You cannot convert the `time` type to any other date and time types because it doesn't contain any date information.

**Convert from datetime**

- Converting `datetime` to `date` extracts the date value from the `datetime` value. For example, conversion of `2020-08-17 14:09:00` to a `date` type is `2020-08-08`.
- Converting `datetime` to `time` extracts the time value from the `datetime` value. For example, conversion of `2020-08-17 14:09:00` to a `time` type is `14:09:00`.
- Because the `datetime` type doesn't contain timezone information, converting to `timestamp` type fills up the timezone value with the session timezone. For example, conversion of `2020-08-17 14:09:00` (UTC) to a `timestamp` type is `2020-08-17 14:09:00 UTC`.

**Convert from timestamp**

- Converting from a `timestamp` type to a `date` type extracts the date value and converting to a `time` type extracts the time value. Converting from a `timestamp` type to `datetime` type extracts only the `datetime` value and leaves out the timezone value. For example, conversion of `2020-08-17 14:09:00` UTC to a `date` type is `2020-08-17`, to a `time` type is `14:09:00`, and to a `datetime` type is `2020-08-17 14:09:00`.

### Functions

You must enable fielddata in the document mapping for most string functions to work properly.

The specification shows the return type of the function with a generic type `T` as the argument.
For example, `abs(number T) -> T` means that the function `abs` accepts a numerical argument of type `T`, which could be any subtype of the `number` type, and it returns the actual type of `T` as the return type.

The SQL plugin supports the following common functions shared across the SQL and PPL languages.

#### Mathematical

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Function  </th>
    <th class="tg-ua3b">Specification   </th>
    <th class="tg-ua3b">Example</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">abs</td>
    <td class="tg-pnl2">abs(number T) -> T</td>
    <td class="tg-pnl2">SELECT abs(0.5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">add</td>
    <td class="tg-pnl2">add(number T, number T) -> T</td>
    <td class="tg-pnl2">SELECT add(1, 5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">cbrt</td>
    <td class="tg-pnl2">cbrt(number T) -> double</td>
    <td class="tg-pnl2">SELECT cbrt(8)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">ceil</td>
    <td class="tg-pnl2">ceil(number T) -> T</td>
    <td class="tg-pnl2">SELECT ceil(0.5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">conv</td>
    <td class="tg-pnl2">conv(string T, integer, integer) -> string</td>
    <td class="tg-pnl2">SELECT conv('2C', 16, 10), conv(1111, 2, 10)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">crc32</td>
    <td class="tg-pnl2">crc32(string) -> string</td>
    <td class="tg-pnl2">SELECT crc32('MySQL')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">divide</td>
    <td class="tg-pnl2">divide(number T, number T) -> T</td>
    <td class="tg-pnl2">SELECT divide(1, 0.5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">e</td>
    <td class="tg-pnl2">e() -> double</td>
    <td class="tg-pnl2">SELECT e()</td>
  </tr>
  <tr>
    <td class="tg-pnl2">exp</td>
    <td class="tg-pnl2">exp(number T) -> double</td>
    <td class="tg-pnl2">SELECT exp(0.5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">expm1</td>
    <td class="tg-pnl2">expm1(number T) -> double</td>
    <td class="tg-pnl2">SELECT expm1(0.5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">floor</td>
    <td class="tg-pnl2">floor(number T) -> long</td>
    <td class="tg-pnl2">SELECT floor(0.5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">ln</td>
    <td class="tg-pnl2">ln(number T) -> double</td>
    <td class="tg-pnl2">SELECT ln(10)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">log</td>
    <td class="tg-pnl2">log(number T) -> double OR log(number T, number T) -> double</td>
    <td class="tg-pnl2">SELECT log(10), SELECT log(2, 16)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">log2</td>
    <td class="tg-pnl2">log2(number T) -> double</td>
    <td class="tg-pnl2">SELECT log2(10)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">log10</td>
    <td class="tg-pnl2">log10(number T) -> double</td>
    <td class="tg-pnl2">SELECT log10(10)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">mod</td>
    <td class="tg-pnl2">mod(number T, number T) -> T</td>
    <td class="tg-pnl2">SELECT mod(2, 3)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">modulus</td>
    <td class="tg-pnl2">modulus(number T, number T) -> T</td>
    <td class="tg-pnl2">SELECT modulus(2, 3)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">multiply</td>
    <td class="tg-pnl2">multiply(number T, number T) -> T</td>
    <td class="tg-pnl2">SELECT multiply(2, 3)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">pi</td>
    <td class="tg-pnl2">pi() -> double</td>
    <td class="tg-pnl2">SELECT pi()</td>
  </tr>
  <tr>
    <td class="tg-pnl2">pow</td>
    <td class="tg-pnl2">pow(number T, number T) -> double</td>
    <td class="tg-pnl2">SELECT pow(2, 3)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">power</td>
    <td class="tg-pnl2">power(number T, number T) -> double</td>
    <td class="tg-pnl2">SELECT power(2, 3)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">rand</td>
    <td class="tg-pnl2">rand() -> float OR rand(number T) -> float</td>
    <td class="tg-pnl2">SELECT rand(), SELECT rand(0.5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">rint</td>
    <td class="tg-pnl2">rint(number T) -> double</td>
    <td class="tg-pnl2">SELECT rint(1.5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">round</td>
    <td class="tg-pnl2">round(number T) -> T OR round(number T, integer) -> T</td>
    <td class="tg-pnl2">SELECT round(1.5), SELECT round(1.175, 2)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">sign</td>
    <td class="tg-pnl2">sign(number T) -> integer</td>
    <td class="tg-pnl2">SELECT sign(1.5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">signum</td>
    <td class="tg-pnl2">signum(number T) -> integer</td>
    <td class="tg-pnl2">SELECT signum(0.5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">sqrt</td>
    <td class="tg-pnl2">sqrt(number T) -> double</td>
    <td class="tg-pnl2">SELECT sqrt(0.5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">strcmp</td>
    <td class="tg-pnl2">strcmp(string T, string T) -> integer</td>
    <td class="tg-pnl2">SELECT strcmp('hello', 'hello world')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">subtract</td>
    <td class="tg-pnl2">subtract(number T, number T) -> T</td>
    <td class="tg-pnl2">SELECT subtract(3, 2)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">truncate</td>
    <td class="tg-pnl2">truncate(number T, number T) -> T</td>
    <td class="tg-pnl2">SELECT truncate(56.78, 1)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">+</td>
    <td class="tg-pnl2">number T + number T -> T</td>
    <td class="tg-pnl2">SELECT 1 + 5</td>
  </tr>
  <tr>
    <td class="tg-pnl2">-</td>
    <td class="tg-pnl2">number T - number T -> T</td>
    <td class="tg-pnl2">SELECT 3 - 2</td>
  </tr>
  <tr>
    <td class="tg-pnl2">*</td>
    <td class="tg-pnl2">number T * number T -> T</td>
    <td class="tg-pnl2">SELECT 2 * 3</td>
  </tr>
  <tr>
    <td class="tg-pnl2">/</td>
    <td class="tg-pnl2">number T / number T -> T</td>
    <td class="tg-pnl2">SELECT 1 / 0.5</td>
  </tr>
  <tr>
    <td class="tg-pnl2">%</td>
    <td class="tg-pnl2">number T % number T -> T</td>
    <td class="tg-pnl2">SELECT 2 % 3</td>
  </tr>
</tbody>
</table>

#### Trigonometric

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Function </th>
    <th class="tg-ua3b">Specification</th>
    <th class="tg-ua3b">Example</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">acos</td>
    <td class="tg-pnl2">acos(number T) -> double</td>
    <td class="tg-pnl2">SELECT acos(0.5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">asin</td>
    <td class="tg-pnl2">asin(number T) -> double</td>
    <td class="tg-pnl2">SELECT asin(0.5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">atan</td>
    <td class="tg-pnl2">atan(number T) -> double</td>
    <td class="tg-pnl2">SELECT atan(0.5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">atan2</td>
    <td class="tg-pnl2">atan2(number T, number T) -> double</td>
    <td class="tg-pnl2">SELECT atan2(1, 0.5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">cos</td>
    <td class="tg-pnl2">cos(number T) -> double</td>
    <td class="tg-pnl2">SELECT cos(0.5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">cosh</td>
    <td class="tg-pnl2">cosh(number T) -> double</td>
    <td class="tg-pnl2">SELECT cosh(0.5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">cot</td>
    <td class="tg-pnl2">cot(number T) -> double</td>
    <td class="tg-pnl2">SELECT cot(0.5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">degrees</td>
    <td class="tg-pnl2">degrees(number T) -> double</td>
    <td class="tg-pnl2">SELECT degrees(0.5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">radians</td>
    <td class="tg-pnl2">radians(number T) -> double</td>
    <td class="tg-pnl2">SELECT radians(0.5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">sin</td>
    <td class="tg-pnl2">sin(number T) -> double</td>
    <td class="tg-pnl2">SELECT sin(0.5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">sinh</td>
    <td class="tg-pnl2">sinh(number T) -> double</td>
    <td class="tg-pnl2">SELECT sinh(0.5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">tan</td>
    <td class="tg-pnl2">tan(number T) -> double</td>
    <td class="tg-pnl2">SELECT tan(0.5)</td>
  </tr>
</tbody>
</table>

#### Date and time

Functions marked with * are only available in SQL.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Function</th>
    <th class="tg-ua3b">Specification </th>
    <th class="tg-ua3b">Example</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">adddate</td>
    <td class="tg-pnl2">adddate(date, INTERVAL expr unit) -> date</td>
    <td class="tg-pnl2">SELECT adddate(date('2020-08-26'), INTERVAL 1 hour)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">addtime</td>
    <td class="tg-pnl2">addtime(date, date) -> date</td>
    <td class="tg-pnl2">SELECT addtime(date('2008-12-12'), date('2008-12-12'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">convert_tz</td>
    <td class="tg-pnl2">convert_tz(date, string, string) -> date</td>
    <td class="tg-pnl2">SELECT convert_tz('2008-12-25 05:30:00', '+00:00', 'America/Los_Angeles')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">curtime</td>
    <td class="tg-pnl2">curtime() -> time</td>
    <td class="tg-pnl2">SELECT curtime()</td>
  </tr>
  <tr>
    <td class="tg-pnl2">curdate</td>
    <td class="tg-pnl2">curdate() -> date</td>
    <td class="tg-pnl2">SELECT curdate()</td>
  </tr>
  <tr>
    <td class="tg-pnl2">current_date</td>
    <td class="tg-pnl2">current_date() -> date</td>
    <td class="tg-pnl2">SELECT current_date()</td>
  </tr>
  <tr>
    <td class="tg-pnl2">current_time</td>
    <td class="tg-pnl2">current_time() -> time</td>
    <td class="tg-pnl2">SELECT current_time()</td>
  </tr>
  <tr>
    <td class="tg-pnl2">current_timestamp</td>
    <td class="tg-pnl2">current_timestamp() -> date</td>
    <td class="tg-pnl2">SELECT current_timestamp()</td>
  </tr>
  <tr>
    <td class="tg-pnl2">date</td>
    <td class="tg-pnl2">date(date) -> date</td>
    <td class="tg-pnl2">SELECT date('2000-01-02')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">datediff</td>
    <td class="tg-pnl2">datediff(date, date) -> integer</td>
    <td class="tg-pnl2">SELECT datediff(date('2000-01-02'), date('2000-01-01'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">datetime</td>
    <td class="tg-pnl2">datetime(string) -> datetime</td>
    <td class="tg-pnl2">SELECT datetime('2008-12-25 00:00:00')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">date_add</td>
    <td class="tg-pnl2">date_add(date, INTERVAL integer UNIT)</td>
    <td class="tg-pnl2">SELECT date_add('2020-08-26', INTERVAL 1 HOUR)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">date_format</td>
    <td class="tg-pnl2">date_format(date, string) -> string OR date_format(date, string, string) -> string</td>
    <td class="tg-pnl2">SELECT date_format(date('2020-08-26'), 'Y')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">date_sub</td>
    <td class="tg-pnl2">date_sub(date, INTERVAL expr unit) -> date</td>
    <td class="tg-pnl2">SELECT date_sub(date('2008-01-02'), INTERVAL 31 day)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">dayofmonth</td>
    <td class="tg-pnl2">dayofmonth(date) -> integer</td>
    <td class="tg-pnl2">SELECT dayofmonth(date('2001-05-07'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">day</td>
    <td class="tg-pnl2">day(date) -> integer</td>
    <td class="tg-pnl2">SELECT day(date('2020-08-25'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">dayname</td>
    <td class="tg-pnl2">dayname(date) -> string</td>
    <td class="tg-pnl2">SELECT dayname(date('2020-08-26'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">dayofmonth</td>
    <td class="tg-pnl2">dayofmonth(date) -> integer</td>
    <td class="tg-pnl2">SELECT dayofmonth(date('2020-08-26'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">dayofweek</td>
    <td class="tg-pnl2">dayofweek(date) -> integer</td>
    <td class="tg-pnl2">SELECT dayofweek(date('2020-08-26'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">dayofyear</td>
    <td class="tg-pnl2">dayofyear(date) -> integer</td>
    <td class="tg-pnl2">SELECT dayofyear(date('2020-08-26'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">dayofweek</td>
    <td class="tg-pnl2">dayofweek(date) -> integer</td>
    <td class="tg-pnl2">SELECT dayofweek(date('2020-08-26'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">day_of_month\*</td>
    <td class="tg-pnl2">day_of_month(date) -> integer</td>
    <td class="tg-pnl2">SELECT day_of_month(date('2020-08-26'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">day_of_week\*</td>
    <td class="tg-pnl2">day_of_week(date) -> integer</td>
    <td class="tg-pnl2">SELECT day_of_week(date('2020-08-26'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">day_of_year\*</td>
    <td class="tg-pnl2">day_of_year(date) -> integer</td>
    <td class="tg-pnl2">SELECT day_of_year(date('2020-08-26'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">extract\*</td>
    <td class="tg-pnl2">extract(part FROM date) -> integer</td>
    <td class="tg-pnl2">SELECT extract(MONTH FROM datetime('2020-08-26 10:11:12'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">from_days</td>
    <td class="tg-pnl2">from_days(N) -> integer</td>
    <td class="tg-pnl2">SELECT from_days(733687)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">from_unixtime</td>
    <td class="tg-pnl2">from_unixtime(N) -> date</td>
    <td class="tg-pnl2">SELECT from_unixtime(1220249547)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">get_format</td>
    <td class="tg-pnl2">get_format(PART, string) -> string</td>
    <td class="tg-pnl2">SELECT get_format(DATE, 'USA')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">hour</td>
    <td class="tg-pnl2">hour(time) -> integer</td>
    <td class="tg-pnl2">SELECT hour(time '01:02:03')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">hour_of_day\*</td>
    <td class="tg-pnl2">hour_of_day(time) -> integer</td>
    <td class="tg-pnl2">SELECT hour_of_day(time '01:02:03')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">last_day\*</td>
    <td class="tg-pnl2">last_day(date) -> integer</td>
    <td class="tg-pnl2">SELECT last_day(date('2020-08-26'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">localtime</td>
    <td class="tg-pnl2">localtime() -> date</td>
    <td class="tg-pnl2">SELECT localtime()</td>
  </tr>
  <tr>
    <td class="tg-pnl2">localtimestamp</td>
    <td class="tg-pnl2">localtimestamp() -> date</td>
    <td class="tg-pnl2">SELECT localtimestamp()</td>
  </tr>
  <tr>
    <td class="tg-pnl2">makedate</td>
    <td class="tg-pnl2">makedate(double, double) -> date</td>
    <td class="tg-pnl2">SELECT makedate(1945, 5.9)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">maketime</td>
    <td class="tg-pnl2">maketime(integer, integer, integer) -> date</td>
    <td class="tg-pnl2">SELECT maketime(1, 2, 3)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">microsecond</td>
    <td class="tg-pnl2">microsecond(expr) -> integer</td>
    <td class="tg-pnl2">SELECT microsecond(time '01:02:03.123456')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">minute</td>
    <td class="tg-pnl2">minute(expr) -> integer</td>
    <td class="tg-pnl2">SELECT minute(time '01:02:03')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">minute_of_day\*</td>
    <td class="tg-pnl2">minute_of_day(expr) -> integer</td>
    <td class="tg-pnl2">SELECT minute_of_day(time '01:02:03')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">minute_of_hour\*</td>
    <td class="tg-pnl2">minute_of_hour(expr) -> integer</td>
    <td class="tg-pnl2">SELECT minute_of_hour(time '01:02:03')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">month</td>
    <td class="tg-pnl2">month(date) -> integer</td>
    <td class="tg-pnl2">SELECT month(date('2020-08-26'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">month_of_year\*</td>
    <td class="tg-pnl2">month_of_year(date) -> integer</td>
    <td class="tg-pnl2">SELECT month_of_year(date('2020-08-26'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">monthname</td>
    <td class="tg-pnl2">monthname(date) -> string</td>
    <td class="tg-pnl2">SELECT monthname(date('2020-08-26'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">now</td>
    <td class="tg-pnl2">now() -> date</td>
    <td class="tg-pnl2">SELECT now()</td>
  </tr>
  <tr>
    <td class="tg-pnl2">period_add</td>
    <td class="tg-pnl2">period_add(integer, integer)</td>
    <td class="tg-pnl2">SELECT period_add(200801, 2)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">period_diff</td>
    <td class="tg-pnl2">period_diff(integer, integer)</td>
    <td class="tg-pnl2">SELECT period_diff(200802, 200703)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">quarter</td>
    <td class="tg-pnl2">quarter(date) -> integer</td>
    <td class="tg-pnl2">SELECT quarter(date('2020-08-26'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">second</td>
    <td class="tg-pnl2">second(time) -> integer</td>
    <td class="tg-pnl2">SELECT second(time '01:02:03')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">second_of_minute\*</td>
    <td class="tg-pnl2">second_of_minute(time) -> integer</td>
    <td class="tg-pnl2">SELECT second_of_minute(time '01:02:03')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">sec_to_time\*</td>
    <td class="tg-pnl2">sec_to_time(integer) -> date</td>
    <td class="tg-pnl2">SELECT sec_to_time(10000)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">subdate</td>
    <td class="tg-pnl2">subdate(date, INTERVAL expr unit) -> date, datetime</td>
    <td class="tg-pnl2">SELECT subdate(date('2008-01-02'), INTERVAL 31 day)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">subtime</td>
    <td class="tg-pnl2">subtime(date, date) -> date</td>
    <td class="tg-pnl2">SELECT subtime(date('2008-12-12'), date('2008-11-15'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">str_to_date\*</td>
    <td class="tg-pnl2">str_to_date(string, format) -> date</td>
    <td class="tg-pnl2">SELECT str_to_date("01,5,2013", "%d,%m,%Y")</td>
  </tr>
  <tr>
    <td class="tg-pnl2">time</td>
    <td class="tg-pnl2">time(expr) -> time</td>
    <td class="tg-pnl2">SELECT time('13:49:00')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">timediff</td>
    <td class="tg-pnl2">timediff(time, time) -> time</td>
    <td class="tg-pnl2">SELECT timediff(time('23:59:59'), time('13:00:00'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">timestamp</td>
    <td class="tg-pnl2">timestamp(date) -> date</td>
    <td class="tg-pnl2">SELECT timestamp('2001-05-07 00:00:00')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">timestampadd</td>
    <td class="tg-pnl2">timestampadd(interval, integer, (date)) -> date</td>
    <td class="tg-pnl2">SELECT timestampadd(DAY, 17, datetime('2000-01-01 00:00:00'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">timestampdiff</td>
    <td class="tg-pnl2">timestampdiff(interval, date, date) -> integer</td>
    <td class="tg-pnl2">SELECT timestampdiff(YEAR, '1997-01-01 00:00:00', '2001-03-06 00:00:00')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">time_format</td>
    <td class="tg-pnl2">time_format(date, string) -> string</td>
    <td class="tg-pnl2">SELECT time_format('1998-01-31 13:14:15.012345', '%f %H %h %I %i %p %r %S %s %T')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">time_to_sec</td>
    <td class="tg-pnl2">time_to_sec(time) -> long</td>
    <td class="tg-pnl2">SELECT time_to_sec(time '22:23:00')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">to_days</td>
    <td class="tg-pnl2">to_days(date) -> long</td>
    <td class="tg-pnl2">SELECT to_days(date '2008-10-07')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">to_seconds</td>
    <td class="tg-pnl2">to_seconds(date) -> integer</td>
    <td class="tg-pnl2">SELECT to_seconds(date('2008-10-07'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">unix_timestamp</td>
    <td class="tg-pnl2">unix_timestamp(date) -> double</td>
    <td class="tg-pnl2">SELECT unix_timestamp(timestamp('1996-11-15 17:05:42'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">utc_date</td>
    <td class="tg-pnl2">utc_date() -> date</td>
    <td class="tg-pnl2">SELECT utc_date()</td>
  </tr>
  <tr>
    <td class="tg-pnl2">utc_time</td>
    <td class="tg-pnl2">utc_time() -> date</td>
    <td class="tg-pnl2">SELECT utc_time()</td>
  </tr>
  <tr>
    <td class="tg-pnl2">utc_timestamp</td>
    <td class="tg-pnl2">utc_timestamp() -> date</td>
    <td class="tg-pnl2">SELECT utc_timestamp()</td>
  </tr>
  <tr>
    <td class="tg-pnl2">week</td>
    <td class="tg-pnl2">week(date[mode]) -> integer</td>
    <td class="tg-pnl2">SELECT week(date('2008-02-20'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">weekofyear</td>
    <td class="tg-pnl2">weekofyear(date[mode]) -> integer</td>
    <td class="tg-pnl2">SELECT weekofyear(date('2008-02-20'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">week_of_year\*</td>
    <td class="tg-pnl2">week_of_year(date[mode]) -> integer</td>
    <td class="tg-pnl2">SELECT week_of_year(date('2008-02-20'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">year</td>
    <td class="tg-pnl2">year(date) -> integer</td>
    <td class="tg-pnl2">SELECT year(date('2001-07-05'))</td>
  </tr>
  <tr>
    <td class="tg-pnl2">yearweek\*</td>
    <td class="tg-pnl2">yearweek(date[mode]) -> integer</td>
    <td class="tg-pnl2">SELECT yearweek(date('2008-02-20'))</td>
  </tr>
</tbody>
</table>

#### String

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Function   </th>
    <th class="tg-ua3b">Specification</th>
    <th class="tg-ua3b">Example</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">ascii</td>
    <td class="tg-pnl2">ascii(string) -> integer</td>
    <td class="tg-pnl2">SELECT ascii('h')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">concat</td>
    <td class="tg-pnl2">concat(string, string) -> string</td>
    <td class="tg-pnl2">SELECT concat('hello', 'world')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">concat_ws</td>
    <td class="tg-pnl2">concat_ws(separator, string, string…) -> string</td>
    <td class="tg-pnl2">SELECT concat_ws(" ", "Hello", "World!")</td>
  </tr>
  <tr>
    <td class="tg-pnl2">left</td>
    <td class="tg-pnl2">left(string, integer) -> string</td>
    <td class="tg-pnl2">SELECT left('hello', 2)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">length</td>
    <td class="tg-pnl2">length(string) -> integer</td>
    <td class="tg-pnl2">SELECT length('hello')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">locate</td>
    <td class="tg-pnl2">locate(string, string, integer) -> integer OR locate(string, string) -> integer</td>
    <td class="tg-pnl2">SELECT locate('o', 'hello'), locate('l', 'hello world', 5)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">replace</td>
    <td class="tg-pnl2">replace(string, string, string) -> string</td>
    <td class="tg-pnl2">SELECT replace('hello', 'l', 'x')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">right</td>
    <td class="tg-pnl2">right(string, integer) -> string</td>
    <td class="tg-pnl2">SELECT right('hello', 2)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">rtrim</td>
    <td class="tg-pnl2">rtrim(string) -> string</td>
    <td class="tg-pnl2">SELECT rtrim('hello')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">substring</td>
    <td class="tg-pnl2">substring(string, integer, integer) -> string</td>
    <td class="tg-pnl2">SELECT substring('hello', 2, 4)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">trim</td>
    <td class="tg-pnl2">trim(string) -> string</td>
    <td class="tg-pnl2">SELECT trim('hello')</td>
  </tr>
  <tr>
    <td class="tg-pnl2">upper</td>
    <td class="tg-pnl2">upper(string) -> string</td>
    <td class="tg-pnl2">SELECT upper('hello world')</td>
  </tr>
</tbody>
</table>

#### Aggregate

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Function</th>
    <th class="tg-ua3b">Specification </th>
    <th class="tg-ua3b">Example</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">avg</td>
    <td class="tg-pnl2">avg(number T) -> T</td>
    <td class="tg-pnl2">SELECT avg(column) FROM my-index</td>
  </tr>
  <tr>
    <td class="tg-pnl2">count</td>
    <td class="tg-pnl2">count(number T) -> T</td>
    <td class="tg-pnl2">SELECT count(date) FROM my-index</td>
  </tr>
  <tr>
    <td class="tg-pnl2">min</td>
    <td class="tg-pnl2">min(number T) -> T</td>
    <td class="tg-pnl2">SELECT min(column) FROM my-index</td>
  </tr>
  <tr>
    <td class="tg-pnl2">show</td>
    <td class="tg-pnl2">show(string) -> string</td>
    <td class="tg-pnl2">SHOW TABLES LIKE my-index</td>
  </tr>
</tbody>
</table>

#### Advanced

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">Function</th>
    <th class="tg-ua3b">Specification </th>
    <th class="tg-ua3b">Example</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">if</td>
    <td class="tg-pnl2">if(boolean, os_type, os_type) -> os_type</td>
    <td class="tg-pnl2">`SELECT if(false, 0, 1),if(true, 0, 1)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">ifnull</td>
    <td class="tg-pnl2">ifnull(os_type, os_type) -> os_type</td>
    <td class="tg-pnl2">SELECT ifnull(0, 1), ifnull(null, 1)</td>
  </tr>
  <tr>
    <td class="tg-pnl2">isnull</td>
    <td class="tg-pnl2">isnull(os_type) -> integer</td>
    <td class="tg-pnl2">SELECT isnull(null), isnull(1)</td>
  </tr>
</tbody>
</table>

#### Relevance-based search (full-text search)

These functions are only available in the `WHERE` clause. For their descriptions and usage examples in SQL and PPL, see [Full-text search](#full-text-search).

### Full-text search

Use SQL commands for full-text search. The SQL plugin supports a subset of full-text queries available in Energy Logserver.

#### Match

Use the `MATCH` function to search documents that match a `string`, `number`, `date`, or `boolean` value for a given field.

#### Syntax

```sql
match(field_expression, query_expression[, option=<option_value>]*)
```

You can specify the following options in any order:

- `analyzer`
- `auto_generate_synonyms_phrase`
- `fuzziness`
- `max_expansions`
- `prefix_length`
- `fuzzy_transpositions`
- `fuzzy_rewrite`
- `lenient`
- `operator`
- `minimum_should_match`
- `zero_terms_query`
- `boost`

Refer to the `match` query for parameter descriptions and supported values.

##### Example 1: Search the `message` field for the text "this is a test":

```json
GET my_index/_search
{
  "query": {
    "match": {
      "message": "this is a test"
    }
  }
}
```

**SQL query:**

```sql
SELECT message FROM my_index WHERE match(message, "this is a test")
```

**PPL query:**

```bash
SOURCE=my_index | WHERE match(message, "this is a test") | FIELDS message
```

##### Example 2: Search the `message` field with the `operator` parameter:

```json
GET my_index/_search
{
  "query": {
    "match": {
      "message": {
        "query": "this is a test",
        "operator": "and"
      }
    }
  }
}
```

**SQL query:**

```sql
SELECT message FROM my_index WHERE match(message, "this is a test", operator='and')
```

**PPL query:**

```bash
SOURCE=my_index | WHERE match(message, "this is a test", operator='and') | FIELDS message
```

##### Example 3: Search the `message` field with the `operator` and `zero_terms_query` parameters:

```json
GET my_index/_search
{
  "query": {
    "match": {
      "message": {
        "query": "to be or not to be",
        "operator": "and",
        "zero_terms_query": "all"
      }
    }
  }
}
```

**SQL query:**

```sql
SELECT message FROM my_index WHERE match(message, "this is a test", operator='and', zero_terms_query='all')
```

**PPL query:**

```sql
SOURCE=my_index | WHERE match(message, "this is a test", operator='and', zero_terms_query='all') | FIELDS message
```

#### Multi-match

To search for text in multiple fields, use `MULTI_MATCH` function. This function maps to the `multi_match` query used in search engine, to returns the documents that match a provided text, number, date or boolean value with a given field or fields.

##### Syntax

The `MULTI_MATCH` function lets you *boost* certain fields using **^** character. Boosts are multipliers that weigh matches in one field more heavily than matches in other fields. The syntax allows to specify the fields in double quotes, single quotes,  surrounded by backticks, or unquoted. Use star ``"*"`` to search all fields. Star symbol should be quoted.

```sql
multi_match([field_expression+], query_expression[, option=<option_value>]*)
```

The weight is optional and is specified after the field name. It could be delimited by the `caret` character -- `^` or by whitespace. Please, refer to examples below:

```sql
multi_match(["Tags" ^ 2, 'Title' 3.4, `Body`, Comments ^ 0.3], ...)
multi_match(["*"], ...)
```

You can specify the following options for `MULTI_MATCH` in any order:

- `analyzer`
- `auto_generate_synonyms_phrase`
- `cutoff_frequency`
- `fuzziness`
- `fuzzy_transpositions`
- `lenient`
- `max_expansions`
- `minimum_should_match`
- `operator`
- `prefix_length`
- `tie_breaker`
- `type`
- `slop`
- `zero_terms_query`
- `boost`

Please, refer to `multi_match` query [documentation](#multi-match) for parameter description and supported values.

##### For example, REST API search for `Dale` in either the `firstname` or `lastname` fields:

```json
GET accounts/_search
{
  "query": {
    "multi_match": {
      "query": "Lane Street",
      "fields": [ "address" ],
    }
  }
}
```

could be called from *SQL* using `multi_match` function

```sql
SELECT firstname, lastname
FROM accounts
WHERE multi_match(['*name'], 'Dale')
```

or `multi_match` *PPL* function

```sql
SOURCE=accounts | WHERE multi_match(['*name'], 'Dale') | fields firstname, lastname
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">firstname</th>
    <th class="tg-ua3b">lastname</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">Dale</td>
    <td class="tg-pnl2">Adams</td>
  </tr>
</tbody>
</table>

##### Query string

To split text based on operators, use the `QUERY_STRING` function. The `QUERY_STRING` function supports logical connectives, wildcard, regex, and proximity search.
This function maps to the to the `query_string` query used in search engine, to return the documents that match a provided text, number, date or boolean value with a given field or fields.

##### Syntax

The `QUERY_STRING` function has syntax similar to `MATCH_QUERY` and lets you *boost* certain fields using **^** character. Boosts are multipliers that weigh matches in one field more heavily than matches in other fields. The syntax allows to specify the fields in double quotes, single quotes,  surrounded by backticks, or unquoted. Use star ``"*"`` to search all fields. Star symbol should be quoted.

```sql
query_string([field_expression+], query_expression[, option=<option_value>]*)
```

The weight is optional and is specified after the field name. It could be delimited by the `caret` character -- `^` or by whitespace. Please, refer to examples below:

```sql
query_string(["Tags" ^ 2, 'Title' 3.4, `Body`, Comments ^ 0.3], ...)
query_string(["*"], ...)
```

You can specify the following options for `QUERY_STRING` in any order:

- `analyzer`
- `allow_leading_wildcard`
- `analyze_wildcard`
- `auto_generate_synonyms_phrase_query`
- `boost`
- `default_operator`
- `enable_position_increments`
- `fuzziness`
- `fuzzy_rewrite`
- `escape`
- `fuzzy_max_expansions`
- `fuzzy_prefix_length`
- `fuzzy_transpositions`
- `lenient`
- `max_determinized_states`
- `minimum_should_match`
- `quote_analyzer`
- `phrase_slop`
- `quote_field_suffix`
- `rewrite`
- `type`
- `tie_breaker`
- `time_zone`

##### Example of using `query_string` in SQL and PPL queries:

The REST API search request

```json
GET accounts/_search
{
  "query": {
    "query_string": {
      "query": "Lane Street",
      "fields": [ "address" ],
    }
  }
}
```

could be called from *SQL*

```sql
SELECT account_number, address
FROM accounts
WHERE query_string(['address'], 'Lane Street', default_operator='OR')
```

or from *PPL*

```sql
SOURCE=accounts | WHERE query_string(['address'], 'Lane Street', default_operator='OR') | fields account_number, address
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">address</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">880 Holmes Lane</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">671 Bristol Street</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">789 Madison Street</td>
  </tr>
</tbody>
</table>

#### Match phrase

To search for exact phrases, use `MATCHPHRASE` or `MATCH_PHRASE` functions.

##### Syntax

```sql
matchphrasequery(field_expression, query_expression)
matchphrase(field_expression, query_expression[, option=<option_value>]*)
match_phrase(field_expression, query_expression[, option=<option_value>]*)
```

The `MATCHPHRASE`/`MATCH_PHRASE` functions let you specify the following options in any order:

- `analyzer`
- `slop`
- `zero_terms_query`
- `boost`

##### Example of using `match_phrase` in SQL and PPL queries:

The REST API search request

```json
GET accounts/_search
{
  "query": {
    "match_phrase": {
      "address": {
        "query": "880 Holmes Lane"
      }
    }
  }
}
```

could be called from *SQL*

```sql
SELECT account_number, address
FROM accounts
WHERE match_phrase(address, '880 Holmes Lane')
```

or *PPL*

```sql
SOURCE=accounts | WHERE match_phrase(address, '880 Holmes Lane') | FIELDS account_number, address
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">address</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">880 Holmes Lane</td>
  </tr>
</tbody>
</table>

#### Simple query string

The `simple_query_string` function maps to the `simple_query_string` query in Energy Logserver. It returns the documents that match a provided text, number, date or boolean value with a given field or fields.
The **^** lets you *boost* certain fields. Boosts are multipliers that weigh matches in one field more heavily than matches in other fields.

##### Syntax

The syntax allows to specify the fields in double quotes, single quotes,  surrounded by backticks, or unquoted. Use star ``"*"`` to search all fields. Star symbol should be quoted.

```sql
simple_query_string([field_expression+], query_expression[, option=<option_value>]*)
```

The weight is optional and is specified after the field name. It could be delimited by the `caret` character -- `^` or by whitespace. Please, refer to examples below:

```sql
simple_query_string(["Tags" ^ 2, 'Title' 3.4, `Body`, Comments ^ 0.3], ...)
simple_query_string(["*"], ...)
```

You can specify the following options for `SIMPLE_QUERY_STRING` in any order:

- `analyze_wildcard`
- `analyzer`
- `auto_generate_synonyms_phrase_query`
- `boost`
- `default_operator`
- `flags`
- `fuzzy_max_expansions`
- `fuzzy_prefix_length`
- `fuzzy_transpositions`
- `lenient`
- `minimum_should_match`
- `quote_field_suffix`

##### *Example* of using `simple_query_string` in SQL and PPL queries:

The REST API search request

```json
GET accounts/_search
{
  "query": {
    "simple_query_string": {
      "query": "Lane Street",
      "fields": [ "address" ],
    }
  }
}
```

could be called from *SQL*

```sql
SELECT account_number, address
FROM accounts
WHERE simple_query_string(['address'], 'Lane Street', default_operator='OR')
```

or from *PPL*

```sql
SOURCE=accounts | WHERE simple_query_string(['address'], 'Lane Street', default_operator='OR') | fields account_number, address
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">account_number</th>
    <th class="tg-ua3b">address</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">1</td>
    <td class="tg-pnl2">880 Holmes Lane</td>
  </tr>
  <tr>
    <td class="tg-pnl2">6</td>
    <td class="tg-pnl2">671 Bristol Street</td>
  </tr>
  <tr>
    <td class="tg-pnl2">13</td>
    <td class="tg-pnl2">789 Madison Street</td>
  </tr>
</tbody>
</table>

#### Match phrase prefix

To search for phrases by given prefix, use `MATCH_PHRASE_PREFIX` function to make a prefix query out of the last term in the query string.

##### Syntax

```sql
match_phrase_prefix(field_expression, query_expression[, option=<option_value>]*)
```

The `MATCH_PHRASE_PREFIX` function lets you specify the following options in any order:

- `analyzer`
- `slop`
- `max_expansions`
- `zero_terms_query`
- `boost`

##### *Example* of using `match_phrase_prefix` in SQL and PPL queries:

The REST API search request

```json
GET accounts/_search
{
  "query": {
    "match_phrase_prefix": {
      "author": {
        "query": "Alexander Mil"
      }
    }
  }
}
```

could be called from *SQL*

```sql
SELECT author, title
FROM books
WHERE match_phrase_prefix(author, 'Alexander Mil')
```

or *PPL*

```sql
source=books | where match_phrase_prefix(author, 'Alexander Mil') | fields author, title
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">author</th>
    <th class="tg-ua3b">title</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">Alan Alexander Milne</td>
    <td class="tg-pnl2">The House at Pooh Corner</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Alan Alexander Milne</td>
    <td class="tg-pnl2">Winnie-the-Pooh</td>
  </tr>
</tbody>
</table>

#### Match boolean prefix

Use the `match_bool_prefix` function to search documents that match text only for a given field prefix.

##### Syntax

```sql
match_bool_prefix(field_expression, query_expression[, option=<option_value>]*)
```

The `MATCH_BOOL_PREFIX` function lets you specify the following options in any order:

- `minimum_should_match`
- `fuzziness`
- `prefix_length`
- `max_expansions`
- `fuzzy_transpositions`
- `fuzzy_rewrite`
- `boost`
- `analyzer`
- `operator`

##### Example of using `match_bool_prefix` in SQL and PPL queries:

The REST API search request

```json
GET accounts/_search
{
  "query": {
    "match_bool_prefix": {
      "address": {
        "query": "Bristol Stre"
      }
    }
  }
}
```

could be called from *SQL*

```sql
SELECT firstname, address
FROM accounts
WHERE match_bool_prefix(address, 'Bristol Stre')
```

or *PPL*

```sql
source=accounts | where match_bool_prefix(address, 'Bristol Stre') | fields firstname, address
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ua3b{border-color:inherit;color:inherit;font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-pnl2{border-color:inherit;color:inherit;text-align:left;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ua3b">firstname</th>
    <th class="tg-ua3b">address</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-pnl2">Hattie</td>
    <td class="tg-pnl2">671 Bristol Street</td>
  </tr>
  <tr>
    <td class="tg-pnl2">Nanette</td>
    <td class="tg-pnl2">789 Madison Street</td>
  </tr>
</tbody>
</table>

## Automation

Automations helps you to interconnect different apps with an API with each other to share and manipulate its data without a single line of code. It is an easy to use, user-friendly and highly customizable module, which uses an intuitive user interface for you to design your unique scenarios very fast.
A automation is a collection of nodes connected together to automate a process.
A automation can be started manually (with the Start node) or by Trigger nodes (e.g. Webhook). When a automation is started, it executes all the active and connected nodes. The automation execution ends when all the nodes have processed their data. You can view your automation executions in the Execution log, which can be helpful for debugging.

![](/media/media/execute_workflow.gif)

**Activating a automation**
Automations that start with a Trigger node or a Webhook node need to be activated in order to be executed. This is done via the Active toggle in the Automation UI.
Active automations enable the Trigger and Webhook nodes to receive data whenever a condition is met (e.g., Monday at 10:00, an update in a Trello board) and in turn trigger the automation execution.
All the newly created automations are deactivated by default.

**Sharing a automation**

Automations are saved in JSON format. You can export your automations as JSON files or import JSON files into your system.
You can export a automation as a JSON file in two ways:

- Download: Click the Download button under the Automation menu in the sidebar. This will download the automation as a JSON file.
- Copy-Paste: Select all the automation nodes in the Automation UI, copy them (Ctrl + c), then paste them (Ctrl + v) in your desired file.
You can import JSON files as automations in two ways:
- Import: Click Import from File or Import from URL under the Automation menu in the sidebar and select the JSON file or paste the link to a automation.
- Copy-Paste: Copy the JSON automation to the clipboard (Ctrl + c) and paste it (Ctrl + v) into the Automation UI.

**Automation settings**

On each automation, it is possible to set some custom settings and overwrite some of the global default settings from the Automation > Settings menu.

![](/media/media/workflow-settings.png)

The following settings are available:

- Error Automation: Select an automation to trigger if the current automation fails.
- Timezone: Sets the timezone to be used in the automation. The Timezone setting is particularly important for the Cron Trigger node.
- Save Data Error Execution: If the execution data of the automation should be saved when the automation fails.
- Save Data Success Execution: If the execution data of the automation should be saved when the automation succeeds.
- Save Manual Executions: If executions started from the Automation UI should be saved.
- Save Execution Progress: If the execution data of each node should be saved. If set to "Yes", the automation resumes from where it stopped in case of an error. However, this might increase latency.
- Timeout Automation: Toggle to enable setting a duration after which the current automation execution should be cancelled.
- Timeout After: Only available when Timeout Automation is enabled. Set the time in hours, minutes, and seconds after which the automation should timeout.

**Failed automations**

If your automation execution fails, you can retry the execution. To retry a failed automation:

1. Open the Executions list from the sidebar.
1. For the automation execution you want to retry, click on the refresh icon under the Status column.
1. Select either of the following options to retry the execution:

  - Retry with currently saved automation: Once you make changes to your automation, you can select this option to execute the automation with the previous execution data.
  - Retry with original automation: If you want to retry the execution without making changes to your automation, you can select this option to retry the execution with the previous execution data.

You can also use the Error Trigger node, which triggers a automation when another automation has an error. Once a automation fails, this node gets details about the failed automation and the errors.

### Connection

A connection establishes a link between nodes to route data through the automation. A connection between two nodes passes data from one node's output to another node's input. Each node can have one or multiple connections.

To create a connection between two nodes, click on the grey dot on the right side of the node and slide the arrow to the grey rectangle on the left side of the following node.

#### Example

An IF node has two connections to different nodes: one for when the statement is true and one for when the statement is false.

![](/media/media/Connection_ifnode.8e006dce.gif)

### Automations List

This section includes the operations for creating and editing automations.

- **New**: Create a new automation
- **Open**: Open the list of saved automations
- **Save**: Save changes to the current automation
- **Save As**: Save the current automation under a new name
- **Rename**: Rename the current automation
- **Delete**: Delete the current automation
- **Download**: Download the current automation as a JSON file
- **Import from URL**: Import a automation from a URL
- **Import from File**: Import a automation from a local file
- **Settings**: View and change the settings of the current automation

### Credentials

This section includes the operations for creating credentials.

Credentials are private pieces of information issued by apps/services to authenticate you as a user and allow you to connect and share information between the app/service and the n8n node.

- **New**: Create new credentials
- **Open**: Open the list of saved credentials

### Executions

This section includes information about your automation executions, each completed run of a automation.

You can enabling logging of your failed, successful, and/or manually selected automations using the Automation > Settings page.

### Node

A node is an entry point for retrieving data, a function to process data, or an exit for sending data. The data process performed by nodes can include filtering, recomposing, and changing data.

There may be one or several nodes for your API, service, or app. By connecting multiple nodes, you can create simple and complex automations. When you add a node to the Editor UI, the node is automatically activated and requires you to configure it (by adding credentials, selecting operations, writing expressions, etc.).

There are three types of nodes:

- Core Nodes
- Regular Nodes
- Trigger Nodes

#### Core nodes

Core nodes are functions or services that can be used to control how automations are run or to provide generic API support.

Use the Start node when you want to manually trigger the automation with the `Execute Automation` button at the bottom of the Editor UI. This way of starting the automation is useful when creating and testing new automations.

If an application you need does not have a dedicated Node yet, you can access the data by using the HTTP Request node or the Webhook node. You can also read about creating nodes and make a node for your desired application.

#### Regular nodes

Regular nodes perform an action, like fetching data or creating an entry in a calendar. Regular nodes are named for the application they represent and are listed under Regular Nodes in the Editor UI.

![](/media/media/Regular_nodes.d3cec3e9.png)

#### Example

A Google Sheets node can be used to retrieve or write data to a Google Sheet.

![](/media/media/Google_sheets.d9ee72a3.png)

#### Trigger nodes

Trigger nodes start automations and supply the initial data.

![](/media/media/Trigger_nodes.5bd536aa.png)

Trigger nodes can be app or core nodes.

- **Core Trigger nodes** start the automation at a specific time, at a time interval, or on a webhook call. For example, to get all users from a Postgres database every 10 minutes, use the Interval Trigger node with the Postgres node.

- **App Trigger nodes** start the automation when an event happens in an app. App Trigger nodes are named like the application they represent followed by "Trigger" and are listed under Trigger Nodes in the Editor. For example, a Telegram trigger node can be used to trigger a automation when a message is sent in a Telegram chat.

![](/media/media/telegram_trigger.fae8dcd9.png)

#### Node settings

Nodes come with global **operations** and **settings**, as well as app-specific **parameters** that can be configured.

#### Operations

The node operations are illustrated with icons that appear on top of the node when you hover on it:

- **Delete**: Remove the selected node from the automation
- **Pause**: Deactivate the selected node
- **Copy**: Duplicate the selected node
- **Play**: Run the selected node

![](/media/media/Node_settings.36ddf764.gif)

To access the node parameters and settings, double-click on the node.

#### Parameters

The node parameters allow you to define the operations the node should perform. Find the available parameters of each node in the node reference.

#### Settings

The node settings allow you to configure the look and execution of the node. The following options are available:

- **Notes**: Optional note to save with the node
- **Display note in flow**: If active, the note above will be displayed in the automation as a subtitle
- **Node Color**: The color of the node in the automation
- **Always Output Data**: If active, the node will return an empty item even if the node returns no data during an initial execution. Be careful setting this on IF nodes, as it could cause an infinite loop.
- **Execute Once**: If active, the node executes only once, with data from the first item it receives.
- **Retry On Fail**: If active, the node tries to execute a failed attempt multiple times until it succeeds
- **Continue On Fail**: If active, the automation continues even if the execution of the node fails. When this happens, the node passes along input data from previous nodes, so the automation should account for unexpected output data.

![](/media/media/Node_parameters.090b2d35.gif)

If a node is not correctly configured or is missing some required information, a **warning sign** is displayed on the top right corner of the node. To see what parameters are incorrect, double-click on the node and have a look at fields marked with red and the error message displayed in the respective warning symbol.

![](/media/media/Node_error.e189f05d.gif)

### How to filter events

You can do it in multiple ways. You can use those nodes:

- IF
- Switch
- Spreadsheet File (a lot of conditions - advanced)

#### Example If usage

If you receive messages from Logstash then you have fields like host.name. You can use if condition to filter known host.

1. Create If node
2. Click Add condition
3. From dropdown menu select String
4. As Value 1 type or select a field which you want use. In this example we use expression `{{ $json["host"]["name"] }}`
5. As Value 2 type host name which you want to process. In this example we use paloalto.paseries.test
6. Next you can select any other node for further process filtered message.

#### Example Case usage

1. Create Case node
2. Select Rules on Mode
3. Select String on Data Type
4. As Value 1 type or select a field which you want use. In this example we use expression `{{ $json["host"]["name"] }}`
5. Click Add Routing Rule
6. As Value 2 type host name which you want to process. In this example, we use paloalto.paseries.test
7. As Output type 0.

You can add multiple conditions. On one node you can add 3 conditions if you need more then add to latest output next node and select this node as Fallback Output.

#### IF

The IF node is used to split a workflow conditionally based on comparison operations.

#### Node Reference

You can add comparison conditions using the Add Condition dropdown. Conditions can be created based on the data type, the available comparison operations vary for each data type.

Boolean

- Equal
- Not Equal
- Number

Smaller

- Smaller Equal
- Equal
- Not Equal
- Larger
- Larger Equal
- Is Empty

String

- Contains
- Equal
- Not Contains
- Not Equal
- Regex
- Is Empty

You can choose to split a workflow when any of the specified conditions are met, or only when all the specified conditions are met using the options in the Combine dropdown list.

#### Switch

The Switch node is used to route a workflow conditionally based on comparison operations. It is similar to the IF node, but supports up to four conditional routes.

#### Node Reference

Mode: This dropdown is used to select whether the conditions will be defined as rules in the node, or as an expression, programmatically.

You can add comparison conditions using the Add Routing Rule dropdown. Conditions can be created based on the data type. The available comparison operations vary for each data type.

Boolean

- Equal
- Not Equal

Number

- Smaller
- Smaller Equal
- Equal
- Not Equal
- Larger
- Larger Equal

String

- Contains
- Equal
- Not Contains
- Not Equal
- Regex

You can route a workflow when none of the specified conditions are met using Fallback Output dropdown list.

#### Spreadsheet File

The Spreadsheet File node is used to access data from spreadsheet files.

#### Basic Operations

- Read from file
- Write to file

#### Node Reference

When writing to a spreadsheet file, the File Format field can be used to specify the format of the file to save the data as.

File Format

- CSV (Comma-separated values)
- HTML (HTML Table)
- ODS (OpenDocument Spreadsheet)
- RTF (Rich Text Format)
- XLS (Excel)
- XLSX (Excel)

Binary Property field: Name of the binary property in which to save the binary data of the spreadsheet file.

Options

- Sheet Name field: This field specifies the name of the sheet from which the data should be read or written to.
- Read As String field: This toggle enables you to parse all input data as strings.
- RAW Data field: This toggle enables you to skip the parsing of data.
- File Name field: This field can be used to specify a custom file name when writing a spreadsheet file to disk.

### Automation integration nodes

To boost your automation you can connect with widely external nodes.

List of automation nodes:

- Action Network
- Activation Trigger
- ActiveCampaign
- ActiveCampaign Trigger
- Acuity Scheduling Trigger
- Affinity
- Affinity Trigger
- Agile CRM
- Airtable
- Airtable Trigger
- AMQP Sender
- AMQP Trigger
- APITemplate.io
- Asana
- Asana Trigger
- Automizy
- Autopilot
- Autopilot Trigger
- AWS Comprehend
- AWS DynamoDB
- AWS Lambda
- AWS Rekognition
- AWS S3
- AWS SES
- AWS SNS
- AWS SNS Trigger
- AWS SQS
- AWS Textract
- AWS Transcribe
- Bannerbear
- Baserow
- Beeminder
- Bitbucket Trigger
- Bitly
- Bitwarden
- Box
- Box Trigger
- Brandfetch
- Bubble
- Calendly Trigger
- Chargebee
- Chargebee Trigger
- CircleCI
- Clearbit
- ClickUp
- ClickUp Trigger
- Clockify
- Clockify Trigger
- Cockpit
- Coda
- CoinGecko
- Compression
- Contentful
- ConvertKit
- ConvertKit Trigger
- Copper
- Copper Trigger
- Cortex
- CrateDB
- Cron
- Crypto
- Customer Datastore (n8n training)
- Customer Messenger (n8n training)
- Customer Messenger (n8n training)
- Customer.io
- Customer.io Trigger
- Date & Time
- DeepL
- Demio
- DHL
- Discord
- Discourse
- Disqus
- Drift
- Dropbox
- Dropcontact
- E-goi
- Edit Image
- Elastic Security
- Elasticsearch
- EmailReadImap
- Emelia
- Emelia Trigger
- ERPNext
- Error Trigger
- Eventbrite Trigger
- Execute Command
- Execute Automation
- Facebook Graph API
- Facebook Trigger
- Figma Trigger (Beta)
- FileMaker
- Flow
- Flow Trigger
- Form.io Trigger
- Formstack Trigger
- Freshdesk
- Freshservice
- Freshworks CRM
- FTP
- Function
- Function Item
- G Suite Admin
- GetResponse
- GetResponse Trigger
- Ghost
- Git
- GitHub
- Github Trigger
- GitLab
- GitLab Trigger
- Gmail
- Google Analytics
- Google BigQuery
- Google Books
- Google Calendar
- Google Calendar Trigger
- Google Cloud Firestore
- Google Cloud Natural Language
- Google Cloud Realtime Database
- Google Contacts
- Google Docs
- Google Drive
- Google Drive Trigger
- Google Perspective
- Google Sheets
- Google Slides
- Google Tasks
- Google Translate
- Gotify
- GoToWebinar
- Grafana
- GraphQL
- Grist
- Gumroad Trigger
- Hacker News
- Harvest
- HelpScout
- HelpScout Trigger
- Home Assistant
- HTML Extract
- HTTP Request
- HubSpot
- HubSpot Trigger
- Humantic AI
- Hunter
- iCalendar
- IF
- Intercom
- Interval
- Invoice Ninja
- Invoice Ninja Trigger
- Item Lists
- Iterable
- Jira Software
- Jira Trigger
- JotForm Trigger
- Kafka
- Kafka Trigger
- Keap
- Keap Trigger
- Kitemaker
- Lemlist
- Lemlist Trigger
- Line
- LingvaNex
- LinkedIn
- Local File Trigger
- Magento 2
- Mailcheck
- Mailchimp
- Mailchimp Trigger
- MailerLite
- MailerLite Trigger
- Mailgun
- Mailjet
- Mailjet Trigger
- Mandrill
- Marketstack
- Matrix
- Mattermost
- Mautic
- Mautic Trigger
- Medium
- Merge
- MessageBird
- Microsoft Dynamics CRM
- Microsoft Excel
- Microsoft OneDrive
- Microsoft Outlook
- Microsoft SQL
- Microsoft Teams
- Microsoft To Do
- Mindee
- MISP
- Mocean
- Monday.com
- MongoDB
- Monica CRM
- Move Binary Data
- MQTT
- MQTT Trigger
- MSG91
- MySQL
- n8n Trigger
- NASA
- Netlify
- Netlify Trigger
- Nextcloud
- No Operation, do nothing
- NocoDB
- Notion (Beta)
- Notion Trigger (Beta)
- One Simple API
- OpenThesaurus
- OpenWeatherMap
- Orbit
- Oura
- Paddle
- PagerDuty
- PayPal
- PayPal Trigger
- Peekalink
- Phantombuster
- Philips Hue
- Pipedrive
- Pipedrive Trigger
- Plivo
- Postgres
- PostHog
- Postmark Trigger
- ProfitWell
- Pushbullet
- Pushcut
- Pushcut Trigger
- Pushover
- QuestDB
- Quick Base
- QuickBooks Online
- RabbitMQ
- RabbitMQ Trigger
- Raindrop
- Read Binary File
- Read Binary Files
- Read PDF
- Reddit
- Redis
- Rename Keys
- Respond to Webhook
- RocketChat
- RSS Read
- Rundeck
- S3
- Salesforce
- Salesmate
- SeaTable
- SeaTable Trigger
- SecurityScorecard
- Segment
- Send Email
- SendGrid
- Sendy
- Sentry.io
- ServiceNow
- Set
- Shopify
- Shopify Trigger
- SIGNL4
- Slack
- sms77
- Snowflake
- Split In Batches
- Splunk
- Spontit
- Spotify
- Spreadsheet File
- SSE Trigger
- SSH
- Stackby
- Start
- Stop and Error
- Storyblok
- Strapi
- Strava
- Strava Trigger
- Stripe
- Stripe Trigger
- SurveyMonkey Trigger
- Switch
- Taiga
- Taiga Trigger
- Tapfiliate
- Telegram
- Telegram Trigger
- TheHive
- TheHive Trigger
- TimescaleDB
- Todoist
- Toggl Trigger
- TravisCI
- Trello
- Trello Trigger
- Twake
- Twilio
- Twist
- Twitter
- Typeform Trigger
- Unleashed Software
- Uplead
- uProc
- UptimeRobot
- urlscan.io
- Vero
- Vonage
- Wait
- Webex by Cisco
- Webex by Cisco Trigger
- Webflow
- Webflow Trigger
- Webhook
- Wekan
- Wise
- Wise Trigger
- WooCommerce
- WooCommerce Trigger
- Wordpress
- Workable Trigger
- Automation Trigger
- Write Binary File
- Wufoo Trigger
- Xero
- XML
- Yourls
- YouTube
- Zendesk
- Zendesk Trigger
- Zoho CRM
- Zoom
- Zulip

## Cooperation of logserver and antivirus program

Energy Logserver utilizes a high disk I/O throughput for its typical indexing tasks. Specifically, disk write operations are highly intensive. These I/O writes can conflict with any product that installs a driver intermediary between our software and the operating system, such as antivirus software that scans when the application accesses mass storage.

When running Energy Logserver or its component on a computer with antivirus software installed, it is necessary to exclude all Energy software processes, including directories such as the installation directory, from any kind of scanning when accessing application resources.
	
**Directories to exclude:**
-        /usr/share/elasticsearch
- 		 /usr/share/kibana
- 		 /usr/share/logstash
- 		 /var/lib/kibana
- 		 Data directory (default /var/lib/elasticsearch )
- 		 /etc/elasticsearch
- 		 /etc/kibana
- 		 /etc/logstash
- 		 /var/log/elasticsearch
- 		 /var/log/kibana
- 		 /var/log/logstash
- 		 Kibana archive directory (default /usr/share/kibana/plugins/archive/archives/ )
- 		 /opt/ai
- 		 /opt/alert
- 		 /opt/cerebro
- 		 /opt/e-doc
- 		 /opt/intelligence
- 		 /opt/license-service
- 		 /opt/plugins
- 		 /opt/skimmer
- 		 /opt/wiki
- 		 Elasticsearch temp directory
- 		 /var/ossec
		
**Exclude processes related to :**
	
- 		 Elasticsearch
- 		 java
- 		 Logstash
- 		 node
- 		 kibana
- 	     alert
- 		 License-service
- 		 Wazuh-manager
- 		 Cerebro
- 		 E-doc
- 		 Intelligence