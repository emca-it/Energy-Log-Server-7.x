# **CHANGELOG**

## v7.4.1

### NewFeatures

- Reports: DOCX support!

### Improvements

- Alert: multi-language support for alert rules
- API: gui-access role is required to interact with the API
- tlstool.sh: new ssl certificate management tool

### BugFixes

- Archive: support for "secure" and "insecure" mode (without valid certificates)
- GUI: better-handled exceptions for custom plugins
- GUI: defaultAppId directive has been restored
- GUI: invalid directory for keystore
- GUI: Module Access Control permission fix
- GUI: users have aliases for different indexes after migration
- Index Management: missing verification for "on save" action
- Index Management: errors during rollover
- Index Management: filtering using the "Enabled" column
- Index Management: unable to update job after changing cron
- Integrations: improved command for importing dashboards
- Reports: custom logo moves the visualization on the dashboard
- Reports: deleting reports (multi, single) does not refresh the list
- Reports: enabling and disabling periodic reports by users
- Reports: incorrect visualization titles are inserted when creating a Data Table report
- Reports: long comment goes off the page when creating a PDF report
- Reports: long title goes off the page when creating a PDF report
- Reports: not translated statuses in the task list
- Reports: problem with Tag Cloud visualization when creating PDF report
- Reports: reports role paths to update, now require `.reports`
- Scheduler: status table sorted by "start date" instead of "name"
- Timeline/Timelion: regex not working due to an incorrectly built package

### SIEM Plan

- Alerts: bugfix: incorrect \_id of the edited alert causes duplicates
- Alerts: bugfix: unable to retrieve a list of risk key fields when updating a rule
- SIEM Engine: better-handled exceptions in RBAC integration

### Security related fixes

- CVE-2023-32002
- CVE-2023-32006
- CVE-2023-32559
- CVE-2021-32014
- CVE-2021-32012
- CVE-2021-32013
- CVE-2023-30533
- CVE-2022-24785
- CVE-2022-31129
- CVE-2022-24785
- CVE-2022-31129
- CVE-2023-22467
- CVE-2023-30533
- CVE-2023-26115

## v7.4.0

### Upgrades

- Complete database redefinition:
  - Segment replication
  - Searchable snapshots
  - Search backpressure feature can now cancel queries at the coordinator level

- Complete user interface redefinition
- Complete SIEM Engine redefinition:
  - New manager
  - New App
  - New Agent

- Input layer uses Logstash-OSS 7.17.11
- Support for Beats OSS Agents => 7.17.11

### NewFeatures

- Logserver: RBAC integration with Wazuh Engine (users can map roles between systems)

### Improvements

- CMDB: Browser-based Time Zone
- Improved error handling when reloading a license (_logserver/license/reload_)
- Archive: deleting tasks with multiselect option
- Unification and organization of Energy Logserver system APIs
- Alert: WebHook: added support for nested fields in http post payload
- Agents: built-in agents templates updated to 7.17.11

### BugFixes

- CMDB: incorrect parsing of values in the date filter
- Archive: blank line in index list on restore

## v7.3.0

### NewFeatures

- Multi-Language Support

### Improvements

- Improved security by using response security headers
- Network Probe: version lock prevents accidental updates
- configuration-backup.sh activated by default

### BugFixes

- Reports: usage of "Include unmapped fields" cause "No data" when exporting csv
- Agents: corrected manifest file for downloading agents
- Archive: error while restoring encrypted archives
- Cerebro: corrected auto-login after redirect

### Integrations

- VMware: Integration with dedicated dashboard and alerts
- AWS: Integration with dedicated dashboard and alerts
- Ruckus Networks: Integration with dedicated dashboard and alerts
- Added Beats templates to beats integration

### SIEM Plan

- WatchGuard: Integration with dedicated dashboard and alerts
- IDS Suricata: Integration with dedicated dashboard and alerts
- Alerts: updated rule database with 90 new alert rules including new Windows Security Group
- Alerts: bugfix: Jira integration
- Alerts: bugfix: duplication of alarms in specific cases
- Alerts: bugfix: top_count_keys doesn't work properly with multiple query_keys
- Alerts: bugfix: Broken Chain method TypeError
- Alerts: bugfix: Exclude Fields for Logical/Chain body correlation
- Alerts: NoLog rule for each alarm group

### Network-Probe

- Added support for sFlow - sfacctd service
- Added IDS Suricata integration with dedicated dashboard and alerts

### Security related

- log4j - logstash-input-tcp

### Required post upgrade

- Recreate bundles/cache: ```rm -rf /usr/share/kibana/optimize/bundles/* && systemctl restart kibana```

## v7.2.0

### **Breaking changes**

- Login: changed how gui access is granted for administrative users - access for any administrator has to be explicitly granted
- Wiki portal renamed to E-Doc

### NewFeatures

