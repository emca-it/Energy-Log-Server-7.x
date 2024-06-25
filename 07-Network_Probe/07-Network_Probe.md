## Network Probe

The Network Probe plugin allows you to manage and control probes distributed among many hosts, as well as manage logstash's probes.

### About

<span style="font-size:1.3em;"> **Network Probe has built-in tools for capturing and analyzing network traffic (Network Security Monitoring):** </span>

#### IDS and Full Packet Capture

Network probe provides a high performance Network IDS, IPS and Network Security Monitoring engine.
It allows you to capture anomalies and log network traffic alarms based on defined rules.
It has the ability to save PCAP of all detected packets.

#### NDR

Network probe acts as a passive network traffic analyzer. Many operators use Network Probe as a network security monitor (NSM) to support investigations of suspicious or malicious activity. It supports a wide range of traffic analysis tasks beyond the security domain, including performance measurement and troubleshooting.
The first benefit a new user derives from Network Probe NDR is the extensive set of logs describing network activity. These logs include not only a comprehensive record of every connection seen on the wire, but also application-layer transcripts. These include all HTTP sessions with their requested URIs, key headers, MIME types, and server responses; DNS requests with replies; SSL certificates; key content of SMTP sessions; and much more. By default, NDR writes all this information into well-structured tab-separated or JSON log files suitable for post-processing with external software. Users can also choose to have external databases or SIEM products consume, store, process, and present the data for querying.

#### Netflow

Netflow collector is a set of multi-flow accounting feature: it is ready index for NetFlow v5/v9, IPFIX and sFlow packets on one or more interfaces (IPv4 and IPv6). Other than acting as a collector, Network Probe can also replicate to 3rd party collectors. It can account, classify, aggregate, replicate and export forwarding-plane data, i.e. IPv4 and IPv6 traffic

### System Requirements


1. Supported Operating Systems

   - Red Hat Linux 7.X
   - Red Hat Linux 8.X
   - Centos 7.X
   - Oracle Linux 8.X - Unbreakable Enterprise Kernel (UEK)
   - Centos Stream 7.X, 8.X
   - AlmaLinux 8.X
   - RockyLinux 8.X

2. Supported Web Browsers

   - Google Chrome
   - Mozilla Firefox
   - Opera
   - Microsoft Edge

3. Network communication

   <table id="id1" class="colwidths-given docutils" border="1"><colgroup>  <col width="5%" /> <col width="22%" /> <col width="20%" /> <col width="6%" /> <col width="9%" />  </colgroup>
   <thead valign="bottom">
     <tr class="row-odd">
       <th class="head">From</th>
       <th class="head">To</th>
       <th class="head">Port</th>
       <th class="head">Protocol</th>
       <th class="head">Description</th>
     </tr>
   </thead>
   <tbody valign="center">
     <tr class="row-odd">
       <td class="first last">Network Probe</td>
       <td class="first last">Logserver</td>
       <td class="first last">9200</td>
       <td class="first last">TCP</td>
       <td class="first last">License verification and Logserver API</td>
     </tr>
    <tr class="row-odd">
    <td>GUI</td>
    <td>License Service</td>
    <td>9000</td>
    <td>TCP</td>
    <td>Manage files, services and pipelines.</td>
    </tr>
    <tr class="row-even">
    <td>Integrated Source</td>
    <td>Network Probe</td>
    <td>Source's individual port</td>
    <td>TCP/UDP</td>
    <td>Data ingestion of managed integrations.</td>
    </tr>
   </tbody>
   </table>

    Moreover, as mentioned in the last row, in order for managed integrations to work properly, it is necessary to open and maintain the ports they use.

### Licensing

The Network Probe feature is available only for admin users and when it is covered by the license.

There is always a banner at the top of the page showing how many probes are currently in use and how many probes can be registered at most. This number is defined in the license. For example, the banner below indicates that 3 probes are currently registered, for a total of 11 probes purchased - 8 more can be registered.

![](/media/media/07_network_probe/license/license_banner.png)

If something has gone wrong, the license can be restored by clicking the "Refresh license" text. However, if the problem persists, please contact support.

![](/media/media/07_network_probe/license/license_banner_fail.png)

