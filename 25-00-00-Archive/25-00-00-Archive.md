# Archive

The Archive module allows you to create compressed data files ([zstd](https://github.com/facebook/zstd)) from Elasticsearch indexes. The archive checks the age of each document in the index and if it is older than defined in the job, it is copied to the archive file.

## Configuration

### Enabling module

To configure module edit `kibana.yml` configuration file end set path to the archive directory - location where the archive files will be stored:

```bash
vim /etc/kibana/kibana.yml
```

remove the comment from the following line and set the correct path to the archive directory:

```vim
archive.archivefolderpath: '/var/lib/elastic_archive_test'
```

## Create Archive task

1. From the main naviagation go to the "Archvie" modue.

   ![](/media/media/image154.png) 

2. On the "Archive" tab select "Create Task" and define the following parameters:

   - `Index pattern`- for the indexes that will be archive, for example `syslog*` ;
   - `Older than (days)` - number of days after which documents will be archived;
   - Schedule task (crontab format) - 