- CMDB: Infrastructure - create an inventory of all sources sending data to SIEM
- CMDB: Relations - ability to create relation topology map based on sources inventory
- Extended auditing support - each plugin can be enabled in GUI config to save its actions in the audit index
- Syntax Assistant for Alerts, Agents, Index Management, Network Probe. Check YAML definition and structure

### Improvements

- Update process will not override /etc/sysconfig/elasticsearch config
- Clear GUI message for expired license
- Agents: improved services information display for not running agents
- Archive: optimization and improvements; added multi threaded processing and Task Retry support
- Login: redesigned audit selection and exclusion settings GUI
- Reports: tasks edit is now more robust and allows modification of advanced parameters
- Reports: moved settings into new Config tab in the plugin from Config -> Settings
- Alerts: loading new alarm Rule Set during update process [install.sh]
- Beats: updated to v7.17.8
- Skimmer: negotiate highest TLS1.3 version if possible
- Skimmer: fixes regarding ssl connection
- Skimmer: added elasticsearch_ssl config option
- Skimmer: added new metric: node_stats_fs_total_free_in_pct
- Skimmer: updated to v1.0.22
- Elasticdump updated to v6.79.4

### BugFixes

- Refreshing audit exclusions caused ELS node to freeze in rare cases
- Update process on RedHat 7.9 could not be run caused by missing package
- LDAP login: improved validation on username input
- Table visualization: fix for "Count percenteges", which was inacurate in some cases
- Skimmer: sometimes did not start after installation
- Agents: small GUI improvements
- Alerts: long alert names presented outside the frame
- Alerts: sorting alert risk on incident tab did not work properly
- Intelligence: malware scanners would rise a false positive on one of the plugin dependencies
- Reports: data export (csv) improvements on file integrity
- Reports: a rare case of a race condition when removing temporary directories
- E-Doc: improvements to https handling when using Elasticsearch as a search engine
- install.sh: installation process always uses LC_ALL=C

### Integrations

- Added new integrations: FireEye, Infoblox, ArcSight Common Event Format

### SIEM Plan

- Agents: SIEM agents updated to 3.13.6
- Alerts: new notification methods: ServiceNow, WebHook, TheHive, Jira
- Alerts: risk values on incident tab formated for clarity
- Alerts: example description supplied with new values regarding escalate and recovery
- Alerts: all alerts in a goup can be seen with a proper row selection
- Alerts: creating risks is now supported on no time based indices
- Alerts: long alert names presented outside of message frame
- Alerts: on incident tab sorting by risk did not work properly
- Alerts: added Ransomware Detection rules

### Network-Probe

- Increased tolerance for status/verification calls

### Security related

- axios - CVE-2021-3749
- qs - CVE-2022-24999
- express - CVE-2022-24999
- moment - CVE-2022-24785
- moment - CVE-2022-31129
- minimist - CVE-2021-44906
- char.js - CVE-2020-7746
- async - CVE-2021-43138
- minimist - CVE-2021-44906
- requestretry - CVE-2022-0654
- xmldom - CVE-2022-39353
- underscore - CVE-2021-23358
- flask-cors - CVE-2020-25032
- kibana - CVE-2022-23707

### Required post upgrade

- Recreate bundles/cache: ```rm -rf /usr/share/kibana/optimize/bundles/* && systemctl restart kibana```
- Wiki portal renamed to E-Doc: if data migration is required follow the steps of UPGRADE.md

## v7.1.3

### Security related

- log4j updated to 2.19.0
- kafka updated to 2.13-3.3.1 (log4j dependency removed)
- logstash: removed obsolete bundled jdk

## v7.1.2

### NewFeatures

- Energy SOAR: Redesigned and improved integration (Security Orchestration, Automation And Response)
- Intelligence: Redesigned and improved Forecasting [experimental]
- Masteragent: New feature: Configuration Templates
- New plugin: CMDB - simple implementation of Configuration Management Database

### Improvements

- es2csv - Performance boost and Memory optimization
- Reports: Support for large report files
- Redirection of HTTPS connection to GUI enabled by default - 443 => 5601
- Login: Home Page moved to Integrations Page
- diagnostic-tool.sh - Added logstash logs
- Elasticsearch: Global timeouts changed to 60s
- Updated LICENSE in all components
- Index Management: Prepare index has been moved from Config to Index-Management tab
- Masteragent: Setting authorization with a client certificate by default
- Masteragent: Possibility to fully disable the HTTP server on masteragent clients

### BugFixes

- Login: Fixed problems with sharing Short Links
- Discovery: Fixed problem with index-patterns name overlapping
- Index Management: Fixed execution time for builin logtrail policies
- Masteragent: Fixed error when getting installed services

### Integrations

- windows-ad: Fixed error in Ad Accounts dashboard
- beats - Fixes in waf ruby filter

