## About the connector
Bitsight is a global cyber risk management leader transforming how companies manage exposure, performance, and risk for themselves and their third parties.
<p>This document provides information about the Bitsight Connector, which facilitates automated interactions, with a Bitsight server using FortiSOAR&trade; playbooks. Add the Bitsight Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Bitsight.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-bitsight</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Bitsight server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Bitsight server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Bitsight</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the URL of Bitsight server to connect and perform the automated operations.
</td>
</tr><tr><td>API Token</td><td>Specify the API token to access the Bitsight server to connect and perform the automated operations.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>
## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Alerts</td><td>Retrieves the detailed list of alerts based on the parameters that you have specified.</td><td>get_alerts <br/>Investigation</td></tr>
<tr><td>Get Companies With Exposed Credentials</td><td>Retrieves the detailed list of companies with exposed credentials in you portfolio based on the parameters that you have specified.</td><td>get_companies_with_exposed_credentials <br/>Investigation</td></tr>
<tr><td>Get Credentials Leaks Affecting Your Portfolio</td><td>Retrieves the detailed list of credentials leaks affecting your portfolio based on the parameters that you have specified.</td><td>get_credentials_leaks <br/>Investigation</td></tr>
<tr><td>Get Threat Evidence</td><td>Retrieves the detailed list of threat evidence based on the parameters that you have specified.</td><td>get_threat_evidence <br/>Investigation</td></tr>
<tr><td>Get Portfolio Threats</td><td>Retrieves the detailed list of portfolio threats based on the parameters that you have specified.</td><td>get_portfolio_threats <br/>Investigation</td></tr>
<tr><td>Get Cataloged Threats</td><td>Retrieves the detailed list of cataloged threats based on the parameters that you have specified.</td><td>get_cataloged_threats <br/>Investigation</td></tr>
<tr><td>Get Threat Statistics</td><td>Retrieves the detailed list of threat statistics based on the parameters that you have specified.</td><td>get_threat_statistics <br/>Investigation</td></tr>
<tr><td>Get Threat Impact</td><td>Retrieves the detailed list of threat impact based on the parameters that you have specified.</td><td>get_threat_impact <br/>Investigation</td></tr>
<tr><td>Get Assets</td><td>Retrieves the detailed list of assets based on the parameters that you have specified.</td><td>get_assets <br/>Investigation</td></tr>
<tr><td>Get Asset Risk Matrix</td><td>Retrieves the detailed list of asset risk matrix based on the parameters that you have specified.</td><td>get_assets_risk_matrix <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Alerts
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Start Date</td><td>Specify the start datetime of the duration from when the data should be fetched.
</td></tr><tr><td>End Date</td><td>Specify the end datetime of the duration till when the data should be fetched.
</td></tr><tr><td>Alert Category</td><td>Specify the alert category to filter the alerts.
</td></tr><tr><td>Company GUID</td><td>Specify the company GUID to filter the alerts.
</td></tr><tr><td>Include Details</td><td>Include additional alert details.
</td></tr><tr><td>Folder GUID</td><td>Specify the folder GUID to filter the alerts.
</td></tr><tr><td>Severity</td><td>Specify the severity to filter the alerts.
</td></tr><tr><td>Limit</td><td>Specify the limit to fetch the records. Default limit is 100.
</td></tr><tr><td>Offset</td><td>Specify the offset to fetch the records.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "links": {
        "previous": "",
        "next": ""
    },
    "count": "",
    "results": [
        {
            "guid": "",
            "alert_type": "",
            "alert_date": "",
            "start_date": "",
            "company_name": "",
            "company_guid": "",
            "company_url": "",
            "folder_guid": "",
            "folder_name": "",
            "severity": "",
            "trigger": ""
        }
    ]
}</pre>
### operation: Get Companies With Exposed Credentials
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Start Date</td><td>Specify the start datetime of the duration from when the data should be fetched.
</td></tr><tr><td>End Date</td><td>Specify the end datetime of the duration till when the data should be fetched.
</td></tr><tr><td>Limit</td><td>Specify the maximum number of records to return in the response.
</td></tr><tr><td>Offset</td><td>Specify the offset index from where the records should be returned. The index starts from 0.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "links": {
        "next": "",
        "previous": ""
    },
    "count": "",
    "results": [
        {
            "company_guid": "",
            "company_name": "",
            "leak_guid": "",
            "date_added": "",
            "unique_domain_count": "",
            "record_count": ""
        }
    ]
}</pre>
### operation: Get Credentials Leaks Affecting Your Portfolio
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Limit</td><td>Specify the maximum number of records to return in the response.
</td></tr><tr><td>Offset</td><td>Specify the offset index from where the records should be returned. The index starts from 0.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "links": {
        "next": "",
        "previous": ""
    },
    "count": "",
    "results": [
        {
            "guid": "",
            "name": "",
            "leak_date": "",
            "date_added": "",
            "description": "",
            "data_types_leaked": [
                {
                    "name": "",
                    "description": ""
                }
            ]
        }
    ]
}</pre>
### operation: Get Threat Evidence
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Company GUID</td><td>Specify the company GUID to filter the records.
</td></tr><tr><td>Threat GUID</td><td>Specify the threat GUID to filter the records.
</td></tr><tr><td>Last Seen Start Date</td><td>Specify the start datetime of the duration from when the data should be fetched.
</td></tr><tr><td>Last Seen End Date</td><td>Specify the end datetime of the duration till when the data should be fetched.
</td></tr><tr><td>Detection Type</td><td>Specify the detection type to filter the records. You can choose from the following options: Exposure, Mitigation.
</td></tr><tr><td>Evidence Certainty</td><td>Specify the evidence certainty to filter the records. You can choose from the following options: Possible, Likely, Confirmed.
</td></tr><tr><td>Exposure Detection</td><td>Specify the exposure detection to filter the records. You can choose from the following options: Currently, Previously.
</td></tr><tr><td>Force Masked</td><td>Specify if you want to force mask.
</td></tr><tr><td>Limit</td><td>Specify the limit to fetch the records. Default value is 10.
</td></tr><tr><td>Offset</td><td>Specify the offset to fetch the records. Default value is 0.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "links": {
        "previous": "",
        "next": ""
    },
    "count": "",
    "results": [
        {
            "identifier": "",
            "certainty": "",
            "exposure_detection": "",
            "detection_type": "",
            "first_seen_date": "",
            "last_seen_date": ""
        }
    ]
}</pre>
### operation: Get Portfolio Threats
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Company GUID</td><td>Specify the company GUID to filter the records.
</td></tr><tr><td>Category Slug</td><td>Specify the category slug to filter the records.
</td></tr><tr><td>Maximum Number of Exposed Entities</td><td>Specify the maximum number of exposed entities to filter the records.
</td></tr><tr><td>Minimum Number of Exposed Entities</td><td>Specify the minimum number of exposed entities to filter the records.
</td></tr><tr><td>Last Seen Start Date</td><td>Specify the start datetime of the duration from when the data should be fetched.
</td></tr><tr><td>Last Seen End Date</td><td>Specify the end datetime of the duration till when the data should be fetched.
</td></tr><tr><td>Expand</td><td>Include the number of questionnaires sent to each threat.
</td></tr><tr><td>Folder</td><td>Specify the folder GUID to filter the records.
</td></tr><tr><td>Impact Group</td><td>Specify the impact to filter the records. You can choose from the following options: True - Include threats that are affecting the entities. False - Include threats that are not affecting the entities.
</td></tr><tr><td>Severity Level</td><td>Specify the severity level to filter the records.
</td></tr><tr><td>Sort</td><td>Sort the objects based on the specified value. To sort in descending order, place a minus sign (-) immediately before the field name.
</td></tr><tr><td>Threat GUID</td><td>Specify the threat GUID to filter the records.
</td></tr><tr><td>Tier</td><td>Specify the tier to filter the records.
</td></tr><tr><td>Limit</td><td>Specify the maximum number of records to return in the response. Default value is 10.
</td></tr><tr><td>Offset</td><td>Specify the offset index from where the records should be returned. The index starts from 0.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "links": {
        "previous": "",
        "next": ""
    },
    "count": "",
    "results": [
        {
            "guid": "",
            "name": "",
            "first_seen_date": "",
            "last_seen_date": "",
            "severity": {
                "level": "",
                "details": ""
            },
            "category": {
                "name": "",
                "slug": ""
            },
            "support_started_date": "",
            "currently_exposed_count": "",
            "previously_exposed_count": "",
            "exposure_trend": "",
            "questionnaires_sent": ""
        }
    ]
}</pre>
### operation: Get Cataloged Threats
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Category</td><td>Specify the category to filter the records.
</td></tr><tr><td>Support Start Date</td><td>Specify the start datetime of the duration from when the data should be fetched.
</td></tr><tr><td>Support End Date</td><td>Specify the end datetime of the duration till when the data should be fetched.
</td></tr><tr><td>GUID</td><td>Specify the guid to filter the records.
</td></tr><tr><td>Name</td><td>Specify the name to filter the records.
</td></tr><tr><td>Severity Level</td><td>Specify the severity level to filter the records.
</td></tr><tr><td>Sort</td><td>Sort the objects based on the specified value. To sort in descending order, place a minus sign (-) immediately before the field name. The default sort is by name.
</td></tr><tr><td>Limit</td><td>Specify the maximum number of records to return in the response. Default value is 10.
</td></tr><tr><td>Offset</td><td>Specify the offset index from where the records should be returned. The index starts from 0.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "links": {
        "previous": "",
        "next": ""
    },
    "count": "",
    "results": [
        {
            "guid": "",
            "name": "",
            "display_name": "",
            "description": "",
            "remediation_tip": "",
            "details": {
                "cvss": "",
                "confidence": "",
                "severity": "",
                "status": ""
            },
            "category": {
                "name": "",
                "slug": ""
            },
            "support_started_date": ""
        }
    ]
}</pre>
### operation: Get Threat Statistics
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Folder</td><td>Specify the folder GUID to filter the records.
</td></tr><tr><td>Scope</td><td>Specify the scope to filter the records.
</td></tr><tr><td>Tier</td><td>Specify the tier GUID to filter the records.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "threats_total_count": "",
    "threats_impacting_count": "",
    "exposure_increasing_count": "",
    "exposure_flat_count": "",
    "exposure_decreasing_count": "",
    "currently_exposed_min": "",
    "currently_exposed_max": "",
    "previously_exposed_min": "",
    "previously_exposed_max": "",
    "exposure_trend_min": "",
    "exposure_trend_max": "",
    "severity_min": "",
    "severity_max": ""
}</pre>
### operation: Get Threat Impact
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Threat GUID</td><td>Specify the threat GUID to filter the records.
</td></tr><tr><td>Last Seen Start Date</td><td>Specify the start datetime of the duration from when the data should be fetched.
</td></tr><tr><td>Last Seen End Date</td><td>Specify the end datetime of the duration till when the data should be fetched.
</td></tr><tr><td>Evidence Certainty</td><td>Specify the evidence certainty to filter the records. You can choose from the following options: Possible, Likely, Confirmed.
</td></tr><tr><td>Expand</td><td>Include the additional information of threat impact.
</td></tr><tr><td>Exposure Detection</td><td>Specify the exposure detection to filter the records. You can choose from the following options: Currently, Previously.
</td></tr><tr><td>Folder</td><td>Specify the folder GUID to filter the records.
</td></tr><tr><td>Sort</td><td>Sort the objects based on the specified value. To sort in descending order, place a minus sign (-) immediately before the field name.
</td></tr><tr><td>Minimum Sub Threats Count</td><td>Specify the minimum sub threat count to filter the records.
</td></tr><tr><td>Maximum Sub Threats Count</td><td>Specify the maximum sub threat count to filter the records.
</td></tr><tr><td>Tier</td><td>Specify the tier GUID to filter the records.
</td></tr><tr><td>Limit</td><td>Specify the maximum number of records to return in the response. Default value is 25.
</td></tr><tr><td>Offset</td><td>Specify the offset index from where the records should be returned. The index starts from 0.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "links": {
        "previous": "",
        "next": ""
    },
    "summaries": {
        "currently_count": "",
        "previously_count": "",
        "total_count": "",
        "entity_group_size": "",
        "sub_threats_count": ""
    },
    "count": "",
    "results": [
        {
            "company_name": "",
            "evidence_certainty": "",
            "exposure_detection": "",
            "first_seen_date": "",
            "last_seen_date": "",
            "company_guid": "",
            "tier": "",
            "tier_name": "",
            "logo": "",
            "workflow_status": "",
            "sub_threats_count": "",
            "detection_types": []
        }
    ]
}</pre>
### operation: Get Assets
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Company GUID</td><td>Specify the company GUID to filter the records.
</td></tr><tr><td>Asset Name</td><td>Specify the asset name to filter the records.
</td></tr><tr><td>Asset Importance</td><td>Filter by asset importance, regardless of whether its importance is calculated or user-assigned.
</td></tr><tr><td>Expand</td><td>Specify the fields to include the additional information. eg: tag_details
</td></tr><tr><td>Minimum Asset Count</td><td>Filter assets by more than or equal to a set number of findings.
</td></tr><tr><td>Maximum Asset Count</td><td>Filter assets by less than or equal to a set number of findings.
</td></tr><tr><td>Hosted By</td><td>Filter by assets associated with a hosting provider. Select true to include only the assets with an associated hosting provider, select false to include all assets, regardless of a known hosting provider.
</td></tr><tr><td>Importance Categories</td><td>Specify the comma separated value of asset importance to filter the records.
</td></tr><tr><td>Importance Overrides</td><td>Filter assets by those with user-assigned asset importance.
</td></tr><tr><td>IP Address</td><td>Specify the IP address to filter the records.
</td></tr><tr><td>Check If IP</td><td>Filter by asset type. Select true to include only the assets that are IP addresses, select false to include only the assets that are domains.
</td></tr><tr><td>Origin Subsidiary</td><td>Filter by assets that are attributed to a subsidiary. Select true to include only the assets that are attributed to a subsidiary, select false to include all assets, regardless of an attributed subsidiary.
</td></tr><tr><td>Calculated or User-Assigned</td><td>Filter assets with calculated or user-assigned asset importance. Select true to include only the assets with calculated importance, select false to include only the assets with user-assigned importance.
</td></tr><tr><td>Tags</td><td>Specify comma separated tags to filter the records.
</td></tr><tr><td>Limit</td><td>Specify the maximum number of records to return in the response. Default value is 100.
</td></tr><tr><td>Offset</td><td>Specify the offset index from where the records should be returned.
</td></tr><tr><td>Attack Surface Analytics</td><td>Select if you have Attack Surface Analytics. The following parameters are also available if you have Attack Surface Analytics.
<br><strong>If you choose 'Available'</strong><ul><li>Countries: Specify the comma separated value of countries to filter the records.</li><li>Hosted By: Specify the comma separated value of company unique identifiers to filter the records.</li><li>Product Name: Specify the comma separated value of product names and version to filter the records. The value can be specified in this format product:version.</li><li>Threat GUID: Specify the comma separated value of vulnerability unique identifiers(vuln_guid) to filter the records.</li><li>Threat Severity Level: Specify the severity level to filter the records.</li></ul></td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "links": {
        "next": "",
        "previous": ""
    },
    "count": "",
    "results": [
        {
            "temporary_id": "",
            "asset": "",
            "asset_type": "",
            "identifier": "",
            "app_grade": "",
            "ip_addresses": [],
            "country_code": "",
            "country": "",
            "hosted_by": {
                "guid": "",
                "name": ""
            },
            "importance": "",
            "importance_category": "",
            "longitude": "",
            "latitude": "",
            "is_ip": "",
            "services": [],
            "origin_subsidiary": {
                "guid": "",
                "name": ""
            },
            "findings": {
                "total_count": "",
                "counts_by_severity": {
                    "severe": "",
                    "material": "",
                    "moderate": "",
                    "minor": ""
                }
            },
            "threats": {
                "rolledup_observation_ids": [],
                "evidence_keys": []
            },
            "tags": [],
            "tag_details": [
                {
                    "guid": "",
                    "name": "",
                    "is_inherited": "",
                    "is_public": ""
                }
            ],
            "overrides": {
                "importance": ""
            },
            "combined_overrides": {
                "importance": ""
            },
            "products": [
                {
                    "type": "",
                    "vendor": "",
                    "product": "",
                    "version": "",
                    "support": ""
                }
            ]
        }
    ]
}</pre>
### operation: Get Asset Risk Matrix
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Company GUID</td><td>Specify the company GUID to filter the records.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "assets": [
        {
            "asset": "",
            "importance": "",
            "importance_category": "",
            "stats": {
                "grades": {
                    "total": "",
                    "good": "",
                    "fair": "",
                    "warn": "",
                    "bad": "",
                    "neutral": "",
                    "na": ""
                }
            },
            "tags": []
        }
    ],
    "stats": {
        "critical": {
            "grades": {
                "total": "",
                "good": "",
                "fair": "",
                "warn": "",
                "bad": "",
                "neutral": "",
                "na": ""
            }
        }
    }
}</pre>
## Included playbooks
The `Sample - bitsight - 1.0.0` playbook collection comes bundled with the Bitsight connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Bitsight connector.

- Get Alerts
- Get Companies With Exposed Credentials
- Get Credentials Leaks Affecting Your Portfolio
- Get Threat Evidence
- Get Portfolio Threats
- Get Cataloged Threats
- Get Threat Statistics
- Get Threat Impact
- Get Assets
- Get Asset Risk Matrix

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