If the license has expired, you will not be able to use the module, and the services managed by the probe will be stopped permanently, until a correct license is retrieved.

### Setting up the probe

#### Registration of a new probe

The first time the probe is started, it will automatically register itself. No additional operations are required.

#### Database connection

The probe requires a connection to the Logserver service to work. Set the appropriate variables in the `/opt/license-service/license-service.conf` file in the `elasticsearch_connection` section. For example:

```yaml
    elasticsearch_connection:
        hosts: ["127.0.0.1:9200"]

        username: license
        password: license

        https: true

        verify_certs: true
        certificate_path: /etc/elasticsearch/rootCA.crt
```

### Gui Plugin

This plugin consist of two main sections - `Pipelines Management` and `Network Probes` which will be detailed below.

#### Pipelines Management

This tab allows you to manage pipelines on all probes simultaneously. The list below presents a list of available pipelines that can be assigned appropriately after clicking the button on the right.

![](/media/media/07_network_probe/pipelines_management_page/all_pipelines_list.png)

Each row of the table describes a pipeline that can be used by the probe. There we can find data such as:
- name of the pipeline
- information about the probes on which the pipeline runs
- how many probes utilize the pipeline

The described list is searchable in two ways: the pipeline can be found by its name or the hostname of the assigned probe to it.

##### Pipeline Details

A green label with a check icon means that this probe is working and the pipeline is enabled. On the other hand, a gray label with a cross means that the pipeline should be working, but the probe is not responding.

Clicking on a probe in the assigned probes column redirects to the statuses of pipelines running on that specific probe.

More details of pipelines can be expanded by clicking on the arrow on the left.

![](/media/media/07_network_probe/pipelines_management_page/all_pipelines_details.png)

In the details, we can find data about the hostname, address, and status of the probes.

##### Manage pipeline

After clicking the pencil icon on the right, a following pipeline configuration window will appear.

![](/media/media/07_network_probe/pipelines_management_page/manage_modal/modal.png)

The list shows the assignment of this pipeline to available probes. If a given row is unchecked, it means that the pipeline is not assigned to this probe. Similarly, if the line is selected, the pipeline already works.

If a given probe cannot be selected, it means that the probe is not working and no changes can be made to it.

After making any changes to the table, pipelines will be highlighted and their status will change after clicking the submit button. In the lower-left corner, there is precise information about what operations will be performed.

![](/media/media/07_network_probe/pipelines_management_page/manage_modal/before_submit.png)

For example, the above photo shows a situation in which the `custom` pipeline will be activated on the first probe. In turn, no operation will be performed for the rest.

The process of activation or deactivation of the pipeline can be monitored based on the status in the `Result` column.

After the operation has been completed, an appropriate icon will be displayed - green if everything went well or red if something went wrong.

![](/media/media/07_network_probe/pipelines_management_page/manage_modal/after_submit.png)

When you hover over the result icon, an error message can be seen, such as presented below:

![](/media/media/07_network_probe/pipelines_management_page/manage_modal/after_submit_failure.png)

Following the changes, clicking the close button, and refreshing the pipeline lists, the change should be visible.

#### Network Probes

This tab shows all registered probes. Here you can check data, such as:
- status - information on whether the probe is working
- operating system
- hostname
- address
- last revision - when the probe responded correctly last time
- services status
- installed services
- pipelines status

![](/media/media/07_network_probe/network_probes_page/probes_list.png)

After hovering over one of the columns regarding services or pipelines, a table with more details will be displayed.

![](/media/media/07_network_probe/network_probes_page/probes_list_details.png)

To open more details of the probe and use the ability to manage services, pipelines, or files click on the eye icon on the right, as shown below.

![](/media/media/07_network_probe/network_probes_page/probes_list_go_to_details.png)

##### Services Section

This section is used to manage defined services. Here you can view their status and, depending on the situation, enable, disable, or restart the service.

![](/media/media/07_network_probe/network_probes_page/services/services_list.png)

Services can be managed individually or by selecting several lines at the same time.

![](/media/media/07_network_probe/network_probes_page/services/services_stop.png)

##### Pipelines Section

This section is used to manage pipelines. Here you can observe the status and statistics of pipelines to monitor their functioning. You can also enable or disable a given pipeline, as well as reload logstash configuration files using the reload method. All functionalities will be described below, but first some introduction to pipeline configuration definition.

