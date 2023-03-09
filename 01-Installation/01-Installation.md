# Installation


## System Requirements

1. Supported Operating Systems

   -  Red Hat Linux 7.X
   -  Red Hat Linux 8.X
   -  Centos 7.X
   -  Centos 8.X
   -  Oracle Linux 8.X - Unbreakable Enterprise Kernel (UEK)
   -  Centos Stream
   -  AlmaLinux 8
   -  RockyLinux 8

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
       <td class="first last" rowspan="3">Elasticsearch</td>
       <td class="first last">9200</td>
       <td class="first last">TCP</td>
       <td class="first last">License verification through License Service</td>
     </tr>
     <tr class="row-even">
       <td class="first last">Integration source</td>
       <td class="first last">9200</td>
       <td class="first last">TCP</td>
       <td class="first last">Elasticsearch API</td>
     </tr>
     <tr class="row-odd">
       <td class="first last">Other cluster nodes</td>
       <td class="first last">9300</td>
       <td class="first last">TCP</td>
       <td class="first last">Elasticsearch transport</td>
     </tr>
     <tr class="row-even">
       <td class="first last" rowspan="3">User browser</td>
       <td class="first last" rowspan="3">Kibana</td>
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
- copy license to installation directory 
  'cp es_*.* install/'
- go to the installation directory (you can run install.sh script from any location)
- run installation script with interactive install command
`./install.sh -i`

During interactive installation you will be ask about following tasks:  
- install & configure Logstash with custom  Energy Logserver Configuration - like Beats, Syslog, Blacklist, Netflow, Wazuh, Winrm, Logtrail, OP5, etc;  
- install the  Energy Logserver Client Node, as well as the other client-node dependencies;  
- install the  Energy Logserver Data Node, as well as the other data-node dependencies;  
- load the  Energy Logserver custom dashboards, alerts and configs;  

### Non-interactive installation mode using "install.sh"

With the help of an install script, installation is possible without questions that require user interaction, which can be helpful with automatic deployment. In this case, you should provide options which components (data, client node) should be installed.

Example: 

`./install.sh -n -d` - will install only data node components. 

`./install.sh -n -c -d` - will install both - data and client node components.