### SIEM Plan

- Vectra.AI: Integration with dedicated dashboard and alerts
- MITRE added to SIEM Dashboard
- Agents: SIEM agents updated to 3.13.4
- Agents: Vulnerability detection & feeds enabled by default
- Alert: Simplified discover_url feature
- Alert: theHive project - Improved integration
- Alert: Fixed exception for risk query
- Alert: SIEM alert group changed to "Correlated"
- Alert: Fixed problem with TypeError: deprecated_search()
- Alert: Fixed logs problem after rotating the file
- Alert: Fixed permission problem in Run Once mode
- Alert: Fixed indentation in query_string
- [bugfix] Added missing library to Qualys Quard venv
- [bugfix] Added missing ports 1514udp-tcp/1515tcp to install.sh

### Required post upgrade

- Recreate bundles/cache: ```rm -rf /usr/share/kibana/optimize/bundles/* && systemctl restart kibana```
- (SIEM only) Update/ReImport SIEM Dashboard for MITRE

## v7.1.1

### NewFeatures

- Elasticsearch Join support - API level query

### Improvements

- es2csv - Breakthrough (50%) performance boost
- es2csv - Renamed to els2csv
- diagnostic-tool.sh - Added logs encryption
- diagnostic-tool.sh - Renamed to `support-tool.sh`
- Skimmer: Indices_stats: run only on master node
- Skimmer: Added two metrics: indices_stats_patterns and indices_stats_regex
- Skimmer: Added cached info about nodes when poll errors out
- Logtrail: Disabled ratelimit in rsyslog for logtrail source files
- Logtrail: Parsing in pipeline for alert,kibana,elasticearch,logstash [added standardized log_level field]
- Logtrail: Added default filter showing only errors ["NOT log_level: INFO"]
- Index Management: Added built-in index policies for common actions
- Discovery: Default QueryLanguage changed to Lucene
- Cerebro updated to v0.9.4
- Curator updated to v5.8.4
- Elasticdump updated to v6.79.4
- Wiki.js updated to v2.5.274

### BugFixes

- Login: In case of unsuccessful login information about "redirection" is lost when using link sharing
- Login: When logging using SSO auth, it doesn't redirect when using link sharing
- Login: Fixed "unable to parse url" when using link sharing
- Login: Corrected Session expired message
- Login: gui-access role added to role-mappings.yml
- Login: When logging using SSO auth, sending the entered password as a default action
- Skimmer: Index store value of _cat/shards in bytes
- Skimmer: Disabled ssl handshake on logstash api
- Logtrail: Corrected syntax highlighting
- Logtrail: Fixed filter selector on columns
- Discovery: Fixed timeout handling
- Wiki: Removed gui-access group
- Index Management: Wait for updates before refreshing the list
- Index Management: Fixed id problem during custom update

### Integrations

- windows-ad/beats: fixed error in ruby{} filter
- netflow - Fixes from 7.1.0
- netflow - network_vis - Fixed incorrect filtering
- netflow - network_vis - Added new option "skip null values"
- syslog-mail - Fixes from 7.1.0

### SIEM Plan

- Added Log4j RCE attacks to Detection Rules ["Wazuh alert [HIGH] - rule group: custom - Log4j RCE"]
- Alert: Fixed problem with modifying alertrulemethod
- Alert: Fixed malfunction of Test Rule in case of "verify_certs: false" setting
- Alert: Simplified Discovery URL
- Alert: Logtrail - Cluster Services Error Logs added to Cluster-Health group

### Security related

- http-proxy - CVE-2022-0155
- xlsx - CVE-2021-32013
- json-schema - CVE-2021-3918
- lodash - CVE-2021-23337
- json-schema - CVE-2021-3918
- pdf-image - CVE-2020-8132
- angular-chart.js - CVE-2020-7746
- pyyaml - CVE-2020-14343
- cryptography - CVE-2020-25659
- aws-sdk - CVE-2020-28472
- pyyaml - CVE-2020-14343
- nodemailer - CVE-2020-7769
- objection - CVE-2021-3766
- socket.io - CVE-2020-28481
- nodejs - CVE-2021-44531

## v7.1.0

### NewFeatures

- Added support for AlmaLinux and RockyLinux
- Agents: Added local repository with GUI download links for agents installs
- Archive: Added 'Run now' for scheduled archive tasks
- Archive: Added option to enable/disable archive task
- Archive: Added option to encrypt archived data
- Audit:  Added report of non-admin user actions in GUI
- Elasticsearch: Added field level security access control for documents
- Kibana: Added support for Saved Query object in access management
- Kibana: Added support for TLS v1.3
- Kibana: Added new plugin Index Management - automate index retention and maintanance
- Reports: Added new report type created from data table visualizations - allows creating a raport like table visualization including all records (pagination splitted into pages)
- Reports: Added option to specify report task name which sets destination file name

