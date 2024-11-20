# MSSP licensing
The **MSSP** mode allows the user to effectively manage sources collected throughout the system. The source can be defined as a host providing data to the system. When the **MSSP** mode is enabled, sources are continuously gathered and monitored so they can be displayed in an understandable way.

## Collecting Sources
The sources are collected in two ways - by the `Network Probe` or the `Logserver` itself.
The `Network Probe` utilizes a unique set of fields against documents of different technologies, to be able to generate an inimitable identifier. This makes it possible to determine from which source the data came and therefore also to manage the system's traffic.

## Managing Sources
Only admin-level users can manage sources in the **Config** plugin. For such users, it displays the **Sources** tab in the side navigation bar, the **Sources** tab in the **Config** plugin, and a blue banner at the top of the screen.

![Source bar](/media/media/13_mssp/bar_sources_b.png)
*Sources tab in the navigation bar*

![Sources config](/media/media/13_mssp/sources_config.png)          
*Sources tab in the Config plugin*

![Blue bar](/media/media/13_mssp/blue_bar.png)
*Blue banner*

## Source types
Two states of sources can be distinguished - `Waiting` and `Allowed`.

![Blue bar](/media/media/13_mssp/sources_type.png)  
*Sources types*

### 1. Waiting
The `waiting` source is a source pending approval. Data related to this source will not be ingested until it is accepted. Only the first document from a given **source** is collected and stored as an example. Its details include information such as when it was indexed, the source from where it was sent, and its contents. In addition, a note can be added to distinguish it from other **sources** and describe it in a memorable way.

![Details](/media/media/13_mssp/details_view.png)

### 2. Allowed
When a `Waiting` document is `Allowed`, the flow of its data is made possible.

### Source removal
Both types of sources can be removed. After deleting the `waiting` source, if the data is still coming in, after a brief moment the source will reappear in the table with the possibility of possible acceptance. On the other hand, if an `allowed` source is deleted, the data will stop coming in, although the data collected up to the time of deletion will not be cleared.

### Manual change of state from `Waiting` to `Allowed`

1. Check the box of the sources which you want to move from `Waiting` to `Allowed` state.
   
2. Press on the button `Allow`.

    ![Manual allow](/media/media/13_mssp/manual_allow.png)

3. A details of the operation will be displayed. If you still want to perform the operation, press `Yes, allow` button.

    ![Manual yes, allow](/media/media/13_mssp/manual_allow2.png)

### Manual change of state from `Allowed` to `Waiting`
1. Go to the `Allowed` tab. 
2. Check the box of the sources which you want to move from `Allowed` to `Waiting` list.
3. Press on the button `Delete`.

    ![Manual delete](/media/media/13_mssp/manual_delete.png)

4. Details of the operation will appear. If you still want to perform the operation, press `Yes, delete` button. 

    ![Manual delete 2](/media/media/13_mssp/manual_delete_2.png)

## Fingerprint
The `Network Probe` generates a unique identifier for each document called a **fingerprint** in the `_mssp_id` field. **Fingerprint** is encrypted data from the document. Sources without **fingerprints** are automatically dropped. Sources whose **fingerprints** cannot be decrypted are placed on a waiting list but without the possibility of being allowed. Documents with valid **fingerprints** are placed on a waiting list with the possibility of approval until the license limit is reached.

## The Permissive Mode
The **Permissive Mode** is enabled out of the box. It automatically allows waiting **sources** until the license limit is completely used. If all available **sources** have been used, no others will be accepted, which is also indicated by the blue banner changing to orange with a warning. The purpose of this transition is to draw the user’s attention to checking whether all allowed **sources** are still being used. If so, it means that a licence covering more **sources** should be purchased.

![Orange bar](/media/media/13_mssp/warning_bar.png)
*Orange banner*

It was introduced to make it easier to use the system, without having to worry and remember about source management. On the other hand, if there is a need to allow or remove troublesome or erroneous **sources** manually, it is always possible to disable this mode and perform manual operations.

### Turn on/off the `Permissive Mode`

1. Go to the **Sources** tab. 
2. Toggle the switch located on the blue bar captioned `Permissive Mode` to the state in which you want it to work.
    ![Permissive switch](/media/media/13_mssp/permissive_mode.png)

### Check MSSP status

1. Go to the **Config** tab in the navigation bar.
2. Select **Licence** section in the top bar.
3. The value of the `MSSP` field in **Licence Details** indicates the status of the module. 
    ![Mssp license](/media/media/13_mssp/mssp_license.png)

### MSSP disabled
However, when `MSSP` mode is disabled, the system still gathers information about sources based on documents, but it does not block or reject any incoming documents. A list of sources can still be viewed in the `Config`->`Sources` tab.