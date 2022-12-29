# User Manual

## Introduction

Energy Logserver is innovation solution allowing for centralize IT
systems events. It allows for an immediately review, analyze and
reporting of system logs - the amount of data does not matter. 
Energy Logserver is a response to the huge demand for storage and
analysis of the large amounts of data from IT systems. 
Energy Logserver is innovation solution that responds to the need of
effectively processing large amounts of data coming from IT
environments of today's organizations. Based on the open-source
project Elasticsearch valued on the marked, we have created an
efficient solution with powerful data storage and searching
capabilities. The System has been enriched of functionality that
ensures the security of stored information, verification of users,
data correlation and visualization, alerting and reporting.

![](/media/media/image2_js.png) 

Energy Logserver project was created to centralize events of all IT
areas in the organization. We focused on creating a tool that
functionality is most expected by IT departments. Because an effective
licensing model has been applied, the solution can be implemented in
the scope expected by the customer even with very large volume of
data. At the same time, the innovation architecture allows for
servicing a large portion of data, which cannot be dedicated to
solution with limited scalability.

### Elasticsearch ##

Elasticsearch is a NoSQL database solution that is the heart of our
system. Text information send to the system, application and system
logs are processed by Logstash filters and directed to Elasticsearch.
This storage environment creates, based on the received data, their
respective layout in a binary form, called a data index. The Index is
kept on Elasticsearch nodes, implementing the appropriate assumptions
from the configuration, such as:

- Replication index between nodes,
- Distribution index between nodes.

The Elasticsearch environment consists of nodes:

- Data node - responsible for storing documents in indexes,
- Master node - responsible for the supervisions of nodes,
- Client node - responsible for cooperation with the client.

Data, Master and Client elements are found even in the smallest
Elasticsearch installations, therefore often the environment is
referred to as a cluster, regardless of the number of nodes
configured. Within the cluster, Elasticsearch decides which data
portions are held on a specific node.

Index layout, their name, set of fields is arbitrary and depends on
the form of system usage. It is common practice to put data of a
similar nature to the same type of index that has a permanent first
part of the name. The second part of the name often remains the date
the index was created, which in practice means that the new index is
created every day. This practice, however, is conventional and every
index can have its own rotation convention, name convention,
construction scheme and its own set of other features. As a result of
passing document through the Logstash engine, each entry receive a
data field, which allow to work witch data in relations to
time. 

The Indexes are built with elementary part called shards. It is good
practice to create Indexes with the number of shards that is the
multiple of the Elasticsearch data nodes number. Elasticsearch in 7.x version has a new feature called Sequence IDs that guarantee more successful and efficient shard recovery.

Elasticsearch use the *mapping* to describes the fields or properties that documents of that type may have. Elasticsearch in 7.x version restrict indices to a single type.

### Kibana

Kibana lets you visualize your Elasticsearch data and navigate the Elastic Stack. Kibana gives you the freedom to select the way you give
shape to your data. And you don’t always have to know what you're looking for. Kibana core ships with the classics: histograms, line
graphs, pie charts, sunbursts, and more. Plus, you can use Vega grammar to design your own visualizations. All leverage the full
aggregation capabilities of Elasticsearch.  Perform advanced time series analysis on your Elasticsearch data with our curated time series
UIs. Describe queries, transformations, and visualizations with powerful, easy-to-learn expressions. Kibana 7.x has two new feature - a new "Full-screen" mode to viewing dashboards, and new the "Dashboard-only" mode which enables administrators to share dashboards safely.

### Logstash
Logstash is an open source data collection engine with real-time pipelining capabilities. Logstash can dynamically unify data from
disparate sources and normalize the data into destinations of your choice. Cleanse and democratize all your data for diverse advanced
downstream analytics and visualization use cases.

While Logstash originally drove innovation in log collection, its capabilities extend well beyond that use case. Any type of event can be
enriched and transformed with a broad array of input, filter, and output plugins, with many native codecs further simplifying the
ingestion process. Logstash accelerates your insights by harnessing a greater volume and variety of data.

Logstash 7.x version supports native support for multiple pipelines. These pipelines are defined in a *pipelines.yml* file which is loaded by default.
Users will be able to manage multiple pipelines within Kibana. This solution uses Elasticsearch to store pipeline configurations and allows for on-the-fly reconfiguration of Logstash pipelines.

### ELK
"ELK" is the acronym for three open source projects: Elasticsearch, Logstash, and Kibana. Elasticsearch is a search and analytics 
engine. Logstash is a server‑side data processing pipeline that ingests data from multiple sources simultaneously, transforms it, 
and then sends it to a "stash" like Elasticsearch. Kibana lets users visualize data with charts and graphs in Elasticsearch.
The Elastic Stack is the next evolution of the ELK Stack.

## Data source

Where does the data come from?

Energy Logserver is a solution allowing effective data processing
from the IT environment that exists in the organization.

The Elsasticsearch engine allows building a database in witch large
amounts of data are stored in ordered indexes. The Logstash module is
responsible for load data into Indexes, whose function is to collect
data on specific tcp/udp ports, filter them, normalize them and place
them in the appropriate index. Additional plugins, that we can use in
Logstash reinforce the work of the module, increase its efficiency,
enabling the module to quick interpret data and parse it.

Below is an example of several of the many available Logstash plugins:

**exec** - receive output of the shell function as an event;

**imap** - read email from IMAP servers;

**jdbc** - create events based on JDC data;

**jms** - create events from Jms broker;

Both Elasticsearch and Logstash are free Open-Source solutions.

