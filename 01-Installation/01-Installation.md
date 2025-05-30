# Installation

## System Requirements

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
     <tr class="row-even">
       <td class="first last" rowspan="3">Siem Agent</td>
       <td class="first last" rowspan="7">Siem service</td>
       <td class="first last">1514</td>
       <td class="first last">TCP (default)</td>
       <td class="first last">Agent connection service</td>
     </tr>
     <tr class="row-odd">
       <td class="first last">1514</td>
       <td class="first last">UDP (optional)</td>
       <td class="first last">Agent connection service (disabled by default)</td>
     </tr>
     <tr class="row-even">
       <td class="first last">1515</td>
       <td class="first last">TCP</td>
       <td class="first last">Agent enrollment service</td>
     </tr>
     <tr class="row-odd">
       <td class="first last">Siem service</td>
       <td class="first last">1516</td>
       <td class="first last">TCP</td>
       <td class="first last">Siem cluster daemon</td>
     </tr>
     <tr class="row-even">
       <td class="first last" rowspan="2">Source</td>
       <td class="first last">****</td>
       <td class="first last">UDP (default)</td>
       <td class="first last">Siem Syslog collector (disabled by default)</td>
     </tr>
     <tr class="row-odd">
       <td class="first last">****</td>
       <td class="first last">TCP (optional)</td>
       <td class="first last">Siem Syslog collector (disabled by default)</td>
     </tr>
     <tr class="row-even">
       <td class="first last">Siem service</td>
       <td class="first last">55000</td>
       <td class="first last">TCP</td>
       <td class="first last">Siem server RESTful API</td>
     </tr>
     <tr class="row-odd">
       <td class="first last">Every ELS component</td>
       <td class="first last" rowspan="3">Data Node</td>
       <td class="first last">9200</td>
       <td class="first last">TCP</td>
       <td class="first last">License verification through License Service</td>
     </tr>
     <tr class="row-even">
       <td class="first last">Integration source</td>
       <td class="first last">9200</td>
       <td class="first last">TCP</td>
       <td class="first last">Data Node API</td>
     </tr>
     <tr class="row-odd">
       <td class="first last">Other cluster nodes</td>
       <td class="first last">9300</td>
       <td class="first last">TCP</td>
       <td class="first last">Data Node transport</td>
     </tr>
     <tr class="row-even">
       <td class="first last" rowspan="3">User browser</td>
       <td class="first last" rowspan="3">Logserver GUI</td>
       <td class="first last">5601</td>
       <td class="first last">TCP</td>
       <td class="first last">Default GUI</td>
     </tr>
     <tr class="row-odd">
       <td class="first last">5602</td>
       <td class="first last">TCP</td>
       <td class="first last">Admin console</td>
     </tr>
     <tr class="row-even">
       <td class="first last">5603</td>
       <td class="first last">TCP</td>
       <td class="first last">Wiki GUI</td>
     </tr>
    <td>GUI</td>
    <td>License Service</td>
    <td>9000</td>
    <td>TCP</td>
    <td>Manage files, services and pipelines.</td>
   </tbody>
   </table>

## Installation method

The Energy Logserver installer is delivered as:

- RPM package energy-logserver-data-node and energy-logserver-client-node,
- "install.sh" installation script

### Interactive installation using "install.sh"

The Energy Logserver comes with simple installation script called `install.sh`. It is designed to facilitate the installation and deployment process of our product. After running (execute) the script, it will detect supported distribution and by default it will ask incl. about the components we want to install. The script is located in the `"install"`directory.

The installation process:

- unpack the archive containing the installer
`tar xjf energy-logserver-${product-version}.x.x86_64.tar.bz2`
- unpack the archive containing the SIEM installer (only in SIEM plan)
`tar xjf energy-logserver-siem-plan-${product-version}.x.x86_64.tar.bz2`
- copy license to installation directory \
  `cp es_*.* install/`
- go to the installation directory (you can run install.sh script from any location)
- run installation script with interactive install command \
   `./install.sh -i`

During interactive installation you will be ask about following tasks:

- install & configure Network Probe with custom  Energy Logserver Configuration - like Beats, Syslog, Blacklist, Netflow, Winrm, Logtrail, OP5, etc;
- install the  Energy Logserver Client Node, as well as the other client-node dependencies;
- install the  Energy Logserver Data Node, as well as the other data-node dependencies;
- load the  Energy Logserver custom dashboards, alerts and configs;

### Non-interactive installation mode using "install.sh"

With the help of an install script, installation is possible without questions that require user interaction, which can be helpful with automatic deployment. In this case, you should provide options which components (data, client node) should be installed.

Example:

`./install.sh -n -d` - will install only data node components.