### Improvements

- Security: log4j updated to address vulnerabilities: CVE-2021-44228, CVE-2021-45046, CVE-2021-45105, CVE-2021-44832, CVE-2021-4104
- Added new directives for LDAP authenctication
- Agents: Changed agent's action name from drop to delete
- Archive: Improvement and optimization of "resume" feature
- Archive: Optimised archivization proces by saving data directly to zstd file
- Archive: Multiple 'Upload' GUI improvements
- Archive: Improved logs verbosity
- Audit: Added template for audit index
- Beats: Updated to v7.12.1
- Curator: Added curator logs for rotation
- Elasticsearch: Extended timeout for starting service
- Elasticsearch: Updated engine to v7.5.2
- install.sh: Improved update section for better handling of services restart
- Kibana: Updated engine to v7.5.2
- Kibana: Clean SSL info in logs
- Kibana: Improved built-in roles
- Kibana: Disabled telemetry
- Kibana: Set Discovery as a default app
- Kibana: Optimized RPM
- Kibana: Improved handling of unauthorized access in Discovery
- Kibana: small changes in UI - Improved Application RBAC, product version
- Kibana: Added new logos
- Kibana: Improved login screen, unauthorized access info
- Kibana: Restricted access to specific apps
- Kibana: Added option to configure default app
- Logrotate: Added Skimmer
- Logstash: Updated to v7.12.1
- Network visualization: UI improvements
- Object permission: Index pattern optimizations
- Plugins: Moved Cluster Management inoto the right top menu, Scheduler and Sync moved to the Config
- Reports: Added report's time range info to raport details description
- small_backup.sh: Added cerebro and alert configuration
- Skimmer: Updated to v1.0.20
- Skimmer: Added new metrics, pgpgin, pgpgout
- Skimmer: Optimised duration_in_milis statistics
- Skimmer: Added option to specify types
- Skimmer: Added option to monitor disk usage
- Wiki: Added support for nonstandard kibana port
- Wiki: Several optimizations for roles
- Wiki: Changed default search engine to elasticsearch
- Wiki: Added support for own CAs
- Wiki: Default authenticator improvements
- XLSX Import: UI improvements

### BugFixes

- Archive: Fixed problems with task statuses
- Archive: Fixed application crash when index name included special characters
- Archive: Fixed 'checksum mismatch' bug
- Archive: Fixed bug for showing unencrypted files as encrypted in upload section
- Elasticsearch: Fixed bug when changing role caused client crash
- Elastfilter: Fixed "_msearch" and "_mget" requests
- Elastfilter: Fixed bug when index pattern creation as an admin caused kibana failure
- Kibana: Fixed timeout handling
- Kibana: Fixed a bug causing application crash when attempting to delete data without permission to it
- Logstash: Fixed breaking geoip db when connection error occurred
- Object permission: Fixed adding dashboard when all its related objects are already assigned
- Reports: Added clearing .tmp files from corrupted csv exports
- Reports: Fixed sending PDF instead of JPEG in scheduled reports
- Reports: Fixed not working scheduled reports with domain selector enabled
- Skimmer: Fixed expected cluster nodes calculation
- Wiki: Added missing home page
- Wiki: Added auto start of wiki service after installation
- Wiki: Fixed logout behaviour

### Integrations

- Fixed labels in Skimmer dashboard
- Fixed Audit dashboard fields
- Updated Windows + AD dashboard and pipeline
- Added Linux Mail dashboard and pipeline
- Added Cisco ASA dashboard and pipeline
- Added FortiGate dashboard and pipeline
- Added Paloalto dashboard and pipeline
- Added Oracle dashboard and pipeline
- Added Waystream dashboard and pipeline
- Added CEF dashboard and pipeline (CheckPoint, FireEye, Air-Watch, Infoblox, Flowmon, TrendMicro, CyberX, Juniper Networks)
- Added monitoring of the alert module on Alert Dashboard

### SIEM Plan

- Updated SIEM dashboard
- Updated QualysGuard integration
- Updated Tenable.SC  integration
- Alert: Updated detection rules (370+)
- Alert: Added Cluster-Health alert rules
- Wazuh: Updated to v3.13.3
- Wazuh: UI improvements
- Alert: Improved groups management
- Alert: Multiple UI/UX tweaks
- Alert: Revised alerts' descriptions and examples
- Alert: Adding included fields when invert:true
- Alert: Changed startup behaviour
- Alert: Added field from 'include' to match_body
- Alert: Optimised loading files with misp lists
- Alert: Added option to set sourceRef in alert definition
- Alert: Include & Exlcude in blacklist-ioc lists
- Alert: Fixed several issue in chain and logical alerts
- Alert: Fixed error when user tried to update alert from newly added group
- Alert: Fixed top_count_keys not working with multiple query_key
- Alert: Fixed bug when match in blacklist-ioc is breaking other rules
- Alert: Fixed empty risk_key breaking alert rule
- Alert: Fixed endless loop during scroll