![](/media/media/07_network_probe/network_probes_page/pipelines/pipelines.png)

###### Pipeline configuration

By default pipeline can be defined as a set of files consisting of:
- `definition file` - file with name and path to configuration files directory and possibly some pipeline-specific options. Such a file can define multiple pipelines at once. The default path is: `/etc/logstash/pipelines.d/pipeline_name.yml`.
- `configuration files` - files containing pipeline plugins configurations. By default, it is: `/etc/logstash/conf.d/pipeline_name/*.conf`, but it can be altered through a definition file.

The above settings can be found in the pipeline details, after clicking the arrow on the left.

![](/media/media/07_network_probe/network_probes_page/pipelines/pipelines_status_disabled.png)

###### Pipeline status

Pipeline status can be one of the following:
- **Active** - pipeline is enabled and running. Everything works as expected, and runtime statistics are available.
- **Active** _with warning_ - the pipeline is enabled and running, but some reload error has occurred.
- **Inactive** - the pipeline should work because it is enabled, but it does not work and its statistics cannot be found.
- **Disabled** - the pipeline is disabled and is not running.
- **Unknown** - pipeline has unexpectedly failed, it covers situations such as wrong configuration, corrupted files or not working logstash.

In addition to the status, the adjacent column displays details that specifically describe the current status and may indicate the cause of a hypothetical error.

The arrow on the left can be clicked to view more details. Configuration details will be displayed for all pipelines, and for _active_ pipelines you can view the runtime statistics such as:
- input, filter, and output events
- queue details
- utilized plugins (input, filter, output, and codecs)

![](/media/media/07_network_probe/network_probes_page/pipelines/pipelines_status_active.png)

If a reload error has occurred, it will also be visible there, as shown below.

![](/media/media/07_network_probe/network_probes_page/pipelines/pipelines_status_active_warning.png)

###### Filtering by status

The list of pipelines can be filtered based on their status using the four buttons next to the search bar. Thanks to this, only pipelines with the same status can be displayed, increasing the readability of the table. Below only disabled pipelines are shown:

![](/media/media/07_network_probe/network_probes_page/pipelines/pipelines_filtering.png)

###### Reload pipelines configuration

The logstash configuration can be reloaded directly from this view, with the help of the `Reload` button. Any changes to the configuration files used by logstash will be reloaded, without the need of restarting the service itself.

![](/media/media/07_network_probe/network_probes_page/pipelines/pipelines_reload.png)

In the case of enabling/disabling pipelines, this operation is performed automatically.

###### Enable/disable pipeline

Depending on the status of the pipeline, it can be enabled or disabled. This can be achieved either for each of them individually or using a multi-selector to select many at once (then all selected must have the same state).

![](/media/media/07_network_probe/network_probes_page/pipelines/pipelines_multi_start.png)

If one configuration file contains definitions for many pipelines at the same time, then, for example, despite selecting one, a given action will be performed for all pipelines defined in it, and an appropriate message will be displayed. Below is the message that will be displayed when clicking one of the 4 pipelines defined in the `aws.yml` file:

![](/media/media/07_network_probe/network_probes_page/pipelines/pipelines_start.png)

However, when stopping a single pipeline, the message may look like the following:

![](/media/media/07_network_probe/network_probes_page/pipelines/pipelines_stop.png)

##### Files Section

This section is used to handle files managed by the probe. Here you can create, update, or delete files, and in some cases check their validation results.

![](/media/media/07_network_probe/network_probes_page/files/files_list.png)

In the file table, we see information about the following:
- file - file's full path
- status - status indicates whether the file is being used by the pipeline. If the file resides within the `/etc/logstash/conf.d` directory and has a `.conf` extension, it can be either enabled or disabled.
- checksum - calculated checksum based on the file content
- revision - date of the latest file version

In the table, we can also see warnings in the form of yellow warning icons in the event of parsing errors in selected files, which will be described later.

###### Filtering and searching

Files can be filtered based on three parameters:
- `Valid`/`Invalid` - parsing correctness
- `Enabled`/`Disabled` - current operating status
- `Directory` - the directory in which they are located