### Check cluster/indices status and Elasticsearch version

    Invoke curl command to check the status of Elasticsearch:

    ```bash
    curl -s -u $CREDENTIAL localhost:9200/_cluster/health?pretty
    {
      "cluster_name" : "elasticsearch",
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
      "cluster_name" : "elasticsearch",
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

- configure  Elasticsearch cluster settings

  ```bash
  vi /etc/elaticserach/elasticsearch.yml
  ```

  - add all IPs of Elasticsearch node in the following directive:

    ```bash
    discovery.seed_hosts: [ "172.10.0.1:9300", "172.10.0.2:9300" ]
    ```

- start Elasticsearch service

  ```bash
  systemc	start elasticsearch
  ```

- start Logstash service

  ```bash
  systemctl start logstash
  ```

- start Cerebro service

  ```bash
  systemctl start cerebro
  ```

- start  Kibana service

  ```bash
  systemctl start kibana
  ```

- start Alert service

  ```bash
  systemctl start alert
  ```

- start Skimmer service

  ```bash
  systemctl start skimmer
  ```

- Example agent configuration files and additional documentation can be found in the Agents directory:

  - filebeat
  - winlogbeat
  - op5 naemon logs
  - op5 perf_data

- For blacklist creation, you can use crontab or kibana scheduler, but the most preferable method is logstash input. Instructions to set it up can be found at `logstash/lists/README.md`

- It is recomended to make small backup of system indices - copy "configuration-backup.sh" script from Agents directory to desired location, and change `backupPath=` to desired location. Then set up a crontab: 

  ```bash
  0 1 * * * /path/to/script/configuration-backup.sh
  ```

- Redirect Kibana port 5601/TCP to 443/TCP

  ```bash
  firewall-cmd --zone=public --add-masquerade --permanent
  firewall-cmd --zone=public --add-forward-port=port=443:proto=tcp:toport=5601 --permanent
  firewall-cmd --reload
  ```

   \# NOTE: Kibana on 443 tcp port *without* redirection needs additional permissions:

  ```bash
  setcap 'CAP_NET_BIND_SERVICE=+eip' /usr/share/kibana/node/bin/node
  ```

- Cookie TTL and Cookie Keep Alive - for better work comfort, you can set two new variables in the Kibana configuration file `/etc/kibana/kibana.yml`:

  ```bash
  login.cookiettl: 10
  login.cookieKeepAlive: true
  ```

  CookieTTL is the value in minutes of the cookie's lifetime. The cookieKeepAlive renews this time with every valid query made by browser clicks.

  After saving changes in the configuration file, you must restart the service:

  ```bash
  systemctl restart kibana
  ```

### Scheduling bad IP lists update

Requirements:

- Make sure you have Logstash 6.4 or newer.
- Enter your credentials into scripts: misp_threat_lists.sh

To update bad reputation lists and to create `.blacklists` index, you have to run misp_threat_lists.sh script (best is to put in schedule).

1. This can be done in cron (host with logstash installed) in /etc/crontab:

  ```bash
  0 2 * * * logstash /etc/logstash/lists/bin/misp_threat_lists.sh
  ```

2. Or with Kibana Scheduller app (**only if logstash is running on the same host**).

  - Prepare script path:

  ```bash
  /bin/ln -sfn /etc/logstash/lists/bin /opt/ai/bin/lists
  chown logstash:kibana /etc/logstash/lists/
  chmod g+w /etc/logstash/lists/
  ```

  - Log in to GUI and go to **Scheduler** app. Set it up with below options and push "Submit" button:

  ```bash
  Name:           MispThreatList
  Cron pattern:   0 2 * * *
  Command:        lists/misp_threat_lists.sh
  Category:       logstash

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
      - data01:/usr/share/elasticsearch/data
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
      - data02:/usr/share/elasticsearch/data
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
      - data03:/usr/share/elasticsearch/data
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
  elastic:
    driver: bridge