### Network-Probe

- Added integration with license service
- Changed plugin icon
- Changed default settings
- Changed logs mapping in logstash
- Optimised netflow template to be more efficient
- Updated .service files
- Updated Network-Probe dashboard

### API Changes

- Elasticsearch: Updated API endpoints.
  - Following endpoints deprecated and update with:
    - `/_auth/account` -> `/_logserver/accounts`
    - `/_license/reload` -> `/_logserver/license/reload`
    - `/_role-mapping/reload` -> `/_logserver/auth/reload`
    - `/user/updatePassword` -> `/_logserver/user/password`
  - Following endpoint was removed and replaced with:
    - `/_license` -> `/_logserver/license`

### **Breaking changes**

- During the update, the "kibana" role will be removed and replaced by "gui-access", "gui-objects", "report". The three will automatically be assigned to all users that prior had the "kibana" role. If you had a custom role that allowed users to log in to the GUI this WILL STOP WORKING and you will have to manually enable the access for users.
- The above is also true for LDAP users. If role mapping has been set for role kibana this will have to be manually updated to "gui-access" and if required "gui-objects" and "report" roles.
- If any changes have been made to the "kibana" role paths, those will be moved to "gui-objects". GUI objects permissions also will be moved to "gui-objects" for "gui-access" cannot be used as a default role.
- The "gui-access" is a read-only role and cannot be modified. By default, it will allow users to access all GUI apps; to constrain user access, assign user a role with limited apps permissions.
- "small_backup.sh" script changed name to "configuration-backup.sh" - this might break existing cron jobs
- SIEM plan is now a separate add-on package (requires an additional license)
- Network-Probe is now a separate add-on package (requires an additional license)
- (SIEM) Verify rpmsave files for alert and restore them if needed for following:
  - /opt/alert/config.yaml
  - /opt/alert/op5_auth_file.yml
  - /opt/alert/smtp_auth_file.yml

### Required post upgrade

- Role "wiki" has to be modified to contain only path: ".wiki" and all methods

## v7.0.6

### NewFeatures

- Alert: Added 5 alerts to detect SUNBURST attack
- Incidents: Added the ability of transferring the calculated risk_value to be sent in any alarm method
- Indidents: Added visibility of unassigned incidents based on user role - security-tenant role
- install.sh: Added the ability to update with ./install.sh -u

### Improvements

- Object permission: Object filtering optimization
- Reports: Date verification with scheduler enabled tasks
- Reports: UI optimization

### BugFixes

- Agents: CVE-2020-28168
- Alert: Fixes problem with Syslog notifications
- Alert: Fixes problem with Test Rule functionality
- Alert: CVE-2020-28168
- Archive: CVE-2020-28168
- Cerebro: CVE-2019-12384
- Kibana-xlsx-import: CVE-2020-28168
- Login: CVE-2020-28168
- Reports: CVE-2020-28168
- Reports: Fixes errors related to background tasks
- Sync: CVE-2020-28168

## v7.0.5

### NewFeatures

- New plugin: Wiki - integration with wiki.js
- Agents: Added index rotation using rollover function
- Alert: Added counter with information about how many rules there are in a given group
- Alert: Added index rotation using rollover function
- Alert: First group will be expanded by default
- Alert: New Alert method for Syslog added to GUI
- Archive: Added compression level support - archive.compressionOptions [kibana.yml]
- Archive: Added mapping/template import support
- Archive: Added number of matches in files
- Archive: Added regexp and extended regexp support
- Archive: Added size information of created archive on list of files for selection
- Archive: Added support for archiving a selected field from the index
- Archive: Added timestamp field for custom timeframe fields
- Audit: Added index rotation using rollover function
- Config: Added configuration possibility for Rollover (audit/alert/.agents indexes) in Settings tab
- Object Permission: When deleting an object to a role in "object permission" now is possible to delete related objects at the same time
- Reports: Ability to delete multiple tasks at once
- Reports: Added details field for each task that includes information about: user, time range, query
- Reports: Added Scheduler for "Data Export" tab
- Reports: Fields to export are now alphabetical, searchable list
- Reports: Scheduled tasks supports: enable, disable, delete
- Reports: Scheduled tasks supports: Logo, Title, Comments, PDF/JPEG, CSV/HTML
- Installation support for Centos7/8, RedHat7/8, Oracle Linux7/8, Scientific Linux 7, Centos Stream
- iFrame embedding support: new directive login.isSameSite in kibana.yml ["Strict" or "None"]

### Improvements

