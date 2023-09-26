#!/usr/bin/env bash
curl -k -u username:password -H "Content-Type: application/xml" -X POST "http://xxx.xxx.xxx.xxx:50105/?????????" -d {
"CEF":"0","Server":"EnergyLogServer","Version":"${19}","NameEvent":"${18}","TimeStamp":"$1","DeviceVendor/Product":"$2-$3","Message""$4","TransportProtocol":"$5","Aggregated":"$6","AttackerAddress":"$7","AttackerMAC":"$8","AttackerPort":"$9","TargetMACAddress":"${10}","TargetPort":"${11}","TargetAddress":"${12}","FlexString1":"${13}","Link":"${14}","EventID":"${15}","EventTime":"${16}","RawEvent":"${17}"
}