`./install.sh -n -c -d` - will install both - data and client node components.

### Check cluster/indices status and Data Node version

Invoke curl command to check the status of Data Node:

```bash
    curl -s -u $CREDENTIAL localhost:9200/_cluster/health?pretty

    {
      "cluster_name" : "logserver",
      "status" : "green",
      "timed_out" : false,
      "number_of_nodes" : 1,
      "number_of_data_nodes" : 1,
      "active_primary_shards" : 25,
      "active_shards" : 25,
      "relocating_shards" : 0,
      "initializing_shards" : 0,
      "unassigned_shards" : 0,
      "delayed_unassigned_shards" : 0,
      "number_of_pending_tasks" : 0,
      "number_of_in_flight_fetch" : 0,
      "task_max_waiting_in_queue_millis" : 0,
      "active_shards_percent_as_number" : 100.0
    }
```

```bash
    curl -s -u $CREDENTIAL localhost:9200

    {
      "name" : "node-1",
      "cluster_name" : "logserver",
      "cluster_uuid" : "igrASEDRRamyQgy-zJRSfg",
      "version" : {
        "number" : "7.3.2",
        "build_flavor" : "oss",
        "build_type" : "rpm",
        "build_hash" : "1c1faf1",
        "build_date" : "2019-09-06T14:40:30.409026Z",
        "build_snapshot" : false,
        "lucene_version" : "8.1.0",
        "minimum_wire_compatibility_version" : "6.8.0",
        "minimum_index_compatibility_version" : "6.0.0-beta1"
      },
      "tagline" : "You Know, for Search"
    }
```

If everything went correctly, we should see 100% allocated shards in  cluster health.

### Generating basic system information report

The `install.sh` script also contains functions for collecting basic information about the system environment - such information can be helpful in the support process or troubleshooting. Note that you can redirect output (`STDOUT`) to external file.

Example:

`./install.sh -s > system_report.txt`

### "install.sh" command list

Run `install.sh --help` to see information about builtin commands and options.

```bash
Usage: install.sh {COMMAND} {OPTIONS}

COMMAND is one of:
    -i|install                  Run Energy Logserver installation wizard.
    -n|noninteractive           Run Energy Logserver installation in non interactive mode.
    -u|upgrade                  Update Energy Logserver packages.
    -s|systeminfo               Get basic system information report.

OPTIONS if one of:
    -v|--verbose                Run commands with verbose flag.
    -d|--data                   Select data node installation for   non interactive mode.
    -c|--client                 Select client node installation for non interactive mode.
```

### Post installation steps

- configure Data Node cluster settings

  ```bash
  vi /etc/logserver/logserver.yml
  ```

  - add all IPs of Data Nodes in the following directive:

    ```bash
    discovery.seed_hosts: [ "172.10.0.1:9300", "172.10.0.2:9300" ]
    ```

- start Data Node service with systemctl start command

- **Example**:
  ```bash
  systemctl start logserver
  ```

- start Network Probe service with systemctl start command

- start Cerebro service with systemctl start command

- start Logserver GUI service with systemctl start command

- **Example**: ```bash
  systemctl start logserver-gui
  ```
- start Alert service with systemctl start command

- **Example**:
  ```bash
  systemctl start alert
  ```

- start Skimmer service with systemctl start command

- **Example**:
  ```bash
  systemctl start skimmer
  ```

- Example agent configuration files and additional documentation can be found in the Agents directory:

  - filebeat
  - winlogbeat
  - op5 naemon logs
  - op5 perf_data

- For blacklist creation, you can use crontab or Logserver GUI scheduler, but the most preferable method is Network Probe input. Instructions to set it up can be found at `logserver-probe/lists/README.md`

- It is recomended to make small backup of system indices - copy "configuration-backup.sh" script from Agents directory to desired location, and change `backupPath=` to desired location. Then set up a crontab:

  ```bash
  0 1 * * * /path/to/script/configuration-backup.sh
  ```

- Redirect Logserver GUI port 5601/TCP to 443/TCP

  ```bash
  firewall-cmd --zone=public --add-masquerade --permanent
  firewall-cmd --zone=public --add-forward-port=port=443:proto=tcp:toport=5601 --permanent
  firewall-cmd --reload
  ```

   \# NOTE: Logserver GUI on 443 tcp port *without* redirection needs additional permissions:

  ```bash
  setcap 'CAP_NET_BIND_SERVICE=+eip' /usr/share/logserver-gui/node/bin/node
  ```