- Access management: Plugin Login for app management  will show itself as Config
- Alert: Added support for nested fields in blacklist-ioc alert type
- Alert: Alert Dashboard rewritten to alert_status pattern - allows you to filter visible alarms per user
- Alert: Cardinality - fix for _thread._local' object has no attribute 'alerts_sent'
- Alert: Chain/Logical - few improvements for output content
- Alert: Rule type example is hidden by default
- Alert: RunOnce - improved results output
- Alert: RunOnce - information that the process has finished
- Alert: TestRule - improved error output
- Archive: Added document sorting, which speeds up elasticsearch response
- Archive: API security -> only admin can use (previously only visual information)
- Archive: Archiving process uses a direct connection, bypassing the elastfilter - proxy
- Archive: Changed UTC time to local time
- Archive: Information about problems with reading/writing to the archive directory
- Archive: Optimized function for loading large files - improved loading time
- Archive: Optimized saving method to a temporary flat file
- Archive: Optimized scroll time which speeds up elasticsearch response
- Audit: Converted SEARCH _id: auditselection to GET _id: auditselection
- Audit: Removed background task used for refresh audit settings
- Beats: Updated to v6.8.14
- Blacklist-IOC: Added Duplicates removal mechanism
- Blacklist-IOC: Automatic configuration of repository access during installation [install.sh]
- Cerebro: Updated to v0.9.3
- Config: Character validation for usernames and roles - can consist only of letters a-z, A-Z, numbers 0-9 and characters _,-
- Config: Deleting a user deletes his tokens/cookies immediately and causes logging out
- Config: Securing the default administrator account against deletion
- Config: Session timeout redirect into login screen from all modules
- Config: Workaround for automatic filling of fields with passwords in modern browsers
- Curator: Updated to v5.8.3 and added support for Python3 as default
- ElasticDump: Updated to v6.65.3 and added support for backup all templates at once
- Elasticsearch: Removed default user "scheduler" with the admin role - is a thing of history
- Elasticsearch: Removed indices.query.bool.max_clause_count from default configuration - causes performance issues
- Elasticsearch: Role caching improvements
- GEOIP: Automatic configuration of repository access during installation [install.sh]
- Incidents: Switching to the Incidents tab creates pattern alert* if not exist
- install.sh: Added workaround for cluster.max_shards_per_node=1000 bug
- Kibana: Removed kibana.autocomplete from default configuration - causes performance issues
- License: Revision and update of license files in all system modules
- Logstash: Updated logstash-codec-sflow to v2.1.3
- Logstash: Updated logstash-input-beats to v6.1.0
- Logstash: Updated to v6.8.14
- Logtrail: Added default actionfile for curator - to clean logtrail indexes after 2 days
- Network visualization: corrected legend and better colors
- Reports: Added Switch button for filtering only scheduled tasks
- Reports: Admin users should see all scheduled reports from every other user
- Reports: Changed "Export Dashboard" to "Report Export"
- Reports: Changed "Export Task Management" to "Data Export"
- Reports: Crontab format validated before Submit in Scheduler
- Reports: Default task list sorted by "start time"
- Reports: Improved security by using kernel namespaces - dropped suid permissions for chrome_sandbox
- Reports: Moved "Schedule Export Dashboard" to "Report Export" tab
- Reports: Try catch for async getScheduler function
- Skimmer: Added alerts: High_lag_on_Kafka_topic, High_node_CPU_usage, High_node_HEAP_usage, High_Flush_duration, High_Indexing_time
- Skimmer: New metric - _cat/shards
- Skimmer: New metric - _cat/tasks
- Skimmer: Updated to v1.0.17
- small_backup.sh: Added sync, archive, wiki support
- small_backup.sh: Information about the completed operation is logged
- Wazuh: Searching in the rule.description field

### BugFixes

