# SIEM Plan

SIEM Plan provides access to a database of hundreds of predefined correlation rules and sets of ready-made visualizations and dashboards that give a quick overview of the organizations security status. At the same time, the system still provides a great flexibility in building your own correlation rules and visualizations exactly as required by your organization.

System responds to the needs of today’s organizations by allowing identification of threats on the basis of a much larger amount of data, not always related to the security area as it is provided by traditional SIEM systems.

Product contains deep expert knowledge about security posture. Using entire ecosystem of correlation rules, security dashboards with ability to create electronic documentation SIEM PLAN allows You to score the readiness of Your organization to prevent cyber-attacks. Embedded integration with MITRE ATT&CK quickly identifies unmanaged areas where Your organization potentially needs improvements. Security design will be measured and scored . Single screen will show You potential risk and the consequences of an attack hitting any area of the organization.

Use SIEM Plan do prevent loss of reputation, data leakage, phishing or any other cyber-attack and stay safe.

## Alert Module

### Enabling the Alert Module

### SMTP server configuration

To configuring STMP server for email notification you should:

- edit `/opt/alert/config.yml` and add the following section:

  ```bash
  # email conf
  smtp_host: "mail.example.conf"
  smtp_port: 587
  smtp_ssl: false
  from_addr: "siem@example.com"
  smtp_auth_file: "/opt/alert/smtp_auth_file.yml"
  ```

- add the new `/opt/alert/smtp_auth_file.yml` file:

  ```bash
  user: "user"
  password: "password"
  ```

- restart `alert` service:

  ```bash
  systemctl restat alert
  ```


### Creating Alerts

To create the alert, click the "Alerts" button from the main menu bar.

 ![](/media/media/image93.png)

We will display a page with tree tabs: Create new alerts in „Create
alert rule", manage alerts in „Alert rules List" and check alert
status „Alert Status".

 In the alert creation windows we have an alert creation form:

 ![](/media/media/image92.PNG)

 - **Name** - the name of the alert, after which we will recognize and
search for it.
- **Index pattern** - a pattern of indexes after which the alert will be
searched.
- **Role** - the role of the user for whom an alert will be available
- **Type** - type of alert
- **Description** - description of the alert.
- **Example** - an example of using a given type of alert. Descriptive
field
- **Alert method** - the action the alert will take if the conditions are
met (sending an email message or executing a command)
- **Any** - additional descriptive field.# List of Alert rules #

The "Alert Rule List" tab contain complete list of previously created 
alert rules:

![](/media/media/image94.png)

In this window, you can activate / deactivate, delete and update alerts 
by clicking on the selected icon with the given alert: ![](/media/media/image63.png).

### Alerts status

In the "Alert status" tab, you can check the current alert status: if
it activated, when it started and when it ended, how long it lasted,
how many event sit found and how many times it worked.

![](/media/media/image95.png)

Also, on this tab, you can recover the alert dashboard, by clicking the "Recovery Alert Dashboard" button.

### Alert Types

The various Rule Type classes, defined in Energy Logserver. 
An instance is held in memory for each rule, passed all of the data returned by querying Elasticsearch 
with a given filter, and generates matches based on that data.

#### Any

The any rule will match everything. Every hit that the query returns will generate an alert.

#### Blacklist

The blacklist rule will check a certain field against a blacklist, and match if it is in the blacklist.

#### Whitelist

Similar to blacklist, this rule will compare a certain field to a whitelist, and match if the list does not contain the term.

#### Change

This rule will monitor a certain field and match if that field changes.

#### Frequency

This rule matches when there are at least a certain number of events in a given time frame.

#### Spike

This rule matches when the volume of events during a given time period is spike_height times larger or smaller than during the previous time period.

#### Flatline

This rule matches when the total number of events is under a given threshold for a time period.

#### New Term

This rule matches when a new value appears in a field that has never been seen before.

#### Cardinality

This rule matches when a the total number of unique values for a certain field within
a time frame is higher or lower than a threshold.

#### Metric Aggregation

This rule matches when the value of a metric within the calculation window is higher or lower than a threshold.

#### Percentage Match

This rule matches when the percentage of document in the match bucket within a calculation window is higher or lower than a threshold.

#### Unique Long Term

This rule matches when there are values of compare_key in each checked timeframe.

#### Find Match

Rule match when in defined period of time, two correlated documents match certain strings.

#### Consecutive Growth

Rule matches for value difference between two aggregations calculated for different periods in time.

#### Logical

Rule matches when a complex, logical criteria is met. Rule can be use for alert data correlation.

An example of using the Logical rule type.

![](/media/media/image149.png)

Alerts that must occur for the rule to be triggered:

- Switch - Port is off-line - the alert must appear 5 times.
  - OR
- Switch - Port is on-line - the alert must appear 5 times.

If both of the above alerts are met within no more than 5 minutes and the values of the "port_number" field are related to each other, the alert rule is triggered. It is possible to use logical connectives such as: OR, AND, NOR, NAND, XOR.

#### Chain

Rule matches when a complex, logical criteria is met. Rule can be use for alert data correlation.

An example of using the Chain rule type.

![](/media/media/image148.png)

Alerts that must occur for the rule to be triggered:

- Linux - Login Failure - the alert must appear 10 times.
- AND
- Linux - Login Success - 1 time triggered alert.

If the sequence of occurrence of the above alerts is met within 5 minutes and the values of the "username" field are related to each other, the alert rule is triggered. The order in which the component alerts occur is important.

#### Difference

This rule calculates percentage difference between aggregations for two non-overlapping time windows.

Let’s assume x represents the current time (i.e. when alert rule is run) then the relation between historical and present time windows is described by the inequality:
```
<x – agg_min – delta_min; x – delta_min> <= <x – agg_min; x>; where x – delta_min <= x – agg_min => delta_min >= agg_min
```
The percentage difference is then described by the following equation:
```
d = | avg_now – avg_history | / max(avg_now, avg_history) * 100; for (avg_now – avg_history != 0; avg_now != 0; avg_history != 0)
d = 0; (in other cases)
```
`avg_now` is the arithmetic mean of `<x – agg_min; x>`
`avg_history` is the arithmetic mean of `<x – agg_min – delta_min; x – delta_min>`

Required parameters:

- Enable the rule by setting type field.
`type: difference`
- Based on the compare_key field aggregation is calculated.
`compare_key: value`
- An alert is triggered when the percentage difference between aggregations is higher than the specified value.
`threshold_pct: 10`
- The difference in minutes between calculated aggregations.
`delta_min: 3`
- Aggregation bucket (in minutes).
`agg_min: 1`

Optional parameters:

If present, for each unique `query_key` aggregation is calculated (it needs to be of type keyword).
`query_key: hostname`

### Alert Methods

When the alert rule is fulfilled, the defined action is performed - the alert method.
The following alert methods have been predefined in the system:

- email;
- commands;
- user;

#### Email

Method that sends information about an alert to defined email addresses.

#### User

Method that sends information about an alert to defined system users.

#### Command

 A method that performs system tasks. For example, it triggers a script that creates a new event in the customer ticket system.

Below is an example of an alert rule definition that uses the "command" alert method to create and recover an ticket in the client's request system:

```bash
index: op5-*
name: change-op5-hoststate
type: change

compare_key: hoststate
ignore_null: true
query_key: hostname

filter:
- query_string:
    query: "_exists_: hoststate AND datatype: \"HOSTPERFDATA\" AND _exists_: hostname"

realert:
  minutes: 0
alert: "command"
command: ["/opt/alert/send_request_change.sh", "5", "%(hostname)s", "SYSTEM_DOWN", "HOST", "Application Collection", "%(hoststate)s", "%(@timestamp)s"]
```

The executed command has parameters which are the values of the fields of the executed alert. Syntax: `%(fields_name)`.

#### The Hive

The alert module can forward information about the alert to *Security Incident Response Platform* **TheHive**.

The configuration of the **Hive Alert** should be done in the definition of the `Rule Definition` alert using the following options:

- `hive_alert_config_type: classic` - allows the use of variables to build The Hive alert
- `hive_alert_config`:
  - `title` (text) : title of the alert (ignored in `classic` config type)
  - `description` (text) : description of the alert (ignored in `classic` config type)
  - `severity` (number) : severity of the alert (1: low; 2: medium; 3: high) **default=2**
  - `date` (date) : date and time when the alert was raised **default=now**
  - `tags` (multi-string) : case tags **default=empty**
  - `tlp` (number) : [TLP](https://www.us-cert.gov/tlp) (`0`: `white`; `1`: `green`; `2: amber`; `3: red`) **default=2**
  - `status` (AlertStatus) : status of the alert (*New*, *Updated*, *Ignored*, *Imported*) **default=New**
  - `type` (string) : type of the alert (read only)
  - `source` (string) : source of the alert (read only)
  - `sourceRef` (string) : source reference of the alert (read only)
  - `artifacts` (multi-artifact) : artifact of the alert. It is a array of JSON object containing artifact attributes **default=empty**
  - `follow` (boolean) : if true, the alert becomes active when updated **default=true**
- `hive_observable_data_mapping` - mapping field values to the The Hive alert.

**Note:** When use: `hive_alert_config_type: classic` the following parameters are ignored:

```yaml
hive_alert_config:
    title: title of the alert
    description: description of the alert
```

and you should use:

```yaml
alert_subject: "title of the alert"
alert_text: "description of the alert"
```

Example of configuration:

```bash
hive_alert_config_type: classic

hive_alert_config:
  type: 'test'
  source: 'elastalert-{rule[name]}'
  severity: 3
  tags: ['malicious behavior']
  tlp: 2
  status: 'New'
  follow: True

hive_observable_data_mapping:
  - ip: "{match[field1]}"
  - source: "{match[field2]}"
```

#### RSA Archer

The alert module can forward information about the alert to the risk management platfrorm **RSA Archer**.

The alert rule must be configure to use **Command** alert method witch execute the following scripts `ucf.sh` or `ucf2.sh`

Configuration steps:

1. Copy and save on the Energy Logserver server the following scripts to appropriate location, for example `/opt/alert/bin`:

   - ucf.sh - for SYSLOG

      ```bash
      #!/usr/bin/env bash
      base_url = "http://localhost/Archer" ##set the appropriate Archer URL
      
      logger -n $base_url -t logger -p daemon.alert -T "CEF:0|LogServer|LogServer|${19}|${18}| TimeStamp=$1 DeviceVendor/Product=$2-$3 Message=$4 TransportProtocol=$5 Aggregated:$6 AttackerAddress=$7 AttackerMAC=$8 AttackerPort=$9 TargetMACAddress=${10} TargetPort=${11} TargetAddress=${12} FlexString1=${13} Link=${14} ${15} $1 ${16} $7 ${17}"
      ```

   - ucf2.sh - for REST API

      ```bash
      #!/usr/bin/env bash
      base_url = "http://localhost/Archer" ##set the appropriate Archer URL
      instance_name = "Archer"
      username = "apiuser"
      password = "Archer"

      curl -k -u $username:$password -H "Content-Type: application/xml" -X POST "$base_url:50105/$instance_name" -d {
      "CEF":"0","Server":"LogServer","Version":"${19}","NameEvent":"${18}","TimeStamp":"$1","DeviceVendor/Product":"$2-$3","Message""$4","TransportProtocol":"$5","Aggregated":"$6","AttackerAddress":"$7","AttackerMAC":"$8","AttackerPort":"$9","TargetMACAddress":"${10}","TargetPort":"${11}","TargetAddress":"${12}","FlexString1":"${13}","Link":"${14}","EventID":"${15}","EventTime":"${16}","RawEvent":"${17}"
      }
      ```
 
2. Alert rule definition: 

   - Index Pattern: `alert*`
   - Name: `alert-sent-to-rsa`
   - Rule Type: `any`
   - Rule Definition:
      
      ```bash
      filter:
      - query:
          query_string:
            query: "_exists_: endTime AND _exists_: deviceVendor AND _exists_: deviceProduct AND _exists_: message AND _exists_: transportProtocol AND _exists_: correlatedEventCount AND _exists_: attackerAddress AND _exists_: attackerMacAddress AND _exists_: attackerPort AND _exists_: targetMacAddress AND _exists_: targetPort AND _exists_: targetAddress AND _exists_: flexString1 AND _exists_: deviceCustomString4 AND _exists_: eventId AND _exists_: applicationProtocol AND _exists_: rawEvent"

      include:
      - endTime
      - deviceVendor
      - deviceProduct
      - message
      - transportProtocol
      - correlatedEventCount
      - attackerAddress
      - attackerMacAddress
      - attackerPort
      - targetMacAddress
      - targetPort
      - targetAddress
      - flexString1
      - deviceCustomString4
      - eventId
      - applicationProtocol
      - rawEvent

      realert:
        minutes: 0
      ```

   - Alert Method: `command`
   - Path to script/command: `/opt/alert/bin/ucf.sh`

### Alert Content

There are several ways to format the body text of the various types of events. In EBNF::

    rule_name           = name
    alert_text          = alert_text
    ruletype_text       = Depends on type
    top_counts_header   = top_count_key, ":"
    top_counts_value    = Value, ": ", Count
    top_counts          = top_counts_header, LF, top_counts_value
    field_values        = Field, ": ", Value

Similarly to ``alert_subject``, ``alert_text`` can be further formatted using standard Python formatting syntax.
The field names whose values will be used as the arguments can be passed with ``alert_text_args`` or ``alert_text_kw``.
You may also refer to any top-level rule property in the ``alert_subject_args``, ``alert_text_args``, ``alert_missing_value``, and ``alert_text_kw fields``.  However, if the matched document has a key with the same name, that will take preference over the rule property.

By default::

    body                = rule_name
    
                          [alert_text]
    
                          ruletype_text
    
                          {top_counts}
    
                          {field_values}

With ``alert_text_type: alert_text_only``::

    body                = rule_name
    
                          alert_text

With ``alert_text_type: exclude_fields``::

    body                = rule_name
    
                          [alert_text]
    
                          ruletype_text
    
                          {top_counts}

With ``alert_text_type: aggregation_summary_only``::

    body                = rule_name
    
                          aggregation_summary

ruletype_text is the string returned by RuleType.get_match_str.

field_values will contain every key value pair included in the results from Elasticsearch. These fields include "@timestamp" (or the value of ``timestamp_field``),
every key in ``include``, every key in ``top_count_keys``, ``query_key``, and ``compare_key``. If the alert spans multiple events, these values may
come from an individual event, usually the one which triggers the alert.

When using ``alert_text_args``, you can access nested fields and index into arrays. For example, if your match was ``{"data": {"ips": ["127.0.0.1", "12.34.56.78"]}}``, then by using ``"data.ips[1]"`` in ``alert_text_args``, it would replace value with ``"12.34.56.78"``. This can go arbitrarily deep into fields and will still work on keys that contain dots themselves.

### Example of rules ##

#### Unix - Authentication Fail ###

- index pattern: 

		syslog-*

- Type:

		Frequency

- Alert Method:

		Email

- Any:

		num_events: 4
		timeframe:
		  minutes: 5
	
	
		filter:
		- query_string:
		    query: "program: (ssh OR sshd OR su OR sudo) AND message: \"Failed password\""

#### Windows - Firewall disable or modify ###

- index pattern: 

		beats-*

- Type:

		Any

- Alert Method:

		Email

- Any:

filter:

		- query_string:
		       query: "event_id:(4947 OR 4948 OR 4946 OR 4949 OR 4954 OR 4956 OR 5025)"

### SIEM Rules

Beginning with version 6.1.7, the following SIEM rules are delivered with the product.

````md
| Nr. | Architecture/Application | Rule Name                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Index name   | Requirements                                     | Source                       | Time definition            | Threashold |
|-----|--------------------------|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|--------------------------------------------------|------------------------------|----------------------------|------------|
| 1   | Windows                  | Windows - Admin night logon                                  | Alert on Windows login events when detected outside business hours                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min                 | 1          |
| 2   | Windows                  | Windows - Admin task as user                                 | Alert when admin task is initiated by regular user.  Windows event id 4732 is verified towards static admin list. If the user does not belong to admin list AND the event is seen than we generate alert. Static Admin list is a logstash  disctionary file that needs to be created manually. During Logstash lookup a field user.role:admin is added to an event.4732: A member was added to a security-enabled local group                                                                                                                                                                                                                                       | winlogbeat-* | winlogbeatLogstash admin dicstionary lookup file | Widnows Security Eventlog    | Every 1min                 | 1          |
| 3   | Windows                  | Windows - diff IPs logon                                     | Alert when Windows logon process is detected and two or more different IP addressed are seen in source field.  Timeframe is last 15min.Detection is based onevents 4624 or 1200.4624: An account was successfully logged on1200: Application token success                                                                                                                                                                                                                                                                                                                                                                                                          | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min, for last 15min | 1          |
| 4   | Windows                  | Windows - Event service error                                | Alert when Windows event 1108 is matched1108: The event logging service encountered an error                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min                 | 1          |
| 5   | Windows                  | Windows - file insufficient privileges                       | Alert when Windows event 5145 is matched5145: A network share object was checked to see whether client can be granted desired accessEvery time a network share object (file or folder) is accessed, event 5145 is logged. If the access is denied at the file share level, it is audited as a failure event. Otherwise, it considered a success. This event is not generated for NTFS access.                                                                                                                                                                                                                                                                       | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min, for last 15min | 50         |
| 6   | Windows                  | Windows - Kerberos pre-authentication failed                 | Alert when Windows event 4625 or 4771 is matched 4625: An account failed to log on 4771: Kerberos pre-authentication failed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min                 | 1          |
| 7   | Windows                  | Windows - Logs deleted                                       | Alert when Windows event 1102 OR 104 is matched1102: The audit log was cleared104: Event log cleared                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min                 | 1          |
| 8   | Windows                  | Windows - Member added to a security-enabled global group    | Alert when Windows event 4728 is matched4728: A member was added to a security-enabled global group                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min                 | 1          |
| 9   | Windows                  | Windows - Member added to a security-enabled local group     | Alert when Windows event 4732 is matched4732: A member was added to a security-enabled local group                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min                 | 1          |
| 10  | Windows                  | Windows - Member added to a security-enabled universal group | Alert when Windows event 4756 is matched4756: A member was added to a security-enabled universal group                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min                 | 1          |
| 11  | Windows                  | Windows - New device                                         | Alert when Windows event 6414 is matched6416: A new external device was recognized by the system                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min                 | 1          |
| 12  | Windows                  | Windows - Package installation                               | Alert when Windows event 4697 is matched 4697: A service was installed in the system                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min                 | 1          |
| 13  | Windows                  | Windows - Password policy change                             | Alert when Windows event 4739 is matched4739: Domain Policy was changed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min                 | 1          |
| 14  | Windows                  | Windows - Security log full                                  | Alert when Windows event 1104 is matched1104: The security Log is now full                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min                 | 1          |
| 15  | Windows                  | Windows - Start up                                           | Alert when Windows event 4608 is matched 4608: Windows is starting up                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min                 | 1          |
| 16  | Windows                  | Windows - Account lock                                       | Alert when Windows event 4740 is matched4740: A User account was Locked out                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min                 | 1          |
| 17  | Windows                  | Windows - Security local group was changed                   | Alert when Windows event 4735 is matched4735: A security-enabled local group was changed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min                 | 1          |
| 18  | Windows                  | Windows - Reset password attempt                             | Alert when Windows event 4724 is matched4724: An attempt was made to reset an accounts password                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min                 | 1          |
| 19  | Windows                  | Windows - Code integrity changed                             | Alert when Windows event 5038 is matched5038: Detected an invalid image hash of a fileInformation:    Code Integrity is a feature that improves the security of the operating system by validating the integrity of a driver or system file each time it is loaded into memory.    Code Integrity detects whether an unsigned driver or system file is being loaded into the kernel, or whether a system file has been modified by malicious software that is being run by a user account with administrative permissions.    On x64-based versions of the operating system, kernel-mode drivers must be digitally signed.The event logs the following information: | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min                 | 1          |
| 20  | Windows                  | Windows - Application error                                  | Alert when Windows event 1000 is matched1000: Application error                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | winlogbeat-* | winlogbeat                                       | Widnows Application Eventlog | Every 1min                 | 1          |
| 21  | Windows                  | Windows - Application hang                                   | Alert when Windows event 1001 OR 1002 is matched1001: Application fault bucket1002: Application hang                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | winlogbeat-* | winlogbeat                                       | Widnows Application Eventlog | Every 1min                 | 1          |
| 22  | Windows                  | Windows - Audit policy changed                               | Alert when Windows event 4719 is matched4719: System audit policy was changed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min                 | 1          |
| 23  | Windows                  | Windows - Eventlog service stopped                           | Alert when Windows event 6005 is matched6005: Eventlog service stopped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min                 | 1          |
| 24  | Windows                  | Windows - New service installed                              | Alert when Windows event 7045 OR 4697 is matched7045,4697: A service was installed in the system                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min                 | 1          |
| 25  | Windows                  | Windows - Driver loaded                                      | Alert when Windows event 6 is matched6: Driver loadedThe driver loaded events provides information about a driver being loaded on the system. The configured hashes are provided as well as signature information. The signature is created asynchronously for performance reasons and indicates if the file was removed after loading.                                                                                                                                                                                                                                                                                                                             | winlogbeat-* | winlogbeat                                       | Widnows System Eventlog      | Every 1min                 | 1          |
| 26  | Windows                  | Windows - Firewall rule modified                             | Alert when Windows event 2005 is matched2005: A Rule has been modified in the Windows firewall Exception List                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min                 | 1          |
| 27  | Windows                  | Windows - Firewall rule add                                  | Alert when Windows event 2004 is matched2004: A firewall rule has been added                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min                 | 1          |
| 28  |                          | Windows - Firewall rule deleted                              | Alert when Windows event 2006 or 2033 or 2009 is matched2006,2033,2009: Firewall rule deleted                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | winlogbeat-* | winlogbeat                                       | Widnows Security Eventlog    | Every 1min                 | 1          |
````

### Playbooks

Energy Logserver has a set of predefined set of rules and activities (called Playbook) that can be attached to a registered event in the Alert module.
Playbooks can be enriched with scripts that can be launched together with Playbook.

#### Create Playbook ###

To add a new playbook, go to the **Alert** module, select the **Playbook** tab and then **Create Playbook**

![](/media/media/image116.png)

In the **Name** field, enter the name of the new Playbook.

In the **Text** field, enter the content of the Playbook message.

In the **Script** field, enter the commands to be executed in the script.

To save the entered content, confirm with the **Submit** button.

#### Playbooks list  ###

To view saved Playbook, go to the **Alert** module, select the **Playbook** tab and then **Playbooks list**:

![](/media/media/image117.png)

To view the content of a given Playbook, select the **Show** button.

To enter the changes in a given Playbook or in its script, select the **Update** button. After making changes, select the **Submit** button.

To delete the selected Playbook, select the **Delete** button.

#### Linking Playbooks with alert rule ###

You can add a Playbook to the Alert while creating a new Alert or by editing a previously created Alert.

To add Palybook to the new Alert rule, go to the **Create alert rule** tab and in the **Playbooks** section use the arrow keys to move the correct Playbook to the right window.

To add a Palybook to existing Alert rule, go to the **Alert rule list** tab with the correct rule select the **Update** button and in the **Playbooks** section use the arrow keys to move the correct Playbook to the right window.

#### Playbook verification ###

When creating an alert or while editing an existing alert, it is possible that the system will indicate the most-suited playbook for the alert. For this purpose, the Validate button is used, which starts the process of searching the existing playbook and selects the most appropriate ones.

![](/media/media/image132.png)

### Risks

Energy Logserver allows you to estimate the risk based on the collected data. The risk is estimated based on the defined category to which the values from 0 to 100 are assigned.

Information on the defined risk for a given field is passed with an alert and multiplied by the value of the Rule Importance parameter.

Risk calculation does not use only logs for its work. Processing the security posture encounters all the information like user behaviour data, performance data, system inventory, running software, vulnerabilities and many more. Having large scope of information Your organization gather an easy way to score its security project and detect all missing spots of the design. Embedded deep expert knowledge is here to help.

#### Create category

To add a new risk Category, go to the **Alert** module, select the **Risks** tab and then **Create Cagtegory**. 

![](/media/media/image118.png)

Enter the **Name** for the new category and the category **Value**.

#### Category list

To view saved Category, go to the **Alert** module, select the **Risks** tab and then **Categories list**:

![](/media/media/image119.png)

To view the content of a given Category, select the **Show** button.

To change the value assigned to a category, select the **Update** button. After making changes, select the **Submit** button.

To delete the selected Category, select the **Delete** button.

#### Create risk

To add a new playbook, go to the Alert module, select the Playbook tab and then Create Playbook

![](/media/media/image120.png)

In the **Index pattern** field, enter the name of the index pattern.
Select the **Read fields** button to get a list of fields from the index.
From the box below, select the field name for which the risk will be determined.

From the **Timerange field**, select the time range from which the data will be analyzed.

Press the **Read valules** button to get values from the previously selected field for analysis.

Next, you must assign a risk category to the displayed values. You can do this for each value individually or use the check-box on the left to mark several values and set the category globally using the **Set global category** button. To quickly find the right value, you can use the search field.

![](/media/media/image122.png)

After completing, save the changes with the **Submit** button.

#### List risk

To view saved risks, go to the **Alert** module, select the **Risks** tab and then **Risks list**:

![](/media/media/image121.png)

To view the content of a given Risk, select the **Show** button.

To enter the changes in a given Risk, select the **Update** button. After making changes, select the **Submit** button.

To delete the selected Risk, select the **Delete** button.

#### Linking risk with alert rule

You can add a Risk key to the Alert while creating a new Alert or by editing a previously created Alert.

To add Risk key to the new Alert rule, go to the **Create alert rule** tab and after entering the index name, select the **Read fields** button and in the **Risk key** field, select the appropriate field name.
In addition, you can enter the validity of the rule in the **Rule Importance** field (in the range 1-100%), by which the risk will be multiplied.

To add Risk key to the existing Alert rule, go to the **Alert rule list**, tab with the correct rule select the **Update** button. 
Use the **Read fields** button and in the **Risk key** field, select the appropriate field name.
In addition, you can enter the validity of the rule in the **Rule Importance**.

#### Risk calculation algorithms

The risk calculation mechanism performs the aggregation of the risk field values.
We have the following algorithms for calculating the alert risk (Aggregation type):

- min - returns the minimum value of the risk values from selected fields;
- max - returns the maximum value of the risk values from selected fields;
- avg - returns the average of risk values from selected fields;
- sum - returns the sum of risk values from selected fields;
- custom - returns the risk value based on your own algorithm

#### Adding a new risk calculation algorithm

The new algorithm should be added in the `./elastalert_modules/playbook_util.py` file in the `calculate_risk` method. There is a sequence of conditional statements for already defined algorithms:

	#aggregate values by risk_key_aggregation for rule
	if risk_key_aggregation == "MIN":
	    value_agg = min(values)
	elif risk_key_aggregation == "MAX":
	    value_agg = max(values)
	elif risk_key_aggregation == "SUM":
	    value_agg = sum(values)
	elif risk_key_aggregation == "AVG":
	    value_agg = sum(values)/len(values)
	else:
	    value_agg = max(values)

To add a new algorithm, add a new sequence as shown in the above code:

	elif risk_key_aggregation == "AVG":
	    value_agg = sum(values)/len(values)
	elif risk_key_aggregation == "AAA":
	    value_agg = BBB
	else:
	    value_agg = max(values)

where **AAA** is the algorithm code, **BBB** is a risk calculation function.

#### Using the new algorithm

After adding a new algorithm, it is available in the GUI in the Alert tab.

To use it, add a new rule according to the following steps:

- Select the `custom` value in the `Aggregation` type field;
- Enter the appropriate value in the `Any` field, e.g. `risk_key_aggregation: AAA`

The following figure shows the places where you can call your own algorithm:

![](/media/media/image123.png)

#### Additional modification of the algorithm (weight)

Below is the code in the `calcuate_risk` method where category values are retrieved - here you can add your weight:

            #start loop by tablicy risk_key
            for k in range(len(risk_keys)):
                risk_key = risk_keys[k]
                logging.info(' >>>>>>>>>>>>>> risk_key: ')
                logging.info(risk_key)
                key_value = lookup_es_key(match, risk_key)
                logging.info(' >>>>>>>>>>>>>> key_value: ')
                logging.info(key_value)
                value = float(self.get_risk_category_value(risk_key, key_value))
                values.append( value )
                logging.info(' >>>>>>>>>>>>>> risk_key values: ')
                logging.info(values)
            #finish loop by tablicy risk_key
            #aggregate values by risk_key_aggregation form rule
            if risk_key_aggregation == "MIN":
                value_agg = min(values)
            elif risk_key_aggregation == "MAX":
                value_agg = max(values)
            elif risk_key_aggregation == "SUM":
                value_agg = sum(values)
            elif risk_key_aggregation == "AVG":
                value_agg = sum(values)/len(values)
            else:
                value_agg = max(values)

`Risk_key` is the array of selected risk key fields in the GUI.
A loop is made on this array and a value is collected for the categories in the line:

	value = float(self.get_risk_category_value(risk_key, key_value))

Based on, for example, Risk_key, you can multiply the value of the value field by the appropriate weight.
The value field value is then added to the table on which the risk calculation algorithms are executed.

### Incidents

SIEM correlation engine allows automatically scores organization security posture showing You what tactic the attacked use and how this puts organization at risk. Every attack can be traced on dashboard reflecting Your security design identifying missing enforcements.

Incidents on the operation of the organization through appropriate points for caught incidents. Hazard situations are presented, using the so-called Mitre ATT / CK matrix. The Energy Logserver system, in addition to native integration with MITER, allows this knowledge to be correlated with other collected data and logs, creating even more complex techniques of behavior detection and analysis. Advanced approach allows for efficient analysis of security design estimation.

The Incident module allows you to handle incidents created by triggered alert rules. 

![](/media/media/image154.png)

Incident handling allows you to perform the following action:

- *Show incident* - shows the details that generated the incident;
- *Verify* - checks the IP addresses of those responsible for causing an incident with the system reputation lists;
- *Preview* - takes you to the Discover module and to the raw document responsible for generating the incident;
- *Update* - allows you to change the Incident status or transfer the incident handling to another user. Status list: *New, Ongoing, False, Solved.*
- *Playbooks* - enables handling of Playbooks assigned to an incident;
- *Note* - User notes about the incident;

#### Incident Escalation

The alarm rule definition allows an incident to be escalated if the incident status does not change (from New to Ongoing) after a defined time.

Configuration parameter

- *escalate_users* - an array of users who get an email alert about the escalation;
- *escalate_after* - the time after which the escalation is triggered;

Example of configuration:

```yaml
escalate_users:["user2", "user3"] 
escalate_after:
	- hours: 6
```

#### Context menu for Alerts::Incidents

In this section, you will find steps and examples that will allow you to add custom items in the actions context menu for the Incidents table. This allows you to expand on the functionalities of the system.

##### Important file paths

- `/usr/share/kibana/plugins/alerts/public/reactui/incidenttab.js`
- `/usr/share/kibana/optimize/bundles/`

##### List element template

```javascript
{
  name: 'Name of the Action to add',
  icon: 'Name of the chosen icon',
  type: 'icon',
  onClick: this.runActionFunction,
}
```
You should pick the icon from available choices. After listing `ls /usr/share/kibana/built_assets/dlls/icon*` if you want to use:
- `icon.editor_align_center-js.bundle.dll.js`  
The for `icon: ` you should set:  
- `editorAlignCenter`  
Use the same transformation for each icon.

##### Action function template

```javascript
runActionFunction = item => {
  // Functino logic to run => information from "item" object can be used here
};
```
Object "item" contains information about the incident that action was used on.

##### Steps to add the first custom action to the codebase

1. Create backup of a file you are about to modify:

   ```bash
   cp /usr/share/kibana/plugins/alerts/public/reactui/incidenttab.js ~/incidenttab.js.bak
   ```

   

2. Working example for the onClick function and action item:

   ```javascript
   showMyLocation = () => {
     const opt = {
       enableHighAccuracy: true,
       timeout: 5000,
       maximumAge: 0
     };
     const success = pos => {
       const crd = pos.coords;
       alert(`Your current position is:\nLatitude: ${
         crd.latitude
       }\nLongitude: ${
         crd.longitude
       }\nMore or less ${
         crd.accuracy
       } meters.`);
     }
     const err = err => {
       alert(`ERROR(${err.code}): ${err.message}`);
     }
     navigator.geolocation.getCurrentPosition(success, err, opt);
   }
   
   const customActions = [
     {
       name: 'Show my location',
       icon: 'broom',
       type: 'icon',
       onClick: this.showMyLocation,
     }
   ];
   incidentactions.push(...customActions);
   ```

   

3. The "showMyLocation" function code should be placed in `/usr/share/kibana/plugins/alerts/public/reactui/incidenttab.js` under:

   ```javascript
     showIncidentModal = incident => {
       const updateIncident = incident;
       this.setState({ showIncidentModal: true, updateIncident });
     };
   
     // paste function here
   
     render() {
   ```

   

4. Custom action with a `push` function should be placed:

   ```javascript
         {
           name: 'Note',
           icon: 'pencil',
           type: 'icon',
           isPrimary: true,
           color: 'danger',
           onClick: this.note,
         },
       ];
   
       // insert HERE your action with function 'push'
   
       const incidentcolumns = [
   ```

   

5. For the changes to take effect run below commands on the client serwer (as root or with sudo):

   ```bash
   systemctl stop kibana
   rm -rf /usr/share/kibana/optimize/bundles
   systemctl start kibana
   # verify that process runs correctly afterwards
   journalctl -fu kibana
   # in case of errors restore backup
   ```

   

6. You should now be able to see an additional item in the action context menu in GUI Alerts::Incidents:

   ![](/media/media/image202.png)

   

7. Running the action will resolve into an alert:  

   ![](/media/media/image203.png)

   

##### Steps to add a second and subsequent custom actions

1. Execute identicly as in the last section.

2. Example of a function that uses `item` object. It will open a new tab in the browser with the default [Alert] dashboard with a custom filter and time set, based on information from the passed `item` variable:

   ```javascript
   openAlertDashboardWithFilter = item => {
     const ruleName = `"${item.rule_name}"`;
     const startT = new Date(item.match_time);
     startT.setHours(0);
     const endT = new Date(item.match_time);
     endT.setHours(24);
     const alertDashboardPath =
       '/app/kibana#/dashboard/777ace50-d200-11e8-98f8-31520a7f9701';
     const timeQuery = 
       `_g=(time:(from:'${startT.toISOString()}',to:'${endT.toISOString()}'))`;
     const nameQuery = 
       `_a=(query:(language:lucene,query:'rule_name:${encodeURIComponent(
         ruleName
       )}'))`;
     const dashboardLocation = `${alertDashboardPath}?${timeQuery}&${nameQuery}`;
     window.open(dashboardLocation, '_blank');
   };
   ``` 

3. Execute identicly as in the last section.

4. The difference in adding subsequent action is that you append a new one to `customActions` array variable. The rest should stay the same:

   ```javascript
   const customActions = [
     {
       name: 'Show my location',
       icon: 'broom',
       type: 'icon',
       onClick: this.showMyLocation,
     },
     {
       name: 'Show on Dashboard',
       icon: 'arrowRight',
       type: 'icon',
       onClick: this.openAlertDashboardWithFilter,
     },
   ];
   incidentactions.push(...customActions);
   ```

   

5. Execute identicly as in the last section.

6. Now both actions should be present on the context menu:

   ![](/media/media/image204.png)

7. Using it will open dashboard in new tab:

   ![](/media/media/image205.png)

##### System update

When updating the system your changes might be overwritten. You should in that case save a backup of your changes and restore them after the update with the use of this instruction. Or for instance, with `vimdiff` compare your changes with the original file:

```bash
vimdiff ~/incidenttab.js.bak /usr/share/kibana/plugins/alerts/public/reactui/incidenttab.js
```

### Indicators of compromise (IoC)

Energy Logserver  has the Indicators of compromise (IoC) functionality, which is based on the Malware Information Sharing Platform (MISP).
IoC observes the logs sent to the system and marks documents if their content is in MISP signature.
Based on IoC markings, you can build alert rules or track incident behavior.

#### Configuration

##### Bad IP list update

To update bad reputation lists and to create `.blacklists` index, you have to run following scripts:

```bash
/etc/logstash/lists/bin/misp_threat_lists.sh
```

##### Scheduling bad IP lists update

This can be done in `cron` (host with Logstash installed):

```bash
0 6 * * * logstash /etc/logstash/lists/bin/misp_threat_lists.sh
```

or with Kibana Scheduller app (**only if Logstash is running on the same host**).

- Prepare script path:

```bash
/bin/ln -sfn /etc/logstash/lists/bin /opt/ai/bin/lists
chown logstash:kibana /etc/logstash/lists/
chmod g+w /etc/logstash/lists/
```

- Log in to Energy Logserver GUI and go to **Scheduler** app. Set it up with below options and push "Submit" button:

```bash
Name:           MispThreatList
Cron pattern:   0 1 * * *
Command:        lists/misp_threat_lists.sh
Category:       logstash
```

After a couple of minutes check for blacklists index:

```bash
curl -sS -u user:password -XGET '127.0.0.1:9200/_cat/indices/.blacklists?s=index&v'
health status index       uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   .blacklists Mld2Qe2bSRuk2VyKm-KoGg   1   0      76549            0      4.7mb          4.7mb
```



### Calendar function

The alert rule can be executed based on a schedule called Calendar.

#### Create a calendar

The configuration of the **Calendar Function** should be done in the definition of the `Rule Definition` alert using the `calendar` and `scheduler` options, in **Crontab** format.

For example, we want to have an alert that:

- triggers only on working days from 8:00 to 16:00;

- only triggers on weekends;

```bash
calendar:
  schedule: "* 8-15 * * mon-fri"