```

## Custom installation the Energy Logserver ##

If you need to install Energy Logserver in non-default location, use the following steps.

1. Define the variable INSTALL_PATH if you do not want default paths like "/"

		export INSTALL_PATH="/"

1. Install the firewalld service

		yum install firewalld

1. Configure the firewalld service

		systemctl enable firewalld
		systemctl start firewalld
		firewall-cmd --zone=public --add-port=22/tcp --permanent
		firewall-cmd --zone=public --add-port=443/tcp --permanent
		firewall-cmd --zone=public --add-port=5601/tcp --permanent
		firewall-cmd --zone=public --add-port=9200/tcp --permanent
		firewall-cmd --zone=public --add-port=9300/tcp --permanent
		firewall-cmd --reload

1. Install and enable the epel repository

		yum install epel-release

1. Install the Java OpenJDK

		yum install java-1.8.0-openjdk-headless.x86_64

1. Install the reports dependencies, e.g. for mail and fonts

		yum install fontconfig freetype freetype-devel fontconfig-devel libstdc++ urw-fonts net-tools ImageMagick ghostscript poppler-utils

1. Create the nessesery users acounts

		useradd -M -d ${INSTALL_PATH}/usr/share/kibana -s /sbin/nologin kibana
		useradd -M -d ${INSTALL_PATH}/usr/share/elasticsearch -s /sbin/nologin elasticsearch
		useradd -M -d ${INSTALL_PATH}/opt/alert -s /sbin/nologin alert

1. Remove .gitkeep files from source directory

		find . -name ".gitkeep" -delete

1. Install the Elasticsearch 6.2.4 files

		/bin/cp -rf elasticsearch/elasticsearch-6.2.4/* ${INSTALL_PATH}/

1. Install the Kibana 6.2.4 files

		/bin/cp -rf kibana/kibana-6.2.4/* ${INSTALL_PATH}/

1. Configure the Elasticsearch system dependencies

		/bin/cp -rf system/limits.d/30-elasticsearch.conf /etc/security/limits.d/
		/bin/cp -rf system/sysctl.d/90-elasticsearch.conf /etc/sysctl.d/
		/bin/cp -rf system/sysconfig/elasticsearch /etc/sysconfig/
		/bin/cp -rf system/rsyslog.d/intelligence.conf /etc/rsyslog.d/
		echo -e "RateLimitInterval=0\nRateLimitBurst=0" >> /etc/systemd/journald.conf
		systemctl daemon-reload
		systemctl restart rsyslog.service
		sysctl -p /etc/sysctl.d/90-elasticsearch.conf

1. Configure the SSL Encryption for the Kibana

		mkdir -p ${INSTALL_PATH}/etc/kibana/ssl
		openssl req -x509 -nodes -days 365 -newkey rsa:2048 -sha256 -subj '/CN=LOGSERVER/subjectAltName=LOGSERVER/' -keyout ${INSTALL_PATH}/etc/kibana/ssl/kibana.key -out ${INSTALL_PATH}/etc/kibana/ssl/kibana.crt

1. Install the Elasticsearch-auth plugin

		cp -rf elasticsearch/elasticsearch-auth ${INSTALL_PATH}/usr/share/elasticsearch/plugins/elasticsearch-auth

1. Install the Elasticsearh configuration files

		/bin/cp -rf elasticsearch/*.yml ${INSTALL_PATH}/etc/elasticsearch/

1. Install the Elasticsicsearch system indices

		mkdir -p ${INSTALL_PATH}/var/lib/elasticsearch
		/bin/cp -rf elasticsearch/nodes ${INSTALL_PATH}/var/lib/elasticsearch/

1.  Add necessary permission for the Elasticsearch directories

		chown -R elasticsearch:elasticsearch ${INSTALL_PATH}/usr/share/elasticsearch ${INSTALL_PATH}/etc/elasticsearch ${INSTALL_PATH}/var/lib/elasticsearch ${INSTALL_PATH}/var/log/elasticsearch

1. Install the Kibana plugins 

		cp -rf kibana/plugins/* ${INSTALL_PATH}/usr/share/kibana/plugins/

1. Extrace the node_modules for plugins and remove archive

		tar -xf ${INSTALL_PATH}/usr/share/kibana/plugins/node_modules.tar -C ${INSTALL_PATH}/usr/share/kibana/plugins/
		/bin/rm -rf ${INSTALL_PATH}/usr/share/kibana/plugins/node_modules.tar

1. Install the Kibana reports binaries

		cp -rf kibana/export_plugin/* ${INSTALL_PATH}/usr/share/kibana/bin/

1. Create directory for the Kibana reports

		/bin/cp -rf kibana/optimize ${INSTALL_PATH}/usr/share/kibana/

1. Install the python dependencies for reports

		tar -xf kibana/python.tar -C /usr/lib/python2.7/site-packages/

1. Install the Kibana custom sources

		/bin/cp -rf kibana/src/* ${INSTALL_PATH}/usr/share/kibana/src/

1. Install the Kibana configuration

		/bin/cp -rf kibana/kibana.yml ${INSTALL_PATH}/etc/kibana/kibana.yml

1. Generate the iron secret salt for Kibana

		echo "server.ironsecret: \"$(</dev/urandom tr -dc _A-Z-a-z-0-9 | head -c32)\"" >> ${INSTALL_PATH}/etc/kibana/kibana.yml

1. Remove old cache files

		rm -rf ${INSTALL_PATH}/usr/share/kibana/optimize/bundles/*

1. Install the Alert plugin

		mkdir -p ${INSTALL_PATH}/opt
		/bin/cp -rf alert ${INSTALL_PATH}/opt/alert

1. Install the AI plugin
	
		/bin/cp -rf ai ${INSTALL_PATH}/opt/ai

1. Set the proper permissions

		chown -R elasticsearch:elasticsearch ${INSTALL_PATH}/usr/share/elasticsearch/
		chown -R alert:alert ${INSTALL_PATH}/opt/alert
		chown -R kibana:kibana ${INSTALL_PATH}/usr/share/kibana ${INSTALL_PATH}/opt/ai ${INSTALL_PATH}/opt/alert/rules ${INSTALL_PATH}/var/lib/kibana
		chmod -R 755 ${INSTALL_PATH}/opt/ai
		chmod -R 755 ${INSTALL_PATH}/opt/alert

1. Install service files for the Alert, Kibana and the Elasticsearch

		/bin/cp -rf system/alert.service /usr/lib/systemd/system/alert.service
		/bin/cp -rf kibana/kibana-6.2.4/etc/systemd/system/kibana.service /usr/lib/systemd/system/kibana.service
		/bin/cp -rf elasticsearch/elasticsearch-6.2.4/usr/lib/systemd/system/elasticsearch.service /usr/lib/systemd/system/elasticsearch.service

1. Set property paths in service files ${INSTALL_PATH}

		perl -pi -e 's#/opt#'${INSTALL_PATH}'/opt#g' /usr/lib/systemd/system/alert.service
		perl -pi -e 's#/etc#'${INSTALL_PATH}'/etc#g' /usr/lib/systemd/system/kibana.service
		perl -pi -e 's#/usr#'${INSTALL_PATH}'/usr#g' /usr/lib/systemd/system/kibana.service
		perl -pi -e 's#ES_HOME=#ES_HOME='${INSTALL_PATH}'#g' /usr/lib/systemd/system/elasticsearch.service
		perl -pi -e 's#ES_PATH_CONF=#ES_PATH_CONF='${INSTALL_PATH}'#g' /usr/lib/systemd/system/elasticsearch.service
		perl -pi -e 's#ExecStart=#ExecStart='${INSTALL_PATH}'#g' /usr/lib/systemd/system/elasticsearch.service

1. Enable the system services

		systemctl daemon-reload
		systemctl reenable alert
		systemctl reenable kibana
		systemctl reenable elasticsearch


1. Set location for Elasticsearch data and logs files in configuration file

	- Elasticsearch

			perl -pi -e 's#path.data: #path.data: '${INSTALL_PATH}'#g' ${INSTALL_PATH}/etc/elasticsearch/elasticsearch.yml
			perl -pi -e 's#path.logs: #path.logs: '${INSTALL_PATH}'#g' ${INSTALL_PATH}/etc/elasticsearch/elasticsearch.yml
			perl -pi -e 's#/usr#'${INSTALL_PATH}'/usr#g' ${INSTALL_PATH}/etc/elasticsearch/jvm.options
			perl -pi -e 's#/usr#'${INSTALL_PATH}'/usr#g' /etc/sysconfig/elasticsearch

	- Kibana

			perl -pi -e 's#/etc#'${INSTALL_PATH}'/etc#g' ${INSTALL_PATH}/etc/kibana/kibana.yml
			perl -pi -e 's#/opt#'${INSTALL_PATH}'/opt#g' ${INSTALL_PATH}/etc/kibana/kibana.yml
			perl -pi -e 's#/usr#'${INSTALL_PATH}'/usr#g' ${INSTALL_PATH}/etc/kibana/kibana.yml

	- AI

			perl -pi -e 's#/opt#'${INSTALL_PATH}'/opt#g' ${INSTALL_PATH}/opt/ai/bin/conf.cfg



1. What next ?

	- Upload License file to ${INSTALL_PATH}/usr/share/elasticsearch/directory.

	- Setup cluster in ${INSTALL_PATH}/etc/elasticsearch/elasticsearch.yml
		
    ```yml
			discovery.zen.ping.unicast.hosts: [ "172.10.0.1:9300", "172.10.0.2:9300" ] 
    ```

	- Redirect GUI to 443/tcp
   
   ```bash	      
	  firewall-cmd --zone=public --add-masquerade --permanent
	  firewall-cmd --zone=public --add-forward-port=port=443:proto=tcp:toport=5601 --permanent
	  firewall-cmd --reload
   ```

## ROOTless setup

To configure Energy Logserver so its services can be managed without root access follow these steps:

1. Create a file in `/etc/sudoers.d` (eg.: 10-logserver) with the content

   ```bash
      %kibana ALL=/bin/systemctl status kibana
    	%kibana ALL=/bin/systemctl status kibana.service
    	%kibana ALL=/bin/systemctl stop kibana
    	%kibana ALL=/bin/systemctl stop kibana.service
    	%kibana ALL=/bin/systemctl start kibana
    	%kibana ALL=/bin/systemctl start kibana.service
    	%kibana ALL=/bin/systemctl restart kibana
    	%kibana ALL=/bin/systemctl restart kibana.service
    	

    	%elasticsearch ALL=/bin/systemctl status elasticsearch
    	%elasticsearch ALL=/bin/systemctl status elasticsearch.service
    	%elasticsearch ALL=/bin/systemctl stop elasticsearch
    	%elasticsearch ALL=/bin/systemctl stop elasticsearch.service
    	%elasticsearch ALL=/bin/systemctl start elasticsearch
    	%elasticsearch ALL=/bin/systemctl start elasticsearch.service
    	%elasticsearch ALL=/bin/systemctl restart elasticsearch
    	%elasticsearch ALL=/bin/systemctl restart elasticsearch.service
    	
    	%alert ALL=/bin/systemctl status alert
    	%alert ALL=/bin/systemctl status alert.service
    	%alert ALL=/bin/systemctl stop alert
    	%alert ALL=/bin/systemctl stop alert.service
    	%alert ALL=/bin/systemctl start alert
    	%alert ALL=/bin/systemctl start alert.service
    	%alert ALL=/bin/systemctl restart alert
    	%alert ALL=/bin/systemctl restart alert.service
    	
    	%logstash ALL=/bin/systemctl status logstash
    	%logstash ALL=/bin/systemctl status logstash.service
    	%logstash ALL=/bin/systemctl stop logstash
    	%logstash ALL=/bin/systemctl stop logstash.service
    	%logstash ALL=/bin/systemctl start logstash
    	%logstash ALL=/bin/systemctl start logstash.service
     	%logstash ALL=/bin/systemctl restart logstash
    	%logstash ALL=/bin/systemctl restart logstash.service
   ```
   
2. Change permissions for files and directories

  - Kibana, Elasticsearch, Alert

     ```bash
     chmod g+rw /etc/kibana/kibana.yml /opt/alert/config.yaml /opt/ai/bin/conf.cfg /etc/elasticsearch/{elasticsearch.yml,jvm.options,log4j2.properties,properties.yml,role-mappings.yml}
     chmod g+rwx /etc/kibana/ssl /etc/elasticsearch/ /opt/{ai,alert} /opt/ai/bin
     chown -R elasticsearch:elasticsearch /etc/elasticsearch/
     chown -R kibana:kibana /etc/kibana/ssl
     ```
  - Logstash

    ```bash
    find /etc/logstash -type f -exec chmod g+rw {} \;
    find /etc/logstash -type d -exec chmod g+rwx {} \;
    chown -R logstash:logstash /etc/logstash
    ```

3. Add a user to groups defined earlier


    ```bash
    usermod -a -G kibana,alert,elasticsearch,logstash service_user
    ```


    From now on this user should be able to start/stop/restart services and modify configurations files.