More information about Elasticsearch module can be find at:
[https://github.com/elastic/elasticsearch](https://github.com/elastic/elasticsearch)

List of available Logstash plugins:
[https://github.com/elastic/logstash-docs/tree/master/docs/plugins](https://github.com/elastic/logstash-docs/tree/master/docs/plugins)

## System services

For proper operation Energy Logserver requires starting the following system services:

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

		systemctl start logstash.service

   we can check its status with a command:

	systemctl status logstash.service

![](/media/media/image88.PNG)

## First login

If you log in to Energy Logserver for the first time, you must
specify the Index to be searched. We have the option of entering the
name of your index, indicate a specific index from a given day, or
using the asterix (\*) to indicate all of them matching a specific
index pattern. Therefore, to start working with Energy Logserver
application, we log in to it (by default the user:
logserver/password:logserver).

![](/media/media/image3.png)

After logging in to the application click the button "Set up index pattern" to add new index patter in Kibana: 

![](/media/media/image3_js.png)

In the "Index pattern" field enter the name of the index or index pattern (after
confirming that the index or sets of indexes exists) and click "Next step" button.

![](/media/media/image4.png)

In the next step, from  drop down menu select the "Time filter field name", after witch individual event (events) should be sorter. By default the *timestamp* is set, which is the time of occurrence of the event, but depending of the preferences. It may also be the time of the indexing or other selected
based on the fields indicate on the event.

![](/media/media/image4_js.png)

At any time, you can add more indexes or index patters by going to the
main tab select „Management" and next select „Index Patterns".

## Index selection

After login into Energy Logserver you will going to „Discover" tab,
where you can interactively explore your data. You have access to 
every document in every index that matches the selected index patterns.

If you want to change selected index, drop down menu with
the name of the current object in the left panel. Clicking on the
object from the expanded list of previously create index patterns,
will change the searched index.

![](/media/media/image6.png)


### Index rollover

Using the rollover function, you can make changes to removing documents from the *audit*, *.agents*, *alert\** indexes. 

You can configure the rollover by going to the *Config* module, then clicking the *Settings* tab, go to the *Index rollover settings* section and select click *Configure* button:

![](/media/media/image167.png)

You can set the following retention parameters for the above indexes:

- Maximum size (GB);
- Maximum age (h);
- Maximum number of documents.

## Discovery

### Time settings and refresh


In the upper right corner there is a section in which it defines the
range of time that Energy Logserver will search in terms of conditions contained in
the search bar. The default value is the last 15 minutes.

![](/media/media/image7.png)

After clicking this selection, we can adjust the scope of search by
selecting one of the three tabs in the drop-down window:

- **Quick**: contain several predefined ranges that should be clicked.
- **Relative**: in this windows specify the day from which Energy Logserver should search for data.
- **Absolute**: using two calendars we define the time range for which the search results are to be returned.

![](/media/media/image8.png)

### Fields

Energy Logserver in the body of searched events, it recognize fields
that can be used to created more precision queries. The extracted
fields are visible in the left panel. They are divided on three types: 
timestamp, marked on clock icon 
![](/media/media/image9.png); text, marked with the letter "t"
![](/media/media/image10.png) and digital, marked witch hashtag
![](/media/media/image11.png).

Pointing to them and clicking on icon
![](/media/media/image12.png), they are automatically transferred to
the „Selected Fields" column and in the place of events a table with 
selected columns is created on regular basis. In the "Selected Fields" 
selection you can also delete specific fields from the table by clicking
![](/media/media/image13.png) on the selected element.

![](/media/media/image14_js.png)

### Filtering and syntax building

We use the query bar to search interesting events. For example, after
entering the word „error", all events that contain the word will be
displayed, additional highlighting them with an yellow background.

![](/media/media/image15_js.png)

#### Syntax
Fields can be used in the similar way by defining conditions that
interesting us. The syntax of such queries is:

	<fields_name:<fields_value>

Example:

	status:500

This query will display all events that contain the „status" fields 
with a value of 500.

#### Filters
The field value does not have to be a single, specific value. For
digital fields we can specify range in the following scheme:

	<fields_name:[<range_from TO <range_to] 

Example: 

	status:[500 TO 599]

This query will return events with status fields that are in the 
range 500 to 599.

#### Operators
The search language used in Energy Logserver allows to you use logical operators
„AND", „OR" and „NOT", which are key and necessary to build more
complex queries.

-   **AND** is used to combined expressions, e.g. „error AND „access
   denied". If an event contain only one expression or the words
   error and denied but not the word access, then it will not be
   displayed.

-   **OR** is used to search for the events that contain one OR other
   expression, e.g. „status:500" OR "denied". This query will display
   events that contain word „denied" or status field value of 500. Energy Logserver
   uses this operator by default, so query „status:500" "denied" would
   return the same results.

-   **NOT** is used to exclude the following expression e.g. „status:[500
   TO 599] NOT status:505" will display all events that have a status
   fields, and the value of the field is between 500 and 599 but will
   eliminate from the result events whose status field value is exactly 505.

-   **The above methods** can be combined with each other by building even
   more complex queries. Understanding how they work and joining it, is
   the basis for effective searching and full use of Energy Logserver.
   
   Example of query built from connected logical operations:
   
	status:[500 TO 599] AND („access denied" OR error) NOT status:505

Returns in the results all events for which the value of status fields
are in the range of 500 to 599, simultaneously contain the word
„access denied" or „error", omitting those events for which the status
field value is 505.

#### Wildcards

Wildcard searches can be run on individual terms, using ? to replace a single character, and * to replace zero or more characters:

`qu?ck bro*`

Be aware that wildcard queries can use an enormous amount of memory and perform very badly — just think how many terms need to be queried to match the query string "a* b* c*".

#### Regular expressions

Regular expression patterns can be embedded in the query string by wrapping them in forward-slashes ("/"):

`name:/joh?n(ath[oa]n)/`

The supported regular expression syntax is explained in Regular expression syntax [https://www.elastic.co/guide/en/elasticsearch/reference/8.3/regexp-syntax.html](https://www.elastic.co/guide/en/elasticsearch/reference/8.3/regexp-syntax.html)

#### Fuzziness

You can run fuzzy queries using the ~ operator:

`quikc~ brwn~ foks~`

For these queries, the query string is normalized. If present, only certain filters from the analyzer are applied. For a list of applicable filters, see Normalizers.

The query uses the Damerau-Levenshtein distance to find all terms with a maximum of two changes, where a change is the insertion, deletion or substitution of a single character, or transposition of two adjacent characters.

The default edit distance is 2, but an edit distance of 1 should be sufficient to catch 80% of all human misspellings. It can be specified as:

`quikc~1`

#### Proximity searches

While a phrase query (eg "john smith") expects all of the terms in exactly the same order, a proximity query allows the specified words to be further apart or in a different order. In the same way that fuzzy queries can specify a maximum edit distance for characters in a word, a proximity search allows us to specify a maximum edit distance of words in a phrase:

`"fox quick"~5`

The closer the text in a field is to the original order specified in the query string, the more relevant that document is considered to be. When compared to the above example query, the phrase "quick fox" would be considered more relevant than "quick brown fox".

#### Ranges

Ranges can be specified for date, numeric or string fields. Inclusive ranges are specified with square brackets [min TO max] and exclusive ranges with curly brackets {min TO max}.

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

    ```
    age:>10
    age:>=10
    age:<10
    age:<=10
    ```

### Saving and deleting queries

Saving queries enables you to reload and use them in the future. 

#### Save query
To save query, click on the "Save" button under on the query bar:

![](/media/media/image16.png) 

This will bring up a window in which we give the query a name and then
click the button ![](/media/media/image17.png).

![](/media/media/image18_js.png)

Saved queries can be opened by going to „Open" from the main menu
at the top of the page, and select saved search from the search list:

![](/media/media/image19.png)

Additional you can use "Saved Searchers Filter.." to filter the search list.

#### Open query
To open a saved query from the search list, you can click on the name of the query 
you are interested in.

After clicking on the icon 
![](/media/media/image21.png) on the name of the saved query and chose 
"Edit Query DSL", we will gain access to the advanced editing mode, 
so that we can change the query on at a lower level. 

![](/media/media/image21.png)

It is a powerful tool designed for advanced users, designed to modify 
the query and the way it is presented by Energy Logserver.

#### Delete query
To delete a saved query, open it from the search list, and
then click on the button ![](/media/media/image23.png) . 

If you want delete many saved queries simultaneously go to the "Management Object"
 -> "Saved Object" -> "Searches" select it in the list (the icon ![](/media/media/image22.png) 
to the left of the query name), and then click "Delete" button. 

![](/media/media/image24_js.png)

From this level, you can also export saved queries in the same way. To
do this, you need to click on
![](/media/media/image25.png) and choose the save location. The file
will be saved in .JSON format. If you then want to import such a file to
Energy Logserver, click on button
![](/media/media/image26.png), at the top of the page and select the
desired file.

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
.kbnDocTableCell__dataField 
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
To create visualization, go to the „Visualize" tab from the main menu.
A new page will be appearing where you can create or load
visualization.

#### Load
To load previously created and saved visualization, you
must select it from the list.

![](/media/media/image89.PNG)

In order to create a new visualization,
you should choose the preferred method of data presentation.

![](/media/media/image89_js.PNG)

Next, specify whether the created visualization will be based on a new or
previously saved query. If on new one, select the index whose
visualization should concern. If visualization is created from a saved
query, you just need to select the appropriate query from the list, or
(if there are many saved searches) search for them by name.

![](/media/media/image90.PNG)

### Vizualization types

Before the data visualization will be created, first you have to
choose the presentation method from an existing list. Currently there
are five groups of visualization types. Each of them serves different purposes.
If you want to see only the current number of products
sold, it is best to choose „Metric", which presents one value.

![](/media/media/image27_js.png)

However, if we would like to see user activity trends on pages in
different hour and days, a better choice will be „Area chart", which
displays a chart with time division.

![](/media/media/image28_js.png)

The „Markdown widget" views is used to place text e.g. information
about the dashboard, explanations and instruction on how to navigate.
Markdown language was used to format the text (the most popular use is
GitHub). 
More information and instruction can be found at this link:
[https://help.github.com/categories/writing-on-github/](https://help.github.com/categories/writing-on-github/)

### Edit visualization and saving

#### Edititing
Editing a saved visualization enables you to directly modify the object 
definition. You can change the object title, add a description, and modify
the JSON that defines the object properties.
After selecting the index and the method of data presentation, you can enter
the editing mode. This will open a new window with empty
visualization.

![](/media/media/image29_js.png)

At the very top there is a bar of queries that cat be edited
throughout the creation of the visualization. It work in the same way
as in the "Discover" tab, which means searching the raw data, but
instead of the data being displayed, the visualization will be edited.
The following example will be based on the „Area chart". The
visualization modification panel on the left is divided into three tabs:
„Data", "Metric & Axes" and „Panel Settings".

In the „Data" tab, you can modify the elements responsible for which data
and how should be presented. In this tab there are two sectors:
"metrics", in which we set what data should be displayed, and
„buckets" in which we specify how they should be presented. 

Select the Metrics & Axes tab to change the way each individual metric is shown 
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

-   **Current time marker** -- places a vertical line on the graph that
    determines the current time.

-   **Set Y-Axis Extents** -- allows you to set minimum and maximum
    values for the Y axis, which increases the readability of the
    graphs. This is useful, if we know that the data will never be
    less then (the minimum value), or to indicate the goals the
    company (maximum value).

-  **Show Tooltip** -- option for displaying the information window
    under the mouse cursor, after pointing to the point on the graph.
   
   ![](/media/media/image31.png)
   
#### Saving
To save the visualization, click on the "Save" button under on the query bar:
![](/media/media/image16.png)
give it a name and click the button
![](/media/media/image17.png). 

#### Load
To load the visualization, go to the "Management Object"
 -> "Saved Object" -> "Visualizations" select it from the list. From this place, 
we can also go into advanced editing mode. To view of the visualization 
use ![](/media/media/image17_js.png) button.

## Dashboards

Dashboard is a collection of several visualizations or searches.
Depending on how it is build and what visualization it contains, it
can be designed for different teams e.g.: 
- SOC - which is responsible for detecting failures or threats in 
the company; 
- business - which thanks to the listings can determine the popularity
of products and define the strategy of future sales and promotions; 
- managers and directors - who may immediately have access to information
about the performance units or branches. 

#### Create
To create a dashboard from previously saved visualization and queries,
go to the „Dashboard" tab in the main menu. When you open it, a
new page will appear.

![](/media/media/image32.png)

Clicking on the icon "Add" at the top of page select "Visualization" or "Saved Search"
tab.

![](/media/media/image32_js.png)

and selecting a saved query and / or visualization from the list will 
add them to the dashboard. If, there are a large number of saved objects, 
use the bar to search for them by name. 

Elements of the dashboard can be enlarged arbitrarily (by clicking on
the right bottom corner of object and dragging the border) and moving
(by clicking on the title bar of the object and moving it). 

#### Saving 

You may change the time period of your dashboard.

At the upper right hand corner, you may choose the time range of your dashboard.

![](/media/media/image147.png)

Click save and choose the 'Store time with dashboard' if you are editing an existing dashboard. Otherwise, you may choose 'Save as a new dashboard' to create a new dashboard with the new time range.

To save a dashboard, click on the "Save" button to the up of the query bar 
and give it a name. 

#### Load
To load the Dashboard, go to the "Management Object"
 -> "Saved Object" -> "Dashborad" select it from the list. From this place, 
we can also go into advanced editing mode. To view of the visualization 
use ![](/media/media/image17_1_js.png) button.

### Sharing dashboards

The dashboard can be share with other Energy Logserver users as well
as on any page - by placing a snippet of code. Provided that it cans
retrieve information from Energy Logserver.

To do this, create new dashboard or open the saved dashboard and click 
on the "Share" to the top of the page. A window
will appear with generated two URL. The content of the first one "Embaded iframe"
is used to provide the dashboard in the page code, and the second "Link" is a link
that can be passed on to another user. There are two option for each, 
the first is to shorten the length of the link, and second on
copies to clipboard the contest of the given bar.

![](/media/media/image37.png)

### Dashboard drilldown

In discovery tab search for message of  Your interest

![](/media/media/image125.png)

----------

Save Your search

![](/media/media/image126.png)

Check You „Shared link” and copy it

![](/media/media/image127.png)
![](/media/media/image128.png)

**! ATTENTION !** Do not copy „?_g=()” at the end.

----------

Select Alerting module

![](/media/media/image129.png)

----------

Once Alert is created use `ANY` frame to add the following directives:

	Use_kibana4_dashboard: paste Your „shared link” here

`use_kibana_dashboard:` - The name of a Kibana dashboard to link to. Instead of generating a dashboard from a template, Alert can use an existing dashboard. It will set the time range on the dashboard to around the match time, upload it as a temporary dashboard, add a filter to the query_key of the alert if applicable, and put the url to the dashboard in the alert. (Optional, string, no default).

----------

	Kibana4_start_timedelta

`kibana4_start_timedelta:` Defaults to 10 minutes. This option allows you to specify the start time for the generated kibana4 dashboard. This value is added in front of the event. For example,

	`kibana4_start_timedelta: minutes: 2`

----------


	Kibana4_end_timedelta`

`kibana4_end_timedelta:` Defaults to 10 minutes. This option allows you to specify the end time for the generated kibana4 dashboard. This value is added in back of the event. For example,

	kibana4_end_timedelta: minutes: 2

----------
Sample:
![](/media/media/image130.png)


----------
Search for triggered alert in Discovery tab. Use alert* search pattern.

![](/media/media/image131.png)

Refresh the alert that should contain url for the dashboard.
Once available, kibana_dashboard field can be exposed to dashboards giving You a real drill down feature.

### Sound notification

You can use sound notification on dashboard when the new document is coming. To configure sound notification on dashboard use the following steps: 
- create and save the `Saved search` in `Discovery` module;
- open the proper dashboard and `add` the previously created `Saved search`;
- exit form dashboard editing mode by click on the `save` button;
- click on three small square on the previously added object and select `Play audio`:
![](/media/media/image162.png)
- select the sound file in the mp3 format from your local disk and click OK:
![](/media/media/image163.png)
- on the dashboard set the automatically refresh data. for example every 5 seconds:
![](/media/media/image164.png)
-  when new document will coming the sound will playing.# Reports #


Energy Logserver contains a module for creating reports that can be
run cyclically and contain only interesting data, e.g. a weekly sales
report.

To go to the reports windows, select to tiles icon from the main menu
bar, and then go to the „Reports" icon (To go back, go to the „Search"
icon).

![](/media/media/image38_js8.png)

## Reports

### CSV Report

To export data to CSV Report click the ***Reports*** icon, you immediately go 
to the first tab - ***Export Data***

In this tab we have the opportunity to specify the source from which
we want to do export. It can be an index pattern. After selecting it,
we confirm the selection with the Submit button and a report is
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

When the process of generating the report (Status:Completed) is
finished, we can download it (Download button) or delete (Delete
button). The downloaded report in the form of \*.csv file can be
opened in the browser or saved to the disk.

![](/media/media/image44_js.png)

In this tab, the downloaded data has a format that we can import into
other systems for further analysis.

### PDF Report

In the Export Dashboard tab we have the possibility to create
graphic reports in PDF files. 
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
2. Add the new task name in 'Task Name' field,
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
which from Dashboard template can generate a report at time intervals. 
To do this goes to the Schedule Export Dashboard tab.

![](/media/media/image48_js.png)

Scheduler Report (Schedule Export Dashboard)

In this tab mark the saved Dashboard.

![](/media/media/image49_js.png)

*Note: The default time period of the dashboard is last 15 minutes.*

*Please refer to **Discovery > Time settings and refresh** to change the time period of your dashboard.*

In the Email Topic field, enter the Message title, in the Email field
enter the email address to which the report should be sent. From
drop-down list choose at what frequency you want the report to be generated and sent. 
The action configured in this way is confirmed with the Submit button.

![](/media/media/image50_js.png)

The defined action goes to the list and will generate a report to the
e-mail address, with the cycle we set, until we cannot cancel it with
the Cancel button.

![](/media/media/image51_js.png)

## User roles and object management

### Users, roles and settings

Energy Logserver allows to you manage users and permission for
indexes and methods used by them. To do this click the "Config" button from the main menu bar.

![](/media/media/image38_js.png)

A new window will appear with three main tabs: „User Management",
„Settings" and „License Info".

From the „User Management" level we have access to the following
possibilities: Creating a user in „Create User", displaying users in
„User List", creating new roles in „Create roles" and displaying
existing roles in „List Role".

### Creating a User (Create User)

#### Creating user
To create a new user click on the Config icon and you immediately
enter the administration panel, where the first tab is to create
a new user (**Create User**).

![](/media/media/image52_js.png)

In the wizard that opens, we enter a unique username (Username field),
password for the user (field Password) and assign a role (field Role). 
In this field we have the option of assigning more than one role. 
Until we select role in the Roles field, the Default Role field 
remains empty. When we mark several roles, these roles appear in 
the Default Role field. In this field we have the opportunity to 
indicate which role for a new user will be the default role with 
which the user will be associated in the first place when logging in. 
The default role field has one more important task - it binds all 
users with the field / role set in one group. When one of the users 
of this group create Visualization or Dashboard it will be available 
to other users from this role(group). Creating the account is confirmed 
with the Submit button.

### User's modification and deletion, (User List)

Once we have created users, we can display their list. We do it in
next tab (**User List**).

![](/media/media/image53_js.png)

In this view, we get a list of user account with assigned roles and we
have two buttons: Delete and Update. The first of these is ability to
delete a user account. Under the Update button is a drop-down menu in
which we can change the previous password to a new one (New password),
change the password (Re-enter Ne Password), change the previously
assigned roles (Roles), to other (we can take the role assigned
earlier and give a new one, extend user permissions with new roles).
The introduced changes are confirmed with the Submit button.

We can also see current user setting and clicking the Update button 
collapses the previously expanded menu.

### Create, modify and delete a role (Create Role), (Role List) 

In the Create Role tab we can define a new role with permissions that 
we assign to a pattern or several index patterns.

![](/media/media/image54_js.png)

In example, we use the syslog2\* index pattern. We give this name
in the Paths field. We can provide one or more index patterns, their
names should be separated by a comma. In the next Methods field, we
select one or many methods that will be assigned to the role. Available
methods:

- PUT - sends data to the server
- POST - sends a request to the server for a change
- DELETE - deletes the index / document
- GET - gets information about the index /document
- HEAD - is used to check if the index /document exists

In the role field, enter the unique name of the role. We confirm addition
of a new role with the Submit button. To see if a new role has been added, 
go to the net Role List tab.

![](/media/media/image55_js.png)

As we can see, the new role has been added to the list. With the
Delete button we have the option of deleting it, while under the
Update button we have a drop-down menu thanks to which we can add or
remove an index pattern and add or remove a method. When we want to
confirm the changes, we choose the Submit button. Pressing the Update
button again will close the menu.

Fresh installation of the application have sewn solid roles which
granting user special rights:

- admin - this role gives unlimited permissions to administer / manage
the application
- alert - a role for users who want to see the Alert module
- kibana - a role for users who want to see the application GUI
- Intelligence - a role for users who are to see the Intelligence moduleObject access permissions (Objects permissions)

In the User Manager tab we can parameterize access to the newly 
created role as well as existing roles. In this tab we can indicate 
to which object in the application the role has access.

Example:

In the Role List tab we have a role called **sys2**, it refers
to all index patterns beginning with syslog\* and the methods get,
post, delete, put and head are assigned.

![](/media/media/image56_js.png)

When we go to the Object permission tab, we have the option to choose
the sys2 role in the drop-down list choose a role:

![](/media/media/image57_js.png)

After selecting, we can see that we already have access to the objects:
two index patterns syslog2\* and Energy Logserver-\* and on dashboard Windows Events. 
There are also appropriate read or updates permissions.

![](/media/media/image58_js.png)

From the list we have the opportunity to choose another object that we
can add to the role. We have the ability to quickly find this object
in the search engine (Find) and narrowing the object class in
the drop-down field "Select object type". The object type are associated
with saved previously documents in the sections Dashboard, Index pattern, 
Search and Visualization. 
By buttons ![](/media/media/image59.png) we have the ability to add or remove or
object, and Save button to save the selection.

### Default user and passwords

The table below contains built-in user accounts and default passwords:

	|Address                |User         |Password     |Role         |Description                                     |Usage          |
	|-----------------------|-------------|-------------|-------------|------------------------------------------------|---------------|
	|https://localhost:5601	|logserver    |logserver    |logserver    |A built-in *superuser* account                  |               |
	|                       |alert        |alert        |alert        |A built-in account for  the Alert module        |               |  
	|                       |intelligence |intelligece  |intelligence |A built-in account for the Intelligence module  | authorizing communication with elasticsearch server | 
	|                       |scheduler    |scheduler    |scheduler    |A built-in account for the Scheduler module     |
	|                       |logstash     |logstash     |logstash     |A built-in account for authorized comuunication form Logstash |
	|                       |cerebro      |     |system acconut only     |A built-in account for authorized comuunication from Cerebro moudule |

### Changing password for the system account

After you change password for one of the system account ( alert, intelligence, logserver, scheduler), you must to do appropriate changes in the application files.

1. Account **Logserver**

	- Update */etc/kibana/kibana.yml*
    
    ```bash
    vi /etc/kibana/kibana.yml
    elasticsearch.password: new_logserver_passowrd
    elastfilter.password: "new_logserver_password"
    cerebro.password: "new_logserver_password"
    ```

  - Update passowrd in */opt/license-service/license-service.conf* file:
    
    ```bash
    elasticsearch_connection:
    hosts: ["10.4.3.185:9200"]
    
    username: logserver
    password: "new_logserver_password"
    
    https: true
    ```

  - Update password in *curator* configuration file: */usr/share/kibana/curator/curator.yml*

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

   - Update the Logstash pipeline configuration files (*.conf) in output sections:

     ```bash
     vi /etc/logstash/conf.d/*.conf
     elasticsearch {
     	hosts => ["localhost:9200"]
     	index => "syslog-%{+YYYY.MM}"
     	user => "logstash"
     	password => "new_password"
     }
     ```


### Module Access

You can restrict access to specific modules for a user role. For example: the user can only use the Discovery, Alert and Cerebro modules, the other modules should be inaccessible to the user.

You can do this by editing the roles in the `Role List` and selecting the application from the `Apps` list. After saving, the user has access only to specific modules.

![](/media/media/image165.png)

### Manage API keys

The system allows you to manage, create and delete API access keys from the level of the GUI management application. 

Examples of implementation:

1. From the main menu select "Dev Tools" button:

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

The Settings tab is used to set the audit on different activates or events 
and consists of several fields:

![](/media/media/image60_js.png)

-   **Time Out in minutes** field - this field defines the time after how
    many minutes the application will automatically log you off
-   **Delete Application Tokens (in days)** - in this field we specify
    after what time the data from the audit should be deleted
-   **Delete Audit Data (in days)** field - in this field we specify after
    what time the data from the audit should be deleted
-   Next field are checkboxes in which we specify what kind of events
    are to be logged (saved) in the audit index. The events that can be
    monitored are: logging (Login), logging out (Logout), creating a
    user (Create User), deleting a user (Delete User), updating user
    (Update User), creating a role (Create Role), deleting a role
    (Delete Role), update of the role (Update Role), start of export
    (Export Start), delete of export (Export Delete), queries (Queries),
    result of the query (Content), if attempt was made to perform a
    series of operation (Bulk)
-   **Delete Exported CSVs (in days)** field - in this field we specify
    after which time exported file with CSV extension have to be removed
-   **Delete Exported PDFs (in days)** field - in this field we specify
    after which time exported file with PDF extension have to be removed

To each field is assigned "Submit" button thanks to which we can confirm the changes.

### License (License Info)

The License Information tab consists of several non-editable
information fields.

![](/media/media/image61_js.png)

These fields contain information:
- Company field, who owns the license - in this case EMCA S.A.
- Data nodes in cluster field - how many nodes we can put in one
  cluster - in this case 100
- No of documents field - empty field
- Indices field - number of indexes, symbol\[\*\] means that we can
  create any number of indices
- Issued on field - date of issue
- Validity field - validity, in this case for 360000 months

#### Renew license

To change the Energy Logserver license files on a running system, do the following steps.

1. Copy the current license files to the backup folder:

   ```bash
   mv /usr/share/elasticsearch/es_* ~/backup/
   ```

2. Copy the new license files to the Elasticsearch installation directory:

   ```bash
   cp es_* /usr/share/elasticsearch/
   ```

3. Add necessary permission to the new license files:

   ```bash
   chown elasticsearch:elasticsearch /usr/share/elasticsearch/es_*
   ```

4. Reload the license using the License API:

   ```bash
   curl -u $USER:$PASSWORD -X POST http://localhost:9200/_license/reload
   ```

### Special accounts

At the first installation of the Energy Logserver application, apart
from the administrative account (logserver), special applications are
created in the application: alert, intelligence and scheduler.

![](/media/media/image62_js.png)

- **Alert Account** - this account is connected to the Alert Module
which is designed to track events written to the index for the
previously defined parameters. If these are met the information
action is started (more on the action in the Alert section)
- **Intelligence Account** - with this account is related to the module
of artificial intelligence which is designed to track events and learn
the network based on previously defined rules artificial intelligence
based on one of the available algorithms (more on operation in the
Intelligence chapter)
- **Scheduler Account** - the scheduler module is associated with this
account, which corresponds to, among others for generating reports

### Restoration procedures

#### Backing up

The backup bash script is located on the hosts with Elasticsearch in location:
```/usr/share/elasticsearch/utils/configuration-backup.sh```.
The script is responsible for backing up the basic data in the Logserver system (these data are the system indexes found in Elasticsearch of those starting with a dot  '.'  in the name),  the configuration of the entire cluster, the set of templates used in the cluster and all the components.
These components include the Logstash configuration located in ```/etc/logstash``` and Kibana configuration located in ```/etc/kibana```.
All data is stored in the ```/tmp``` folder and then packaged using the ```/usr/bin/tar``` utility to ```tar.gz``` format with the exact date and time of execution in the target location, then the files from ```/tmp``` are deleted.

crontab
It is recommended to configure ```crontab```.
- Before executing the following commands, you need to create a crontab file, set the path to backup and direct them there.

In the below example, the task was configured on hosts with the Elasticsearch module on the root.
```bash
# crontab -l #Printing the Crontab file for the currently logged in user 
0 1 * * * /bin/bash /usr/share/elasticsearch/utils/configuration-backup.sh
```

- The client-node host saves the backup in the /archive/configuration-backup/ folder.
- Receiver-node  hosts save the backup in the /root/backup/ folder.

#### Restoration from backup

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

In order to restore any of the configurations e.g. ```kibana/logstash/elastic/wazuh```, follow the steps below:

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

##  Index management

**Note**
***Before use *Index Management* module is necessary to set appropriate password for *Log Server* user in the following file: ```/usr/share/kibana/curator/curator.yml```***

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

This action closes the selected indices, and optionally deletes associated aliases beforehand.

Settings required:

- Action Name
- Schedule Cron Pattern - it sets when the task is to be executed, to decode cron format use on-line tool: [https://crontab.guru](https://crontab.guru),
- Pattern filter kind  - it sets the index filtertype for the task,
- Pattern filter value - it sets value for the index filter,
- Index age - it sets index age for the task.

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
- Schedule Cron Pattern - it sets when the task is to be executed, to decode cron format use on-line tool: [https://crontab.guru](https://crontab.guru)/,
- Pattern filter kind  - it sets the index filtertype for the task,
- Pattern filter value - it sets value for the index filter,
- Index age - it sets index age for the task.

Optional settings:

 - Delete Aliases
 - Skip Flush
 - Ignore Empty List
 - Ignore Sync Failures

![](/media/media/image222.png)

### Force Merge action

This action performs a forceMerge on the selected indices, merging them in specific number of segments per shard.

Settings required:

- Action Name
- Schedule Cron Pattern - it sets when the task is to be executed, to decode cron format use on-line tool: [https://crontab.guru](https://crontab.guru)/,
- Max Segments - it sets the number of segments for the shard,
- Pattern filter kind  - it sets the index filtertype for the task,
- Pattern filter value - it sets value for the index filter,
- Index age - it sets index age for the task.

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

Task will try to meet these conditions. If it is unable to meet them all, it will not perform a shrink operation.

Settings required:

- Action Name
- Schedule Cron Pattern - it sets when the task is to be executed, to decode cron format use on-line tool: [https://crontab.guru](https://crontab.guru)/,
- Number of primary shards in the target indexs - it sets the number of shared for the target index,
- Pattern filter kind  - it sets the index filtertype for the task,
- Pattern filter value - it sets value for the index filter,
- Index age - it sets index age for the task.

Optional settings:

 - Ignore Empty List
 - Continue if exception
 - Delete source index after operation
 - Closed indices filter
 - Empty indices filter

![](/media/media/image224.png)

### Rollover action

This action uses the Elasticsearch Rollover API to create a new index, if any of the described conditions are met.

Settings required:

- Action Name
- Schedule Cron Pattern - it sets when the task is to be executed, to decode cron format use on-line tool: [https://crontab.guru](https://crontab.guru)/,
- Alias Name - it sets alias for index,
- Set max age (hours) - it sets age for index after then index will rollover,
- Set max docs - it sets number of documents for index after which index will rollover,
- Set max size (GiB) - it sets index size in GB after which index will rollover.

Optional settings:
 - New index name (optional)

![](/media/media/image225.png)

### Custom action

Additionally, the module allows you to define your own actions in line with the Curator documentation: https://www.elastic.co/guide/en/elasticsearch/client/curator/current/actions.html

To create a Custom action, select *Custom* from *Select Action*, enter a name in the *Action Name* field and set the schedule in the *Schedule Cron Pattern* field. In the edit field, enter the definition of a custom action:

![](/media/media/image226.png)

Custom Action examles:

#### Open index

```
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

```
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

```
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

```actions:
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

## Intelligence Module

A dedicated artificial intelligence module has been built in the 
Energy Logserver system that allows prediction of parameter values
relevant to the maintenance of infrastructure and IT systems. Such
parameters include:

- use of disk resources,
- use of network resources,
- using the power of processors
- detection of known incorrect behaviour of IT systems

To access of the Intelligence module, click the tile icon
from the main meu bar and then go to the „Intelligence" icon (To go
back, click to the „Search" icon).

![](/media/media/image38_js4.png)

There are 4 screens available in the
module:![](/media/media/image64.png)

- **Create AI Rule** - the screen allows you to create artificial
     intelligence rules and run them in scheduler mode or immediately
- **AI Rules List** - the screen presents a list of created artificial
     intelligence rules with the option of editing, previewing and
     deleting them
- **AI Learn** - the screen allows to define the conditions for teaching
     the MLP neural network
- **AI Learn Tasks** - a screen on which the initiated and completed
     learning processes of neural networks with the ability to preview
     learning results are presented.# Create AI Rule #

To create the AI Rule, click on the tile icon from the main menu bar, 
go to the „Intelligence" icon and select "Create AI Rule" tab. 
The screen allows to defining the rules of artificial intelligence
based on one of the available algorithms (a detailed description of
the available algorithms is available in a separate document).

![](/media/media/image65_js.png)

Description of the controls available on the fixed part of screen:

- **Algorithm** - the name of the algorithm that forms the basis of the
artificial intelligence rule
- **Choose search** - search defined in the Energy Logserver system,
which is used to select a set of data on which the artificial
intelligence rule will operate
- **Run** - a button that allows running the defined AI rule or saving it
to the scheduler and run as planned

The rest of the screen will depend on the chosen artificial
intelligence algorithm.

### The fixed part of the screen

![](/media/media/image65.png)

Description of the controls available on the fixed part of screen:

- Algorithm - the name of the algorithm that forms the basis of the artificial intelligence rule

- Choose search - search defined in the Energy Logserver system, which is used to select a set of data on which the artificial intelligence rule will operate

- Run - a button that allows running the defined AI rule or saving it to the scheduler and run as planned

The rest of the screen will depend on the chosen artificial intelligence algorithm.

### Screen content for regressive algorithms

![](/media/media/image66_js.png)

Description of controls:

- **feature to analyze from search** - analyzed feature (dictated)
- **multiply by field** - enable multiplication of algorithms after
    unique values of the feature indicated here. Multiplication allows
    you to run the AI rule one for e.g. all servers. The value "none" in
    this field means no multiplication.
- **multiply by values** - if a trait is indicated in the „multiply by
    field", then unique values of this trait will appear in this field.
    Multiplications will be made for the selected values. If at least
    one of value is not selected, the „Run" buttons will be inactive.\`

In other words, multiplication means performing an analysis for many values from the indicated field, for example: `sourece_node_host`- which we indicate in `Multiply by field (from search)`.

However, in `Multiply by values (from search)` we already indicate values of this field for which the analysis will be performed, for example: host1, host2, host3, ....

- **time frame** - feature aggregation method (1 minute, 5 minute, 15
    minute, 30 minute, hourly, weekly, monthly, 6 months, 12 months)
- **max probes** - how many samples back will be taken into account for
    analysis. A single sample is an aggregated data according to the
    aggregation method.
- **value type** - which values to take into account when aggregating for
    a given time frame (e.g. maximum from time frame, minimum, average)
- **max predictions** - how many estimates we make for ahead (we take
    time frame)
- **data limit** - limits the amount of date downloaded from the source.
    It speeds up processing but reduces its quality
- **start date** - you can set a date earlier than the current date in
    order to verify how the selected algorithm would work on historical
    data
- **Scheduler** - a tag if the rule should be run according to the plan
    for the scheduler. If selected, additional fields will appear;

![](/media/media/image67.png)

- **Prediction cycle** - plan definition for the scheduler, i.e. the
    cycle in which the prediction rule is run (e.g. once a day, every
    hour, once a week). In the field, enter the command that complies
    with the cron standard. Enable -- whether to immediately launch
    the scheduler plan or save only the definition
- **Role** - only users with the roles selected here and the
    administrator will be able to run the defend AI rules The selected
    „time frame" also affects the prediction period. If we choose
    "time frame = monthly", we will be able to predict a one month
    ahead from the moment of prediction (according to the "prediction
    cycle" value)

### Screen content for the Trend algorithm

![](/media/media/image68_js.png)

Description of controls:

- **feature to analyze from search** - analyzed feature (dictated)
- **multiply by field** - enable multiplication of algorithms after
    unique values of the feature indicated here. Multiplication allows
    you to run the AI rule one for e.g. all servers. The value "none" in
    this field means no multiplication.
- **multiply by values** - if a trait is indicated in the „multiply by
    field", then unique values of this trait will appear in this field.
    Multiplications will be made for the selected values. If at least
    one of value is not selected, the „Run" buttons will be inactive.\`

In other words, multiplication means performing an analysis for many values from the indicated field, for example: `sourece_node_host`- which we indicate in `Multiply by field (from search)`.

However, in `Multiply by values (from search)` we already indicate values of this field for which the analysis will be performed, for example: host1, host2, host3, ....

- **time frame** - feature aggregation method (1 minute, 5 minute, 15
    minute, 30 minute, hourly, weekly, monthly, 6 months, 12 months)
- **max probes** - how many samples back will be taken into account for
    analysis. A single sample is an aggregated data according to the
    aggregation method.
- **value type** - which values to take into account when aggregating for
    a given time frame (e.g. maximum from time frame, minimum, average)
- **max predictions** - how many estimates we make for ahead (we take
    time frame)
- **data limit** - limits the amount of date downloaded from the source.
    It speeds up processing but reduces its quality
- **start date** - you can set a date earlier than the current date in
    order to verify how the selected algorithm would work on historical
    data
- **Scheduler** - a tag if the rule should be run according to the plan
    for the scheduler. If selected, additional fields will appear;

![](/media/media/image67.png)

- **Prediction cycle** - plan definition for the scheduler, i.e. the
    cycle in which the prediction rule is run (e.g. once a day, every
    hour, once a week). In the field, enter the command that complies
    with the cron standard. Enable -- whether to immediately launch
    the scheduler plan or save only the definition
- **Role** - only users with the roles selected here and the
    administrator will be able to run the defend AI rules The selected
    „time frame" also affects the prediction period. If we choose
    "time frame = monthly", we will be able to predict a one month
    ahead from the moment of prediction (according to the "prediction
    cycle" value)
- **Threshold** - default values -1 (do not search). Specifies the
    algorithm what level of exceeding the value of the feature „feature
    to analyze from cheese" is to look for. The parameter currently used
    only by the "Trend" algorithm.

### Screen content for the neural network (MLP) algorithm ##

![](/media/media/image69_js.png)

Descriptions of controls:

- **Name** - name of the learned neural network
- **Choose search** - search defined in Energy Logserver, which is used
    to select a set of data on which the rule of artificial intelligence
    will work
- **Below**, on the left, a list of attributes and their weights based on
    teaching ANN will be defined during the teaching. The user for each
    attribute will be able to indicate the field from the above
    mentioned search, which contain the values of the attribute and
    which will be analyzed in the algorithm. The presented list (for
    input and output attributes) will have a static and dynamic part.
    Static creation by presenting key with the highest weights. The key
    will be presented in the original form, i.e. perf\_data./ The second
    part is a DropDown type list that will serve as a key update
    according to the user's naming. On the right side, the attribute
    will be examined in a given rule / pattern. Here also the user must
    indicate a specific field from the search. In both cases, the input
    and output are narrowed based on the search fields indicated in
    Choose search.
- **Data limit** - limits the amount of data downloaded from the source.
    It speeds up the processing, but reduces its quality.
- **Scheduler** - a tag if the rule should be run according to the plan
    or the scheduler. If selected, additional fields will appear:

![](/media/media/image67.png)

- **Prediction cycle** - plan definition for the scheduler, i.e. the
     cycle in which the prediction rule is run (e.g. once a day, every
     hour, once a week). In the field, enter the command that complies
     with the *cron* standard
- **Enable** - whether to immediately launch the scheduler plan or save
     only the definition
- **Role** - only users with the roles selected here and the
     administrator will be able to run the defined AI rules

### AI Rules List ##

![](/media/media/image70.png)

Column description:

- **Status**:
    - ![](/media/media/image71.png)- the process is being processed (the pid of the process is in brackets)
    - ![](/media/media/image72.png) - process completed correctly
    - ![](/media/media/image73.png) - the process ended with an error
- **Name** - the name of the rule
- **Search** - the search on which the rule was run
- **Method** - an algorithm used in the AI rule
- **Actions** - allowed actions:
    - **Show** - preview of the rule definition
    - **Enable/Disable** - rule activation /deactivation
    - **Delete** - deleting the rule
    - **Update** - update of the rule definition
    - **Preview** - preview of the prediction results (the action is
        available after the processing has been completed correctly).

### AI Learn ##

![](/media/media/image74.png)

Description of controls:

- **Search** - a source of data for teaching the network
- **prefix name** - a prefix added to the id of the learned model that
  allows the user to recognize the model
- **Input cols** - list of fields that are analyzed / input features.
  Here, the column that will be selected in the output col should
  not be indicated. Only those columns that are related to processing
  should be selected. **
- **Output col** - result field, the recognition of which is learned by
  the network. **This field should exist in the learning and testing
  data, but in the production data is unnecessary and should not
  occur. This field cannot be on the list of selected fields in "input
  col".**
- **Output class category** - here you can enter a condition in SQL
  format to limit the number of output categories e.g. `if((outputCol)
  \< 10,(floor((outputCol))+1), Double(10))`. This condition limits the
  number of output categories to 10. **Such conditions are necessary
  for fields selected in "output col" that have continuous values.
  They must necessarily by divided into categories. In the Condition,
  use your own outputCol name instead of the field name from the index
  that points to the value of the "output col" attribute.**
- **Time frame** - a method of aggregation of features to improve their
  quality (e.g. 1 minute, 5 minutes, 15 minutes, 30 minutes, 1 hour, 1
  daily).
- **Time frames output shift** - indicates how many time frame units to
  move the output category. This allows teaching the network with
  current attributes, but for categories for the future.
- **Value type** - which values to take into account when aggregating for
  a given time frame (e.g. maximum from time frame, minimum, average)
- **Output class count**- the expected number of result classes. **If
  during learning the network identifies more classes than the user
  entered, the process will be interrupted with an error, therefore it
  is better to set up more classes than less, but you have to keep in
  mind that this number affects the learning time.**
- **Neurons in first hidden layer (from, to)** - the number of neurons in
  the first hidden layer. Must have a value \> 0. Jump every 1.
- **Neurons in second hidden layer (from, to)** - the number of neurons
  in second hidden layer. If = 0, then this layer is missing. Jump
  every 1.
- **Neurons in third hidden layer (from, to)** - the number of neurons in
  third hidden layer. If = 0 then this layer is missing. Jump every 1.
- **Max iter** (from, to) - maximum number of network teaching
  repetitions (the same data is used for learning many times in
  internal processes of the neural network). The slower it is. Jump
  every 100. The maximum value is 10, the default is 1.
- **Split data to train&test** - for example, the entered value of 0.8
  means that the input data for the network will be divided in the
  ratio 0.8 to learning, 0.2 for the tests of the network learned.
- **Data limit** - limits the amount of data downloaded from the source.
  It speeds up the processing, but reduces its quality.
- **Max probes** - limits the number of samples taken to learn the
  network. Samples are already aggregated according to the selected
  "Time frame" parameter. It speed up teaching but reduces its
  quality.
- **Build** - a button to start teaching the network. The button contains
  the number of required teaching curses. You should be careful and
  avoid one-time learning for more than 1000 courses. It is better to
  divide them into several smaller ones. One pass after a full data
  load take about 1-3 minutes on a 4 core 2.4.GHz server.
  **The module has implemented the best practices related to the number
  of neurons in individual hidden layers. The values suggested by the
  system are optimal from the point of view of these practices, but the
  user can decide on these values himself.**

Under the parameters for learning the network there is an area in
which teaching results will appear.

After pressing the "Refresh" button, the list of the resulting models
will be refreshed.

Autorefresh - selecting the field automatically refreshes the list of
learning results every 10s.

The following information will be available in the table on the left:

- **Internal name** - the model name given by the system, including the
    user - specified prefix

- **Overall efficiency** - the network adjustment indicator - allow to
    see at a glance whether it is worth dealing with the model. The
    grater the value, the better.

After clicking on the table row, detailed data collected during the
learning of the given model will be displayed. This data will be
visible in the box on the right.

The selected model can be saved under its own name using the "Save
algorithm" button. This saved algorithm will be available in the
"Choose AI Rule" list when creating the rule (see Create AI Rule).

### AI Learn Tasks ##

The "AI Learn Task" tab shows the list of processes initiated teaching the ANN network
with the possibility of managing processes.

Each user can see only the process they run. The user in the role of
Intelligence sees all running processes.

![](/media/media/image75.png)

Description of controls:

- **Algorithm prefix** - this is the value set by the user on the AI
    Learn screen in the Prefix name field
 - **Progress** - here is the number of algorithms generated / the number of all to be generated
- **Processing time** - duration of algorithm generation in seconds (or
     maybe minutes or hours)
- **Actions**:
    - **Cancel** - deletes the algorithm generation task (user require
        confirmation of operation)
    - **Pause / Release** - pause / resume algorithm generation process.

AI Learn tab contain the Show in the preview mode of the ANN hyperparameters
After completing the learning activity or after the user has interrupted it, 
the "Delete" button appears in "Action" field. This button allows you to permanently 
delete the learning results of a specific network.

![](/media/media/image76.png)

### Scenarios of using algorithms implemented in the Intelligence module


#### Teaching MLP networks and choosing the algorithm to use:

1. Go to the AI Learn tab,
1. We introduce the network teaching parameters,
1. Enter your own prefix for the names of the algorithms you have learned,
1. Press Build.
1. We observe the learned networks on the list (we can also stop the observation at any moment and go to other functions of the system. We will return to the learning results by going to the AI Learn Tasks tab and clicking the show action),
1. We choose the best model from our point of view and save it under our own name,
1. From this moment the algorithm is visible in the Create AI Rule tab.

#### Starting the MLP network algorithm:

1. 	Go to the Create AI Rule tab and create rules,
1. 	Select the previously saved model of the learned network,
1. 	Specify parameters visible on the screen (specific to MLP),
1. 	Press the Run button.

#### Starting regression algorithm:

1. Go to the Create AI Rule tab and create rules,
1. We choose AI Rule, e.g. Simple Moving Average, Linear Regression or Random Forest Regression, etc.,
1. Enter your own rule name (specific to regression),
1. Set the parameters of the rule ( specific to regression),
1. Press the Run button.

#### Management of available rules:

1. Go to the AI Rules List tab,
1. A list of AI rules available for our role is displayed,
1. We can perform the actions available on the right for each rule.# Results of algorithms #

The results of the "AI algorithms" are saved to the index „intelligence" specially created
for this purpose. The index with the prediction result. These
following fields are available in the index (where xxx is the name of
the attribute being analyzed):

-   **xxx\_pre** - estimate value
-   **xxx\_cur** - current value at the moment of estimation
-   **method\_name** - name of the algorithm used
-   **rmse** - avarage square error for the analysis in which \_cur values
     were available. **The smaller the value, the better.**
-   **rmse\_normalized** - mean square error for the analysis in which
     \_cur values were available, normalized with \_pre values. **The
     smaller the value, the better.**
-   **overall\_efficiency** - efficiency of the model. **The greater the
     value, the better. A value less than 0 may indicate too little
     data to correctly calculate the indicator**
-   **linear\_function\_a** - directional coefficient of the linear
     function y = ax + b. **Only for the Trend and Linear Regression
     Trend algorithm**
-   **linear\_function\_b** - the intersection of the line with the Y axis
     for the linear function y = ax + b. **Only for the Trend and
     Linear Regression Trend algorithm.**

Visualization and signals related to the results of data analysis
should be created from this index. The index should be available to
users of the Intelligence module.

### Permission

Permission have been implemented in the following way:

- Only the user in the admin role can create / update rules.
- When creating rules, the roles that will be able to enables /
  disengage / view the rules will be indicated.

We assume that the Learn process works as an administrator.

We assume that the visibility of Search in AI Learn is preceded by
receiving the search permission in the module object permission.

The role of "Intelligence" launches the appropriate tabs.

An ordinary user only sees his models. The administrator sees all
models.

### Register new algorithm

For register new algorithm:

- **Login** to the Energy Logserver
- Select **Intelligence**
- Select **Algorithm**
- Fill Create algorithm form and press **Submit** button

Form fields:

	| Field   | Description                                                                                                      |
	|---------|------------------------------------------------------------------------------------------------------------------|
	| Code    | Short name for algorithm                                                                                         |
	| Name    | Algorithm name                                                                                                   |
	| Command | Command to execute. The command must be in the directory pointed to by the parameter elastscheduler.commandpath. |

Energy Logserver execute command:

	<command> <config> <error file> <out file>

Where:

- command	-	Command from command filed of Create algorithm form.
- config		-	Full path of json config file. The name of file is id of process status document in index .intelligence_rules
- error file	-	Unique name for error file. Not used by predefined algorithms.
- out file		-	Unique name for output file. Not used by predefined algorithms.

Config file:

Json document:

	| Field                  | Value                                                                               | Screen field (description)                                           |
	|------------------------|-------------------------------------------------------------------------------------|----------------------------------------------------------------------|
	| algorithm_type         | GMA, GMAL, LRS, LRST, RFRS, SMAL, SMA, TL                                           | Algorithm. For customs method field Code from Create algorithm form. |
	| model_name             | Not empty string.                                                                   | AI Rule Name.                                                        |
	| search                 | Search id.                                                                          | Choose search.                                                       |
	| label_field.field      |                                                                                     | Feature to analyse.                                                  |
	| max_probes             | Integer value                                                                       | Max probes                                                           |
	| time_frame             | 1 minute, 5 minutes, 15 minutes, 30 minutes, 1 hour, 1 day, 1 week, 30 day, 365 day | Time frame                                                           |
	| value_type             | min, max, avg, count                                                                | Value type                                                           |
	| max_predictions        | Integer value                                                                       | Max predictions                                                      |
	| threshold              | Integer value                                                                       | Threshold                                                            |
	| automatic_cron         | Cron format string                                                                  | Automatic cycle                                                      |
	| automatic_enable       | true/false                                                                          | Enable                                                               |
	| automatic              | true/false                                                                          | Automatic                                                            |
	| start_date             | YYYY-MM-DD HH:mm or now                                                             | Start date                                                           |
	| multiply_by_values     | Array of string values                                                              | Multiply by values                                                   |
	| multiply_by_field      | None or full field name eg.: system.cpu                                             | Multiply by field                                                    |
	| selectedroles          | Array of roles name                                                                 | Role                                                                 |
	| last_execute_timestamp |                                                                                     | Last execute                                                         |
	
	| Not screen fields     |                                     |
	|-----------------------|-------------------------------------|
	| preparation_date      | Document preparation date.          |
	| machine_state_uid     | AI rule machine state uid.          |
	| path_to_logs          | Path to ai machine logs.            |
	| path_to_machine_state | Path to ai machine state files.     |
	| searchSourceJSON      | Query string.                       |
	| processing_time       | Process operation time.             |
	| last_execute_mili     | Last executed time in milliseconds. |
	| pid                   | Process pid if ai rule is running.  |
	| exit_code             | Last executed process exit code.    |

The command must update the process status document in the system during operation. It is elastic partial document update.

	| Process status         | Field (POST body)          | Description                                    |
	|------------------------|----------------------------|------------------------------------------------|
	| START                  | doc.pid                    | System process id                              |
	|                        | doc.last_execute_timestamp | Current timestamp. yyyy-MM-dd HH:mm            |
	|                        | doc.last_execute_mili      | Current timestamp in millisecunds.             |
	| END PROCESS WITH ERROR | doc.error_description      | Error description.                             |
	|                        | doc.error_message          | Error message.                                 |
	|                        | doc.exit_code              | System process exit code.                      |
	|                        | doc.pid                    | Value 0.                                       |
	|                        | doc.processing_time        | Time of execute process in seconds.            |
	| END PROCESS OK         | doc.pid                    | Value 0.                                       |
	|                        | doc.exit_code              | System process exit code. Value 0 for success. |
	|                        | doc.processing_time        | Time of execute process in seconds.            |

The command must insert data for prediction chart.

	| Field             | Value             | Description                                            |
	|-------------------|-------------------|--------------------------------------------------------|
	| model_name        | Not empty string. | AI Rule Name.                                          |
	| preparationUID    | Not empty string. | Unique prediction id                                   |
	| machine_state_uid | Not empty string. | AI rule machine state uid.                             |
	| model_uid         | Not empty string. | Model uid from config file                             |
	| method_name       | Not empty string. | User friendly algorithm name.                          |
	| <field>           | Json              | Field calculated. For example: system.cpu.idle.pct_pre |

Document sample:

			{
			  "_index": "intelligence",
			  "_type": "doc",
			  "_id": "emca_TL_20190304_080802_20190531193000",
			  "_version": 2,
			  "_score": null,
			  "_source": {
			    "machine_state_uid": "emca_TL_20190304_080802",
			    "overall_efficiency": 0,
			    "processing_time": 0,
			    "rmse_normalized": 0,
			    "predictionUID": "emca_TL_20190304_080802_20190531193000",
			    "linear_function_b": 0,
			    "@timestamp": "2019-05-31T19:30:00.000+0200",
			    "linear_function_a": 0.006787878787878788,
			    "system": {
			      "cpu": {
			        "idle": {
			          "pct_pre": 0.8213333333333334
			        }
			      }
			    },
			    "model_name": "emca",
			    "method_name": "Trend",
			    "model_uid": "emca_TL_20190304_080802",
			    "rmse": 0,
			    "start_date": "2019-03-04T19:30:01.279+0100"
			  },
			  "fields": {
			    "@timestamp": [
			      "2019-05-31T17:30:00.000Z"
			    ]
			  },
			  "sort": [
			    1559323800000
			  ]
			}

## Archive

The Archive module allows you to create compressed data files ([zstd](https://github.com/facebook/zstd)) from Elasticsearch indexes. The archive checks the age of each document in the index and if it is older than defined in the job, it is copied to the archive file.

### Configuration

#### Enabling module

To configure module edit `kibana.yml` configuration file end set path to the archive directory - location where the archive files will be stored:

```bash
vim /etc/kibana/kibana.yml
```

remove the comment from the following line and set the correct path to the archive directory:

```vim
archive.archivefolderpath: '/var/lib/elastic_archive_test'
```

### Archive Task

##### Create Archive task

1. From the main navigation go to the "Archvie" module.

   ![](/media/media/image155.png) 

2. On the "Archive" tab select "Create Task" and define the following parameters:

   - `Index pattern`- for the indexes that will be archive, for example `syslog*` ;
   - `Older than (days)` - number of days after which documents will be archived;
   - `Schedule task` (crontab format) - the work schedule of the ordered task.
   
   ![](/media/media/image156.png) 

#### Task List

In the `Task List` you can follow the current status of ordered tasks. You can modify task scheduler or delete ordered task.

![](/media/media/image157.png) 

If the archiving task finds an existing archive file that matches the data being archived, it will check the number of documents in the archive and the number of documents in the index. If there is a difference in the number of documents then new documents will be added to the archive file.

### Archive Search

The Archive Search module can search archive files for the specific content and back result in the `Task List`

#### Create Search task

1. From the main navigation go to the `Archive` module.
2. On the `Search` tab select `Create Task` and define the following parameters:

   - `Search text` - field for entered the text to be searched.
   - `File name` - list of archive file that will be searched.

![](/media/media/image158.png) 

#### Task list

The searching process will can take long time. On the `Task List` you can follow the status of the searching process. Also you can view result and delete tasks.

![](/media/media/image159.png) 

### Archive Upload

The Archive Upload module move data from archive to Elasticsearch index and make it online.

#### Create Upload task

1. From the main navigation go to the `Archive` module.

2. On the `Upload` tab select `Create Task` and define the following parameters:

   - `Destination index` - If destination index does not exist it will be created. If exists data will append.
- `File name` - list of archive file that will be recover to Elasticsearch index.
  

![](/media/media/image160.png) 

#### Task List

The process will index data back into Elasticsearch. Depend on archive size the process can take long time. On the `Task List` you can follow the status of the recovery process. Also you can view result and delete tasks.

![](/media/media/image161.png) 

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

## Wiki

### Wiki.js

**Wiki.js** is one of the most powerful and extensible Wiki software. The **Energy Logserver** have integration plugin with **Wiki.js**, which allows you to access **Wiki.js** directly from the Energy Logserver GUI. Additionally, Energy Logserver provides access management to the Wiki content.

#### Login to Wiki

Access to the **Wiki** is from the main **Energy Logserver** GUI window via the **Wiki** button located at the top of the window:

![](/media/media/image168.png)

#### Creating a public site

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

     

#### Creating a site with the permissions of a given group

To create sites with the permissions of a given group, do the following:

1. Check the permissions of the group to which the user belongs. To do this, click on the ***Account*** button in the top right menu in Wiki.js:

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

   

#### Content management

##### Text formatting features

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
- inserting text blocks Wiki.js also offers non-text insertion.



##### Insert Links

- To insert links, click in the site editor on the ***Link*** icon on the editor icon bar:

![](/media/media/image182.png)



- After clicking on the icon, a text field will appear to enter the website address:

  ![](/media/media/image183.png)

  

- Then click the ***Save*** button (green sign next to the text field), then the address to the external site will appear on the current site:

  ![](/media/media/image184.png)

  

##### Insert images

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

***Wiki.js*** does not offer a document tree structure directly. Creating a structure (tree) of documents is done automatically by grouping sites according to the paths in which they are available.

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

   ```wiki
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

## Celebro - Cluster Health

Cerebro is the Elasticsearch administration tool that allows you to perform the following tasks:

- monitoring and management of indexing nodes, indexes and shards:

![](/media/media/image217.png)

- monitoring and management of index shapshoots :

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
                    The maximum number of requests the can be made concurrently to a specified transport.
                    (default: 1)       
--concurrencyInterval
                    The length of time in milliseconds in which up to <intervalCap> requests can be made
                    before the interval request count resets. Must be finite.
                    (default: 5000)       
--intervalCap
                    The maximum number of transport requests that can be made within a given <concurrencyInterval>.
                    (default: 5)
--carryoverConcurrencyCount
                    If true, any incomplete requests from a <concurrencyInterval> will be carried over to
                    the next interval, effectively reducing the number of new requests that can be created
                    in that next interval.  If false, up to <intervalCap> requests can be created in the
                    next interval regardless of the number of incomplete requests from the previous interval.
                    (default: true)                                                                                       
--throttleInterval
                    Delay in milliseconds between getting data from an inputTransport and sending it to an
                    outputTransport.
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
                    (default: ((metrics|logs|\\..+)(-.+)?)
--delete
                    Delete documents one-by-one from the input as they are
                    moved.  Will not delete the source index
                    (default: false)
--searchBody
                    Preform a partial extract based on search results
                    when ES is the input, default values are
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
--headers
                    Add custom headers to Elastisearch requests (helpful when
                    your Elasticsearch instance sits behind a proxy)
                    (default: '{"User-Agent": "elasticdump"}')
--params
                    Add custom parameters to Elastisearch requests uri. Helpful when you for example
                    want to use elasticsearch preference
                    (default: null)
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
                            are requirements
                                                Negative:
                                                     1. Recently added data may not be indexed
                                                         with big data indexing,
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
                                                        --transform
                                                                            A method/function which can be called to modify documents
                                                                            before writing to a destination. A global variable 'doc'
                                                                            is available.
                                                                            Example script for computing a new field 'f2' as doubled
                                                                            value of field 'f1':
                                                                                doc._source["f2"] = doc._source.f1 * 2;
                                                                            May be used multiple times.
                                                                            Additionally, transform may be performed by a module. See [Module Transform](#module-transform) below.
                                                        --awsChain
                                                                            Use [standard](https://aws.amazon.com/blogs/security/a-new-and-standardized-way-to-manage-credentials-in-the-aws-sdks/) location and ordering for resolving credentials including environment variables, config files, EC2 and ECS metadata locations
                                                                            _Recommended option for use with AWS_
                                                                            Use [standard](https://aws.amazon.com/blogs/security/a-new-and-standardized-way-to-manage-credentials-in-the-aws-sdks/) 
                                                                            location and ordering for resolving credentials including environment variables, 
                                                                            config files, EC2 and ECS metadata locations _Recommended option for use with AWS_
                                                        --awsAccessKeyId
                                                        --awsSecretAccessKey
                                                                            When using Amazon Elasticsearch Service protected by
                                                                            AWS Identity and Access Management (IAM), provide
                                                                            your Access Key ID and Secret Access Key.
                                                                            --sessionToken can also be optionally provided if using temporary credentials
                                                        --awsIniFileProfile
                                                                            Alternative to --awsAccessKeyId and --awsSecretAccessKey,
                                                                            loads credentials from a specified profile in aws ini file.
                                                                            For greater flexibility, consider using --awsChain
                                                                            and setting AWS_PROFILE and AWS_CONFIG_FILE
                                                                            environment variables to override defaults if needed
                                                        --awsIniFileName
                                                                            Override the default aws ini file name when using --awsIniFileProfile
                                                                            Filename is relative to ~/.aws/
                                                                            (default: config)
                                                        --awsService
                                                                            Sets the AWS service that the signature will be generated for
                                                                            (default: calculated from hostname or host)
                                                        --awsRegion
                                                                            Sets the AWS region that the signature will be generated for
                                                                            (default: calculated from hostname or host)
                                                        --awsUrlRegex
                                                                            Regular expression that defined valied AWS urls that should be signed
                                                                            (default: ^https?:\\.*.amazonaws.com.*$)
                                                        --support-big-int   
                                                                            Support big integer numbers
                                                        --big-int-fields   
                                                                            Sepcifies a comma-seperated list of fields that should be checked for big-int support
                                                                            (default '')
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
                    NB : Type validation is handled by the bulk endpoint and not by elasticsearch-dump
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
                    NB:  (If the first row is treated as headers, they aren't a part of the count)
                    (default : 0)
--csvMaxRows        
                    If number is > 0 then only the specified number of rows will be parsed.(e.g. 100 would return the first 100 rows of data)
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

---
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

  ```bash
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

  ```bash
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

  ```bash
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

  ```bash
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

  ```bash
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

                input {
                        beats {
                                port => 5044
                        }
                }

### Getting data from share folder

Using beats, you can reading data from FTP, SFTP, SMB share.
Connection to remote resources should be done as follows:

#### Input - FTP server

- Installation

		yum install curlftpfs

- Create mount ftp directory

		mkdir /mnt/my_ftp

- Use `curlftpfs` to mount your remote ftp site. Suppose my access credentials are as follows:

		urlftpfs ftp-user:ftp-pass@my-ftp-location.local /mnt/my_ftp/

#### Input - SFTP server

- Install the required packages

		yum install sshfs

- Add user

		sudo adduser yourusername fuse

- Create local folder

		mkdir ~/Desktop/sftp

- Mount remote folder to local:

		sshfs HOSTuser@remote.host.or.ip:/host/dir/to/mount ~/Desktop/sftp

#### Input - SMB/CIFS server

- Create local folder

		mkdir ~/Desktop/smb

- Mount remote folder to local:

		mount -t smbfs //remoate.host.or.ip/freigabe /mnt -o username=testuser

	or
		mount -t cifs //remoate.host.or.ip/freigabe /mnt -o username=testuser


### Logstash - Input "network" ##

This plugin read events over a TCP or UDP socket assigns the appropriate tags:

```yaml
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

		input {
		  snmp {
		    get => ["1.3.6.1.2.1.1.1.0"]
		    hosts => [{host => "udp:127.0.0.1/161" community => "public" version => "2c"  retries => 2  timeout => 1000}]
		  }
		}


### Logstash - Input HTTP / HTTPS

Using this input you can receive single or multiline events over http(s). Applications can send an HTTP request to the endpoint started by this input and Logstash will convert it into an event for subsequent processing. Sample definition:

		input {
		 http {
		    host => "0.0.0.0"
		    port => "8080"
		  }
		}

Events are by default sent in plain text. You can enable encryption by setting ssl to true and configuring the ssl_certificate and ssl_key options:


		input {
		 http {
		    host => "0.0.0.0"
		    port => "8080"
		    ssl => "true"
		    ssl_certificate => "path_to_certificate_file"
		    ssl_key => "path_to_key_file"
		  }
		}
		
### Logstash - Input Relp

#### Installation

For plugins not bundled by default, it is easy to install by running bin/logstash-plugin install logstash-input-relp.

#### Description

Read RELP events over a TCP socket.

This protocol implements application-level acknowledgements to help protect against message loss.

Message acks only function as far as messages being put into the queue for filters; anything lost after that point will not be retransmitted.

#### Relp input configuration options

This plugin supports the following configuration options plus the Common Options described later.

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
<td><p class="first last">host</p>
</td>
<td><p class="first last">string</p>
</td>
<td><p class="first last">No</p>
</td>
</tr>

<tr class="row-even"><td><p class="first last">2</p>
</td>
<td><p class="first last">port</p>
</td>
<td><p class="first last">number</p>
</td>
<td><p class="first last">Yes</p>
</td>
</tr>

<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last">ssl_cacert</p>
</td>
<td><p class="first last">a valid filesystem path</p>
</td>
<td><p class="first last">No</p>
</td>
</tr>

<tr class="row-even"><td><p class="first last">4</p>
</td>
<td><p class="first last">ssl_cert</p>
</td>
<td><p class="first last">a valid filesystem path</p>
</td>
<td><p class="first last">No</p>
</td>
</tr>

<tr class="row-even"><td><p class="first last">5</p>
</td>
<td><p class="first last">ssl_enable</p>
</td>
<td><p class="first last">boolean</p>
</td>
<td><p class="first last">No</p>
</td>
</tr>

<tr class="row-even"><td><p class="first last">6</p>
</td>
<td><p class="first last">ssl_key</p>
</td>
<td><p class="first last">a valid filesystem path</p>
</td>
<td><p class="first last">No</p>
</td>
</tr>

<tr class="row-even"><td><p class="first last">7</p>
</td>
<td><p class="first last">ssl_key_passphrase</p>
</td>
<td><p class="first last">password</p>
</td>
<td><p class="first last">No</p>
</td>
</tr>

<tr class="row-even"><td><p class="first last">8</p>
</td>
<td><p class="first last">ssl_verify</p>
</td>
<td><p class="first last">string</p>
</td>
<td><p class="first last">boolean</p>
</td>
</tr>


</td>
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

```yml
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

```yml
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

		file {
		    path => "/tmp/access_log"
		    start_position => "beginning"
		  }

### Logstash - Input database

This plugin can read data in any database with a JDBC interface into Logstash. You can periodically schedule ingestion using a cron syntax (see schedule setting) or run the query one time to load data into Logstash. Each row in the resultset becomes a single event. Columns in the resultset are converted into fields in the event.

#### Logasth input - MySQL

Download jdbc driver: [https://dev.mysql.com/downloads/connector/j/](https://dev.mysql.com/downloads/connector/j/)

Sample definition:

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

#### Logasth input - MSSQL

Download jdbc driver: [https://docs.microsoft.com/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server?view=sql-server-ver15](https://docs.microsoft.com/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server?view=sql-server-ver15)

Sample definition:

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

#### Logstash input - Oracle
Download jdbc driver: [https://www.oracle.com/database/technologies/appdev/jdbc-downloads.html](https://www.oracle.com/database/technologies/appdev/jdbc-downloads.html)

Sample definition:

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

#### Logstash input - PostgreSQL
Download jdbc driver: [https://jdbc.postgresql.org/download.html](https://jdbc.postgresql.org/download.html)

Sample definition:

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

```
sudo apt-get install gcc-multilib g++-multilib libelf-dev:i386 libpam0g:i386 zlib1g-dev:i386
```

If you are using **CentOS or RHEL**, please run:

```
sudo yum install gcc gcc-c++ make glibc-devel.i686 elfutils-libelf-devel.i686 zlib-devel.i686 libstdc++-devel.i686 pam-devel.i686
```

#### Compile source code

Building should be as simple as running GNU Make in the project root folder:

```
make
```

If the build process complains, you might need to tweak some variables inside the `Makefile` (e.g. `CC`, `LD` and `OPSEC_PKG_DIR`) according to your environment.

#### Install FW1-LogGrabber

To install FW1-LogGrabber into its default location `/usr/local/fw1-loggrabber` (defined by `INSTALL_DIR` variable), please run

```
sudo make install
```

#### Set environment variables

FW1-LogGraber makes use of two environment variables, which should be defined in the shell configuration files.

* `LOGGRABBER_CONFIG_PATH` defines a directory containing configuration files (`fw1-loggrabber.conf`, `lea.conf`). If the variable is not defined, the program expects to find these files in the current directory.
* `LOGGRABBER_TEMP_PATH` defines a directory where FW1-LogGrabber will store temporary files. If the
  variable is not defined, the program stores these files in the current directory.

Since the binary is dynamically linked to Checkpoint OPSEC libraries, please also add `/usr/local/fw1-loggrabber/lib` to `LD_LIBRARY_PATH` or to your dynamic linker configuration with

```
sudo echo /usr/local/fw1-loggrabber/lib > /etc/ld.so.conf.d/fw1-loggrabber.conf
sudo ldconfig
```
#### Configuration files

#### lea.conf file

Starting with version 1.11, FW1-LogGrabber uses the default connection configuration procedure for OPSEC applications. This includes server, port and authentication settings. From now on, all this parameters can only be configured using the configuration file `lea.conf` (see `--leaconfigfile` option to use a different LEA configuration file) and not using the command-line as before.

* `lea_server ip <IP address>` specifies the IP address of the FW1 management station, to which FW1-LogGrabber should connect to.

* `lea_server port <port number>` is the port on the FW1 management station to which FW1-LogGrabber should connect to (for unauthenticated connections only).

* `lea_server auth_port <port number>` is the port to be used for authenticated connection to your FW1 management station.

* `lea_server auth_type <authentication mechanism>` you can use this parameter to specify the authentication
  mechanism to be used (default is `sslca`); valid values are `sslca`, `sslca_clear`, `sslca_comp`, `sslca_rc4`, `sslca_rc4_comp`, `asym_sslca`, `asym_sslca_comp`, `asym_sslca_rc4`, `asym_sslca_rc4_comp`, `ssl`, `ssl_opsec`,
  `ssl_clear`, `ssl_clear_opsec`, `fwn1` and `auth_opsec`.

* `opsec_sslca_file <p12-file>` specify the location of the PKCS#12 certificate, when using authenticated connections.

* `opsec_sic_name <LEA client SIC name>` is the SIC name of the LEA client for authenticated connections.

* `lea_server opsec_entity_sic_name <LEA server SIC name>` is the SIC name of your FW1 management station when using authenticated connections.

##### fw1-loggrabber.conf file

This paragraph deals with the options that can be set within the configuration file. The default configuration file is `fw1-loggrabber.conf` (see `--configfile` option to use a different configuration file). The precedence of given options is as follows: command line, configuration file, default value. E.g. if you set the resolve-mode to be used in the configuration file, this can be overwritten by command line option `--noresolve`; only if an option isn't set neither on command line nor in the configuration file, the default value will be used.

* `DEBUG_LEVEL=<0-3>` sets the debug level to the specified value; zero means no output of debug information, and further levels will cause output of program specific as well as OPSEC specific debug information.

* `FW1_LOGFILE=<name of log file>` specifies the name of the FW1 logfile to be read; this can be either done exactly or using only a part of the filename; if no exact match can be found in the list of logfiles returned by the FW-1 management station, all logfiles which contain the specified string are processed; if this
  parameter is omitted, the default logfile `fw.log` will be processed.

* `FW1_OUTPUT=<files|logs>` specifies whether FW1-LogGrabber should only display the available logfiles (`files`) on the FW11 server or display the content of these logfiles (`logs`).

* `FW1_TYPE=<ng|2000>` choose which version of FW1 to connect to; for Checkpoint FW-1 5.0 you have to specify `NG` and for Checkpoint FW-1 4.1 you have to specify `2000`.

* `FW1_MODE=<audit|normal>` specifies whether to display `audit` logs, which contain administrative actions, or `normal` security logs, which contain data about dropped and accepted connections.

* `MODE=<online|online-resume|offline>` when using online mode, FW1-LogGrabber starts retrieving logging data from the end of the specified logfile and displays all future log entries (mainly used for continuously processing); the online-resume mode is similar to the online mode, but if FW1-LogGrabber is stopped and started again, it resumes processing from where it was stopped; if you instead choose the offline mode, FW1-LogGrabber quits after having displayed the last log entry.

* `RESOLVE_MODE=<yes|no>` with this option (enabled by default), IP addresses will be resolved to names using FW1 name resolving behaviour; this resolving mechanism will not cause the machine running FW1-LogGrabber to initiate DNS requests, but the name resolution will be done directly on the FW1 machine; if you disable resolving mode, IP addresses will be displayed in log output instead of names.

* `RECORD_SEPARATOR=<char>` can be used to change the default record separator `|` (pipe) into another
  character; if you choose a character which is contained in some log data, the occurrence within the logdata will be escaped by a backslash.

* `LOGGING_CONFIGURATION=<screen|file|syslog>` can be used for redirecting logging output to other destinations than the default destination `STDOUT`; currently it is possible to redirect output to a file or to the syslog daemon.

* `OUTPUT_FILE_PREFIX=<prefix of output file>` when using file output, this parameter defines a prefix for the output filename; default value is simply `fw1-loggrabber`.

* `OUTPUT_FILE_ROTATESIZE=<rotatesize in bytes>` when using file output, this parameter specifies the maximum size of the output files, before they will be rotated with suffix `-YYYY-MM-DD-hhmmss[-x].log`; default value is 1048576 bytes, which equals 1 MB; setting a zero value disables file rotation.

* `SYSLOG_FACILITY=<USER|LOCAL0|...|LOCAL7>` when using syslog output, this parameter sets the syslog facility to be used.

* `FW1_FILTER_RULE="<filterexpression1>[;<filterexpression2>]"` defines filters for `normal` log mode; you can find a more detailed description of filter rules, along with some examples, [in a separate chapter below](#filtering).

* `AUDIT_FILTER_RULE="<filterexpression1>[;<filterexpression2>]"` defines filters for `audit` log mode; you can find a more detailed description of filter rules, along with some examples, [in a separate chapter below](#filtering).

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

```
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

In contrast to online mode, when using `--offline` mode FW1-LogGrabber quits after having displayed the last
log entry. This is the default behavior and is mainly used for analysis of historic log data.

#### Audit and normal logs

Using the `--auditlog` mode, content of the audit logfile (`fw.adtlog`) can be displayed. This includes administrator actions and uses different fields than normal log data.

The default `--normallog` mode of FW1-LogGrabber processes normal FW1 logfiles. In contrast to the `--auditlog` option, no administrative actions are displayed in this mode, but all regular log data is.

#### Filtering

Filter rules provide the possibility to display only log entries that match a given set of rules. There can be
specified one or more filter rules using one or multiple `--filter` arguments on the command line.

All individual filter rules are related by OR. That means a log entry will be displayed if at least one of the filter rules matches. You can specify multiple argument values by separating the values by `,` (comma).

Within one filter rule, there can be specified multiple arguments which have to be separated by `;` (semi-colon). All these arguments are related by AND. That means a filter rule matches a given log entry only, if all of the filter arguments match.

If you specify `!=` instead of `=` between name and value of the filter argument, you can negate the name/value pair.

For arguments that expect IP addresses, you can specify either a single IP address, multiple IP addresses separated by `,` (comma) or a network address with netmask (e.g. `10.0.0.0/255.0.0.0`). Currently it is not possible to specify a network address and a single IP address within the same filter argument.

##### Supported filter arguments

Normal mode:

```
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

```
action=<ctl|accept|drop|reject|encrypt|decrypt|keyinst>
administrator=<string>
endtime=<YYYYMMDDhhmmss>
orig=<IP address>
product=<SmartDashboard|Policy Editor|SmartView Tracker|SmartView Status|SmartView Monitor|System Monitor|cpstat_monitor|SmartUpdate|CPMI Client>
starttime=<YYYYMMDDhhmmss>
```

##### Example filters

Display all dropped connections:

```
--filter "action=drop"
```

Display all dropped and rejected connections:

```
--filter "action=drop,reject"
--filter "action!=accept"
```

Display all log entries generated by rules 20 to 23:

```
--filter "rule=20,21,22,23"
--filter "rule=20-23"
```

Display all log entries generated by rules 20 to 23, 30 or 40 to 42:

```
--filter "rule=20-23,30,40-42"
```

Display all log entries to `10.1.1.1` and `10.1.1.2`:

```
--filter "dst=10.1.1.1,10.1.1.2"
```

Display all log entries from `192.168.1.0/255.255.255.0`:

```
--filter "src=192.168.1.0/255.255.255.0"
```

Display all log entries starting from `2004/03/02 14:00:00`:

```
--filter "starttime=20040302140000"
```

#### Checkpoint device configuration

Modify `$FWDIR/conf/fwopsec.conf` and define the port to be used for authenticated LEA connections (e.g. 18184):

```
lea_server port 0 
lea_server auth_port 18184 
lea_server auth_type sslca
```

Restart in order to activate changes:

```
cpstop; cpstart
```

Create a new OPSEC Application Object with the following details:

```
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

```
lea_server ip 10.1.1.1 
lea_server auth_port 18184 
lea_server auth_type sslca 
opsec_sslca_file opsec.p12 
opsec_sic_name "CN=myleaclient,O=cpmodule..gysidy"
lea_server opsec_entity_sic_name "cn=cp_mgmt,o=cpmodule..gysidy"
```

Get the tool `opsec_pull_cert` either from `opsec-tools.tar.gz` from the project home page or directly from the OPSEC SDK. This tool is needed to establish the Secure Internal Communication (SIC) between FW1-LogGrabber and the FW1 management server.

Get the clients certificate from the management station (e.g. `10.1.1.1`). The activation key has to be the same as specified before in the firewall policy. After that, copy the resulting PKCS#12 file (default name `opsec.p12`) to your FW1-LogGrabber directory.

```
opsec_pull_cert -h 10.1.1.1 -n myleaclient -p def456
```

#### Authenticated SSL OPSEC connections

##### Checkpoint device configuration

Modify `$FWDIR/conf/fwopsec.conf` and define the port to be used for authenticated LEA connections (e.g. 18184):

```
lea_server port 0 
lea_server auth_port 18184 
lea_server auth_type ssl_opsec
```

Restart in order to activate changes:

```
cpstop; cpstart
```

Set a password (e.g. `abc123`) for the LEA client (e.g. `10.1.1.2`):

```
fw putkey -ssl -p abc123 10.1.1.2
```

Create a new OPSEC Application Object with the following details:

```
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

##### FW1-LogGrabber configuration

Modify `$LOGGRABBER_CONFIG_PATH/lea.conf` and define the IP address of your FW1 management station (e.g. `10.1.1.1`) as well as port (e.g. `18184`), authentication type and SIC names for authenticated LEA connections. The SIC names you can get from the object properties of your LEA client object respectively the Management Station object (see above for details about Client DN and Server DN).

```
lea_server ip 10.1.1.1 
lea_server auth_port 18184 
lea_server auth_type ssl_opsec 
opsec_sslca_file opsec.p12 
opsec_sic_name "CN=myleaclient,O=cpmodule..gysidy"
lea_server opsec_entity_sic_name "cn=cp_mgmt,o=cpmodule..gysidy"
```

Set password for the connection to the LEA server. The password has to be the same as specified on the LEA server.

```
opsec_putkey -ssl -p abc123 10.1.1.1
```

Get the tool `opsec_pull_cert` either from `opsec-tools.tar.gz` from the project home page or directly from the OPSEC SDK. This tool is needed to establish the Secure Internal Communication (SIC) between FW1-LogGrabber and the FW1 management server.

Get the clients certificate from the management station (e.g. `10.1.1.1`). The activation key has to be the same as specified before in the firewall policy.

```
opsec_pull_cert -h 10.1.1.1 -n myleaclient -p def456
```

#### Authenticated OPSEC connections

##### Checkpoint device configuration

Modify `$FWDIR/conf/fwopsec.conf` and define the port to be used for authenticated LEA connections (e.g. 18184):

```
lea_server port 0 
lea_server auth_port 18184 
lea_server auth_type auth_opsec
```

Restart in order to activate changes

```
fwstop; fwstart
```

Set a password (e.g. `abc123`) for the LEA client (e.g. `10.1.1.2`).

```
fw putkey -opsec -p abc123 10.1.1.2
```

Add a rule to the policy to allow the port defined above from the FW1-LogGrabber machine to the FW1 management
server.

Finally, install the policy.

##### FW1-LogGrabber configuration

Modify `$LOGGRABBER_CONFIG_PATH/lea.conf` and define the IP address of your FW1 management station (e.g. `10.1.1.1`) as well as port (e.g. 18184) and authentication type for authenticated LEA connections:

```
lea_server ip 10.1.1.1 
lea_server auth_port 18184 
lea_server auth_type auth_opsec
```

Set password for the connection to the LEA server. The password has to be the same as specified on the LEA server.

```
opsec_putkey -p abc123 10.1.1.1
```

#### Unauthenticated connections

##### Checkpoint device configuration

Modify `$FWDIR/conf/fwopsec.conf` and define the port to be used for unauthenticated LEA connections (e.g. 50001):

```
lea_server port 50001 
lea_server auth_port 0
```

Restart in order to activate changes:

```
fwstop; fwstart  # for 4.1
cpstop; cpstart  # for NG
```

Add a rule to the policy to allow the port defined above from the FW1-LogGrabber machine to the FW1 management
server.

Finally, install the policy.

##### FW1-LogGrabber configuration

Modify `$LOGGRABBER_CONFIG_PATH/lea.conf` and define the IP address of your FW1 management station (e.g. `10.1.1.1`) and port (e.g. `50001`) for unauthenticated LEA connections:

```
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
							match => [ "[system][auth][timestamp]", 
							"MMM  d HH:mm:ss", 
						"MMM dd HH:mm:ss" 
						]
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

### Logstash - Filter "network" ##

This filter processing an event data with network type:

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
			   network => [ "0.0.0.0/32", "10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16", "fc00::/7", "127.0.0.0/8", "::1/128",
					"169.254.0.0/16", "fe80::/10","224.0.0.0/4", "ff00::/8","255.255.255.255/32" ]
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
		  match => [ "log_data",
			"MMM dd HH:mm:ss",
			"MMM  dd HH:mm:ss",
			"MMM dd HH:mm:ss.SSS",
			"MMM  dd HH:mm:ss.SSS",
			"ISO8601"
		  ]
		  target => "log_data"
		}
	
	 }
	}

### Logstash - Filter "geoip" ##

This filter processing an events data with IP address and check localization:

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


##### Input event

```ruby
{
    "@timestamp" => 2018-02-25T10:04:22.338Z,
    "@version" => "1",
    "myUid" => "u501565"
}
```

##### Logstash filter

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

##### Output event

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

#### Parameters availables

Here is a list of all parameters, with their default value, if any, and their description.

```
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
```

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

​		Sample dictionary file:

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
		output=`curl -s -k -u monitor:monitor "https://192.168.1.1/api/filter/count?query=%5Bhosts%5D%28address%20~~%20%22#	{checkip}%22%20%29" 2>&1`
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

	output {
		elasticsearch {
		   hosts => [ "127.0.0.1:9200" ]
	
		   index => "%{type}-%{+YYYY.MM.dd}"
	
		   user => "logstash"
		   password => "logstash"
		}
	}

### Logstash plugin for "naemon beat"

This Logstash plugin has example of complete configuration for integration with *naemon* application:

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

### Logstash plugin for "perflog"

This Logstash plugin has example of complete configuration for integration with perflog:


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
    

### Logstash plugin for LDAP data enrichement

1. Download logstash plugin with dependencies ![logstash-filter-ldap-0.2.4.zip](/files/logstash-filter-ldap-0.2.4.zip) and upload files to your server.

2. Unzip file.

3. Install logstash plugin.

	```/usr/share/logstash/bin/logstash-plugin install /directory/to/file/logstash-filter-ldap-0.2.4.gem```
	
4. Create new file in beats pipeline. To do this, go to beats folder (/etc/logstash/conf.d/beats) and create new config file, for example ```031-filter-ldap-enrichement.conf```

5. Below is an example of the contents of the configuration file:
	
	```filter {
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
	
	
6. Fields description

	```	identifier_value - Identifier of the value to search. If identifier type is uid, then the value should be the uid to search for.
	identifier_key - Type of the identifier to search.
	identifier_type - Object class of the object to search.
	host - LDAP server host adress.
	ldap_port - LDAP server port for non-ssl connection.
	username - Username to use for search in the database.
	password - Password of the account linked to previous username.
	search_dn - Domain name in which search inside the ldap database (usually your userdn or groupdn).
	enable_error_logging - When there is a problem with the connection with the LDAP database, write reason in the event.
	attributes - List of attributes to get. If not set, all attributes available will be get.

### Single password in all Logstash outputs

You can set passwords and other Logstash pipeline settings as environment variables. This can be useful if the password was changed for the `logastash` user and it must be to update in the configuration files.

Configuration steps:

1. Create the service file:

	mkdir –p /etc/systemd/system/logstash.service.d
	vi /etc/systemd/system/logstash.service.d/logstash.conf
	
			[Service]
			Environment="ELASTICSEARCH_ES_USER=logserver"
			Environment="ELASTICSEARCH_ES_PASSWD=logserver"

1. Reload systemctl daemon:

		systemctl daemon-reload

1. Sample definition of Logstash output pipline seciotn:

		output  {
		  elasticsearch {
		    index => "test-%{+YYYY.MM.dd}"
		    user => "${ELASTICSEARCH_ES_USER:elastic}"
		    password => "${ELASTICSEARCH_ES_PASSWD:changeme}"
		  }
		}

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

## Join
**Note**
***Before use *Join* upgrade *Log Server* to at least v7.1.1***

This plugin extends Elasticsearch with new search actions which enables possibility to perform a "Join" between two set of documents (in the same index or in different indexes).

Join is basically a inner join between two set of documents based on a common attribute, where the result only contains the attributes of one of the joined set of documents. 

Current implementation of Join, includes:
 - Inner join 
 - API extended with the _join method
 - Full support for query dsl
 - Possibility of use on the graphic interface (Dev Tools plugin)

![](/media/media/image231.png)

### Query Syntax 
#### Simple query
```
POST index-1,index-2/_join
{
  "left": {
    "field":"field-1",
    "query": {"match_all":{}}
  },
  "right": {
    "field":"field-2",
    "query": {"match_all":{}}
  },
  "out": {
    "field":"joined",
    "scroll_time": "1m",
    "batch":1000
  }
}
```
#### Complex query
```
POST index-1,index-2/_join
{
  "left": {
    "field":"field-1",
        "query": {
            "bool": {
              "should": [
                {"wildcard":{"field-1":{"value":"10.*"}}}
              ]
            }
          },
    "size": 100,
    "source": {
      "includes": [ "field-A", "field-B" ]
    }
  },
  "right": {
    "field":"field-2",
        "query": {
            "bool": {
              "must": [
                {"wildcard":{"field-2":{"value":"10.*"}}},
                {"term":{"field-3":{"value":"XXX"}}}
              ]
            }
          },
    "size": 1,
    "source": {
      "includes": [ "field-C", "field-D" ]
    }
  },
  "out": {
    "field":"joined",
    "scroll_time": "1m",
    "batch":1000
  }
}
```
### Filter interface

You can use "source_left" and/or "source_right" or neither in join query.
source fields can be:

* true, false, {} -- empty object, "*", or omitted -- means return everything
* "" -- empty string, return empty object for the hit
* "fieldPattern" -- string with patter
* ["fieldPattern1", "fieldPattern2"] -- list of field patterns
* {
        "includes": [ "tags", "re*" ],
        "excludes": [ "referer" ]
    } -- object with "includes" and/or "excludes" fields or neither

Patterns examples:
"tags", "*.lon", "*.lat", "Flight*", "*ht*", "g*o.l*"

by default all sources are returned:
```

POST kibana_sample_data_flights,kibana_sample_data_logs/_join
{
  "left": {
    "field": "DestCountry",
    "query": {"term": {"DestCountry": {"value": "AE"}}}
  }

  "right": {
    "field": "geo.dest",
    "query": {"term": {"geo.dest": {"value": "AE"}}}
  }

  "out": {
    "field": "joined_field",
    "scroll_time": "1m",
    "batch": 100
  }
}
>>
{
  "hits" : {
    "total" : {
      "value" : 92,
      "relation" : "eq"
    },
    "max_score" : 0.0,
    "hits" : [
      {
        "_index" : "kibana_sample_data_flights",
        "_type" : "_doc",
        "_id" : "rvy5qXwBqY4c6J5A_fe7",
        "_score" : 5.637857,
        "_source" : {
          "Cancelled" : false,
          "joined_field" : [
            {
              "referer" : "http://www.elastic-elastic-elastic.com/success/thomas-d-jones",
              "request" : "/beats/metricbeat/metricbeat-6.3.2-amd64.deb",
              "agent" : "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
              "extension" : "deb",
              "ip" : "17.86.191.67",
```


Same effect will be if we specify "source_left/right":"true" as source value:

```
POST kibana_sample_data_flights,kibana_sample_data_logs/_join
{
  "left": {
    "field": "DestCountry",
    "query": {"term": {"DestCountry": {"value": "AE"}}},
    "source": true
  }

  "right": {
    "field": "geo.dest",
    "query": {"term": {"geo.dest": {"value": "AE"}}},
    "source": true
  }

  "out": {
    "field": "joined_field",
    "scroll_time": "1m",
    "batch": 100
  }
}
```

"source_left/right":"false" will be ignored, if you really want to ignore source of parent or children
use empty string "source_left/right":

```
POST kibana_sample_data_flights,kibana_sample_data_logs/_join
{
  "left": {
    "field": "DestCountry",
    "query": {"term": {"DestCountry": {"value": "AE"}}},
    "source": ""
  }

  "right": {
    "field": "geo.dest",
    "query": {"term": {"geo.dest": {"value": "AE"}}},
    "source": ""
  }

  "out": {
    "field": "joined_field",
    "scroll_time": "1m",
    "batch": 100
  }
}
>>>
{
  "hits" : {
    "total" : {
      "value" : 92,
      "relation" : "eq"
    },
    "max_score" : 0.0,
    "hits" : [
      {
        "_index" : "kibana_sample_data_flights",
        "_type" : "_doc",
        "_id" : "rvy5qXwBqY4c6J5A_fe7",
        "_score" : 5.637857,
        "_source" : {
          "joined_field" : [
            { },
            { },
            { },
            { },
            { },
            { },
            { },
            { },
            { },
            { },
            { },
            { }
          ]
        }
      },
```

You can use simple string patterns:

```
POST kibana_sample_data_flights,kibana_sample_data_logs/_join
{
  "left": {
    "field": "DestCountry",
    "query": {"term": {"DestCountry": {"value": "AE"}}},
    "source": "Flight*"
  }

  "right": {
    "field": "geo.dest",
    "query": {"term": {"geo.dest": {"value": "AE"}}},
    "source": "client*"
  }

  "out": {
    "field": "joined_field",
    "scroll_time": "1m",
    "batch": 100
  }
}
>>>
{
  "hits" : {
    "total" : {
      "value" : 92,
      "relation" : "eq"
    },
    "max_score" : 0.0,
    "hits" : [
      {
        "_index" : "kibana_sample_data_flights",
        "_type" : "_doc",
        "_id" : "rvy5qXwBqY4c6J5A_fe7",
        "_score" : 5.637857,
        "_source" : {
          "FlightNum" : "BPD98PD",
          "FlightDelay" : false,
          "FlightTimeHour" : 4.603366103053058,
          "FlightTimeMin" : 276.20196618318346,
          "FlightDelayMin" : 0,
          "joined_field" : [
            {
              "clientip" : "17.86.191.67"
            },
            {
              "clientip" : "154.128.131.34"
            },
            {
              "clientip" : "239.67.210.53"
            },
```


You can combine different ways of specifying filters:

```
POST kibana_sample_data_flights,kibana_sample_data_logs/_join
{
  "left": {
    "field": "DestCountry",
    "query": {"term": {"DestCountry": {"value": "AE"}}},
    "source": {
      "includes": "Orig*",
      "excludes": [ "*.lat" ]
    }
  }

  "right": {
    "field": "geo.dest",
    "query": {"term": {"geo.dest": {"value": "AE"}}},
    "source": {
      "includes": [ "tags", "re*" ],
      "excludes": "*onse"
    }
  }

  "out": {
    "field": "joined_field",
    "scroll_time": "1m",
    "batch": 100
  }
}
>>>
{
  "hits" : {
    "total" : {
      "value" : 92,
      "relation" : "eq"
    },
    "max_score" : 0.0,
    "hits" : [
      {
        "_index" : "kibana_sample_data_flights",
        "_type" : "_doc",
        "_id" : "rvy5qXwBqY4c6J5A_fe7",
        "_score" : 5.637857,
        "_source" : {
          "Origin" : "Cologne Bonn Airport",
          "OriginLocation" : {
            "lon" : "7.142739773"
          },
          "OriginWeather" : "Thunder & Lightning",
          "OriginCityName" : "Cologne",
          "OriginCountry" : "DE",
          "joined_field" : [
            {
              "referer" : "http://www.elastic-elastic-elastic.com/success/thomas-d-jones",
              "request" : "/beats/metricbeat/metricbeat-6.3.2-amd64.deb",
              "tags" : [
                "success",
                "info"
              ]
            },
            {
              "referer" : "http://twitter.com/success/steven-r-nagel",
              "request" : "/elasticsearch",
              "tags" : [
                "success",
                "security"
              ]
            },
```

### Scroll interface

List all active join scrolls:

```
GET _join/_all
>>>
{
  "keys" : [
    "ruzwsksdbhyxcgikljiaogrdozttswwpfqbmrrrlgbtgbqdxpg",
    "gtqviwpmhowdlkmustlqenegfpucojiewlvuxtdmhemdkixmrz",
    "fhrsfecirojrmjtwzwlsyfbnhgqeizjbawwmqryguvtdmtefgy",
    "sgimqhproexwcnlskdggvowqwbyhborrczqajculpzjtjbznbo",
    "ekdtmyomzwjmmhdrcnznuebqgtpcrrfvfdjnphnzdmmtmdbaic",
    "dycswnigareojnngyudjbddzcnawyoqyvlmhwcwfwwszwgckxh"
  ]
}
```

Request with batch size smaller than number of hits

```
POST /kibana_sample_data_ecommerce,kibana_sample_data_flights/_join
{
  "left": {
    "field": "geoip.city_name",
    "query": {
      "term": {
        "geoip.city_name": {
          "value": "Istanbul"
        }
      }
    }
  },

  "right": {
    "field": "DestCityName",
    "query": {
      "term": {
        "DestWeather": {
          "value": "Sunny"
        }
      }
    }
  },

  "out": {
    "field": "flights",
    "scroll_time": "30m",
    "batch":100
  }
}
>>>
{
  "_scroll_id" : "qwhnoxnjihhqokcphoiffxzmjcniambrmbxgmxxykusyymobrp",
  "hits" : {
    "total" : {
      "value" : 100,
      "relation" : "eq"
    },
    "max_score" : 0.0,
    "hits" : [
      {
        "_index" : "kibana_sample_data_ecommerce",
        "_type" : "_doc",
        "_id" : "B_0WbXwBixBDsVfntYZX",
        "_score" : 2.881619,
        "_source" : {
          "geoip" : {
            "continent_name" : "Asia",
```

Pagination using scroll_id:

```
POST /_join
{
  "scroll_id":"qwhnoxnjihhqokcphoiffxzmjcniambrmbxgmxxykusyymobrp"
}
>>>
{
  "scroll_id" : "qwhnoxnjihhqokcphoiffxzmjcniambrmbxgmxxykusyymobrp",
  "hits" : {
    "total" : {
      "value" : 100,
      "relation" : "eq"
    },
    "max_score" : 0.0,
    "hits" : [
      {
        "_index" : "kibana_sample_data_ecommerce",
        "_type" : "_doc",
        "_id" : "W_0WbXwBixBDsVfnt4yV",
        "_score" : 2.881619,
        "_source" : {
          "geoip" : {
            "continent_name" : "Asia",
```

Last page will have no scroll_id:

```
POST /_join
{
  "scroll_id":"qwhnoxnjihhqokcphoiffxzmjcniambrmbxgmxxykusyymobrp"
}
>>>
{
  "hits" : {
    "total" : {
      "value" : 29,
      "relation" : "eq"
    },
    "max_score" : 0.0,
    "hits" : [
      {
        "_index" : "kibana_sample_data_ecommerce",
        "_type" : "_doc",
        "_id" : "o_0WbXwBixBDsVfnu5Uc",
        "_score" : 2.881619,
        "_source" : {
          "geoip" : {
            "continent_name" : "Asia",
```

If you try to scroll more it will raise an error:

```
POST /_join
{
  "scroll_id":"qwhnoxnjihhqokcphoiffxzmjcniambrmbxgmxxykusyymobrp"
}
>>>
{
  "error": {
    "root_cause": [
      {
        "type": "illegal_argument_exception",
        "reason": "scroll_id is not known or expired"
      }
    ],
    "type": "illegal_argument_exception",
    "reason": "scroll_id is not known or expired"
  },
  "status": 400
}
```

### Examples


This chapter contains examples of how to use the plugin join. For proper work, Logserver should be feeded with sample indexes with data

Action required:
```
curl -s -k -X POST -ulogserver:logserver "https://127.0.0.1:5601/api/sample_data/ecommerce" -H 'kbn-xsrf: true' -H 'Content-Type: application/json'
curl -s -k -X POST -ulogserver:logserver "https://127.0.0.1:5601/api/sample_data/flights" -H 'kbn-xsrf: true' -H 'Content-Type: application/json'
curl -s -k -X POST -ulogserver:logserver "https://127.0.0.1:5601/api/sample_data/logs" -H 'kbn-xsrf: true' -H 'Content-Type: application/json'
```
#### Example 1

Left query:
```
POST kibana_sample_data_flights/_search
{
  "query": {
    "term": {"DestCountry": {"value": "AE"}}
  }
}
```

Right query:
```
POST kibana_sample_data_logs/_search
{
  "query": {
    "term": {"geo.dest": {"value": "AE"}}
  }
}
```

Join query:
```
POST kibana_sample_data_flights,kibana_sample_data_logs/_join
{
  "left": {
    "field": "DestCountry",
    "query": {"term": {"DestCountry": {"value": "AE"}}}
  },

  "right: {
    "field": "geo.dest",
    "query": {"term": {"geo.dest": {"value": "AE"}}}
  },

  "out": {
    "field": "joined_field",
    "scroll_time": "1m",
    "batch": 100
  }
}
```


#### Example 2
```
POST kibana_sample_data_ecommerce,kibana_sample_data_flights/_join
{
  "left": {
    "field":"geoip.city_name",
    "query": {"term": {"geoip.city_name": {"value":"Istanbul"}}}
  },

  "right": {
    "field":"DestCityName",
    "query": {"term": {"DestWeather": {"value":"Sunny"}}}
  },

  "out": {
    "field":"flights",
    "scroll_time": "1m",
    "batch":1000
  }
}
```

#### Example 3
```
POST kibana_sample_data_ecommerce,kibana_sample_data_flights/_join
{
  "left": {
    "field":"geoip.city_name",
    "query": {"match_all":{}}
  },

  "right": {
    "field":"DestCityName",
    "query": {"match_all":{}}
  },

  "out": {
    "field_out":"flights",
    "scroll_time": "1m"
  }
}
```

#### Example 4 - correlation (httpd and winlogbeat)

```
POST httpd-*,winlogbeat2*/_join
{
  "left": {
    "field":"client.ip",
        "query": {
            "bool": {
              "should": [
                {"wildcard":{"client.ip":{"value":"10.4.4.3"}}}
              ]
            }
          },
    "size": 100,
    "source": {
      "includes": [ "domain", "client.ip" ]
    }
  },
  "right": {
    "field":"host.ip",
        "query": {
            "bool": {
              "must": [
                {"wildcard":{"host.ip":{"value":"10.*"}}},
                {"term":{"winlog.event_id":{"value":"5379"}}}
              ]
            }
          },
    "size": 1,
    "source": {
      "includes": [ "@timestamp", "host.name", "winlog.event_data.SubjectUserName" ]
    }
  },
  "out": {
    "field":"correlated",
    "scroll_time": "1m",
    "batch":1000
  }
}
```

#### Example 5 - correlation (dhcpd and winlogbeat)
```
POST syslog-*,winlogbeat2*/_join
{
  "left": {
    "field":"client.mac",
        "query": {
            "bool": {
              "must": [
                {"wildcard":{"client.ip":{"value":"10.4.4.3"}}},
                {"term":{"program":{"value":"dhcpd"}}}
              ]
            }
          },
    "size": 100,
    "source": {
      "includes": [ "client.ip", "client.mac" ]
    }
  },
  "right": {
    "field":"host.mac",
        "query": {
            "bool": {
              "must": [
                {"wildcard":{"host.ip":{"value":"10.4.4.*"}}}
              ]
            }
          },
    "size": 1,
    "source": {
      "includes": [ "@timestamp", "host.name", "host.mac", "winlog.event_data.SubjectUserName", "event_data.TargetUserName" ]
    }
  },
  "out": {
    "field":"correlated",
    "scroll_time": "1m",
    "batch":1000
  }
}
```

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
*	Download: Click the Download button under the Automation menu in the sidebar. This will download the automation as a JSON file.
*	Copy-Paste: Select all the automation nodes in the Automation UI, copy them (Ctrl + c), then paste them (Ctrl + v) in your desired file.
You can import JSON files as automations in two ways:
*	Import: Click Import from File or Import from URL under the Automation menu in the sidebar and select the JSON file or paste the link to a automation.
*	Copy-Paste: Copy the JSON automation to the clipboard (Ctrl + c) and paste it (Ctrl + v) into the Automation UI.

**Automation settings**

On each automation, it is possible to set some custom settings and overwrite some of the global default settings from the Automation > Settings menu.

![](/media/media/workflow-settings.png)
 
The following settings are available:
*	Error Automation: Select a automation to trigger if the current automation fails. 
*	Timezone: Sets the timezone to be used in the automation. The Timezone setting is particularly important for the Cron Trigger node.
*	Save Data Error Execution: If the execution data of the automation should be saved when the automation fails.
*	Save Data Success Execution: If the execution data of the automation should be saved when the automation succeeds.
*	Save Manual Executions: If executions started from the Automation UI should be saved.
*	Save Execution Progress: If the execution data of each node should be saved. If set to "Yes", the automation resumes from where it stopped in case of an error. However, this might increase latency.
*	Timeout Automation: Toggle to enable setting a duration after which the current automation execution should be cancelled.
*	Timeout After: Only available when Timeout Automation is enabled. Set the time in hours, minutes, and seconds after which the automation should timeout. 

**Failed automations**

If your automation execution fails, you can retry the execution. To retry a failed automation:
1.	Open the Executions list from the sidebar.
2.	For the automation execution you want to retry, click on the refresh icon under the Status column.
3.	Select either of the following options to retry the execution: 
*	Retry with currently saved automation: Once you make changes to your automation, you can select this option to execute the automation with the previous execution data.
*	Retry with original automation: If you want to retry the execution without making changes to your automation, you can select this option to retry the execution with the previous execution data.

You can also use the Error Trigger node, which triggers a automation when another automation has an error. Once a automation fails, this node gets details about the failed automation and the errors.

### Connection

A connection establishes a link between nodes to route data through the automation. A connection between two nodes passes data from one node's output to another node's input. Each node can have one or multiple connections.

To create a connection between two nodes, click on the grey dot on the right side of the node and slide the arrow to the grey rectangle on the left side of the following node.

##### Example

An IF node has two connections to different nodes: one for when the statement is true and one for when the statement is false.

![](/media/media/Connection_ifnode.8e006dce.gif)

### Automations List

This section includes the operations for creating and editing automations.

* **New**: Create a new automation
* **Open**: Open the list of saved automations
* **Save**: Save changes to the current automation
* **Save As**: Save the current automation under a new name
* **Rename**: Rename the current automation
* **Delete**: Delete the current automation
* **Download**: Download the current automation as a JSON file
* **Import from URL**: Import a automation from a URL
* **Import from File**: Import a automation from a local file
* **Settings**: View and change the settings of the current automation

### Credentials

This section includes the operations for creating credentials.

Credentials are private pieces of information issued by apps/services to authenticate you as a user and allow you to connect and share information between the app/service and the n8n node.

* **New**: Create new credentials
* **Open**: Open the list of saved credentials

### Executions

This section includes information about your automation executions, each completed run of a automation.

You can enabling logging of your failed, successful, and/or manually selected automations using the Automation > Settings page.

### Node

A node is an entry point for retrieving data, a function to process data, or an exit for sending data. The data process performed by nodes can include filtering, recomposing, and changing data.

There may be one or several nodes for your API, service, or app. By connecting multiple nodes, you can create simple and complex automations. When you add a node to the Editor UI, the node is automatically activated and requires you to configure it (by adding credentials, selecting operations, writing expressions, etc.).

There are three types of nodes:

* Core Nodes
* Regular Nodes
* Trigger Nodes

#### Core nodes

Core nodes are functions or services that can be used to control how automations are run or to provide generic API support.

Use the Start node when you want to manually trigger the automation with the `Execute Automation` button at the bottom of the Editor UI. This way of starting the automation is useful when creating and testing new automations.

If an application you need does not have a dedicated Node yet, you can access the data by using the HTTP Request node or the Webhook node. You can also read about creating nodes and make a node for your desired application.


#### Regular nodes

Regular nodes perform an action, like fetching data or creating an entry in a calendar. Regular nodes are named for the application they represent and are listed under Regular Nodes in the Editor UI.

![](/media/media/Regular_nodes.d3cec3e9.png)

##### Example

A Google Sheets node can be used to retrieve or write data to a Google Sheet.

![](/media/media/Google_sheets.d9ee72a3.png)

#### Trigger nodes

Trigger nodes start automations and supply the initial data.

![](/media/media/Trigger_nodes.5bd536aa.png)

Trigger nodes can be app or core nodes.

* **Core Trigger nodes** start the automation at a specific time, at a time interval, or on a webhook call. For example, to get all users from a Postgres database every 10 minutes, use the Interval Trigger node with the Postgres node.

* **App Trigger nodes** start the automation when an event happens in an app. App Trigger nodes are named like the application they represent followed by "Trigger" and are listed under Trigger Nodes in the Editor. For example, a Telegram trigger node can be used to trigger a automation when a message is sent in a Telegram chat.

![](/media/media/telegram_trigger.fae8dcd9.png)

#### Node settings

Nodes come with global **operations** and **settings**, as well as app-specific **parameters** that can be configured.

##### Operations

The node operations are illustrated with icons that appear on top of the node when you hover on it:
* **Delete**: Remove the selected node from the automation
* **Pause**: Deactivate the selected node
* **Copy**: Duplicate the selected node
* **Play**: Run the selected node

![](/media/media/Node_settings.36ddf764.gif)

To access the node parameters and settings, double-click on the node.

##### Parameters

The node parameters allow you to define the operations the node should perform. Find the available parameters of each node in the node reference.

##### Settings

The node settings allow you to configure the look and execution of the node. The following options are available:

* **Notes**: Optional note to save with the node
* **Display note in flow**: If active, the note above will be displayed in the automation as a subtitle
* **Node Color**: The color of the node in the automation
* **Always Output Data**: If active, the node will return an empty item even if the node returns no data during an initial execution. Be careful setting this on IF nodes, as it could cause an infinite loop.
* **Execute Once**: If active, the node executes only once, with data from the first item it receives.
* **Retry On Fail**: If active, the node tries to execute a failed attempt multiple times until it succeeds
* **Continue On Fail**: If active, the automation continues even if the execution of the node fails. When this happens, the node passes along input data from previous nodes, so the automation should account for unexpected output data.

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
4. As Value 1 type or select a field which you want use. In this example we use expression {{ $json["host"]["name"] }}
5. As Value 2 type host name which you want to process. In this example we use paloalto.paseries.test
6. Next you can select any other node for further process filtered message.

#### Example Case usage

1. Create Case node
2. Select Rules on Mode 
3. Select String on Data Type
4. As Value 1 type or select a field which you want use. In this example we use expression {{ $json["host"]["name"] }}
5. Click Add Routing Rule
6. As Value 2 type host name which you want to process. In this example we use paloalto.paseries.test
7. As Output type 0.

You can add multiple conditions. On one node you can add 3 conditions if you need more then add to latest output next node and select this node as Fallback Output.

#### IF

The IF node is used to split a workflow conditionally based on comparison operations.

##### Node Reference

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

##### Node Reference

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

##### Basic Operations

- Read from file
- Write to file

##### Node Reference

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