```

If `aggregation` is used in the alert definition, remember that the aggregation schedule should be the same as the defined calendar.



### Windows Events ID repository
```
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Category           | Subcategory                   | Event ID | Dashboard                              | Type             | Event Log | Describe                                                                     | Event ID for Windows 2003 |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Object             | Access                        | 561      |  AD DNS Changes                        | Success          | Security  | Handle Allocated                                                                                         |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| System             | Security State Change         | 4608     | [AD] Event Statistics                  | Success          | Security  | Windows is starting up                                                       | 512                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| System             | Security System Extension     | 4610     | [AD] Event Statistics                  | Success          | Security  | An authentication package has been loaded by the Local Security Authority    | 514                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| System             | System Integrity              | 4612     | [AD] Event Statistics                  | Success          | Security  | Internal resources allocated for the queuing of audit                        | 516                       |
|                    |                               |          |                                        |                  |           | messages have been exhausted, leading to the loss of some audits             |                           |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| System             | System Integrity              | 4615     | [AD] Event Statistics                  | Success          | Security  | Invalid use of LPC port                                                      | 519                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| System             | Security State Change         | 4616     | [AD] Servers Audit                     | Success          | Security  | The system time was changed.                                                 | 520                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Logon/Logoff       | Logon                         | 4624     | [AD] Total Logins -> AD Login   Events | Success          | Security  | An account was successfully logged on                                        | 528 , 540                 |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Logon/Logoff       | Logon                         | 4625     | [AD] Inventory, [AD] Failed Logins ->  | Failure          | Security  | An account failed to log on                                                  | 529, 530, 531, 532, 533,  |
|                    |                               |          | AD Failed Login Events                 |                  |           |                                                                              | 534, 535, 536, 537, 539   |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Object Access      | File System, Registry, SAM,   | 4656     | [AD] Removable Device Auditing         | Success, Failure | Security  | A handle to an object was requested                                          | 560                       |
|                    | Handle Manipulation,          |          |                                        |                  |           |                                                                              |                           |
|                    | Other Object Access Events    |          |                                        |                  |           |                                                                              |                           |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Object Access      | File System, Registry,        | 4663     | [AD] Removable Device Auditing         | Success          | Security  | An attempt was made to access an object                                      | 567                       |
|                    | Kernel Object, SAM,           |          |                                        |                  |           |                                                                              |                           |
|                    | Other Object Access Events    |          |                                        |                  |           |                                                                              |                           |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Object Access      | File System, Registry,        | 4670     | [AD] GPO Objects Overview              | Success          | Security  | Permissions on an object were   changed                                                                  |
|                    | Policy Change,                |          |                                        |                  |           |                                                                                                          |
|                    | Authorization Policy Change   |          |                                        |                  |           |                                                                                                          |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | User Account Management       | 4720     | [AD] Accounts Overview ->              | Success          | Security  |  A user account was created                                                  | 624                       |
|                    |                               |          | [AD] A user account was created        |                  |           |                                                                              |                           |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | User Account Management       | 4722     | [AD] Accounts Overview ->              | Success          | Security  | A user account was enabled                                                   | 626                       |
|                    |                               |          | [AD] A user account was disabled       |                  |           |                                                                              |                           |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | User Account Management       | 4723     | [AD] Accounts Overview ->              | Success          | Security  | An attempt was made to change an account's password                          | 627                       |
|                    |                               |          | [AD] An attempt was made               |                  |           |                                                                              |                           |
|                    |                               |          | to change an account's password        |                  |           |                                                                              |                           |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | User Account Management       | 4724     | [AD] Accounts Overview ->              | Success          | Security  | An attempt was made to reset an accounts password                            | 628                       |
|                    |                               |          | [AD] An attempt was made               |                  |           |                                                                              |                           |
|                    |                               |          | to change an account's password        |                  |           |                                                                              |                           |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | User Account Management       | 4725     | [AD] Accounts Overview ->              | Success          | Security  | A user account was disabled                                                  | 629                       |
|                    |                               |          | [AD] A user account was disabled       |                  |           |                                                                              |                           |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | User Account Management       | 4726     | [AD] Accounts Overview ->              | Success          | Security  | A user account was deleted                                                   | 630                       |
|                    |                               |          | [AD] A user account was deleted        |                  |           |                                                                              |                           |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Security Group Management     | 4727     | [AD] Security Group Change History     | Success          | Security  | A security-enabled global group was created                                  | 631                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Security Group Management     | 4728     | [AD] Organizational Unit               | Success          | Security  | A member was added to a security-enabled global group                        | 632                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Security Group Management     | 4729     | [AD] Organizational Unit               | Success          | Security  | A member was removed from a security-enabled global group                    | 633                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Security Group Management     | 4730     | [AD] Organizational Unit               | Success          | Security  | A security-enabled global group was deleted                                  | 634                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Security Group Management     | 4731     | [AD] Organizational Unit               | Success          | Security  | A security-enabled local group was created                                   | 635                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Security Group Management     | 4732     | [AD] Organizational Unit               | Success          | Security  | A member was added to a security-enabled local group                         | 636                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Security Group Management     | 4733     | [AD] Organizational Unit               | Success          | Security  | A member was removed from a security-enabled local group                     | 637                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Security Group Management     | 4734     | [AD] Organizational Unit               | Success          | Security  | A security-enabled local group was deleted                                   | 638                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | User Account Management       | 4738     | [AD] Accounts Overview                 | Success          | Security  | A user account was changed                                                   | 642                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | User Account Management       | 4740     | [AD] Accounts Overview ->              | Success          | Security  | A user account was locked out                                                | 644                       |
|                    |                               |          | AD   Account - Account Locked          |                  |           |                                                                              |                           |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Computer Account Management   | 4741     | [AD] Computer Account Overview         | Success          | Security  | A computer account was created                                               | 645                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Computer Account Management   | 4742     | [AD] Computer Account Overview         | Success          | Security  | A computer account was changed                                               | 646                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Computer Account Management   | 4743     | [AD] Computer Account Overview         | Success          | Security  | A computer account was deleted                                               | 647                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Distribution Group Management | 4744     | [AD] Organizational Unit               | Success          | Security  | A security-disabled local group was created                                  | 648                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Distribution Group Management | 4746     | [AD] Security Group Change History     | Success          | Security  | A member was added to a security-disabled local group                        | 650                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Distribution Group Management | 4747     | [AD] Security Group Change History     | Success          | Security  | A member was removed from a security-disabled local group                    | 651                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Distribution Group Management | 4748     | [AD] Organizational Unit               | Success          | Security  | A security-disabled local group was deleted                                  | 652                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Distribution Group Management | 4749     | [AD] Organizational Unit               | Success          | Security  | A security-disabled global group was created                                 | 653                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Distribution Group Management | 4751     | [AD] Security Group Change History     | Success          | Security  | A member was added to a security-disabled global group                       | 655                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Distribution Group Management | 4752     | [AD] Security Group Change History     | Success          | Security  | A member was removed from a security-disabled global group                   | 656                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Distribution Group Management | 4753     | [AD] Organizational Unit               | Success          | Security  | A security-disabled global group was deleted                                 | 657                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Security Group Management     | 4754     | [AD] Organizational Unit               | Success          | Security  | A security-enabled universal group was created                               | 658                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Security Group Management     | 4755     | [AD] Organizational Unit               | Success          | Security  | A security-enabled universal group was changed                               | 659                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Security Group Management     | 4756     | [AD] Organizational Unit               | Success          | Security  | A member was added to a security-enabled universal group                     | 660                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Security Group Management     | 4757     | [AD] Organizational Unit               | Success          | Security  | A member was removed from a security-enabled universal group                 | 661                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Security Group Management     | 4758     | [AD] Organizational Unit               | Success          | Security  | A security-enabled universal group was deleted                               | 662                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Distribution Group Management | 4759     | [AD] Security Group Change History     | Success          | Security  | A security-disabled universal group was created                              | 663                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Distribution Group Management | 4761     | [AD] Security Group Change History     | Success          | Security  | A member was added to a security-disabled universal group                    | 655                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Distribution Group Management | 4762     | [AD] Security Group Change History     | Success          | Security  | A member was removed from a security-disabled universal group                | 666                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | Security Group Management     | 4764     | [AD] Organizational Unit               | Success          | Security  | A groups type was changed                                                    | 668                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | User Account Management       | 4765     | [AD] Accounts Overview ->              | Success          | Security  | SID History was added to an account                                                                      |
|                    |                               |          | AD Account - Account History           |                  |           |                                                                                                          |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+----------------------------------------------------------------------------------------------------------+
| Account Management | User Account Management       | 4766     | [AD] Accounts Overview ->              | Failure          | Security  | An attempt to add SID History to an   account failed                                                     |
|                    |                               |          | AD Account - Account History           |                  |           |                                                                                                          |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | User Account Management       | 4767     | [AD] Accounts Overview                 | Success          | Security  | A computer account was changed                                               | 646                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Logon      | Credential Validation         | 4776     | [AD] Failed Logins                     | Success, Failure | Security  | The domain controller attempted to validate the credentials for an   account | 680, 681                  |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Account Management | User Account Management       | 4781     | [AD] Accounts Overview                 | Success          | Security  | The name of an account was changed                                           | 685                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Directory Service  | Directory Service Changes     | 5136     | [AD] Organizational Unit               | Success          | Security  | A directory service object was modified                                      | 566                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Directory Service  | Directory Service Changes     | 5137     | [AD] Organizational Unit               | Success          | Security  | A directory service object was created                                       | 566                       |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+------------------------------------------------------------------------------+---------------------------+
| Directory Service  | Directory Service Changes     | 5138     | [AD] Organizational Unit               | Success          | Security  | A directory service object was   undeleted                                                               |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+----------------------------------------------------------------------------------------------------------+
| Directory Service  | Directory Service Changes     | 5139     | [AD] Organizational Unit               | Success          | Security  | A directory service object was moved                                                                     |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+----------------------------------------------------------------------------------------------------------+
| Object Access      | File Share                    | 5140     | [AD] File Audit                        | Success          | Security  | A network share object was accessed                                                                      |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+----------------------------------------------------------------------------------------------------------+
| Directory Service  | Directory Service Changes     | 5141     | [AD] Organizational Unit               | Failure          | Security  | A directory service object was   deleted                                                                 |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+----------------------------------------------------------------------------------------------------------+
| Object Access      | File Share                    | 5142     | [AD] File Audit                        | Success          | Security  | A network share object was added.                                                                        |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+----------------------------------------------------------------------------------------------------------+
| Object Access      | Detailed File Share           | 5145     | [AD] File Audit                        | Success, Failure | Security  | A network share object was checked   to see whether client can be granted desired access                 |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+----------------------------------------------------------------------------------------------------------+
| Process Tracking   |  Plug and Play                | 6416     | [AD] Removable Device Auditing         | Success          | Security  |  A new external device was   recognized by the system.                                                   |
+--------------------+-------------------------------+----------+----------------------------------------+------------------+-----------+----------------------------------------------------------------------------------------------------------+
```

#### Netflow analyzis

The Logstash collector receives and decodes Network Flows using the provided decoders. During decoding, IP address reputation analysis is performed and the result is added to the event document.

#### Installation

##### Install/update logstash codec plugins for netflox and sflow

```bash
/usr/share/logstash/bin/logstash-plugin install file:///etc/logstash/plugins/logstash-codec-sflow-2.1.3.gem.zip
/usr/share/logstash/bin/logstash-plugin install file:///etc/logstash/plugins/logstash-codec-netflow-4.2.1.gem.zip
/usr/share/logstash/bin/logstash-plugin install file:///etc/logstash/plugins/logstash-input-udp-3.3.4.gem.zip
/usr/share/logstash/bin/logstash-plugin update logstash-input-tcp
/usr/share/logstash/bin/logstash-plugin update logstash-filter-translate
/usr/share/logstash/bin/logstash-plugin update logstash-filter-geoip
/usr/share/logstash/bin/logstash-plugin update logstash-filter-dns
```

#### Configuration

##### Enable Logstash pipeline

```bash
vim /etc/logstash/pipeline.yml

- pipeline.id: flows
  path.config: "/etc/logstash/conf.d/netflow/*.conf"