- Cookie TTL and Cookie Keep Alive - for better work comfort, you can set two new variables in the Logserver GUI configuration .yml file `/etc/logserver-gui/`:

  ```bash
  login.cookiettl: 10
  login.cookieKeepAlive: true
  ```

  CookieTTL is the value in minutes of the cookie's lifetime. The cookieKeepAlive renews this time with every valid query made by browser clicks.

  After saving changes in the configuration file, you must restart the logserver GUI service with systemctl restart command

### Scheduling bad IP lists update

Requirements:

- Make sure you have Logserver 7.0 or newer.
- Enter your credentials into scripts: misp_threat_lists.sh

To update bad reputation lists and to create `.blacklists` index, you have to run misp_threat_lists.sh script (best is to put in schedule).

1. This can be done in cron (host with Network Probe installed) in /etc/crontab:

   ```bash
   0 2 * * * user /etc/logserver-probe/lists/bin/misp_threat_lists.sh
   ```

2. Or with Logserver GUI Scheduller app (**only if Network Probe is running on the same host**).

   - Prepare script path:

   ```bash
   /bin/ln -sfn /etc/logserver-probe/lists/bin /opt/ai/bin/lists
   chown user:group /etc/logserver-probe/lists/
   chmod g+w /etc/logserver-probe/lists/
   ```

   - Log in to Logserver GUI and go to **Scheduler** app. Set it up with below options and push "Submit" button:

   ```bash
   Name:           MispThreatList
   Cron pattern:   0 2 * * *
   Command:        lists/misp_threat_lists.sh
   Category:       network-probe
   ```

3. After a couple of minutes check for blacklists index:

   ```bash
   curl -sS -u logserver:logserver -XGET '127.0.0.1:9200/_cat/indices/.blacklists?s=index&v'

   health status index       uuid                   pri rep docs.count docs.deleted store.size pri.store.size
   green  open   .blacklists Mld2Qe2bSRuk2VyKm-KoGg   1   0      76549            0      4.7mb          4.7mb
   ```

### Web Application Firewall requriments

The Energy Logserver GUI requires the following request parameters to be allowed in WAF:

- URI Length: 2048 characters,
- Cookie Number In Request: 16,
- Header Number In Request: 50,
- Request Header Name Length: 1024 characters,
- Request Header Value Length: 4096 characters,
- URL Parameter Name Length: 1024 characters,
- URL Parameter Value Length: 4096 characters,
- Request Header Length: 8192 bytes,
- Request Body Length: 67108864 bytes.

## Docker support

To get system cluster up and running in Docker, you can use Docker Compose.

Sample a `docker-compose.yml` file:

```bash
version: '7.1.0'
services:
  energy-logserver-client-node:
    image: docker.emca.pl/energy-logserver-client-node:7.1.0
    container_name: energy-logserver-client-node
    environment:
      - node.name=energy-logserver-client-node
      - cluster.name=logserver
      - discovery.seed_hosts=energy-logserver-client-node,energy-logserver-data-node,energy-logserver-collector-node
      - cluster.initial_master_nodes=energy-logserver-client-node,energy-logserver-data-node,energy-logserver-collector-node
      - bootstrap.memory_lock=true
      - "ES_JAVA_OPTS=-Xms1024m -Xmx1024m"
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - data01:/usr/share/logserver/data
    ports:
      - 9200:9200
    networks:
      - logserver
  energy-logserver-data-node:
    image: docker.emca.pl/energy-logserver-client-node:7.1.0
    container_name: energy-logserver-data-node
    environment:
      - node.name=energy-logserver-data-node
      - cluster.name=logserver
      - discovery.seed_hosts=energy-logserver-client-node,energy-logserver-data-node,energy-logserver-collector-node
      - cluster.initial_master_nodes=energy-logserver-client-node,energy-logserver-data-node,energy-logserver-collector-node
      - bootstrap.memory_lock=true
      - "ES_JAVA_OPTS=-Xms1024m -Xmx1024m"
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - data02:/usr/share/logserver/data
    networks:
      - logserver
  energy-logserver-collector-node:
    image: docker.emca.pl/energy-logserver-collector-node:7.1.0
    container_name: energy-logserver-collector-node
    environment:
      - node.name=energy-logserver-collector-node
      - cluster.name=logserver
      - discovery.seed_hosts=energy-logserver-client-node,energy-logserver-data-node,energy-logserver-collector-node
      - cluster.initial_master_nodes=energy-logserver-client-node,energy-logserver-data-node,energy-logserver-collector-node
      - bootstrap.memory_lock=true
      - "ES_JAVA_OPTS=-Xms1024m -Xmx1024m"
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - data03:/usr/share/logserver/data
    networks:
      - logserver

volumes:
  data01:
    driver: local
  data02:
    driver: local
  data03:
    driver: local

networks:
  logserver:
    driver: bridge
```