- Access Management: Cosmetic issue in apps select box for default roles (like admin, alert, intelligence, kibana etc.)
- Alert: Category name did not appear on the "Risk" list
- Alert: Description update for find_match alert type
- Alert: Fixes bug where after renaming the alert it is not immediately visible on the list of alerts
- Alert: Fixes bug where editing of alert, causes it returns to the Other group
- Alert: Fixes incorrect function alertMethodData - problem with TestRule operation [itrs op5 alert-method]
- Alert: Fixes problem with '[]' in rule name
- Alert: Fixes process status in Alert Status tab
- Alert: In groups, if there is pagination, it is not possible to change the page - does not occur with the default group "Others"
- Alert: Missing op5_url directive in /opt/alert/config.yaml [itrs op5 alert-method]
- Alert: Missing smtp_auth_file directive in /opt/alert/config.yaml [itrs op5 alert-method]
- Alert: Missing username directive in /opt/alert/config.yaml [itrs op5 alert-method]
- Alert: Overwrite config files after updating, now it should create /opt/alert/config.yml.rpmnew
- Archive: Fixes exception during connection problems to elasticsearch
- Archive: Missing symlink to runTask.js
- Cerebro: Fixes problems with PID file after cerebro crash
- Cerebro: Overwrite config files after updating, now it should create /opt/cerebro/conf/application.conf.rpmnew
- Config: SSO login misreads application names entered in Access Management
- Elasticsearch: Fixes "No value present" message log when not using a radius auth [properties.yml]
- Elasticsearch: Fixes "nullPointerException" by adding default value for licenseFilePath [properties.yml]
- Incidents: Fixes problem with vanishing status
- install.sh: Opens the ports required by logstash via firewall-cmd
- install.sh: Set openjdk11 as the default JAVA for the operating system
- Kibana: Fixes exception during connection problems to elasticsearch - will stop restarting
- Kibana: Fixes URL shortening when using Store URLs in session storage
- Logtrail: Fixes missing logrotate definitions for Logtrail logfiles
- Logtrail: Overwrite config files after updating, now it should create /usr/share/kibana/plugins/logtrail/logtrail.json.rpmnew
- Object Permission: Fixes permission verification error if the overwritten object's title changes
- Reports: Fixes Image Creation failed exception
- Reports: Fixes permission problem for checkpass Reports API
- Reports: Fixes problems with AD/Radius/LDAP users
- Reports: Fixes problem with choosing the date for export
- Reports: Fixes setting default index pattern for technical users when using https
- Skimmer: Changed kafka.consumer_id to number in default mapping
- Skimmer: Fixes in indices stats monitoring
- Skimmer: Overwrite config files after updating, now it should create /opt/skimmer/skimmer.conf.rpmnew

## v7.0.4

### NewFeatures

- New plugin: Archive specified indices
- Applications Access management based on roles
- Dashboards: Possibility to play a sound on the dashboard
- Tenable.SC: Integration with dedicated dashboard
- QualysGuard: Integration with dedicated dashboard
- Wazuh: added installation package
- Beats: added to installation package
- Central Agents Management (masteragent): Stop & start & restart for each registered agent
- Central Agents Management (masteragent): Status of detected beats and master agent in each registered agent
- Central Agents Management (masteragent): Tab with the list of agents can be grouped
- Central Agents Management (masteragent): Autorolling documents from .agents index based on a Settings in Config tab
- Alert: New Alert method for op5 Monitor added to GUI.
- Alert: New Alert method for Slack added to GUI.
- Alert: Name-change - the ability to rename an already created rule
- Alert: Groups for different alert types
- Alert: Possibility to modify all alarms in selected group
- Alert: Calendar - calendar for managing notifications
- Alert: Escalate - escalate alarm after specified time
- Alert: TheHive integration

### Improvements

- Object Permission: When adding an object to a role in "object permission" now is possible to add related objects at the same time
- Skimmer: New metric - increase of documents in a specific index
- Skimmer: New metric - size of a specific index
- Skimmer: New metric - expected datanodes
- Skimmer: New metric - kafka offset in Kafka cluster
- Installation script: The setup script validates the license
- Installation script: Support for Centos 8
- AD integration: Domain selector on login page
- Incidents: New fieldsToSkipForVerify option for skipping false-positives
- Alert: Added sorting of labels in comboxes
- User Roles: Alphabetical, searchable list of roles
- User Roles: List of users assigned to a given role
- Audit: Cache for audit settings (performance)
- Diagnostic-tool.sh: Added cerebro to audit files
- Alert Chain/Logical: Few improvements

### BugFixes

- Role caching fix for working in multiple node setup.
- Alert: Aggregation schedule time
- Alert: Loading new_term fields
- Alert: RecursionError: maximum recursion depth exceeded in comparison
- Alert: Match_body.kibana_discover_url malfunction in aggregation
- Alert: Dashboard Recovery from Alert Status tab
- Reports: Black bars after JPEG dashboard export
- Reports: Problems with Scheduled reports
- Elasticsearch-auth: Forbidden - not authorized when querying an alias with a wildcard
- Dashboards: Logserver_table is not present in 7.X, it has been replaced with basic table
- Logstash: Mikrotik pipeline - failed to start pipeline

## v7.0.3

### NewFeatures

- Alert: new type - Chain - create alert from underlying rules triggered in defined order
- Alert: new type - Logical - create alert from underlying rules triggered with defined logic (OR,AND,NOR)
- Alert: correlate alerts for Chain and Logical types - alert is triggered only if each rule return same value (ip, username, process etc)
- Alert: each triggered alert is indexed with uniqe alert_id - field added to default field schema
- Alert: Processing Time visualization on Alert dashboard - easy to identify badly designed alerts
- Alert: support for automatic search link generation
- Input: added mikrotik parsing rules
- Auditing : added IP address field for each action
- Auditing : possibility to exclude values from auditing
- Skimmer: indexing rate visualization
- Skimmer: new metric: offset in Kafka topics
- SKimmer: new metric: expected-datanodes
- MasterAgent: added possibility for beats agents restart and the master agent itself (GUI)