```

##### Elasticsearch template installation

```bash
curl -XPUT -H 'Content-Type: application/json' -u logserver:logserver 'http://127.0.0.1:9200/_template/netflow' -d@/etc/logstash/templates.d/netflow-template.json
```

##### Importing Kibana dashboards

```bask
curl -k -X POST -ulogserver:logserver "https://localhost:5601/api/kibana/dashboards/import" -H 'kbn-xsrf: true' -H 'Content-Type: application/json' -d@overview.json
curl -k -X POST -ulogserver:logserver "https://localhost:5601/api/kibana/dashboards/import" -H 'kbn-xsrf: true' -H 'Content-Type: application/json' -d@security.json
curl -k -X POST -ulogserver:logserver "https://localhost:5601/api/kibana/dashboards/import" -H 'kbn-xsrf: true' -H 'Content-Type: application/json' -d@sources.json
curl -k -X POST -ulogserver:logserver "https://localhost:5601/api/kibana/dashboards/import" -H 'kbn-xsrf: true' -H 'Content-Type: application/json' -d@history.json
curl -k -X POST -ulogserver:logserver "https://localhost:5601/api/kibana/dashboards/import" -H 'kbn-xsrf: true' -H 'Content-Type: application/json' -d@destinations.json
```

##### Enable reverse dns lookup

To enbled revere DNS lookup set the **USE_DNS:false** to **USE_DNS:true** in **13-filter-dns-geoip.conf**

Optionally set both dns servers ${DNS_SRV:8.8.8.8} to your local dns

### Security rules

#### MS Windows SIEM rules

<table border="1" class="colwidths-given docutils" id="id1">
<colgroup>
<col width="2%" />
<col width="10%" />
<col width="17%" />
<col width="20%" />
<col width="6%" />
<col width="9%" />
<col width="12%" />
<col width="4%" />
<col width="20%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Admin night logon</p>
</td>
<td><p class="first last">Alert on Windows login events when detected outside business hours</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: &quot;event_id:(4624 OR 1200) AND user.role:admin  AND event.hour:(20 OR 21 OR 22 OR 23 0 OR 1 OR 2 OR 3)&quot;</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Admin task as user</p>
</td>
<td><p class="first last">Alert when admin task is initiated by regular user.  
Windows event id 4732 is verified towards static admin list. If the user does not belong to admin list AND the event is seen than we generate alert. 
Static Admin list is a logstash  disctionary file that needs to be created manually. During Logstash lookup a field user.role:admin is added to an event.
4732: A member was added to a security-enabled local group</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat
Logstash admin dicstionary lookup file</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: &quot;event_id:4732 AND NOT user.role:admin&quot;</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - diff IPs logon</p>
</td>
<td><p class="first last">Alert when Windows logon process is detected and two or more different IP addressed are seen in source field.  Timeframe is last 15min.
Detection is based onevents 4624 or 1200.
4624: An account was successfully logged on
1200: Application token success</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">cardinality</p>
</td>
<td><p class="first last">max_cardinality: 1
timeframe:
   minutes: 15
filter:
 - query_string:
     query: &quot;event_id:(4624 OR 1200) AND NOT _exists_:user.role AND NOT event_data.IpAddress:\&quot;-\&quot; &quot;
query_key: username</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Event service error</p>
</td>
<td><p class="first last">Alert when Windows event 1108 is matched
1108: The event logging service encountered an error </p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: &quot;event_id:1108&quot;</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">5</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - file insufficient privileges</p>
</td>
<td><p class="first last">Alert when Windows event 5145 is matched
5145: A network share object was checked to see whether client can be granted desired access
Every time a network share object (file or folder) is accessed, event 5145 is logged. If the access is denied at the file share level, it is audited as a failure event. Otherwise, it considered a success. This event is not generated for NTFS access.</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">query_key: &quot;event_data.IpAddress&quot;
num_events: 50
timeframe:
  minutes: 15
filter:
 - query_string:
     query: &quot;event_id:5145&quot;</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">6</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Kerberos pre-authentication failed</p>
</td>
<td><p class="first last">Alert when Windows event 4625 or 4771 is matched
 4625: An account failed to log on
 4771: Kerberos pre-authentication failed</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: &quot;event_id:4625 OR event_id:4771&quot;</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">7</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Logs deleted</p>
</td>
<td><p class="first last">Alert when Windows event 1102 OR 104 is matched
1102: The audit log was cleared
104: Event log cleared</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: 'event_desc:&quot;1102 The audit log was cleared&quot;'</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">8</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Member added to a security-enabled global group</p>
</td>
<td><p class="first last">Alert when Windows event 4728 is matched
4728: A member was added to a security-enabled global group</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: &quot;event_id:4728&quot;</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">9</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Member added to a security-enabled local group</p>
</td>
<td><p class="first last">Alert when Windows event 4732 is matched
4732: A member was added to a security-enabled local group</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: &quot;event_id:4732&quot;</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">10</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Member added to a security-enabled universal group</p>
</td>
<td><p class="first last">Alert when Windows event 4756 is matched
4756: A member was added to a security-enabled universal group</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: &quot;event_id:4756&quot;</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">11</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - New device</p>
</td>
<td><p class="first last">Alert when Windows event 6414 is matched
6416: A new external device was recognized by the system</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: &quot;event_id:6416&quot;</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">12</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Package installation</p>
</td>
<td><p class="first last">Alert when Windows event 4697 is matched
 4697: A service was installed in the system</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: &quot;event_id:4697&quot;</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">13</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Password policy change</p>
</td>
<td><p class="first last">Alert when Windows event 4739 is matched
4739: Domain Policy was changed</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: &quot;event_id:4739&quot;</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">14</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Security log full</p>
</td>
<td><p class="first last">Alert when Windows event 1104 is matched
1104: The security Log is now full</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: &quot;event_id:1104&quot;</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">15</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Start up</p>
</td>
<td><p class="first last">Alert when Windows event 4608 is matched
 4608: Windows is starting up</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: &quot;event_id:4608&quot;</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">16</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Account lock</p>
</td>
<td><p class="first last">Alert when Windows event 4740 is matched
4740: A User account was Locked out</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: &quot;event_id:4740&quot;</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">17</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Security local group was changed</p>
</td>
<td><p class="first last">Alert when Windows event 4735 is matched
4735: A security-enabled local group was changed</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: &quot;event_id:4735&quot;</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">18</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Reset password attempt</p>
</td>
<td><p class="first last">Alert when Windows event 4724 is matched
4724: An attempt was made to reset an accounts password</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: &quot;event_id:4724&quot;</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">19</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Code integrity changed</p>
</td>
<td><p class="first last">Alert when Windows event 5038 is matched
5038: Detected an invalid image hash of a file
Information:    Code Integrity is a feature that improves the security of the operating system by validating the integrity of a driver or system file each time it is loaded into memory.
    Code Integrity detects whether an unsigned driver or system file is being loaded into the kernel, or whether a system file has been modified by malicious software that is being run by a user account with administrative permissions.
    On x64-based versions of the operating system, kernel-mode drivers must be digitally signed.
The event logs the following information:</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: &quot;event_id:5038&quot;</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">20</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Application error</p>
</td>
<td><p class="first last">Alert when Windows event 1000 is matched
1000: Application error</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Application Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: &quot;event_id:1000&quot;</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">21</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Application hang</p>
</td>
<td><p class="first last">Alert when Windows event 1001 OR 1002 is matched
1001: Application fault bucket
1002: Application hang</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Application Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: &quot;event_id:1002 OR event_id:1001&quot;</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">22</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Audit policy changed</p>
</td>
<td><p class="first last">Alert when Windows event 4719 is matched
4719: System audit policy was changed</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: &quot;event_id:4719&quot;</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">23</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Eventlog service stopped</p>
</td>
<td><p class="first last">Alert when Windows event 6005 is matched
6005: Eventlog service stopped</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: &quot;event_id:6005&quot;</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">24</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - New service installed</p>
</td>
<td><p class="first last">Alert when Windows event 7045 OR 4697 is matched
7045,4697: A service was installed in the system</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: &quot;event_id:7045 OR event_id:4697&quot;</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">25</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Driver loaded</p>
</td>
<td><p class="first last">Alert when Windows event 6 is matched
6: Driver loaded
The driver loaded events provides information about a driver being loaded on the system. The configured hashes are provided as well as signature information. The signature is created asynchronously for performance reasons and indicates if the file was removed after loading.</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows System Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: &quot;event_id:6&quot;</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">26</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Firewall rule modified</p>
</td>
<td><p class="first last">Alert when Windows event 2005 is matched
2005: A Rule has been modified in the Windows firewall Exception List</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: 'event_desc:&quot;4947 A change has been made to Windows Firewall exception list. A rule was modified&quot;'</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">27</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Firewall rule add</p>
</td>
<td><p class="first last">Alert when Windows event 2004 is matched
2004: A firewall rule has been added</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: &quot;event_id:2004&quot;</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">28</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - Firewall rule deleted</p>
</td>
<td><p class="first last">Alert when Windows event 2006 or 2033 or 2009 is matched
2006,2033,2009: Firewall rule deleted</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: &quot;event_id:2006 OR event_id:2033 OR event_id:2009&quot;</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">29</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - System has been shutdown </p>
</td>
<td><p class="first last">This event is written when an application causes the system to restart, or when the user initiates a restart or shutdown by clicking Start or pressing CTRL+ALT+DELETE, and then clicking Shut Down.</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: 'event_id:&quot;1074&quot;'</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">30</p>
</td>
<td><p class="first last">Windows</p>
</td>
<td><p class="first last">Windows - The system time was changed</p>
</td>
<td><p class="first last">The system time has been changed. The event describes the old and new time.</p>
</td>
<td><p class="first last">winlogbeat-*</p>
</td>
<td><p class="first last">winlogbeat</p>
</td>
<td><p class="first last">Widnows Security Eventlog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: 'event_id:&quot;4616&quot;'</p>
</td>
</tr>
</tbody>
</table>


#### Network Switch SIEM rules

<table border="1" class="docutils" id="id1">
<colgroup>
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last">Switch</p>
</td>
<td><p class="first last">Switch - Blocked by LACP</p>
</td>
<td><p class="first last">ports:  port &lt;nr&gt; is Blocked by LACP</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot;Blocked by LACP&quot;”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last">Switch</p>
</td>
<td><p class="first last">Switch - Blocked by STP</p>
</td>
<td><p class="first last">ports:  port &lt;nr&gt; is Blocked by STP</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot;Blocked by STP&quot;”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last">Switch</p>
</td>
<td><p class="first last">Switch - Port state changed</p>
</td>
<td><p class="first last">Port state changed to down or up</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot;changed state to&quot;”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4</p>
</td>
<td><p class="first last">Switch</p>
</td>
<td><p class="first last">Switch - Configured from console</p>
</td>
<td><p class="first last">Configurations changes from console</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot;Configured from console&quot;”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">5</p>
</td>
<td><p class="first last">Switch</p>
</td>
<td><p class="first last">Switch - High collision or drop rate</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot;High collision or drop rate&quot;”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">6</p>
</td>
<td><p class="first last">Switch</p>
</td>
<td><p class="first last">Switch - Invalid login</p>
</td>
<td><p class="first last"> auth:  Invalid user name/password on SSH session</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot;auth:  Invalid user name/password on SSH session&quot;”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">7</p>
</td>
<td><p class="first last">Switch</p>
</td>
<td><p class="first last">Switch - Logged to switch</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot; mgr:  SME SSH from&quot;”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">8</p>
</td>
<td><p class="first last">Switch</p>
</td>
<td><p class="first last">Switch - Port is offline</p>
</td>
<td><p class="first last"> ports:  port &lt;nr&gt; is now off-line</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot; is now off-line&quot;”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">9</p>
</td>
<td><p class="first last">Switch</p>
</td>
<td><p class="first last">Switch - Port is online</p>
</td>
<td><p class="first last"> ports:  port &lt;nr&gt; is now on-line</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot; is now on-line&quot;”</p>
</td>
</tr>
</tbody>
</table>


#### Cisco ASA devices SIEM rules

<table border="1" class="docutils" id="id1">
<colgroup>
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last">Cisco ASA</p>
</td>
<td><p class="first last">Cisco ASA - Device interface administratively up</p>
</td>
<td><p class="first last">Device interface administratively up</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog from Cisco ASA devices</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: ‘cisco.id:”%ASA-4-411003”’</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last">Cisco ASA</p>
</td>
<td><p class="first last">Cisco ASA - Device configuration has been changed or reloaded</p>
</td>
<td><p class="first last">Device configuration has been changed or reloaded</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog from Cisco ASA devices</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: ‘cisco.id:(“%ASA-5-111007” OR “%ASA-5-111008”)’</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last">Cisco ASA</p>
</td>
<td><p class="first last">Cisco ASA - Device interface administratively down</p>
</td>
<td><p class="first last">Device interface administratively down</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog from Cisco ASA devices</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: ‘cisco.id:”%ASA-4-411004”’</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4</p>
</td>
<td><p class="first last">Cisco ASA</p>
</td>
<td><p class="first last">Cisco ASA - Device line protocol on Interface changed state to down</p>
</td>
<td><p class="first last">Device line protocol on Interface changed state to down</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog from Cisco ASA devices</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: ‘cisco.id:”%ASA-4-411002”’</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">5</p>
</td>
<td><p class="first last">Cisco ASA</p>
</td>
<td><p class="first last">Cisco ASA - Device line protocol on Interface changed state to up</p>
</td>
<td><p class="first last">Device line protocol on Interface changed state to up</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog from Cisco ASA devices</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: ‘cisco.id:”%ASA-4-411001”’</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">6</p>
</td>
<td><p class="first last">Cisco ASA</p>
</td>
<td><p class="first last">Cisco ASA - Device user executed shutdown</p>
</td>
<td><p class="first last">Device user executed shutdown</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog from Cisco ASA devices</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: ‘cisco.id:”%ASA-5-111010”’</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">7</p>
</td>
<td><p class="first last">Cisco ASA</p>
</td>
<td><p class="first last">Cisco ASA - Multiple VPN authentication failed</p>
</td>
<td><p class="first last">Multiple VPN authentication failed</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog from Cisco ASA devices</p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">query_key: “src.ip”
num_events: 10
timeframe:
  minutes: 240
filter:
 - query_string:
     query: “cisco.id:&quot;%ASA-6-113005&quot;”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">8</p>
</td>
<td><p class="first last">Cisco ASA</p>
</td>
<td><p class="first last">Cisco ASA - VPN authentication failed</p>
</td>
<td><p class="first last">VPN authentication failed</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog from Cisco ASA devices</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “cisco.id:&quot;%ASA-6-113005&quot;”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">9</p>
</td>
<td><p class="first last">Cisco ASA</p>
</td>
<td><p class="first last">Cisco ASA - VPN authentication successful</p>
</td>
<td><p class="first last">VPN authentication successful</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog from Cisco ASA devices</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “cisco.id:&quot;%ASA-6-113004&quot;”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">10</p>
</td>
<td><p class="first last">Cisco ASA</p>
</td>
<td><p class="first last">Cisco ASA - VPN user locked out</p>
</td>
<td><p class="first last">VPN user locked out</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog from Cisco ASA devices</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “cisco.id:&quot;%ASA-6-113006&quot;”</p>
</td>
</tr>
</tbody>
</table>


#### Linux Mail SIEM rules

<table border="1" class="docutils" id="id1">
<colgroup>
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last">Mail Linux</p>
</td>
<td><p class="first last">Mail - Flood Connect from</p>
</td>
<td><p class="first last">Connection flood, possible DDOS attack</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog</p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot;connect from&quot;”
query_key: host
timeframe:
  hours: 1
num_events: 50</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last">Mail Linux</p>
</td>
<td><p class="first last">Mail - SASL LOGIN authentication failed</p>
</td>
<td><p class="first last">User authentication failure</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog</p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot;SASL LOGIN authentication failed: authentication failure&quot;”
query_key: host
timeframe:
  hours: 1
num_events: 30</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last">Mail Linux</p>
</td>
<td><p class="first last">Mail - Sender rejected</p>
</td>
<td><p class="first last">Sender rejected</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog</p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot;NOQUEUE: reject: RCPT from&quot;”
query_key: host
timeframe:
  hours: 1
num_events: 20</p>
</td>
</tr>
</tbody>
</table>


#### Linux DNS Bind SIEM Rules

  <table border="1" class="docutils" id="id1">
<colgroup>
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">1</th>
<th class="head">DNS</th>
<th class="head">DNS - Anomaly in geographic region</th>
<th class="head">DNS anomaly detection in geographic region</th>
<th class="head">filebeat-*</th>
<th class="head"></th>
<th class="head">filebeat</th>
<th class="head">spike</th>
<th class="head">query_key: geoip.country_code2
threshold_ref: 500
spike_height: 3
spike_type: “up”
timeframe:
  minutes: 10
filter:
 - query_string:
     query: “NOT geoip.country_code2:(US OR PL OR NL OR IE OR DE OR FR OR GB OR SK OR AT OR CZ OR NO OR AU OR DK OR FI OR ES OR LT OR BE OR CH) AND _exists_:geoip.country_code2 AND NOT domain:(*.outlook.com OR *.pool.ntp.org)”</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">2</p>
</td>
<td><p class="first last">DNS</p>
</td>
<td><p class="first last">DNS - Domain requests</p>
</td>
<td><p class="first last">Domain requests</p>
</td>
<td><p class="first last">filebeat-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">filebeat</p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">query_key: “domain”
num_events: 1000
timeframe:
  minutes: 5
filter:
 - query_string:
     query: “NOT domain:(/.*localdomain/) AND _exists_:domain”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">3</p>
</td>
<td><p class="first last">DNS</p>
</td>
<td><p class="first last">DNS - Domain requests by source IP</p>
</td>
<td><p class="first last">Domain requests by source IP</p>
</td>
<td><p class="first last">filebeat-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">filebeat</p>
</td>
<td><p class="first last">cadrinality</p>
</td>
<td><p class="first last">query_key: “src_ip”
cardinality_field: “domain”
max_cardinality: 3000
timeframe:
  minutes: 10
filter:
 - query_string:
     query: “(NOT domain:(/.*.arpa/ OR /.*localdomain/ OR /.*office365.com/) AND _exists_:domain”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">4</p>
</td>
<td><p class="first last">DNS</p>
</td>
<td><p class="first last">DNS - Resolved domain matches IOC IP blacklist</p>
</td>
<td><p class="first last">Resolved domain matches IOC IP blacklist</p>
</td>
<td><p class="first last">filebeat-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">filebeat</p>
</td>
<td><p class="first last">blacklist-ioc</p>
</td>
<td><p class="first last">compare_key: “domain_ip”
blacklist-ioc:
 - “!yaml /etc/logstash/lists/misp_ip.yml”</p>
</td>
</tr>
</tbody>
</table>


#### Fortigate Devices SIEM rules

<table border="1" class="docutils" id="id1">
<colgroup>
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last">FortiOS 6.x</p>
</td>
<td><p class="first last">Fortigate virus</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">fortigate*</p>
</td>
<td><p class="first last">FortiOS with Antivirus, IPS, Fortisandbox modules, Logstash KV filter, default-base-template</p>
</td>
<td><p class="first last">syslog from Forti devices</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “subtype:virus and action:blocked”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last">FortiOS 6.x</p>
</td>
<td><p class="first last">Fortigate http server attack by destination IP</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">fortigate*</p>
</td>
<td><p class="first last">FortiOS with waf, IPS,  modules, Logstash KV filter, default-base-template</p>
</td>
<td><p class="first last">syslog from Forti devices</p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">query_key: “dst_ip”
num_events: 10
timeframe:
  hours: 1
filter:
 - query_string:
     query: “level:alert and subtype:ips and action:dropped and profile:protect_http_server”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last">FortiOS 6.x</p>
</td>
<td><p class="first last">Fortigate forward deny by  source IP</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">fortigate*</p>
</td>
<td><p class="first last">FortiOS with IPS,  modules, Logstash KV filter, default-base-template</p>
</td>
<td><p class="first last">syslog from Forti devices</p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">query_key: “src_ip”
num_events: 250
timeframe:
  hours: 1
filter:
 - query_string:
     query: “subtype:forward AND action:deny”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4</p>
</td>
<td><p class="first last">FortiOS 6.x</p>
</td>
<td><p class="first last">Fortigate failed login</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">fortigate*</p>
</td>
<td><p class="first last">FortiOS with IPS,  modules, Logstash KV filter, default-base-template</p>
</td>
<td><p class="first last">syslog from Forti devices</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “action:login and status:failed”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">5</p>
</td>
<td><p class="first last">FortiOS 6.x</p>
</td>
<td><p class="first last">Fortigate failed login same source</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">fortigate*</p>
</td>
<td><p class="first last">FortiOS with IPS,  modules, Logstash KV filter, default-base-template</p>
</td>
<td><p class="first last">syslog from Forti devices</p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">query_key: “src_ip”
num_events: 18
timeframe:
  minutes: 45
filter:
 - query_string:
     query: “action:login and status:failed”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">6</p>
</td>
<td><p class="first last">FortiOS 6.x</p>
</td>
<td><p class="first last">Fortigate device configuration changed</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">fortigate*</p>
</td>
<td><p class="first last">FortiOS with IPS,  modules, Logstash KV filter, default-base-template</p>
</td>
<td><p class="first last">syslog from Forti devices</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query:”&quot;Configuration is changed in the admin session&quot;”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">7</p>
</td>
<td><p class="first last">FortiOS 6.x</p>
</td>
<td><p class="first last">Fortigate unknown tunneling setting</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">fortigate*</p>
</td>
<td><p class="first last">FortiOS with IPS,  modules, Logstash KV filter, default-base-template</p>
</td>
<td><p class="first last">syslog from Forti devices</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query:”&quot;http_decoder: HTTP.Unknown.Tunnelling&quot;”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">8</p>
</td>
<td><p class="first last">FortiOS 6.x</p>
</td>
<td><p class="first last">Fortigate multiple tunneling same source</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">fortigate*</p>
</td>
<td><p class="first last">FortiOS with IPS,  modules, Logstash KV filter, default-base-template</p>
</td>
<td><p class="first last">syslog from Forti devices</p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">query_key: “src_ip”
num_events: 18
timeframe:
  minutes: 45
filter:
 - query_string:
     query: “&quot;http_decoder: HTTP.Unknown.Tunnelling&quot;”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">9</p>
</td>
<td><p class="first last">FortiOS 6.x</p>
</td>
<td><p class="first last">Fortigate firewall configuration changed</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">fortigate*</p>
</td>
<td><p class="first last">FortiOS with IPS,  modules, Logstash KV filter, default-base-template</p>
</td>
<td><p class="first last">syslog from Forti devices</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query:”action:Edit”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">10</p>
</td>
<td><p class="first last">FortiOS 6.x</p>
</td>
<td><p class="first last">Fortigate SSL VPN login fail</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">fortigate*</p>
</td>
<td><p class="first last">FortiOS with IPS,  modules, Logstash KV filter, default-base-template</p>
</td>
<td><p class="first last">syslog from Forti devices</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query:”ssl-login-fail”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">11</p>
</td>
<td><p class="first last">FortiOS 6.x</p>
</td>
<td><p class="first last">Fortigate Multiple SSL VPN login failed same source</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">fortigate*</p>
</td>
<td><p class="first last">FortiOS with IPS,  modules, Logstash KV filter, default-base-template</p>
</td>
<td><p class="first last">syslog from Forti devices</p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">query_key: “src_ip”
num_events: 18
timeframe:
  minutes: 45
filter:
 - query_string:
     query: “ssl-login-fail”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">12</p>
</td>
<td><p class="first last">FortiOS 6.x</p>
</td>
<td><p class="first last">Fortigate suspicious traffic</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">fortigate*</p>
</td>
<td><p class="first last">FortiOS with IPS,  modules, Logstash KV filter, default-base-template</p>
</td>
<td><p class="first last">syslog from Forti devices</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query:”type:traffic AND status:high”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">13</p>
</td>
<td><p class="first last">FortiOS 6.x</p>
</td>
<td><p class="first last">Fortigate suspicious traffic same source</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">fortigate*</p>
</td>
<td><p class="first last">FortiOS with IPS,  modules, Logstash KV filter, default-base-template</p>
</td>
<td><p class="first last">syslog from Forti devices</p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">query_key: “src_ip”
num_events: 18
timeframe:
  minutes: 45
filter:
 - query_string:
     query: “type:traffic AND status:high”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">14</p>
</td>
<td><p class="first last">FortiOS 6.x</p>
</td>
<td><p class="first last">Fortigate URL blocked</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">fortigate*</p>
</td>
<td><p class="first last">FortiOS with IPS,  modules, Logstash KV filter, default-base-template</p>
</td>
<td><p class="first last">syslog from Forti devices</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query:”action:blocked AND status:warning”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">15</p>
</td>
<td><p class="first last">FortiOS 6.x</p>
</td>
<td><p class="first last">Fortigate multiple URL blocked same source</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">fortigate*</p>
</td>
<td><p class="first last">FortiOS with IPS,  modules, Logstash KV filter, default-base-template</p>
</td>
<td><p class="first last">syslog from Forti devices</p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">query_key: “src_ip”
num_events: 18
timeframe:
  minutes: 45
filter:
 - query_string:
     query: “action:blocked AND status:warning”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">16</p>
</td>
<td><p class="first last">FortiOS 6.x</p>
</td>
<td><p class="first last">Fortigate attack detected</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">fortigate*</p>
</td>
<td><p class="first last">FortiOS with IPS,  modules, Logstash KV filter, default-base-template</p>
</td>
<td><p class="first last">syslog from Forti devices</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query:”attack AND action:detected”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">17</p>
</td>
<td><p class="first last">FortiOS 6.x</p>
</td>
<td><p class="first last">Fortigate attack dropped</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">fortigate*</p>
</td>
<td><p class="first last">FortiOS with IPS,  modules, Logstash KV filter, default-base-template</p>
</td>
<td><p class="first last">syslog from Forti devices</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query:”attack AND action:dropped”</p>
</td>
</tr>
</tbody>
</table>


#### Linux Apache SIEM rules

<table border="1" class="docutils" id="id1">
<caption><span class="caption-text">Table caption</span><a class="headerlink" href="#id1" title="Permalink to this table">¶</a></caption>
<colgroup>
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last">Apache</p>
</td>
<td><p class="first last">HTTP 1xx peak</p>
</td>
<td><p class="first last">Response status 1xx</p>
</td>
<td><p class="first last">httpd*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Apache logs</p>
</td>
<td><p class="first last">spike</p>
</td>
<td><p class="first last">threshold_cur: 100
timeframe:
  hours: 2
spike_height: 5
spike_type: “up”
filter:
- query:
    query_string:
      query: “response.status.code:1*”
- type:
  value: “_doc”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last">Apache</p>
</td>
<td><p class="first last">HTTP 2xx responses for unwanted URLs</p>
</td>
<td><p class="first last"> Requests for URLS like: - /phpMyAdmin, /wpadmin, /wp-login.php, /.env, /admin, /owa/auth/logon.aspx, /api, /license.txt, /api/v1/pods, /solr/admin/info/system, /backup/, /admin/config.php, /dana-na, /dbadmin/, /myadmin/, /mysql/, /php-my-admin/, /sqlmanager/, /mysqlmanager/, config.php
</p>
</td>
<td><p class="first last">httpd*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Apache logs</p>
</td>
<td><p class="first last">blacklist</p>
</td>
<td><p class="first last">compare_key: http.request
ignore_null: true
blacklist:
  - /phpMyAdmin
  - /wpadmin
  - /wp-login.php
  - /.env
  - /admin
  - /owa/auth/logon.aspx
  - /api
  - /license.txt
  - /api/v1/pods
  - /solr/admin/info/system
  - /backup/
  - /admin/config.php
  - /dana-na
  - /dbadmin/
  - /myadmin/
  - /mysql/
  - /php-my-admin/
  - /sqlmanager/
  - /mysqlmanager/
  - config.php</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last">Apache</p>
</td>
<td><p class="first last">HTTP 2xx spike</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">httpd*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Apache logs</p>
</td>
<td><p class="first last">spike</p>
</td>
<td><p class="first last">threshold_cur: 100
timeframe:
    hours: 2
spike_height: 5
spike_type: “up”
filter:
- query:
    query_string:
      query: “response.status.code:2*”
- type:
  value: “_doc”
</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4</p>
</td>
<td><p class="first last">Apache</p>
</td>
<td><p class="first last">HTTP 3x spike</p>
</td>
<td><p class="first last">Response status 3xx</p>
</td>
<td><p class="first last">httpd*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Apache logs</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">threshold_cur: 100
timeframe:
  hours: 2
spike_height: 5
spike_type: “up”
filter:
- query:
    query_string:
      query: “response.status.code:3*”
- type:
  value: “_doc”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">5</p>
</td>
<td><p class="first last">Apache</p>
</td>
<td><p class="first last">HTTP 4xx spike</p>
</td>
<td><p class="first last">Response status 4xx</p>
</td>
<td><p class="first last">httpd*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Apache logs</p>
</td>
<td><p class="first last">spike</p>
</td>
<td><p class="first last">threshold_cur: 100
timeframe:
  hours: 2
spike_height: 5
spike_type: “up”
filter:
- query:
    query_string:
      query: “response.status.code:4*”
- type:
  value: “_doc”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">6</p>
</td>
<td><p class="first last">Apache</p>
</td>
<td><p class="first last">HTTP 5xx spike</p>
</td>
<td><p class="first last">Response status 5xx</p>
</td>
<td><p class="first last">httpd*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Apache logs</p>
</td>
<td><p class="first last">spike</p>
</td>
<td><p class="first last">threshold_cur: 100
timeframe:
  hours: 2
spike_height: 5
spike_type: “up”
filter:
- query:
    query_string:
      query: “response.status.code:5*”
- type:
  value: “_doc”</p>
</td>
</tr>
</tbody>
</table>


#### RedHat / CentOS system SIEM rules

<table border="1" class="docutils" id="id1">
<colgroup>
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last">Linux</p>
</td>
<td><p class="first last">Linux - Group Change</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot;added by root to group&quot;”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last">Linux</p>
</td>
<td><p class="first last">Linux - Group Created</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot;new group: &quot;”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last">Linux</p>
</td>
<td><p class="first last">Linux - Group Removed</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot;removed group: &quot; OR message:&quot;removed shadow group: &quot;”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4</p>
</td>
<td><p class="first last">Linux</p>
</td>
<td><p class="first last">Linux - Interrupted Login</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot;Connection closed by&quot;” </p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">5</p>
</td>
<td><p class="first last">Linux</p>
</td>
<td><p class="first last">Linux -Login Failure</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot;Failed password for&quot;”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">6</p>
</td>
<td><p class="first last">Linux</p>
</td>
<td><p class="first last">Linux - Login Success</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot;Accepted password for&quot;”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">7</p>
</td>
<td><p class="first last">Linux</p>
</td>
<td><p class="first last">Linux - Out of Memory</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot;killed process&quot;”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">8</p>
</td>
<td><p class="first last">Linux</p>
</td>
<td><p class="first last">Linux - Password Change</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot;password changed&quot;”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">9</p>
</td>
<td><p class="first last">Linux</p>
</td>
<td><p class="first last">Linux - Process Segfaults</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:segfault”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">10</p>
</td>
<td><p class="first last">Linux</p>
</td>
<td><p class="first last">Linux - Process Traps</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:traps” </p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">11</p>
</td>
<td><p class="first last">Linux</p>
</td>
<td><p class="first last">Linux - Service Started</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:Started”  </p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">12</p>
</td>
<td><p class="first last">Linux</p>
</td>
<td><p class="first last">Linux - Service Stopped</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:Stopped” </p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">13</p>
</td>
<td><p class="first last">Linux</p>
</td>
<td><p class="first last">Linux - Software Erased</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot;Erased: &quot;”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">14</p>
</td>
<td><p class="first last">Linux</p>
</td>
<td><p class="first last">Linux - Software Installed</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot;Installed: &quot;”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">15</p>
</td>
<td><p class="first last">Linux</p>
</td>
<td><p class="first last">Linux - Software Updated</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot;Updated: &quot;”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">16</p>
</td>
<td><p class="first last">Linux</p>
</td>
<td><p class="first last">Linux - User Created</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot;new user: &quot;”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">17</p>
</td>
<td><p class="first last">Linux</p>
</td>
<td><p class="first last">Linux - User Removed</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “message:&quot;delete user&quot;”</p>
</td>
</tr>
</tbody>
</table>



#### Checkpoint devices SIEM rules

<table border="1" class="docutils" id="id1">
<colgroup>
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last">VPN-1 &amp; FireWall-1</p>
</td>
<td><p class="first last">Checkpoint - Drop a packet by source IP</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">checkpoint*</p>
</td>
<td><p class="first last">Checkpoint devices, fw1-grabber ( https://github.com/certego/fw1-loggrabber )</p>
</td>
<td><p class="first last">Checkpoint firewall, OPSEC Log Export APIs (LEA)</p>
</td>
<td><p class="first last">Frequency</p>
</td>
<td><p class="first last">query_key: “src”
num_events: 10
timeframe:
  hours: 1
filter:
 - query_string:
     query: “action:drop”
use_count_query: true
doc_type: doc</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last">VPN-1 &amp; FireWall-1</p>
</td>
<td><p class="first last">Checkpoint - Reject by source IP</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">checkpoint*</p>
</td>
<td><p class="first last">Checkpoint devices, fw1-grabber ( https://github.com/certego/fw1-loggrabber )</p>
</td>
<td><p class="first last">Checkpoint firewall, OPSEC Log Export APIs (LEA)</p>
</td>
<td><p class="first last">Frequency</p>
</td>
<td><p class="first last">query_key: “src”
num_events: 10
timeframe:
  hours: 1
filter:
 - query_string:
     query: “action:reject”
use_count_query: true
doc_type: doc</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last">VPN-1 &amp; FireWall-1</p>
</td>
<td><p class="first last">Checkpoint - User login</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">checkpoint*</p>
</td>
<td><p class="first last">Checkpoint devices, fw1-grabber ( https://github.com/certego/fw1-loggrabber )</p>
</td>
<td><p class="first last">Checkpoint firewall, OPSEC Log Export APIs (LEA)</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">query_key: “user”
filter:
- query_string:
       query: “auth_status:&quot;Successful Login&quot;”
use_count_query: true
doc_type: doc</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4</p>
</td>
<td><p class="first last">VPN-1 &amp; FireWall-1</p>
</td>
<td><p class="first last">Checkpoint - Failed Login</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">checkpoint*</p>
</td>
<td><p class="first last">Checkpoint devices, fw1-grabber ( https://github.com/certego/fw1-loggrabber )</p>
</td>
<td><p class="first last">Checkpoint firewall, OPSEC Log Export APIs (LEA)</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">query_key: “user”
filter:
- query_string:
       query: “auth_status:&quot;Failed Login&quot;”
use_count_query: true
doc_type: doc</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">5</p>
</td>
<td><p class="first last">VPN-1 &amp; FireWall-1</p>
</td>
<td><p class="first last">Checkpoint - Application Block by user</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">checkpoint*</p>
</td>
<td><p class="first last">Checkpoint devices, fw1-grabber ( https://github.com/certego/fw1-loggrabber )</p>
</td>
<td><p class="first last">Checkpoint firewall, OPSEC Log Export APIs (LEA)</p>
</td>
<td><p class="first last">Frequency</p>
</td>
<td><p class="first last">query_key: “user”
num_events: 10
timeframe:
  hours: 1
filter:
 - query_string:
     query: “action:block AND product:&quot;Application Control&quot;”
use_count_query: true
doc_type: doc</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">6</p>
</td>
<td><p class="first last">VPN-1 &amp; FireWall-1</p>
</td>
<td><p class="first last">Checkpoint - URL Block by user</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">checkpoint*</p>
</td>
<td><p class="first last">Checkpoint devices, fw1-grabber ( https://github.com/certego/fw1-loggrabber )</p>
</td>
<td><p class="first last">Checkpoint firewall, OPSEC Log Export APIs (LEA)</p>
</td>
<td><p class="first last">Frequency</p>
</td>
<td><p class="first last">query_key: “user”
num_events: 10
timeframe:
  hours: 1
filter:
 - query_string:
     query: “action:block AND product:&quot;URL Filtering&quot;”
use_count_query: true
doc_type: doc</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">7</p>
</td>
<td><p class="first last">VPN-1 &amp; FireWall-1</p>
</td>
<td><p class="first last">Checkpoint - Block action with user</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">checkpoint*</p>
</td>
<td><p class="first last">Checkpoint devices, fw1-grabber ( https://github.com/certego/fw1-loggrabber )</p>
</td>
<td><p class="first last">Checkpoint firewall, OPSEC Log Export APIs (LEA)</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">query_key: “user”
filter:
 - query_string:
     query: “action:block”
use_count_query: true
doc_type: doc</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">8</p>
</td>
<td><p class="first last">VPN-1 &amp; FireWall-1</p>
</td>
<td><p class="first last">Checkpoint - Encryption keys were created</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">checkpoint*</p>
</td>
<td><p class="first last">Checkpoint devices, fw1-grabber ( https://github.com/certego/fw1-loggrabber )</p>
</td>
<td><p class="first last">Checkpoint firewall, OPSEC Log Export APIs (LEA)</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: “action:keyinst”
use_count_query: true
doc_type: doc</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">9</p>
</td>
<td><p class="first last">VPN-1 &amp; FireWall-1</p>
</td>
<td><p class="first last">Checkpoint - Connection was detected by Interspect</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">checkpoint*</p>
</td>
<td><p class="first last">Checkpoint devices, fw1-grabber ( https://github.com/certego/fw1-loggrabber )</p>
</td>
<td><p class="first last">Checkpoint firewall, OPSEC Log Export APIs (LEA)</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: “action:detect”
use_count_query: true
doc_type: doc</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">10</p>
</td>
<td><p class="first last">VPN-1 &amp; FireWall-1</p>
</td>
<td><p class="first last">Checkpoint - Connection was subject to a configured protections</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">checkpoint*</p>
</td>
<td><p class="first last">Checkpoint devices, fw1-grabber ( https://github.com/certego/fw1-loggrabber )</p>
</td>
<td><p class="first last">Checkpoint firewall, OPSEC Log Export APIs (LEA)</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: “action:inspect”
use_count_query: true
doc_type: doc</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">11</p>
</td>
<td><p class="first last">VPN-1 &amp; FireWall-1</p>
</td>
<td><p class="first last">Checkpoint - Connection with source IP was quarantined</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">checkpoint*</p>
</td>
<td><p class="first last">Checkpoint devices, fw1-grabber ( https://github.com/certego/fw1-loggrabber )</p>
</td>
<td><p class="first last">Checkpoint firewall, OPSEC Log Export APIs (LEA)</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">query_key: “src”
filter:
 - query_string:
     query: “action:quarantine”
use_count_query: true
doc_type: doc</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">12</p>
</td>
<td><p class="first last">VPN-1 &amp; FireWall-1</p>
</td>
<td><p class="first last">Checkpoint - Malicious code in the connection with source IP was replaced</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">checkpoint*</p>
</td>
<td><p class="first last">Checkpoint devices, fw1-grabber ( https://github.com/certego/fw1-loggrabber )</p>
</td>
<td><p class="first last">Checkpoint firewall, OPSEC Log Export APIs (LEA)</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">query_key: “src”
filter:
 - query_string:
     query: “action:&quot;Replace Malicious code&quot;”
use_count_query: true
doc_type: doc</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">13</p>
</td>
<td><p class="first last">VPN-1 &amp; FireWall-1</p>
</td>
<td><p class="first last">Checkpoint - Connection with source IP was routed through the gateway acting as a central hub</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">checkpoint*</p>
</td>
<td><p class="first last">Checkpoint devices, fw1-grabber ( https://github.com/certego/fw1-loggrabber )</p>
</td>
<td><p class="first last">Checkpoint firewall, OPSEC Log Export APIs (LEA)</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">query_key: “src”
filter:
 - query_string:
     query: “action:&quot;VPN routing&quot;”
use_count_query: true
doc_type: doc</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">14</p>
</td>
<td><p class="first last">VPN-1 &amp; FireWall-1</p>
</td>
<td><p class="first last">Checkpoint - Security event with user was monitored</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">checkpoint*</p>
</td>
<td><p class="first last">Checkpoint devices, fw1-grabber ( https://github.com/certego/fw1-loggrabber )</p>
</td>
<td><p class="first last">Checkpoint firewall, OPSEC Log Export APIs (LEA)</p>
</td>
<td><p class="first last">Frequency</p>
</td>
<td><p class="first last">query_key: “user”
num_events: 10
timeframe:
  hours: 1
filter:
 - query_string:
     query: “action:Monitored”
use_count_query: true
doc_type: doc</p>
</td>
</tr>
</tbody>
</table>


#### Cisco ESA devices SIEM rule

<table border="1" class="docutils" id="id1">
<colgroup>
<col width="7%" />
<col width="7%" />
<col width="9%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="40%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last">Cisco ESA</p>
</td>
<td><p class="first last">ESA - Attachments exceeded the URL scan</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Cisco ESA</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”attachments exceeded the URL scan”’</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last">Cisco ESA</p>
</td>
<td><p class="first last">ESA - Extraction Failure</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Cisco ESA</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”Extraction Failure”’</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last">Cisco ESA</p>
</td>
<td><p class="first last">ESA - Failed to expand URL</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Cisco ESA</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”Failed to expand URL”’</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4</p>
</td>
<td><p class="first last">Cisco ESA</p>
</td>
<td><p class="first last">ESA - Invalid host configured</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Cisco ESA</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”Invalid host configured”’</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">5</p>
</td>
<td><p class="first last">Cisco ESA</p>
</td>
<td><p class="first last">ESA - Marked unscannable due to RFC Violation</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Cisco ESA</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”was marked unscannable due to RFC Violation”’</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">6</p>
</td>
<td><p class="first last">Cisco ESA</p>
</td>
<td><p class="first last">ESA - Message was not scanned for Sender Domain Reputation</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Cisco ESA</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”Message was not scanned for Sender Domain Reputation”’</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">7</p>
</td>
<td><p class="first last">Cisco ESA</p>
</td>
<td><p class="first last">ESA - URL Reputation Rule</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Cisco ESA</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”URL Reputation Rule”’</p>
</td>
</tr>
</tbody>
</table>


#### Forcepoint devices SIEM rules

<table border="1" class="docutils" id="id1">
<colgroup>
<col width="7%" />
<col width="7%" />
<col width="9%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="40%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Forcepoint HIGH</p>
</td>
<td><p class="first last">All high alerts</p>
</td>
<td><p class="first last">syslog-dlp*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">alert_text_type: alert_text_only 
alert_text: “Forcepoint HIGH alert\n\n When: {}\n Analyzed by: {}\n User name: {}\n Source: {}\nDestination: {}\n\n{}\n” 
alert_text_args: 
  - timestamp_timezone
  - Analyzed_by
  - user
  - Source
  - Destination
  - kibana_link 
use_kibana4_dashboard: “link do saved search” 
kibana4_start_timedelta: 
 minutes: 5 
kibana4_end_timedelta: 
 minutes: 0 
 filter:
 - query_string:
        query: “Severity:HIGH”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Forcepoint MEDIUM</p>
</td>
<td><p class="first last">All medium alerts</p>
</td>
<td><p class="first last">syslog-dlp*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">alert_text_type: alert_text_only 
alert_text: “Forcepoint MEDIUM alert\n\n When: {}\n Analyzed by: {}\n User name: {}\n Source: {}\nDestination: {}\n\n{}\n” 
alert_text_args: 
  - timestamp_timezone
  - Analyzed_by
  - user
  - Source
  - Destination
  - kibana_link 
use_kibana4_dashboard: “link do saved search” 
kibana4_start_timedelta: 
 minutes: 5 
kibana4_end_timedelta: 
 minutes: 0 
 filter:
 - query_string:
        query: “Severity:MEDIUM”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Forcepoint LOW</p>
</td>
<td><p class="first last">All low alerts</p>
</td>
<td><p class="first last">syslog-dlp*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">alert_text_type: alert_text_only 
alert_text: “Forcepoint LOW alert\n\n When: {}\n Analyzed by: {}\n User name: {}\n Source: {}\nDestination: {}\n\n{}\n” 
alert_text_args: 
  - timestamp_timezone
  - Analyzed_by
  - user
  - Source
  - Destination
  - kibana_link 
use_kibana4_dashboard: “link do saved search” 
kibana4_start_timedelta: 
 minutes: 5 
kibana4_end_timedelta: 
 minutes: 0 
 filter:
 - query_string:
        query: “Severity:LOW”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Forcepoint blocked email</p>
</td>
<td><p class="first last">Email was blocked by forcepoint</p>
</td>
<td><p class="first last">syslog-dlp*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">alert_text_type: alert_text_only 
alert_text: “Email blocked\n\n When: {}\n Analyzed by: {}\n File name: {}\n Source: {}\nDestination: {}\n\n{}\n” 
alert_text_args: 
  - timestamp_timezone
  - Analyzed_by
  - File_Name
  - Source
  - Destination
  - kibana_link 
use_kibana4_dashboard: “link do saved search” 
kibana4_start_timedelta: 
 minutes: 5 
kibana4_end_timedelta: 
 minutes: 0 
 filter:
 - query_string:
        query: “Action:Blocked and Channel:Endpoint Email”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">5</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Forcepoint removables</p>
</td>
<td><p class="first last">Forcepoint blocked data transfer to removeable device</p>
</td>
<td><p class="first last">syslog-dlp*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">alert_text_type: alert_text_only 
alert_text: “Data transfer to removable device blocked\n\n When: {}\n Analyzed by: {}\n File name: {}\n Source: {}\nDestination: {}\n\n{}\n” 
alert_text_args: 
  - timestamp_timezone
  - Analyzed_by
  - File_Name
  - Source
  - Destination
  - kibana_link 
use_kibana4_dashboard: “link do saved search” 
kibana4_start_timedelta: 
 minutes: 5 
kibana4_end_timedelta: 
 minutes: 0 
 filter:
 - query_string:
        query: “Action:Blocked and Channel:Endpoint Removable Media”</p>
</td>
</tr>
</tbody>
</table>


#### Oracle Database Engine SIEM rules

<table border="1" class="docutils" id="id1">
<colgroup>
<col width="7%" />
<col width="7%" />
<col width="9%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="40%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last">Oracle DB</p>
</td>
<td><p class="first last">Oracle - Allocate memory ORA-00090</p>
</td>
<td><p class="first last">Failed to allocate memory for cluster database</p>
</td>
<td><p class="first last">oracle-*</p>
</td>
<td><p class="first last">Filebeat</p>
</td>
<td><p class="first last">Oracle Alert Log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
  minutes: 15
filter:
  - term:
      oracle.code: “ora-00090”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last">Oracle DB</p>
</td>
<td><p class="first last">Oracle logon denied ORA-12317</p>
</td>
<td><p class="first last"> logon to database (link name string) </p>
</td>
<td><p class="first last">oracle-*</p>
</td>
<td><p class="first last">Filebeat</p>
</td>
<td><p class="first last">Oracle Alert Log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
    minutes: 15
filter:
  - term:
      oracle.code: “ora-12317”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last">Oracle DB</p>
</td>
<td><p class="first last">Oracle credential failed ORA-12638</p>
</td>
<td><p class="first last">Credential retrieval failed</p>
</td>
<td><p class="first last">oracle-*</p>
</td>
<td><p class="first last">Filebeat</p>
</td>
<td><p class="first last">Oracle Alert Log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
    minutes: 15
num_events: 10
filter:
  - term:
      oracle.code: “ora-12638”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4</p>
</td>
<td><p class="first last">Oracle DB</p>
</td>
<td><p class="first last">Oracle client internal error ORA-12643</p>
</td>
<td><p class="first last">Client received internal error from server</p>
</td>
<td><p class="first last">oracle-*</p>
</td>
<td><p class="first last">Filebeat</p>
</td>
<td><p class="first last">Oracle Alert Log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
    minutes: 15
num_events: 10
filter:
  - term:
      oracle.code: “ora-12643”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">5</p>
</td>
<td><p class="first last">Oracle DB</p>
</td>
<td><p class="first last">ORA-00018: maximum number of sessions exceeded</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">oracle-*</p>
</td>
<td><p class="first last">Filebeat</p>
</td>
<td><p class="first last">Oracle Alert Log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
    minutes: 15
filter:
  - term:
      oracle.code: “ora-00018”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">6</p>
</td>
<td><p class="first last">Oracle DB</p>
</td>
<td><p class="first last">ORA-00019: maximum number of session licenses exceeded</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">oracle-*</p>
</td>
<td><p class="first last">Filebeat</p>
</td>
<td><p class="first last">Oracle Alert Log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
    minutes: 15
filter:
  - term:
      oracle.code: “ora-00019”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">7</p>
</td>
<td><p class="first last">Oracle DB</p>
</td>
<td><p class="first last">ORA-00020: maximum number of processes (string) exceeded</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">oracle-*</p>
</td>
<td><p class="first last">Filebeat</p>
</td>
<td><p class="first last">Oracle Alert Log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
    minutes: 15
filter:
  - term:
      oracle.code: “ora-00020”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">8</p>
</td>
<td><p class="first last">Oracle DB</p>
</td>
<td><p class="first last">ORA-00024: logins from more than one process not allowed in single-process mode</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">oracle-*</p>
</td>
<td><p class="first last">Filebeat</p>
</td>
<td><p class="first last">Oracle Alert Log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
    minutes: 15
filter:
  - term:
      oracle.code: “ora-00024”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">9</p>
</td>
<td><p class="first last">Oracle DB</p>
</td>
<td><p class="first last">ORA-00025: failed to allocate string ( out of memory )</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">oracle-*</p>
</td>
<td><p class="first last">Filebeat</p>
</td>
<td><p class="first last">Oracle Alert Log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
    minutes: 15
filter:
  - term:
      oracle.code: “ora-00025”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">10</p>
</td>
<td><p class="first last">Oracle DB</p>
</td>
<td><p class="first last">ORA-00055: maximum number of DML locks exceeded</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">oracle-*</p>
</td>
<td><p class="first last">Filebeat</p>
</td>
<td><p class="first last">Oracle Alert Log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
    minutes: 15
filter:
  - term:
      oracle.code: “ora-00055”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">11</p>
</td>
<td><p class="first last">Oracle DB</p>
</td>
<td><p class="first last">ORA-00057: maximum number of temporary table locks exceeded</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">oracle-*</p>
</td>
<td><p class="first last">Filebeat</p>
</td>
<td><p class="first last">Oracle Alert Log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
    minutes: 15
filter:
  - term:
      oracle.code: “ora-00057”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">12</p>
</td>
<td><p class="first last">Oracle DB</p>
</td>
<td><p class="first last">ORA-00059: maximum number of DB_FILES exceeded</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">oracle-*</p>
</td>
<td><p class="first last">Filebeat</p>
</td>
<td><p class="first last">Oracle Alert Log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
    minutes: 15
filter:
  - term:
      oracle.code: “ora-00059”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">13</p>
</td>
<td><p class="first last">Oracle DB</p>
</td>
<td><p class="first last">Oracle - Deadlocks ORA - 0060</p>
</td>
<td><p class="first last">Deadlock detected while waiting for resource</p>
</td>
<td><p class="first last">oracle-*</p>
</td>
<td><p class="first last">Filebeat</p>
</td>
<td><p class="first last">Oracle Alert Log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
    minutes: 15
filter:
  - term:
      oracle.code: “ora-00060”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">14</p>
</td>
<td><p class="first last">Oracle DB</p>
</td>
<td><p class="first last">ORA-00063: maximum number of log files exceeded</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">oracle-*</p>
</td>
<td><p class="first last">Filebeat</p>
</td>
<td><p class="first last">Oracle Alert Log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
    minutes: 15
filter:
  - term:
      oracle.code: “ora-00063”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">15</p>
</td>
<td><p class="first last">Oracle DB</p>
</td>
<td><p class="first last">ORA-00064: object is too large to allocate on this O/S</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">oracle-*</p>
</td>
<td><p class="first last">Filebeat</p>
</td>
<td><p class="first last">Oracle Alert Log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
    minutes: 15
filter:
  - term:
      oracle.code: “ora-00064”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">16</p>
</td>
<td><p class="first last">Oracle DB</p>
</td>
<td><p class="first last">ORA-12670: Incorrect role password</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">oracle-*</p>
</td>
<td><p class="first last">Filebeat</p>
</td>
<td><p class="first last">Oracle Alert Log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
    minutes: 15
num_events: 10
filter:
  - term:
      oracle.code: “ora-12670”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">17</p>
</td>
<td><p class="first last">Oracle DB</p>
</td>
<td><p class="first last">ORA-12672: Database logon failure</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">oracle-*</p>
</td>
<td><p class="first last">Filebeat</p>
</td>
<td><p class="first last">Oracle Alert Log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
    minutes: 15
num_events: 10
filter:
  - term:
      oracle.code: “ora-12672”</p>
</td>
</tr>
</tbody>
</table>


#### Paloalto devices SIEM rules

<table border="1" class="docutils" id="id1">
<colgroup>
<col width="7%" />
<col width="7%" />
<col width="9%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="40%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Paloalto - Configuration changes failed</p>
</td>
<td><p class="first last">Config changes Failed</p>
</td>
<td><p class="first last">paloalto-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">timeframe:
  minutes: 15
num_events: 10
filter:
  - term:
      pan.type: CONFIG
  - term:
      result: Failed</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Paloalto - Flood detected</p>
</td>
<td><p class="first last">Flood detected via a Zone Protection profile</p>
</td>
<td><p class="first last">paloalto-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">timeframe:
    minutes: 15
num_events: 10
filter:
  - term:
      pan.type: THREAT
  - term:
      pan.subtype: flood</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Paloalto - Scan detected</p>
</td>
<td><p class="first last">Scan detected via a Zone Protection profile</p>
</td>
<td><p class="first last">paloalto-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">timeframe:
    minutes: 15
num_events: 10
filter:
  - term:
      pan.type: THREAT
  - term:
      pan.subtype: scan</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Paloalto - Spyware detected</p>
</td>
<td><p class="first last">Spyware detected via an Anti-Spyware profile</p>
</td>
<td><p class="first last">paloalto-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">timeframe:
    minutes: 15
num_events: 10
filter:
  - term:
      pan.type: THREAT
  - term:
      pan.subtype: spyware</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">5</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Paloalto - Unauthorized configuration changed</p>
</td>
<td><p class="first last">Attepmted Unauthorized configuration changes</p>
</td>
<td><p class="first last">paloalto-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">timeframe:
    minutes: 15
num_events: 10
filter:
  - term:
      pan.type: CONFIG
  - term:
      result: Unathorized</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">6</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Paloalto - Virus detected</p>
</td>
<td><p class="first last">Virus detected via an Antivirus profile.</p>
</td>
<td><p class="first last">paloalto-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">timeframe:
    minutes: 15
num_events: 10
filter:
  - term:
      pan.type: THREAT
  - terms:
      pan.subtype: [ “virus”, “wildfire-virus” ]</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">7</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Paloalto - Vulnerability exploit detected</p>
</td>
<td><p class="first last">Vulnerability exploit detected via a Vulnerability Protection profile</p>
</td>
<td><p class="first last">paloalto-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">timeframe:
    minutes: 15
num_events: 10
filter:
  - term:
      pan.type: THREAT
  - term:
      pan.subtype: vulnerability</p>
</td>
</tr>
</tr>
</tbody>
</table>


#### Microsoft Exchange SIEM rules

<table border="1" class="docutils" id="id1">
<caption><span class="caption-text">Table caption</span><a class="headerlink" href="#id1" title="Permalink to this table">¶</a></caption>
<colgroup>
<col width="7%" />
<col width="7%" />
<col width="9%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="40%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last">MS Exchange</p>
</td>
<td><p class="first last">Exchange - Increased amount of incoming emails</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">exchange-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">spike</p>
</td>
<td><p class="first last">metric_agg_key: “exchange.network-message-id”
metric_agg_type: “cardinality”
doc_type: “_doc”
max_threshold: 10
buffer_time:
  minutes: 1
filter:
 - query_string:
     query: “exchange.sender-address:*.company.com AND exchange.event-id:SEND AND exchange.message-subject:*”
query_key: [“exchange.message-subject-agg”, “exchange.sender-address”]</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last">MS Exchange</p>
</td>
<td><p class="first last">Exchange - Internal sender sent email to public provider</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">exchange-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">whitelist</p>
</td>
<td><p class="first last">metric_agg_key: “exchange.network-message-id”
metric_agg_type: “cardinality”
doc_type: “_doc”
max_threshold: 10
buffer_time:
    minutes: 1
filter:
 - query_string:
     query: “NOT exchange.sender-address:(*&#64;company.com) AND exchange.event-id:SEND AND exchange.message-subject:* AND NOT exchange.recipient-address:public&#64;company.com”
query_key: [“exchange.message-subject-agg”, “exchange.sender-address”]</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last">MS Exchange</p>
</td>
<td><p class="first last">Exchange - Internal sender sent ethe same title to many recipients</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">exchange-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">metric_aggregation</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: “NOT exchange.recipient-address:public&#64;company.com AND NOT exchange.sender-address:(*&#64;company.com) AND exchange.event-id:SEND AND exchange.data.atch:[1 TO *] AND _exists_:exchange AND exchange.message-subject:(/.*invoice.*/ OR /.*payment.*/ OR /.*faktur.*/)”
query_key: [“exchange.sender-address”]</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4</p>
</td>
<td><p class="first last">MS Exchange</p>
</td>
<td><p class="first last">Exchange - Received email with banned title</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">exchange-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">threshold_ref: 5
timeframe:
    days: 1
spike_height: 3
spike_type: “up”
alert_on_new_data: false
use_count_query: true
doc_type: _doc
query_key: [“exchange.sender-address”]
filter:
 - query_string:
     query: “NOT exchange.event-id:(DEFER OR RECEIVE OR AGENTINFO) AND _exists_:exchange”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">5</p>
</td>
<td><p class="first last">MS Exchange</p>
</td>
<td><p class="first last">Exchange - The same title to many recipients</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">exchange-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">metric_aggregation</p>
</td>
<td><p class="first last">compare_key: “exchange.sender-address”
ignore_null: true
filter:
 - query_string:
     query: “NOT exchange.recipient-address:(*&#64;company.com) AND _exists_:exchange.recipient-address AND exchange.event-id:AGENTINFO AND NOT exchange.sender-address:(bok&#64;* OR postmaster&#64;*) AND exchange.data.atch:[1 TO *] AND exchange.recipient-count:1 AND exchange.recipient-address:(*&#64;gmail.com OR *&#64;wp.pl OR *&#64;o2.pl OR *&#64;interia.pl OR *&#64;op.pl OR *&#64;onet.pl OR *&#64;vp.pl OR *&#64;tlen.pl OR *&#64;onet.eu OR *&#64;poczta.fm OR *&#64;interia.eu OR *&#64;hotmail.com OR *&#64;gazeta.pl OR *&#64;yahoo.com OR *&#64;icloud.com OR *&#64;outlook.com OR *&#64;autograf.pl OR *&#64;neostrada.pl OR *&#64;vialex.pl OR *&#64;go2.pl OR *&#64;buziaczek.pl OR *&#64;yahoo.pl OR *&#64;post.pl OR *&#64;wp.eu OR *&#64;me.com OR *&#64;yahoo.co.uk OR *&#64;onet.com.pl OR *&#64;tt.com.pl OR *&#64;spoko.pl OR *&#64;amorki.pl OR *&#64;7dots.pl OR *&#64;googlemail.com OR *&#64;gmx.de OR *&#64;upcpoczta.pl OR *&#64;live.com OR *&#64;piatka.pl OR *&#64;opoczta.pl OR *&#64;web.de OR *&#64;protonmail.com OR *&#64;poczta.pl OR *&#64;hot.pl OR *&#64;mail.ru OR *&#64;yahoo.de OR *&#64;gmail.pl OR *&#64;02.pl OR *&#64;int.pl OR *&#64;adres.pl OR *&#64;10g.pl OR *&#64;ymail.com OR *&#64;data.pl OR *&#64;aol.com OR *&#64;gmial.com OR *&#64;hotmail.co.uk)”
whitelist:
  - allowed&#64;example.com
  - allowed&#64;example2.com</p>
</td>
</tr>
</tbody>
</table>


#### Juniper Devices SIEM Rules

<table border="1" class="docutils" id="id1">
<colgroup>
<col width="7%" />
<col width="7%" />
<col width="9%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="40%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last">Junos-IDS</p>
</td>
<td><p class="first last">Juniper - IDS attact detection</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">junos*</p>
</td>
<td><p class="first last">JunOS devices with IDS module</p>
</td>
<td><p class="first last">Syslog from Juniper devices</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “_exists_:attack-name”
include:
 - attack-name</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last">Junos-IDS</p>
</td>
<td><p class="first last">Junos - RT flow session deny</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">junos*</p>
</td>
<td><p class="first last">JunOS devices SRX, RT Fflow</p>
</td>
<td><p class="first last">Syslog from Juniper devices</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “category:RT_FLOW AND subcat:RT_FLOW_SESSION_DENY”
include:
 - srcip
- dstip</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last">Junos-IDS</p>
</td>
<td><p class="first last">Junos - RT flow reassemble fail</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">junos*</p>
</td>
<td><p class="first last">JunOS devices SRX, RT Fflow</p>
</td>
<td><p class="first last">Syslog from Juniper devices</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “category:RT_FLOW AND subcat:FLOW_REASSEMBLE_FAIL”
include:
 - srcip
- dstip</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4</p>
</td>
<td><p class="first last">Junos-IDS</p>
</td>
<td><p class="first last">Junos - RT flow mcast rpf fail</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">junos*</p>
</td>
<td><p class="first last">JunOS devices SRX, RT Fflow</p>
</td>
<td><p class="first last">Syslog from Juniper devices</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “category:RT_FLOW AND subcat:FLOW_MCAST_RPF_FAIL”
include:
 - srcip
- dstip</p>
</td>
</tr>
</tr>
</tbody>
</table>


#### Fudo SIEM Rules

<table border="1" class="docutils" id="id1">
<colgroup>
<col width="7%" />
<col width="7%" />
<col width="9%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="40%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Fudo - General Error</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">fudo*</p>
</td>
<td><p class="first last">http://download.wheelsystems.com/documentation/fudo/4_0/online_help/en/reference/en/log_messages.html</p>
</td>
<td><p class="first last">Syslog FUDO</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “syslog_serverity:error”
include:
- fudo_message</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Fudo - Failed to authenticate using password</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">fudo*</p>
</td>
<td><p class="first last">http://download.wheelsystems.com/documentation/fudo/4_0/online_help/en/reference/en/log_messages.html</p>
</td>
<td><p class="first last">Syslog FUDO</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “fudo_code:FSE0634”
include:
- fudo_user</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Fudo - Unable to establish connection</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">fudo*</p>
</td>
<td><p class="first last">http://download.wheelsystems.com/documentation/fudo/4_0/online_help/en/reference/en/log_messages.html</p>
</td>
<td><p class="first last">Syslog FUDO</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “fudo_code:FSE0378”
include:
- fudo_connection
- fudo_login</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Fudo - Authentication timeout</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">fudo*</p>
</td>
<td><p class="first last">http://download.wheelsystems.com/documentation/fudo/4_0/online_help/en/reference/en/log_messages.html</p>
</td>
<td><p class="first last">Syslog FUDO</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “fudo_code:FUE0081”</p>
</td>
</tr>
</tbody>
</table>


#### Squid SIEM Rules

<table border="1" class="docutils" id="id1">
<colgroup>
<col width="7%" />
<col width="7%" />
<col width="9%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="40%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last">Squid</p>
</td>
<td><p class="first last">Squid - Configuration file changed</p>
</td>
<td><p class="first last">Modyfing squid.conf file</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last">Audit module</p>
</td>
<td><p class="first last">syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: ‘message:”File /etc/squid/squid.conf checksum changed.”’</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last">Squid</p>
</td>
<td><p class="first last">Squid - Cannot open HTTP port</p>
</td>
<td><p class="first last">Cannot open HTTP Port</p>
</td>
<td><p class="first last">squid-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">squid</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”Cannot open HTTP Port”’</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last">Squid</p>
</td>
<td><p class="first last">Squid - Unauthorized connection</p>
</td>
<td><p class="first last">Unauthorized connection, blocked website entry</p>
</td>
<td><p class="first last">squid-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">squid</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘squid_request_status:”TCP_DENIED/403”’</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4</p>
</td>
<td><p class="first last">Squid</p>
</td>
<td><p class="first last">Squid - Proxy server stopped</p>
</td>
<td><p class="first last">Service stopped</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”Stopped Squid caching proxy.”’</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">5</p>
</td>
<td><p class="first last">Squid</p>
</td>
<td><p class="first last">Squid - Proxy server started</p>
</td>
<td><p class="first last">Service started</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”Started Squid caching proxy.”’</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">6</p>
</td>
<td><p class="first last">Squid</p>
</td>
<td><p class="first last">Squid - Invalid request</p>
</td>
<td><p class="first last">Invalid request</p>
</td>
<td><p class="first last">squid-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">squid</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘squid_request_status:”error:invalid-request”’</p>
</td>
</tr>
</tbody>
</table>



#### McAfee SIEM Rules

<table border="1" class="docutils" id="id1">
<colgroup>
<col width="7%" />
<col width="7%" />
<col width="9%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="40%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last">Squid</p>
</td>
<td><p class="first last">Squid - Configuration file changed</p>
</td>
<td><p class="first last">Modyfing squid.conf file</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last">Audit module</p>
</td>
<td><p class="first last">syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: ‘message:”File /etc/squid/squid.conf checksum changed.”’</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last">Squid</p>
</td>
<td><p class="first last">Squid - Cannot open HTTP port</p>
</td>
<td><p class="first last">Cannot open HTTP Port</p>
</td>
<td><p class="first last">squid-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">squid</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”Cannot open HTTP Port”’</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last">Squid</p>
</td>
<td><p class="first last">Squid - Unauthorized connection</p>
</td>
<td><p class="first last">Unauthorized connection, blocked website entry</p>
</td>
<td><p class="first last">squid-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">squid</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘squid_request_status:”TCP_DENIED/403”’</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4</p>
</td>
<td><p class="first last">Squid</p>
</td>
<td><p class="first last">Squid - Proxy server stopped</p>
</td>
<td><p class="first last">Service stopped</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”Stopped Squid caching proxy.”’</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">5</p>
</td>
<td><p class="first last">Squid</p>
</td>
<td><p class="first last">Squid - Proxy server started</p>
</td>
<td><p class="first last">Service started</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”Started Squid caching proxy.”’</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">6</p>
</td>
<td><p class="first last">Squid</p>
</td>
<td><p class="first last">Squid - Invalid request</p>
</td>
<td><p class="first last">Invalid request</p>
</td>
<td><p class="first last">squid-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">squid</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘squid_request_status:”error:invalid-request”’</p>
</td>
</tr>
</tbody>
</table>


#### Microsoft  DNS Server SIEM Rules

<table border="1" class="docutils" id="id1">
<colgroup>
<col width="7%" />
<col width="7%" />
<col width="9%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="40%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1.</p>
</td>
<td><p class="first last">WINDOWS DNS</p>
</td>
<td><p class="first last">WIN DNS - Format Error</p>
</td>
<td><p class="first last">Format error; DNS server did not understand the update request</p>
</td>
<td><p class="first last">prod-win-dns-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
  minutes: 15
filter:
  - term:
      dns.result: SERVFAIL</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2.</p>
</td>
<td><p class="first last">WINDOWS DNS</p>
</td>
<td><p class="first last">WIN DNS - DNS server internal error</p>
</td>
<td><p class="first last">DNS server encountered an internal error, such as a forwarding timeout</p>
</td>
<td><p class="first last">prod-win-dns-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
  - minutes: 15
filter:
  - term:
       dns.result: FORMERR</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3.</p>
</td>
<td><p class="first last">WINDOWS DNS</p>
</td>
<td><p class="first last">WIN DNS - DNS refuses to perform the update</p>
</td>
<td><p class="first last">DNS server refuses to perform the update</p>
</td>
<td><p class="first last">prod-win-dns-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">“timeframe:
  - minutes: 15
filter:
  - term:
       dns.result: REFUSED</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4.</p>
</td>
<td><p class="first last">WINDOWS DNS</p>
</td>
<td><p class="first last">WIN DNS - DNS Zone Deleted</p>
</td>
<td><p class="first last">DNS Zone delete</p>
</td>
<td><p class="first last">prod-win-dns-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
  minutes: 15
filter:
  - term:
       event.id: 513</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">5.</p>
</td>
<td><p class="first last">WINDOWS DNS</p>
</td>
<td><p class="first last">WIN DNS - DNS Record Deleted</p>
</td>
<td><p class="first last">DNS Record Delete</p>
</td>
<td><p class="first last">prod-win-dns-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
  minutes: 15
filter:
  - term:
       event.id: 516</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">6.</p>
</td>
<td><p class="first last">WINDOWS DNS</p>
</td>
<td><p class="first last">WIN DNS - DNS Node Deleted</p>
</td>
<td><p class="first last">DNS Node Delete</p>
</td>
<td><p class="first last">prod-win-dns-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
  minutes: 15
filter:
  - term:
       event.id: 518</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">7.</p>
</td>
<td><p class="first last">WINDOWS DNS</p>
</td>
<td><p class="first last">WIN DNS - DNS Remove Trust Point</p>
</td>
<td><p class="first last">DNS Remove trust point</p>
</td>
<td><p class="first last">prod-win-dns-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
  minutes: 15
filter:
  - term:
       event.id: 546</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">8.</p>
</td>
<td><p class="first last">WINDOWS DNS</p>
</td>
<td><p class="first last">WIN DNS - DNS Restart Server</p>
</td>
<td><p class="first last">Restart Server</p>
</td>
<td><p class="first last">prod-win-dns-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
  minutes: 15
filter:
  - term:
       event.id: 548</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">9.</p>
</td>
<td><p class="first last">WINDOWS DNS</p>
</td>
<td><p class="first last">WIN DNS - DNS Response failure</p>
</td>
<td><p class="first last">Response Failure</p>
</td>
<td><p class="first last">prod-win-dns-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">timeframe:
  minutes: 5
num_events: 20
filter:
  - term:
       event.id: 258</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">10.</p>
</td>
<td><p class="first last">WINDOWS DNS</p>
</td>
<td><p class="first last">WIN DNS - DNS Ignored Query</p>
</td>
<td><p class="first last">Ignored Query</p>
</td>
<td><p class="first last">prod-win-dns-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">timeframe:
  minutes: 5
num_events: 20
filter:
  - term:
       event.id: 259</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">11.</p>
</td>
<td><p class="first last">WINDOWS DNS</p>
</td>
<td><p class="first last">WIN DNS - DNS Recursive query timeout</p>
</td>
<td><p class="first last">Recursive query timeout</p>
</td>
<td><p class="first last">prod-win-dns-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">timeframe:
  minutes: 5
num_events: 20
filter:
  - term:
       event.id: 262</p>
</td>
</tr>
</tbody>
</table>


#### Microsoft DHCP SIEM Rules

  <table border="1" class="docutils" id="id1">
<colgroup>
<col width="7%" />
<col width="7%" />
<col width="9%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="40%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last">Windows DHCP</p>
</td>
<td><p class="first last">MS DHCP low disk space</p>
</td>
<td><p class="first last">The log was temporarily paused due to low disk space.</p>
</td>
<td><p class="first last">prod-win-dhcp-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
  minutes: 15
filter:
  - term:
      dhcp.event.id: 02</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last">Windows DHCP</p>
</td>
<td><p class="first last">MS DHCP lease denied</p>
</td>
<td><p class="first last">A lease was denied</p>
</td>
<td><p class="first last">prod-win-dhcp-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">timeframe:
  minutes: 15
num_events: 10
filter:
- terms:
    dhcp.event.id: [ “15”, “16” ]
include:
  - dhcp.event.id
  - src.ip
  - src.mac
  - dhcp.event.descr
summary_table_field:
  - src.ip
  - src.mac
  - dhcp.event.descr</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last">Windows DHCP</p>
</td>
<td><p class="first last">MS DHCP update denied</p>
</td>
<td><p class="first last">DNS update failed</p>
</td>
<td><p class="first last">prod-win-dhcp-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">timeframe:
  minutes: 15
num_events: 50
filter:
- term:
    dhcp.event.id: 31</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4</p>
</td>
<td><p class="first last">Windows DHCP</p>
</td>
<td><p class="first last">MS DHCP Data Corruption</p>
</td>
<td><p class="first last">Detecting DHCP Jet Data Corruption</p>
</td>
<td><p class="first last">prod-win-dhcp-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
  minutes: 15
filter:
  - term:
      dhcp.event.id: 1014</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">5</p>
</td>
<td><p class="first last">Windows DHCP</p>
</td>
<td><p class="first last">MS DHCP service shutting down</p>
</td>
<td><p class="first last">The DHCP service is shutting down due to the following error</p>
</td>
<td><p class="first last">prod-win-dhcp-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
  minutes: 15
filter:
  - term:
      dhcp.event.id: 1008</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">6</p>
</td>
<td><p class="first last">Windows DHCP</p>
</td>
<td><p class="first last">MS DHCP Service Failed to restore database</p>
</td>
<td><p class="first last">The DHCP service failed to restore the database</p>
</td>
<td><p class="first last">prod-win-dhcp-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
  minutes: 15
filter:
  - term:
      dhcp.event.id: 1018</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">7</p>
</td>
<td><p class="first last">Windows DHCP</p>
</td>
<td><p class="first last">MS DHCP Service Failed to restore registry</p>
</td>
<td><p class="first last">The DHCP service failed to restore the DHCP registry configuration</p>
</td>
<td><p class="first last">prod-win-dhcp-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
  minutes: 15
filter:
  - term:
      dhcp.event.id: 1019</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">8</p>
</td>
<td><p class="first last">Windows DHCP</p>
</td>
<td><p class="first last">MS DHCP Can not find domain</p>
</td>
<td><p class="first last">The DHCP/BINL service on the local machine encountered an error while trying to find the domain of the local machine</p>
</td>
<td><p class="first last">prod-win-dhcp-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">timeframe:
  minutes: 15
filter:
  - term:
     dhcp.event.id: 1049</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">9</p>
</td>
<td><p class="first last">Windows DHCP</p>
</td>
<td><p class="first last">MS DHCP Network Failure</p>
</td>
<td><p class="first last">The DHCP/BINL service on the local machine encountered a network error</p>
</td>
<td><p class="first last">prod-win-dhcp-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">timeframe:
  minutes: 15
filter:
  - term:
      dhcp.event.id: 1050</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">10</p>
</td>
<td><p class="first last">Windows DHCP</p>
</td>
<td><p class="first last">MS DHCP - There are no IP addresses available for lease</p>
</td>
<td><p class="first last">There are no IP addresses available for lease in the scope or superscope</p>
</td>
<td><p class="first last">prod-win-dhcp-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">timeframe:
  minutes: 15
filter:
  - term:
     dhcp.event.id: 1063</p>
</td>
</tr>
</tbody>
</table>


#### Linux DHCP Server SIEM Rules

<table border="1" class="docutils" id="id1">
<colgroup>
<col width="7%" />
<col width="7%" />
<col width="9%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="40%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last">DHCP Linux</p>
</td>
<td><p class="first last">DHCP Linux - Too many requests</p>
</td>
<td><p class="first last">Too many DHCP requests</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Linux DHCP Server / Syslog</p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">query_key: “src_mac”
num_events: 30
timeframe:
  minutes: 1
filter:
 - query_string:
     query: “DHCPREQUEST”
use_count_query: true
doc_type: doc</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last">DHCP Linux</p>
</td>
<td><p class="first last">DHCP Linux - IP already assigned</p>
</td>
<td><p class="first last">IP is already assigned to another client</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Linux DHCP Server / Syslog</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: “DHCPNAK”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last">DHCP Linux</p>
</td>
<td><p class="first last">DHCP Linux - Discover flood</p>
</td>
<td><p class="first last">DHCP Discover flood</p>
</td>
<td><p class="first last">syslog-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Linux DHCP Server / Syslog</p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">query_key: “src_mac”
num_events: 30
timeframe:
  minutes: 1
filter:
 - query_string:
     query: “DHCPDISCOVER”
use_count_query: true
doc_type: doc</p>
</td>
</tr>
</tbody>
</table>


#### Cisco VPN devices SIEM Rules

<table border="1" class="docutils" id="id1">
<colgroup>
<col width="7%" />
<col width="7%" />
<col width="9%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="40%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last">Cisco IOS - Cisco VPN Concentrator</p>
</td>
<td><p class="first last">CiscoVPN - VPN authentication failed</p>
</td>
<td><p class="first last">Jan 8 09:10:37 vpn.example.com 11504 01/08/2007 09:10:37.780 SEV=3 AUTH/5 RPT=124 192.168.0.1 Authentication rejected: Reason = Unspecified handle = 805, server = auth.example.com, user = testuser, domain = &lt;not specified&gt;</p>
</td>
<td><p class="first last">cisco*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “cisco.id:(&quot;AUTH\/5&quot; OR &quot;AUTH\/9&quot; OR &quot;IKE\/167&quot; OR &quot;PPP\/9&quot; OR &quot;SSH\/33&quot; OR &quot;PSH\/23&quot;)”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last">Cisco IOS - Cisco VPN Concentrator</p>
</td>
<td><p class="first last">CiscoVPN - VPN authentication successful</p>
</td>
<td><p class="first last">jw.</p>
</td>
<td><p class="first last">cisco*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “cisco.id:(&quot;IKE\/52&quot;)”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last">Cisco IOS - Cisco VPN Concentrator</p>
</td>
<td><p class="first last">CiscoVPN - VPN Admin authentication successful</p>
</td>
<td><p class="first last">jw.</p>
</td>
<td><p class="first last">cisco*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “cisco.id:(&quot;HTTP\/47&quot; OR &quot;SSH\/16&quot;)”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4</p>
</td>
<td><p class="first last">Cisco IOS - Cisco VPN Concentrator</p>
</td>
<td><p class="first last">CiscoVPN - Multiple VPN authentication failures</p>
</td>
<td><p class="first last">jw.</p>
</td>
<td><p class="first last">cisco*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">query_key: “src.ip”
num_events: 10
timeframe:
  minutes: 240
filter:
 - query_string:
     query: “cisco.id:(&quot;AUTH\/5&quot; OR &quot;AUTH\/9&quot; OR &quot;IKE\/167&quot; OR &quot;PPP\/9&quot; OR &quot;SSH\/33&quot; OR &quot;PSH\/23&quot;)”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">5</p>
</td>
<td><p class="first last">Cisco IOS - Cisco ASA</p>
</td>
<td><p class="first last">Cisco ASA - VPN authentication failed</p>
</td>
<td><p class="first last">jw.</p>
</td>
<td><p class="first last">cisco*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “cisco.id:&quot;\%ASA-6-113005&quot;”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">6</p>
</td>
<td><p class="first last">Cisco IOS - Cisco ASA</p>
</td>
<td><p class="first last">Cisco ASA - VPN authentication successful</p>
</td>
<td><p class="first last">jw.</p>
</td>
<td><p class="first last">cisco*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “cisco.id:&quot;\%ASA-6-113004&quot;”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">7</p>
</td>
<td><p class="first last">Cisco IOS - Cisco ASA</p>
</td>
<td><p class="first last">Cisco ASA - VPN user locked out</p>
</td>
<td><p class="first last">jw.</p>
</td>
<td><p class="first last">cisco*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
- query_string:
       query: “cisco.id:&quot;\%ASA-6-113006&quot;”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">8</p>
</td>
<td><p class="first last">Cisco IOS - Cisco ASA</p>
</td>
<td><p class="first last">Cisco ASA - Multiple VPN authentication failed</p>
</td>
<td><p class="first last">jw.</p>
</td>
<td><p class="first last">cisco*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">query_key: “src.ip”
num_events: 10
timeframe:
  minutes: 240
filter:
 - query_string:
     query: “cisco.id:&quot;\%ASA-6-113005&quot;”</p>
</td>
</tr>
</tbody>
</table>


#### Netflow SIEM Rules

<table border="1" class="docutils" id="id1">
<colgroup>
<col width="7%" />
<col width="7%" />
<col width="9%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="40%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Netflow - DNS traffic abnormal</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">stream-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">spike</p>
</td>
<td><p class="first last">threshold_ref: 1000
spike_height: 4
spike_type: up
timeframe:
  hours: 2
filter:
- query:
    query_string:
      query: “netflow.dst.port:53”
query_key: [netflow.src.ip]
use_count_query: true
doc_type:  “doc”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Netflow - ICMP larger than 64b</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">stream-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
  - query:
      query_string:
        query: “netflow.protocol: 1 AND netflow.packet_bytes:&gt;64”
query_key: “netflow.dst_addr”
use_count_query: true
doc_type: “doc”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Netflow - Port scan</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">stream-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">cardinality</p>
</td>
<td><p class="first last">timeframe:
    minutes: 5
max_cardinality: 100
query_key: [netflow.src.ip, netflow.dst.ip]
cardinality_field: “netflow.dst.port”
filter:
-  query:
        query_string:
            query: “_exists_:(netflow.dst.ip AND netflow.src.ip) NOT netflow.dst.port: (443 OR 80)”
aggregation:
    minutes: 5
aggregation_key: netflow.src.ip</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Netflow - SMB traffic</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">stream-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
  - query:
      query_string:
        query: “netflow.dst.port:(137 OR 138 OR 445 OR 139)”
query_key: “netflow.src.ip”
use_count_query: true
doc_type: “doc”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">5</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Netflow - Too many req to port 161</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">stream-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">num_events: 60
timeframe:
  minutes: 1
filter:
  - query:
      query_string:
        query: “netflow.dst.port:161”
query_key: “netflow.src.ip”  
use_count_query: true
doc_type: “doc”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">6</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Netflow - Too many req to port 25</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">stream-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">num_events: 60
timeframe:
  minutes: 1
filter:
  - query:
      query_string:
        query: “netflow.dst.port:25”
query_key: “netflow.src.ip”  
use_count_query: true
doc_type: “doc”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">7</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Netflow - Too many req to port 53</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">stream-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">num_events: 120
timeframe:
  minutes: 1
filter:
  - query:
      query_string:
        query: “netflow.dst.port:53”
query_key: “netflow.src.ip”  
use_count_query: true
doc_type: “doc”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">8</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Netflow – Multiple connections from source badip</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">stream-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">num_events: 10
timeframe:
  minutes: 5
filter:
  - query:
      query_string:
        query: “netflow.src.badip:true”
query_key: “netflow.src.ip”
use_count_query: true
doc_type: “doc”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">9</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Netflow – Multiple connections to destination badip</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">stream-*</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">num_events: 10
timeframe:
  minutes: 5
filter:
  - query:
      query_string:
        query: “netflow.dst.badip:true”
query_key: “netflow.dst.ip”
use_count_query: true
doc_type: “doc”</p>
</td>
</tr>
</tbody>
</table>


#### MikroTik devices SIEM Rules

<table border="1" class="docutils" id="id1">
<colgroup>
<col width="7%" />
<col width="7%" />
<col width="9%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="40%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">All system errors</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">alert_text_type: alert_text_only 
alert_text: “System error\n\n When: {}\n Device IP: {}\n From: {}\n\n{}\n” 
alert_text_args: 
  - timestamp_timezone
  - host
  - login.ip 
  - kibana_link 
use_kibana4_dashboard: “link do saved search” 
kibana4_start_timedelta: 
 minutes: 5 
kibana4_end_timedelta: 
 minutes: 0 
 filter:
 - query_string:
        query: “topic2:error and topic3:critical”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">All errors connected with logins to the administrative interface of the device eg wrong password or wrong login name </p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">alert_text_type: alert_text_only 
alert_text: “Login error\n\n When: {}\n Device IP: {}\n From: {}\n by: {}\n to account: {}\n\n{}\n” 
alert_text_args: 
  - timestamp_timezone
  - host
  - login.ip 
  - login.method
  - user 
  - kibana_link 
use_kibana4_dashboard: “link do saved search” 
kibana4_start_timedelta: 
 minutes: 5 
kibana4_end_timedelta: 
 minutes: 0 
 filter:
 - query_string:
        query: “topic2:error and topic3:critical and login.status:login failure”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">All errors connected with wireless eg device is banned on access list, or device had poor signal on AP and was disconected</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">alert_text_type: alert_text_only 
alert_text: “Wifi auth issue\n\n When: {}\n Device IP: {}\n Interface: {}\n MAC: {}\n ACL info: {}\n\n{}\n” 
alert_text_args: 
  - timestamp_timezone
  - host
  - interface
  - wlan.mac
  - wlan.ACL
  - kibana_link 
use_kibana4_dashboard: “link do saved search” 
kibana4_start_timedelta: 
 minutes: 5 
kibana4_end_timedelta: 
 minutes: 0 
 filter:
 - query_string:
        query: “wlan.status:reject or wlan.action:banned”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Dhcp offering fail</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">alert_text_type: alert_text_only 
alert_text: “Dhcp offering fail\n\n When: {}\n Client lease: {}\n for MAC: {}\n to MAC: {}\n\n{}\n” 
alert_text_args: 
  - timestamp_timezone
  - dhcp.ip
  - dhcp.mac
  - dhcp.mac2
  - kibana_link 
use_kibana4_dashboard: “link do saved search” 
kibana4_start_timedelta: 
 minutes: 5 
kibana4_end_timedelta: 
 minutes: 0 
 filter:
 - query_string:
        query: “dhcp.status:without success”</p>
</td>
</tr>
</tbody>
</table>


#### Microsoft SQL Server SIEM Rules

<table border="1" class="docutils" id="id1">
<colgroup>
<col width="7%" />
<col width="7%" />
<col width="9%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="40%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Logon errors, alert any</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Rule definition
alert_text_type: alert_text_only 
alert_text: “Logon error\n\n When: {}\n Error code: {}\n Severity: {}\n\n{}\n” 
alert_text_args: 
  - timestamp_timezone
  - mssql.error.code
  - mssql.error.severity
  - kibana_link 
use_kibana4_dashboard: “link do saved search” 
kibana4_start_timedelta: 
 minutes: 5 
kibana4_end_timedelta: 
 minutes: 0 
 filter:
 - query_string:
        query: “mssql.error.code:* and mssql.error.severity:*”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Login failed for users, alert any</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">alert_text_type: alert_text_only 
alert_text: “Login failed\n\n When: {}\n User login: {}\n Reason: {}\n Client: {}\n\n{}\n” 
alert_text_args: 
  - timestamp_timezone
  - mssql.login.user
  - mssql.error.reason
  - mssql.error.client
  - kibana_link 
use_kibana4_dashboard: “link do saved search” 
kibana4_start_timedelta: 
 minutes: 5 
kibana4_end_timedelta: 
 minutes: 0 
 filter:
 - query_string:
        query: “mssql.login.status:failed and mssql.login.user:*”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">server is going down, alert any</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">alert_text_type: alert_text_only 
alert_text: “Server is going down\n\n When: {}\n\n{}\n” 
alert_text_args: 
  - timestamp_timezone
  - kibana_link 
use_kibana4_dashboard: “link do saved search” 
kibana4_start_timedelta: 
 minutes: 5 
kibana4_end_timedelta: 
 minutes: 0 
 filter:
 - query_string:
        query: “mssql.server.status:shutdown”</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">NET stopped, alert any</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">alert_text_type: alert_text_only 
alert_text: “NET Framework runtime has been stopped.\n\n When: {}\n\n{}\n” 
alert_text_args: 
  - timestamp_timezone
  - kibana_link 
use_kibana4_dashboard: “link do saved search” 
kibana4_start_timedelta: 
 minutes: 5 
kibana4_end_timedelta: 
 minutes: 0 
 filter:
 - query_string:
        query: “mssql.net.status:stopped”</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">5</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">Database Mirroring stopped, alert any</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">alert_text_type: alert_text_only 
alert_text: “Database Mirroring endpoint is in stopped state.\n\n When: {}\n\n{}\n” 
alert_text_args: 
  - timestamp_timezone
  - kibana_link 
use_kibana4_dashboard: “link do saved search” 
kibana4_start_timedelta: 
 minutes: 5 
kibana4_end_timedelta: 
 minutes: 0 
 filter:
 - query_string:
        query: “mssql.db.status:stopped”</p>
</td>
</tr>
</tbody>
</table>



#### Postgress SQL SIEM Rules

<table border="1" class="docutils" id="id1">
<colgroup>
<col width="7%" />
<col width="7%" />
<col width="9%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="40%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head"></th>
<th class="head"></th>
<th class="head"></th>
<th class="head"></th>
<th class="head"></th>
<th class="head"></th>
<th class="head"></th>
<th class="head"></th>
<th class="head"></th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last"></p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">Nr.</p>
</td>
<td><p class="first last">Architecture/Application</p>
</td>
<td><p class="first last">Rule Name</p>
</td>
<td><p class="first last">Description</p>
</td>
<td><p class="first last">Index name</p>
</td>
<td><p class="first last">Requirements</p>
</td>
<td><p class="first last">Source</p>
</td>
<td><p class="first last">Rule type</p>
</td>
<td><p class="first last">Rule definition</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last">PostgreSQL</p>
</td>
<td><p class="first last">PostgresSQL - New user created</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">postgres-*</p>
</td>
<td><p class="first last">Filebeat, Logstash, PostgreSQL</p>
</td>
<td><p class="first last">pg_log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”LOG: CREATE USER”’</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last">PostgreSQL</p>
</td>
<td><p class="first last">PostgresSQL - User selected database</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">postgres-*</p>
</td>
<td><p class="first last">Filebeat, Logstash, PostgreSQL</p>
</td>
<td><p class="first last">pg_log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”LOG: SELECT d.datname FROM pg_catalog.pg_database”’</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last">PostgreSQL</p>
</td>
<td><p class="first last">PostgresSQL - User password changed</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">postgres-*</p>
</td>
<td><p class="first last">Filebeat, Logstash, PostgreSQL</p>
</td>
<td><p class="first last">pg_log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”ALTER USER WITH PASSWORD”’</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4</p>
</td>
<td><p class="first last">PostgreSQL</p>
</td>
<td><p class="first last">PostgreSQL - Multiple authentication failures</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">postgres-*</p>
</td>
<td><p class="first last">Filebeat, Logstash, PostgreSQL</p>
</td>
<td><p class="first last">pg_log</p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">query_key: “src_ip”
num_events: 5
timeframe:
  seconds: 25
filter:
 - query_string:
     query: ‘message:”FATAL:  password authentication failed for user”’
use_count_query: true
doc_type: doc</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">5</p>
</td>
<td><p class="first last">PostgreSQL</p>
</td>
<td><p class="first last">PostgreSQL - Granted all privileges to user</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">postgres-*</p>
</td>
<td><p class="first last">Filebeat, Logstash, PostgreSQL</p>
</td>
<td><p class="first last">pg_log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”LOG: GRANT ALL PRIVILEGES ON”’</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">6</p>
</td>
<td><p class="first last">PostgreSQL</p>
</td>
<td><p class="first last">PostgresSQL - User displayed users table</p>
</td>
<td><p class="first last">User displayed users table</p>
</td>
<td><p class="first last">postgres-*</p>
</td>
<td><p class="first last">Filebeat, Logstash, PostgreSQL</p>
</td>
<td><p class="first last">pg_log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”LOG: SELECT r.rolname FROM pg_catalog.pg_roles”’</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">7</p>
</td>
<td><p class="first last">PostgreSQL</p>
</td>
<td><p class="first last">PostgresSQL - New database created</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">postgres-*</p>
</td>
<td><p class="first last">Filebeat, Logstash, PostgreSQL</p>
</td>
<td><p class="first last">pg_log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”LOG: CREATE DATABASE”’</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">8</p>
</td>
<td><p class="first last">PostgreSQL</p>
</td>
<td><p class="first last">PostgresSQL - Database shutdown</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">postgres-*</p>
</td>
<td><p class="first last">Filebeat, Logstash, PostgreSQL</p>
</td>
<td><p class="first last">pg_log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”LOG: database system was shut down at”’</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">9</p>
</td>
<td><p class="first last">PostgreSQL</p>
</td>
<td><p class="first last">PostgresSQL - New role created</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">postgres-*</p>
</td>
<td><p class="first last">Filebeat, Logstash, PostgreSQL</p>
</td>
<td><p class="first last">pg_log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”LOG: CREATE ROLE”’</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">10</p>
</td>
<td><p class="first last">PostgreSQL</p>
</td>
<td><p class="first last">PostgresSQL - User deleted</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">postgres-*</p>
</td>
<td><p class="first last">Filebeat, Logstash, PostgreSQL</p>
</td>
<td><p class="first last">pg_log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”LOG: DROP USER”’</p>
</td>
</tr>
</tbody>
</table>


#### MySQL SIEM Rules

<table border="1" class="docutils" id="id1">
<colgroup>
<col width="7%" />
<col width="7%" />
<col width="9%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="7%" />
<col width="40%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Architecture/Application</th>
<th class="head">Rule Name</th>
<th class="head">Description</th>
<th class="head">Index name</th>
<th class="head">Requirements</th>
<th class="head">Source</th>
<th class="head">Rule type</th>
<th class="head">Rule definition</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last">MySQL</p>
</td>
<td><p class="first last">MySQL - User created</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">mysql-*</p>
</td>
<td><p class="first last">Filebeat, Logstash, MySQL</p>
</td>
<td><p class="first last">mysql-general.log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”CREATE USER”’</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">2</p>
</td>
<td><p class="first last">MySQL</p>
</td>
<td><p class="first last">MySQL - User selected database</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">mysql-*</p>
</td>
<td><p class="first last">Filebeat, Logstash, MySQL</p>
</td>
<td><p class="first last">mysql-general.log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”Query show databases”’</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last">MySQL</p>
</td>
<td><p class="first last">MySQL - Table dropped</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">mysql-*</p>
</td>
<td><p class="first last">Filebeat, Logstash, MySQL</p>
</td>
<td><p class="first last">mysql-general.log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”Query drop table”’</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">4</p>
</td>
<td><p class="first last">MySQL</p>
</td>
<td><p class="first last">MySQL - User password changed</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">mysql-*</p>
</td>
<td><p class="first last">Filebeat, Logstash, MySQL</p>
</td>
<td><p class="first last">mysql-general.log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”UPDATE mysql.user SET Password=PASSWORD” OR message:”SET PASSWORD FOR” OR message:”ALTER USER”’</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">5</p>
</td>
<td><p class="first last">MySQL</p>
</td>
<td><p class="first last">MySQL - Multiple authentication failures</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">mysql-*</p>
</td>
<td><p class="first last">Filebeat, Logstash, MySQL</p>
</td>
<td><p class="first last">mysql-general.log</p>
</td>
<td><p class="first last">frequency</p>
</td>
<td><p class="first last">query_key: “src_ip”
num_events: 5
timeframe:
  seconds: 25
filter:
 - query_string:
     query: ‘message:”Access denied for user”’
use_count_query: true
doc_type: doc</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">6</p>
</td>
<td><p class="first last">MySQL</p>
</td>
<td><p class="first last">MySQL - All priviliges to user granted</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">mysql-*</p>
</td>
<td><p class="first last">Filebeat, Logstash, MySQL</p>
</td>
<td><p class="first last">mysql-general.log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”GRANT ALL PRIVILEGES ON”’</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">7</p>
</td>
<td><p class="first last">MySQL</p>
</td>
<td><p class="first last">MySQL - User displayed users table</p>
</td>
<td><p class="first last">User displayed users table</p>
</td>
<td><p class="first last">mysql-*</p>
</td>
<td><p class="first last">Filebeat, Logstash, MySQL</p>
</td>
<td><p class="first last">mysql-general.log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”Query select * from user”’</p>
</td>
</tr>
<tr class="row-odd"><td><p class="first last">8</p>
</td>
<td><p class="first last">MySQL</p>
</td>
<td><p class="first last">MySQL - New database created</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">mysql-*</p>
</td>
<td><p class="first last">Filebeat, Logstash, MySQL</p>
</td>
<td><p class="first last">mysql-general.log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”Query create database”’</p>
</td>
</tr>
<tr class="row-even"><td><p class="first last">9</p>
</td>
<td><p class="first last">MySQL</p>
</td>
<td><p class="first last">MySQL - New table created</p>
</td>
<td><p class="first last"></p>
</td>
<td><p class="first last">mysql-*</p>
</td>
<td><p class="first last">Filebeat, Logstash, MySQL</p>
</td>
<td><p class="first last">mysql-general.log</p>
</td>
<td><p class="first last">any</p>
</td>
<td><p class="first last">filter:
 - query_string:
     query: ‘message:”Query create table”’</p>
</td>
</tr>
</tbody>
</table>
# Alert Module #

Energy Logserver allows you to create alerts, i.e. monitoring
queries. These are constant queries that run in the background and
when the conditions specified in the alert are met, the specify action
is taken. 

![](/media/media/image91.PNG)

For example, if you want to know when more than 20
„status:500" response code from on our homepage appear within an one
hour, then we create an alert that check the number of occurrences of
the „status:500" query for a specific index every 5 minutes. If the
condition we are interested in is met, we send an action in the form
of sending a message to our e-mail address. In the action, you can
also set the launch of any script.

### Incident detection and mitigation time

The Energy Logserver allows you to keep track of the time and actions taken in the incident you created. 
A detected alert incident has the date the incident occurred `match_body.@timestamp` and the date and time the incident was detected `alert.time`. 

In addition, it is possible to enrich the alert event with the date and time of incident resolution `alert_solvedtime` using the following pipeline:

```conf
  input {
      elasticsearch {
          hosts => "http://localhost:9200"
          user => logserver
          password => logserver
          index => "alert*"
          size => 500
          scroll => "5m"
          docinfo => true
          schedule => "*/5 * * * *"
          query => '{ "query": {     "bool": {
        "must": [
          {
            "match_all": {}
          }
        ],
        "filter": [
          {
            "match_phrase": {
              "alert_info.status": {
                "query": "solved"
              }
            }
          }
        ],
        "should": [],
        "must_not": [{
            "exists": {
              "field": "alert_solvedtime"
            }
          }]
      }
  }, "sort": [ "_doc" ] }'
      }
  }
  filter {
          ruby {
                  code => "event.set('alert_solvedtime', Time.now());"
          }
  }
  output {
      elasticsearch {
          hosts => "http://localhost:9200"
          user => logserver
          password => logserver
          action => "update"
          document_id => "%{[@metadata][_id]}"
          index => "%{[@metadata][_index]}"
      }
  }