However, in addition to filtering, the search functionality based on its content, a fragment of the access path, or its checksum may help in finding a specific file.

In the example below, a directory filter was used and all files containing the "5044" phrase entered in the search bar were found.

![](/media/media/07_network_probe/network_probes_page/files/files_filtering.png)

###### Create file

To create a new file, click the "New File" button. The file can be created in two ways: it can be created completely from scratch, or you can upload an existing file using the form in the lower left corner - the file name and its content will be uploaded. The available directories are directories managed by the probe - you cannot create a file in a place other than the allowed location.

![](/media/media/07_network_probe/network_probes_page/files/files_create_new.png)

###### Update file

A previously created file can also be edited. As with creation, a file can be overwritten by uploading an existing one, or individual elements of the file can be edited, (such as name, or content).

![](/media/media/07_network_probe/network_probes_page/files/files_edit_yaml.png)

###### Delete file

An existing file can be deleted using the button to the right of the table row.

![](/media/media/07_network_probe/network_probes_page/files/files_delete.png)

###### Enable/disable file

Pipeline configuration files can be either enabled or disabled. When a file is enabled it is being used by the corresponding pipeline. It can be disabled so that they are not taken into account, for example for testing purposes.

![](/media/media/07_network_probe/network_probes_page/files/files_enable_file.png)

A similar confirmation modal will appear for disabling the file operation.

###### Files parsing

If the file is located in logstash-related directories and has the extension `.conf`, it is parsed to check its correctness.

If the file cannot be parsed, a warning will appear in the list informing you about the error.

![](/media/media/07_network_probe/network_probes_page/files/files_list_with_warning.png)

The warning icon can be clicked to review the error message and correct it if possible. After clicking, the following modal will show up:

![](/media/media/07_network_probe/network_probes_page/files/files_details_modal_with_error.png)

In addition to the previously described `.conf` files, when `.yml` or `.yaml` files are created/edited, the built-in editor checks the correctness of the entered text, signaling any errors. If the file is incorrect, any creation or editing of the file will be blocked until the errors are corrected.

###### Files re-registration

Files can be re-registered using the "Re-register" button. Using this functionality refreshes all monitored files, while simultaneously parsing pipeline configuration files.

### Troubleshooting

#### Debugging

To check probe's logs:

  ```bash
  journalctl -fu license-service
  ```

By default, only errors and warnigs are logged. To change that, and enable for example `debug` level, set `log_level: DEBUG` in the `/opt/license-service/license-service.conf` file.

#### Restarting the probe

To restart the service enter:

  ```bash
  systemctl restart license-service
  ```

#### Removing already registered probe

1. If the probe is running stop the service:
    ```bash
    systemctl stop license-service
    ```
2. Open the "Network Probes" tab in the GUI and go into the details of the probe you are interested in.
3. After opening the details, copy the opened url and cut out the id located after the `/app/network_probe/probes/` section and the `/services` section. For example id extracted from url below is `f7fdb48bf5252cb41ab4162d96144a0d463b7ae5330bae6f37f501cb97fb272d199a59cc97bfdc1d2fd46e981ae42a8a59c66a40932c4bce27d786efe1f2dcc3`.

    ```
    https://127.0.0.1:5601/app/network_probe/probes/f7fdb48bf5252cb41ab4162d96144a0d463b7ae5330bae6f37f501cb97fb272d199a59cc97bfdc1d2fd46e981ae42a8a59c66a40932c4bce27d786efe1f2dcc3/services
    ```

4. Execute the following query, replacing `$ID` with the value obtained in the previous step, as well as `$USER` and `$PASSWORD` to elasticsearch:

   ```bash
   curl -u$USER:$PASSWORD -XDELETE '127.0.0.1:9200/.networkprobes/_doc/$ID'
   ```

#### Re-registering probe

If you have a problem with the probe and would like to re-register it, you have to:
1. Follow the steps in the previous section - [_Removing already registered probe_](#removing-already-registered-probe).
2. Remove the following file: `/opt/license-service/hashKeyKS.p12.network_probe`.
3. Start the probe:
    ```bash
    systemctl start license-service
    ```

The probe will be registered as a brand new one, if the license allows it and free slots are available.