### Improvements

- Search and sort support for User List in Config section
- Copy/Sync: now supports "insecure" mode (operations without certificates)
- Fix for "add sample data & web sample dashboard" from Home Page -> changes in default-base-template
- Skimmer: service status check rewriteen to dbus api
- Masteragent: possibility to exclude older SSL protocols
- Masteragent: now supports Centos 8 and related distros
- XLSX import: updated to 7.6.1
- Logstash: masteragent pipeline shipped by default
- Blacklist: Name field and Field names in the Fields column & Default field exclusions
- Blacklist: runOnce is only killed on a fatal Alert failure
- Blacklist: IOC excludes threats marked as false-positive
- Incidents: new design for Preview
- Incidents: Note - new feature, ability to add notes to incidents
- Risks: possibility to add new custom value for risk, without the need to index that value
- Alert: much better performance with multithread support - now default
- Alert: Validation of email addresses in the Alerts plugin
- Alert: "Difference" rule description include examples for alert recovery function
- Logtrail: improved the beauty and readability of the plugin
- Security: jquery updated to 3.5.1
- Security: bootstrap updated to 4.5.0
- The HELP button (in kibana) now leads to the official product documentation
- Centralization of previous alert code changes to single module

### BugFixes

- Individual special characters caused problems in user passwords
- Bad permissions for scheduler of Copy/Sync module has been corrected
- Wrong Alert status in the alert status tab
- Skimmer: forcemerge caused under 0 values for cluster_stats_indices_docs_per_sec metric
- diagnostic-tool.sh: wrong name for the archive in output
- Reports: export to csv support STOP action
- Reports: scroll errors in csv exports
- Alert: .alertrules is not a required index for proper system operation
- Alert: /opt/alerts/testrules is not a required directory for proper system operation
- Alert: .riskcategories is not a required index for proper system operation
- Malfunction in Session Timeout
- Missing directives service_principal_name in bundled properties.yml
- Blacklist: Removal of the _doc_ type in blacklist template
- Blacklist: Problem with "generate_kibana_discover_url: true" directive
- Alert: Overwriting an alert when trying to create a new alert with the same name
- Reports: When exporting dashboards, PDF generates only one page or cuts the page
- Wrong product logo when viewing dashboards in full screen mode

## v7.0.2

### NewFeatures

- Manual incident - creating manual incidents from the Discovery section
- New kibana plugin - Sync/Copy between clusters
- Alert: Analyze historical data with defined alert
- Indicators of compromise (IoC) - providing blacklists based on Malware Information Sharing Platform (MISP)
- Automatic update of MaxMind GeoIP Databases [asn, city, country]
- Extended LDAP support
- Cross cluster search
- Diagnostic script to collect information about the environment, log files, configuration files - utils/diagnostic-tool.sh
- New beat: op5beat - dedicated data shipper from op5 Monitor

### Improvements

- Added `_license` API for elasticsearch (it replaces `license` path which is now deprecated and will stop working in future releases)
- `_license` API now shows **expiration_date** and **days_left**
- Visual indicator on **Config** tab for expiring license (for 30 days and less)
- Creating a new user now requires reentering the passoword
- Complexity check for password fields
- Incidents can be supplemented with notes
- Alert Spike: more detailed description of usage
- ElasticDump added to base installation - /usr/share/kibana/elasticdump
- Alert plugin updated - frontend
- Reimplemented session timeout for user activity
- Skimmer: new metrics and dashboard for Cluster Monitoring
- Wazuh config/keys added to small_backup.sh script
- Logrotate definitions for Logtrail logfiles
- Incidents can be sorted by Risk value
- UTF-8 support for credentials
- Wazuh: wrong document_type and timestamp field

### BugFixes

- Audit: Missing Audit entry for succesfull **SSO** login
- Report: "stderr maxBuffer length exceeded" - export to csv
- Report: "Too many scroll contexts" - export to csv
- Intelligence: incorrect work in updated environments
- Agents: fixed wrong document type
- Kibana: "Add Data to Kibana" from Home Page
- Incidents: the preview button uses the wrong index-pattern
- Audit: Missing information about login errors of ad/ldap users
- Netflow: fix for netflow v9
- MasterAgent: none/certificade verification mode should work as intended
- Incorrect CSS injections for dark theme
- The role could not be removed in specific scenarios

## v7.0.1

- init
- migrated features from branch 6 [ latest:6.1.8 ]
- XLSX import [kibana]
- curator added to /usr/share/kibana/curator
- node_modules updated! [kibana]
- elasticsearch upgraded to 7.3.2
- kibana upgraded to 7.3.2
- dedicated icons for all kibana modules
- eui as default framework for login,raports
- bugfix: alerts type description fix