```


## Siem Module

Energy Logserver, through its built-in vulnerability detection module use of best practices defined in the CIS, allows to audit monitored environment for security vulnerabilities, misconfigurations, or outdated software versions. File Integrity Monitoring functionality allows for detailed monitoring and alerting of unauthorized access attempts to most sensitive data.

SIEM Plan is a solution that provides a ready-made set of tools for compliance regulations such as CIS, PCI DSS, GDPR, NIST 800-53, ISO 27001.The system enables mapping of detected threats to Mitre ATT&CK tactics. By integrating with the MISP Energy Logserver, allows to get real-time information about new threats on the network by downloading the latest IoC lists.

To configure the SIEM agents see the *Configuration* section.

### Active response

The SIEM agent automates the response to threats by running actions when these are detected. The agent has the ability to block network connections, stop running processes, and delete malicious files, among other actions. In addition, it can also run customized scripts developed by the user (e.g., Python, Bash, or PowerShell).

To use this feature, users define the conditions that trigger the scripted actions, which usually involve threat detection and assessment. For example, a user can use log analysis rules to detect an intrusion attempt and an IP address reputation database to assess the threat by looking for the source IP address of the attempted connection.

In the scenario described above, when the source IP address is recognized as malicious (low reputation), the monitored system is protected by automatically setting up a firewall rule to drop all traffic from the attacker. Depending on the active response, this firewall rule is temporary or permanent.

On Linux systems, the Wazuh agent usually integrates with the local Iptables firewall for this purpose. On Windows systems, instead, it uses the null routing technique (also known as blackholing). Below you can find the configuration to define two scripts that are used for automated connection blocking:

```xml
    <command>
      <name>firewall-drop</name>
      <executable>firewall-drop</executable>
      <timeout_allowed>yes</timeout_allowed>
    </command>
```

```xml
    <command>
      <name>win_route-null</name>
      <executable>route-null.exe</executable>
      <timeout_allowed>yes</timeout_allowed>
    </command>
```

On top of the defined commands, active responses set the conditions that need to be met to trigger them. Below is an example of a configuration that triggers the ``firewall-drop`` command when the log analysis rule ``100100`` is matched.

```xml
    <active-response>
      <command>firewall-drop</command>
      <location>local</location>
      <rules_id>100100</rules_id>
      <timeout>60</timeout>
    </active-response>
```

In this case, rule ``100100`` is used to look for alerts where the source IP address is part of a well-known IP address reputation database.

```xml
   <rule id="100100" level="10">
     <if_group>web|attack|attacks</if_group>
     <list field="srcip" lookup="address_match_key">etc/lists/blacklist-alienvault</list>
     <description>IP address found in AlienVault reputation database.</description>
   </rule>
```

Below you can find a screenshot with two SIEM alerts: one that is triggered when a web attack is detected trying to exploit a PHP server vulnerability, and one that informs that the malicious actor has been blocked.

![](/media/media/image240.png)

### Log data collection

Log data collection is the real-time process of making sense out of the records generated by servers or devices. This component can receive logs through text files or Windows event logs. It can also directly receive logs via remote syslog which is useful for firewalls and other such devices.

The purpose of this process is the identification of application or system errors, mis-configurations, intrusion attempts, policy violations or security issues.

The memory and CPU requirements of the SIEM agent are insignificant since its primary duty is to forward events to the manager. However, on the SIEM manager, CPU and memory consumption can increase rapidly depending on the events per second (EPS) that the manager has to analyze.

#### How it works
Log files
The Log analysis engine can be configured to monitor specific files on the servers.

Linux:
```xml
<localfile>
  <location>/var/log/example.log</location>
  <log_format>syslog</log_format>
</localfile>
```
Windows:
```xml
<localfile>
  <location>C:\myapp\example.log</location>
  <log_format>syslog</log_format>
</localfile>
```

Windows event logs
Wazuh can monitor classic Windows event logs, as well as the newer Windows event channels.
Event log:
```xml
<localfile>
  <location>Security</location>
  <log_format>eventlog</log_format>
</localfile>
```

Event channel:
```xml
<localfile>
  <location>Microsoft-Windows-PrintService/Operational</location>
  <log_format>eventchannel</log_format>
</localfile>
```

Remote syslog
In order to integrate network devices such as routers, firewalls, etc, the log analysis component can be configured to receive log events through syslog. To do that we have two methods available:

One option is for SIEM to receive syslog logs by a custom port:
```xml
<ossec_config>
  <remote>
    <connection>syslog</connection>
    <port>513</port>
    <protocol>udp</protocol>
    <allowed-ips>192.168.2.0/24</allowed-ips>
  </remote>
</ossec_config>
```

```<connection>syslog</connection>``` indicates that the manager will accept incoming syslog messages from across the network.
```<port>513</port>``` defines the port that Wazuh will listen to retrieve the logs. The port must be free.
```<protocol>udp</protocol>``` defines the protocol to listen the port. It can be UDP or TCP.
```<allowed-ips>192.168.2.0/24</allowed-ips>```defines the network or IP from which syslog messages will be accepted.

The other option store the logs in a plaintext file and monitor that file with SIEM. If a ```/etc/rsyslog.conf``` configuration file is being used and we have defined where to store the syslog logs we can monitor them in SIEM ```ossec.conf``` using a ```<localfile>``` block with ```syslog``` as the log format.

```xml
<localfile>
  <log_format>syslog</log_format>
  <location>/custom/file/path</location>
</localfile>
```

```<log_format>syslog</log_format>``` indicates the source log format, in this case, syslog format.
```<location>/custom/file/path</location>``` indicates where we have stored the syslog logs.

Analysis
Pre-decoding

In the pre-decoding phase of analysis, static information from well-known fields all that is extracted from the log header.
```bash
Feb 14 12:19:04 localhost sshd[25474]: Accepted password for rromero from 192.168.1.133 port 49765 ssh2
```

Extracted information:
- hostname: 'localhost'
- program_name: 'sshd'

Decoding

In the decoding phase, the log message is evaluated to identify what type of log it is and known fields for that specific log type are then extracted.
Sample log and its extracted info:
```bash
Feb 14 12:19:04 localhost sshd[25474]: Accepted password for rromero from 192.168.1.133 port 49765 ssh2
```
Extracted information:
- program name: sshd
- dstuser: rromero
- srcip: 192.168.1.133

Rule matching
In the next phase, the extracted log information is compared to the ruleset to look for matches:
For the previous example, rule 5715 is matched:

```xml
<rule id="5715" level="3">
  <if_sid>5700</if_sid>
  <match>^Accepted|authenticated.$</match>
  <description>sshd: authentication success.</description>
  <group>authentication_success,pci_dss_10.2.5,</group>
</rule>
```

Alert
Once a rule is matched, the manager will create an alert as below:
```bash
** Alert 1487103546.21448: - syslog,sshd,authentication_success,pci_dss_10.2.5,
2017 Feb 14 12:19:06 localhost->/var/log/secure
Rule: 5715 (level 3) -> 'sshd: authentication success.'
Src IP: 192.168.1.133
User: rromero
Feb 14 12:19:04 localhost sshd[25474]: Accepted password for rromero from 192.168.1.133 port 49765 ssh2
```

By default, alerts will be generated on events that are important or of security relevance. To store all events even if they do not match a rule, enable the ```<logall>``` option.

Alerts will be stored at ```/var/ossec/logs/alerts/alerts.(json|log)``` and events at ```/var/ossec/logs/archives/archives.(json|log)```. Logs are rotated and an individual directory is created for each month and year.

#### How to collect Windows logs

Windows events can be gathered and forwarded to the manager, where they are processed and alerted if they match any rule. There are two formats to collect Windows logs:

- Eventlog (supported by every Windows version)
- Eventchannel (for Windows Vista and later versions)

Windows logs are descriptive messages which come with relevant information about events that occur in the system. They are collected and shown at the Event Viewer, where they are classified by the source that generated them.

This information is gathered by the Windows agent, including the event description, the ```system``` standard fields and the specific ```eventdata``` information from the event. Once an event is sent to the manager, it is processed and translated to JSON format, which leads to an easier way of querying and filtering the event fields.

Eventlog uses as well the Windows API to obtain events from Windows logs and return the information in a specific format.


Windows Eventlog vs Windows Eventchannel
Eventlog is supported on every Windows version and can monitor any logs except for particular Applications and Services Logs, this means that the information that can be retrieved is reduced to System, Application and Security channels.
On the other hand, Eventchannel is maintained since Windows Vista and can monitor the Application and Services logs along with the basic Windows logs. In addition, the use of queries to filter by any field is supported for this log format.

Monitor the Windows Event Log with Wazuh
To monitor a Windows event log, it is necessary to provide the format as "eventlog" and the location as the name of the event log.
```xml
<localfile>
    <location>Security</location>
    <log_format>eventlog</log_format>
</localfile>
```
These logs are obtained through Windows API calls and sent to the manager where they will be alerted if they match any rule.

Monitor the Windows Event Channel with Wazuh
Windows event channels can be monitored by placing their name at the location field from the localfile block and "eventchannel" as the log format.
```xml
<localfile>
    <location>Microsoft-Windows-PrintService/Operational</location>
    <log_format>eventchannel</log_format>
</localfile>
```

<table border="1" class="colwidths-given docutils" id="id1">
<colgroup>
<col width="2%" />
<col width="10%" />
<col width="20%" />
<col width="5%" />
<col width="63%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Nr.</th>
<th class="head">Source</th>
<th class="head">Channel location</th>
<th class="head">Provider name</th>
<th class="head">Description</th>
</tr>
</thead>
<tbody valign="top">
	
<tr class="row-even"><td><p class="first last">1</p>
</td>
<td><p class="first last">Application</p>
</td>
<td><p class="first last">Application</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">This log retrieves every event related to system applications management and is one of the main Windows administrative channels along with Security and System.</p>
</td>
</tr>

<tr class="row-even"><td><p class="first last">2</p>
</td>
<td><p class="first last">Security</p>
</td>
<td><p class="first last">Security</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">This channel gathers information related to users and groups creation, login, logoff and audit policy modifications.</p>
</td>
</tr>
	
<tr class="row-even"><td><p class="first last">3</p>
</td>
<td><p class="first last">System</p>
</td>
<td><p class="first last">System</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">The System channel collects events associated with kernel and service control.</p>
</td>
</tr>

<tr class="row-even"><td><p class="first last">4</p>
</td>
<td><p class="first last">Sysmon</p>
</td>
<td><p class="first last">Microsoft-Windows-Sysmon/Operational</p>
</td>
<td><p class="first last">Microsoft-Windows-Sysmon</p>
</td>
<td><p class="first last">Sysmon monitors system activity as process creation and termination, network connection and file changes.</p>
</td>
</tr>
	
<tr class="row-even"><td><p class="first last">5</p>
</td>
<td><p class="first last">Windows Defender</p>
</td>
<td><p class="first last">Microsoft-Windows-Windows Defender/Operational</p>
</td>
<td><p class="first last">Microsoft-Windows-Windows Defender</p>
</td>
<td><p class="first last">The Windows Defender log file shows information about the scans passed, malware detection and actions taken against them.</p>
</td>
</tr>
	
<tr class="row-even"><td><p class="first last">6</p>
</td>
<td><p class="first last">McAfee</p>
</td>
<td><p class="first last">Application</p>
</td>
<td><p class="first last">McLogEvent</p>
</td>
<td><p class="first last">This source shows McAfee scan results, virus detection and actions taken against them.</p>
</td>
</tr>

<tr class="row-even"><td><p class="first last">7</p>
</td>
<td><p class="first last">EventLog</p>
</td>
<td><p class="first last">System</p>
</td>
<td><p class="first last">Eventlog</p>
</td>
<td><p class="first last">This source retrieves information about audit and Windows logs.</p>
</td>
</tr>

<tr class="row-even"><td><p class="first last">8</p>
</td>
<td><p class="first last">Microsoft Security Essentials</p>
</td>
<td><p class="first last">System</p>
</td>
<td><p class="first last">Microsoft Antimalware</p>
</td>
<td><p class="first last">This software gives information about real-time protection for the system, malware-detection scans and antivirus settings.</p>
</td>
</tr>

<tr class="row-even"><td><p class="first last">9</p>
</td>
<td><p class="first last">Remote Access</p>
</td>
<td><p class="first last">File Replication Service</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">Other channels (they are grouped in a generic Windows rule file).</p>
</td>
</tr>
	
<tr class="row-even"><td><p class="first last">10</p>
</td>
<td><p class="first last">Terminal Services</p>
</td>
<td><p class="first last">Service Microsoft-Windows-TerminalServices-RemoteConnectionManager</p>
</td>
<td><p class="first last">Any</p>
</td>
<td><p class="first last">Other channels (they are grouped in a generic Windows rule file).</p>
</td>
</tr>

</tbody>
</table>

## Tenable.sc

Tenable.sc is vulnerability management tool, which make a scan systems and environments to find vulnerabilities. The Logstash collector can connect to Tebable.sc API to get results of the vulnerability scan and send it to the Elasticsarch index. Reporting and analysis of the collected data is carried out using a prepared dashboard `[Vulnerability] Overview Tenable`

![](/media/media/image166.png)

### Configuration

- enable pipeline in Logstash configuration:

  ```bash
  vim /etc/logstash/pipelines.yml
  ```

  uncomment following lines:

  ```bash
  - pipeline.id: tenable.sc
    path.config: "/etc/logstash/conf.d/tenable.sc/*.conf"
  ```

- configure connection to Tenable.sc manager:

  ```bash
  vim /etc/logstash/conf.d/tenable.sc/venv/main.py
  ```

  set of the connection parameters:

  - TENABLE_ADDR - IP address and port Tenable.sc manger;
  - TENABLE_CRED - user and password;
  - LOGSTASH_ADDR = IP addresss and port Logstash collector;

  example:

  ```bash
  TENABLE_ADDR = ('10.4.3.204', 443)
  TENABLE_CRED = ('admin', 'passowrd')
  LOGSTASH_ADDR = ('127.0.0.1', 10000)
  ```

## Qualys Guard

Qualys Guard is vulnerability management tool, which make a scan systems and environments to find vulnerabilities. The Logstash collector can connect to Qualys Guard API to get results of the vulnerability scan and send it to the Elasticsarch index. Reporting and analysis of the collected data is carried out using a prepared dashboard `[Vulnerability] Overview Tenable`

![](/media/media/image166.png)

### Configuration

- enable pipeline in Logstash configuration:

  ```bash
  vim /etc/logstash/pipelines.yml
  ```

  uncomment following lines:

  ```bash
  - pipeline.id: qualys
    path.config: "/etc/logstash/conf.d/qualys/*.conf"
  ```

- configure connection to Qualys Guard manager:

  ```bash
  vim /etc/logstash/conf.d/qualys/venv/main.py
  ```

  set of the connection parameters:

  - LOGSTASH_ADDR - IP address and port of the Logstash collector;

  - hostname - IP address and port of the Qualys Guard manger;
  - username - user have access to Qualys Guard manger;
  - password - password for user have access to Qualys Guard manger.

  example:

  ```bash
  LOGSTASH_ADDR = ('127.0.0.1', 10001)
  
  # connection settings
  conn = qualysapi.connect(
      username="emcas5ab1",
      password="Lewa#stopa1",
      hostname="qualysguard.qg2.apps.qualys.eu"
  )
  ```


## UEBA

Energy Logserver system allows building and maintaining user's database model (UBA) and computers (EBA), and uses build in mechanisms of Machine Learning and Artificial Intelligence. Both have been implemented withing UEBA module.

The UEBA module enables premium features of Energy Logserver SIEM Plan. This is module which collects knowledge and functionalities which were always available in our system. This cybersecurity approach helps analytics to discover threads in user and entities behaviour. Module tracks user or resource actions and scans common behaviour patterns. With UEBA system provides deep knowledge of daily trends in actions enabling SOC teams to detect any abnormal and suspicious activities. UEBA differs a lot from regular SIEM approach based on logs analytics in time.

The module focus on actions and not the logs itself. Every user, host or other resource is identified as an entity in the system and its behaviour describes its work. Energy Logserver provide new data schema that mark each action over time. Underlying Energy search engine analyse incoming data in order to identify log corresponding to action. We leave the log for SIEM use cases, but incoming data is associated with an action categories. New data model stores actions for each entity and mark them down as metadata stored in individual index.

Once tracking is done, SOC teams can investigate patterns for single action among many entities or many actions for a single user/entity. This unique approach creates an activity map for everyone working in the organization and for any resource. Created dataset is stored in time. All actions can be analysed for understanding the trend and comparing it with historical profile. UEBA is designed to give information about the common type of action that user or entity performs and allows to identify specific time slots for each. Any differences noted, abnormal occurances of an event can be a subject of automatic alerts. UEBA comes with defined dashboards which shows discovered actions and metrics for them.

![](/media/media/image238.png)

It is easy to filter presented data with single username/host or a group of users/hosts using query syntax. With help of saved searches SOC can create own outlook to stay focused on users at high risk of an attack.
Energy Logserver is made for working with data. UEBA gives new analytics approach, but what is more important it brings new metrics that we can work with. Artificial Intelligence functionality build in Energy Logserver help to calculate forecast for each action over single user or entire organization. In the same time thanks to extended set of rule types, Energy Logserver can correlate behavioral analysis with other data collected from environment. Working with Energy Logserver SIEM Plan with UEBA module greatly enlarge security analytics scope.

## BCM Remedy

Energy Logserver creates incidents that require handling based on notifications from the Alert module. This can be done, for example, in the BMC Remedy system using API requests. 

BMC Remedy configuration details: [https://docs.bmc.com/docs/ars91/en/bmc-remedy-ar-system-rest-api-overview-609071509.html](https://docs.bmc.com/docs/ars91/en/bmc-remedy-ar-system-rest-api-overview-609071509.html) .

To perform this incident notification in an external system.  You need to select in the configuration of the alert rule "Alert Method" "Command" and in the "Path to script/command" field enter the correct request.

![](/media/media/image239.png)

It is possible to close the incident in the external system using a parameter added to the alert rule.

```yaml
  #Recovery definition:
  recovery: true
  recovery_command: "mail -s 'Recovery Alert for rule RULE_NAME' user@example.com < /dev/null"
```

## SIEM Virtus Total integration

This integration utilizes the VirusTotal API to detect malicious content within the files monitored by **File Integrity Monitoring**. This integration functions as described below:

1. FIM looks for any file addition, change, or deletion onthe monitored folders. This module stores the hash of thesefiles and triggers alerts when any changes are made.
2. When the VirusTotal integration is enabled, it istriggered when an FIM alert occurs. From this alert, themodule extracts the hash field of the file.
3. The module then makes an HTTP POST request to theVirusTotal database using the VirusTotal API for comparisonbetween the extracted hash and the information contained inthe database.
4. A JSON response is then received that is the result ofthis search which will trigger one of the following alerts:
    - Error: Public API request rate limit reached.
    - Error: Check credentials.
    - Alert: No records in VirusTotal database.
    - Alert: No positives found.
    - Alert: X engines detected this file.

The triggered alert is logged in the ``integration.log`` file and stored in the ``alerts.log`` file with all other alerts.

Find examples of these alerts in the `VirusTotal integrationalerts`_ section below.

### Configuration

  Follow the instructions from :ref:`manual_integration` to enable the **Integrator** daemon and configure the VirusTotal integration.

  This is an example configuration to add on the ``ossec.conf`` file:

```xml
  <integration>
    <name>virustotal</name>
    <api_key>API_KEY</api_key> <!-- Replace with your   sTotal API key -->
    <group>syscheck</group>
    <alert_format>json</alert_format>
  </integration>
```

## SIEM Custom integration

The integrator tool is able to connect SIEM module with other external software. 

This is an example configuration for a custom integration in `ossec.conf`:

```xml
  <!--Custom external Integration -->
  <integration>
    <name>custom-integration</name>
    <hook_url>WEBHOOK</hook_url>
    <level>10</level>
    <group>multiple_drops|authentication_failures</group>
    <api_key>APIKEY</api_key> <!-- Replace with your external service API key -->
    <alert_format>json</alert_format>
  </integration>
```

To start the custom integration, the `ossec.conf` file, including the block integration component, has to be modified in the manager. The following parameters can be used:

 - name: Name of the script that performs the integration. In the case of a custom integration like the one discussed in this article, the name must start with “custom-“.
 - hook_url: URL provided by the software API to connect to the API itself. Its use is optional, since it can be included in the script.
 - api_key: Key of the API that enables us to use it. Its use is also optional for the same reason the use of the hook_url is optional.
 - level: Sets a level filter so that the script will not receive alerts below a certain level.
 - rule_id: Sets a filter for alert identifiers.
 - group: Sets an alert group filter.
 - event_location: Sets an alert source filter.
 - alert_format: Indicates that the script receives the alerts in JSON format (recommended). By default, the script will receive the alerts in full_log format.

## License Service

License service configuration is required when using the SIEM Plan license. To configure the License Service, set the following parameters in the configuration file:


hosts - Elasticsearch cluster hosts IP,
password - password for Logserver  user,
https - true or false.

```bash
vi /opt/license-service/license-service.conf
```

```bash
elasticsearch_connection:
  hosts: ["els_host_IP:9200"]

  username: logserver
  password: "logserver_password"

  https: true
```
