from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


@dataclass
class Row:
    cve: Optional[str] = field(
        default=None,
        metadata={
            "name": "CVE",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    power_scrit_cust_fld1: Optional[str] = field(
        default=None,
        metadata={
            "name": "PowerScritCustFld1",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    power_scrit_cust_fld2: Optional[str] = field(
        default=None,
        metadata={
            "name": "PowerScritCustFld2",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    power_scrit_cust_fld3: Optional[str] = field(
        default=None,
        metadata={
            "name": "PowerScritCustFld3",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    power_scrit_cust_fld4: Optional[str] = field(
        default=None,
        metadata={
            "name": "PowerScritCustFld4",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    a_clid: Optional[str] = field(
        default=None,
        metadata={
            "name": "aCLID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    a_cltype: Optional[str] = field(
        default=None,
        metadata={
            "name": "aCLType",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    aaa_password: Optional[str] = field(
        default=None,
        metadata={
            "name": "aaaPassword",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    aaa_user_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "aaaUserName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    access_methods: Optional[str] = field(
        default=None,
        metadata={
            "name": "accessMethods",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    access_trigger: Optional[str] = field(
        default=None,
        metadata={
            "name": "accessTrigger",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    action_taken: Optional[str] = field(
        default=None,
        metadata={
            "name": "actionTaken",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    aggregated_ports: Optional[str] = field(
        default=None,
        metadata={
            "name": "aggregatedPorts",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    allow_failover: Optional[int] = field(
        default=None,
        metadata={
            "name": "allowFailover",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    application: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    application_state: Optional[int] = field(
        default=None,
        metadata={
            "name": "applicationState",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    applies_to_entire_device_family: Optional[int] = field(
        default=None,
        metadata={
            "name": "appliesToEntireDeviceFamily",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    approval_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "approvalPriority",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    approval_status: Optional[int] = field(
        default=None,
        metadata={
            "name": "approvalStatus",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    approval_users: Optional[str] = field(
        default=None,
        metadata={
            "name": "approvalUsers",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    approve_by_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "approveByDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    asset_tag: Optional[str] = field(
        default=None,
        metadata={
            "name": "assetTag",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    associated_channel_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "associatedChannelID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    associated_channel_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "associatedChannelName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    associated_table: Optional[str] = field(
        default=None,
        metadata={
            "name": "associatedTable",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    associated_table_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "associatedTableID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    associated_user_group_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "associatedUserGroupID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    associated_vlan_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "associatedVlanID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    authentication_rule_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "authenticationRuleID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    base_model_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "baseModelName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    block_end_pattern: Optional[str] = field(
        default=None,
        metadata={
            "name": "blockEndPattern",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    block_format: Optional[int] = field(
        default=None,
        metadata={
            "name": "blockFormat",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    block_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "blockSize",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    block_start_pattern: Optional[str] = field(
        default=None,
        metadata={
            "name": "blockStartPattern",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    block_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "blockType",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    boot_romrequired: Optional[str] = field(
        default=None,
        metadata={
            "name": "bootROMRequired",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    change_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "changeDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    change_event_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "changeEventData",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    changed_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "changedBy",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    checksum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    child_device_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "childDeviceID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    column_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "columnName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    commands: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    comments: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    complete_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "completeDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    conditions: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    config_comments: Optional[str] = field(
        default=None,
        metadata={
            "name": "configComments",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    config_exception_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "configExceptionID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    config_hash: Optional[str] = field(
        default=None,
        metadata={
            "name": "configHash",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    config_hash_mode: Optional[int] = field(
        default=None,
        metadata={
            "name": "configHashMode",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    config_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "configID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    config_policy_dynamic_scope_filter_criteria: Optional[str] = field(
        default=None,
        metadata={
            "name": "configPolicyDynamicScopeFilterCriteria",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    config_policy_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "configPolicyID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    config_policy_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "configPolicyName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    config_rule_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "configRuleID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    config_rule_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "configRuleName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    configuration_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "configurationVersion",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    configured_duplex: Optional[str] = field(
        default=None,
        metadata={
            "name": "configuredDuplex",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    configured_speed: Optional[str] = field(
        default=None,
        metadata={
            "name": "configuredSpeed",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    console_ipaddress: Optional[str] = field(
        default=None,
        metadata={
            "name": "consoleIPAddress",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    console_port: Optional[int] = field(
        default=None,
        metadata={
            "name": "consolePort",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    console_realm_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "consoleRealmName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    contact: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    containing_user_group_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "containingUserGroupID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    core: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    core_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "coreID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    create_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "createDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    create_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "createType",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    create_user_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "createUserID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    created_by: Optional[int] = field(
        default=None,
        metadata={
            "name": "createdBy",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    cross_reference_topology_data_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "crossReferenceTopologyDataID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    csv_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "csvData",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    csv_group_task: Optional[int] = field(
        default=None,
        metadata={
            "name": "csvGroupTask",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    current_vlannumber: Optional[int] = field(
        default=None,
        metadata={
            "name": "currentVLANNumber",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    custom_data_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "customDataID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    custom_field_definition_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "customFieldDefinitionID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    custom_field_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "customFieldID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    custom_field_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "customFieldName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    custom_field_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "customFieldValue",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    custom_model: Optional[int] = field(
        default=None,
        metadata={
            "name": "customModel",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    custom_script_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "customScriptID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    data: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    data_block: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataBlock",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    destination_device_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "destinationDeviceID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_aclid: Optional[int] = field(
        default=None,
        metadata={
            "name": "deviceACLID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_access_log_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "deviceAccessLogID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_authentication_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "deviceAuthenticationID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "deviceCount",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_custom1: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceCustom1",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_custom2: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceCustom2",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_custom3: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceCustom3",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_custom4: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceCustom4",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_custom5: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceCustom5",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_custom6: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceCustom6",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_data_custom1: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceDataCustom1",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_data_custom2: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceDataCustom2",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_data_custom3: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceDataCustom3",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_data_custom4: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceDataCustom4",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_data_custom5: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceDataCustom5",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_data_custom6: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceDataCustom6",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_data_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "deviceDataID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_family: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceFamily",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_family_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceFamilyName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_group1_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "deviceGroup1ID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_group2_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "deviceGroup2ID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_group3_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "deviceGroup3ID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_group_custom1: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceGroupCustom1",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_group_custom2: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceGroupCustom2",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_group_custom3: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceGroupCustom3",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_group_custom4: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceGroupCustom4",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_group_custom5: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceGroupCustom5",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_group_custom6: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceGroupCustom6",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_group_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "deviceGroupID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_group_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceGroupName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_groups: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceGroups",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "deviceID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_ip: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceIP",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_module_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "deviceModuleID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_port_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "devicePortID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_relationship_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "deviceRelationshipID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_software_image_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "deviceSoftwareImageID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_topology_data_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "deviceTopologyDataID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceType",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_vtpid: Optional[int] = field(
        default=None,
        metadata={
            "name": "deviceVTPID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_view_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "deviceViewID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_view_idchanged: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceViewIDChanged",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    device_vlan_info_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "deviceVlanInfoID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    devices: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    disclosure_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "disclosureDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    distinguished_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "distinguishedName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    domain_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "domainName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    driver_lookup_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "driverLookupID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    driver_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "driverName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    driver_names: Optional[str] = field(
        default=None,
        metadata={
            "name": "driverNames",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    driver_required: Optional[str] = field(
        default=None,
        metadata={
            "name": "driverRequired",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    drivers: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    duplex_mismatch_detected: Optional[int] = field(
        default=None,
        metadata={
            "name": "duplexMismatchDetected",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    duration: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    duration_str: Optional[str] = field(
        default=None,
        metadata={
            "name": "durationStr",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    dynamic_filter: Optional[str] = field(
        default=None,
        metadata={
            "name": "dynamicFilter",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    dynamic_filter_xml: Optional[str] = field(
        default=None,
        metadata={
            "name": "dynamicFilterXML",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    email_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "emailAddress",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    end_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "endDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    end_range: Optional[str] = field(
        default=None,
        metadata={
            "name": "endRange",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    evaluation_logic: Optional[str] = field(
        default=None,
        metadata={
            "name": "evaluationLogic",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    event_class: Optional[int] = field(
        default=None,
        metadata={
            "name": "eventClass",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    event_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "eventData",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    event_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "eventDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    event_device_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "eventDeviceID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    event_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "eventID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    event_task_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "eventTaskID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    event_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "eventText",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    event_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "eventType",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    event_user_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "eventUserID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    exact_order: Optional[str] = field(
        default=None,
        metadata={
            "name": "exactOrder",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    exception_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "exceptionType",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    exclude_from_poll: Optional[int] = field(
        default=None,
        metadata={
            "name": "excludeFromPoll",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    expensive: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    expiration_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "expirationDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    external_change_request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externalChangeRequestID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    failed_child_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "failedChildCount",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    failure_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "failureType",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    feed_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "feedSource",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    field_data_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "fieldDataType",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    field_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "fieldID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    field_label: Optional[str] = field(
        default=None,
        metadata={
            "name": "fieldLabel",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    field_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fieldName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    field_values: Optional[str] = field(
        default=None,
        metadata={
            "name": "fieldValues",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    firmware_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "firmwareVersion",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "firstName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    first_seen: Optional[str] = field(
        default=None,
        metadata={
            "name": "firstSeen",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    flags: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    flash_memory: Optional[int] = field(
        default=None,
        metadata={
            "name": "flashMemory",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    flash_ramrequired: Optional[int] = field(
        default=None,
        metadata={
            "name": "flashRAMRequired",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    force_save: Optional[str] = field(
        default=None,
        metadata={
            "name": "forceSave",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    free_ports: Optional[int] = field(
        default=None,
        metadata={
            "name": "freePorts",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    geographical_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "geographicalLocation",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    granted_resources: Optional[str] = field(
        default=None,
        metadata={
            "name": "grantedResources",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    groups: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    handle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    hardware_required: Optional[str] = field(
        default=None,
        metadata={
            "name": "hardwareRequired",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    hardware_revision: Optional[str] = field(
        default=None,
        metadata={
            "name": "hardwareRevision",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    hash_alg: Optional[str] = field(
        default=None,
        metadata={
            "name": "hashAlg",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    hierarchy_layer: Optional[int] = field(
        default=None,
        metadata={
            "name": "hierarchyLayer",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    host_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "hostName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    id_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "idValue",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    image_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "imageName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    image_path: Optional[str] = field(
        default=None,
        metadata={
            "name": "imagePath",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    image_set_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "imageSetName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    image_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "imageSize",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    importance: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    in_compliance: Optional[int] = field(
        default=None,
        metadata={
            "name": "inCompliance",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    in_use: Optional[int] = field(
        default=None,
        metadata={
            "name": "inUse",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    interceptor_log_custom1: Optional[str] = field(
        default=None,
        metadata={
            "name": "interceptorLogCustom1",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    interceptor_log_custom2: Optional[str] = field(
        default=None,
        metadata={
            "name": "interceptorLogCustom2",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    interceptor_log_custom3: Optional[str] = field(
        default=None,
        metadata={
            "name": "interceptorLogCustom3",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    interceptor_log_custom4: Optional[str] = field(
        default=None,
        metadata={
            "name": "interceptorLogCustom4",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    interceptor_log_custom5: Optional[str] = field(
        default=None,
        metadata={
            "name": "interceptorLogCustom5",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    interceptor_log_custom6: Optional[str] = field(
        default=None,
        metadata={
            "name": "interceptorLogCustom6",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    interceptor_log_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "interceptorLogID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    ip_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "ipAddress",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    ip_addresses: Optional[str] = field(
        default=None,
        metadata={
            "name": "ipAddresses",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    ip_custom1: Optional[str] = field(
        default=None,
        metadata={
            "name": "ipCustom1",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    ip_custom2: Optional[str] = field(
        default=None,
        metadata={
            "name": "ipCustom2",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    ip_custom3: Optional[str] = field(
        default=None,
        metadata={
            "name": "ipCustom3",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    ip_custom4: Optional[str] = field(
        default=None,
        metadata={
            "name": "ipCustom4",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    ip_custom5: Optional[str] = field(
        default=None,
        metadata={
            "name": "ipCustom5",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    ip_custom6: Optional[str] = field(
        default=None,
        metadata={
            "name": "ipCustom6",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    ip_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ipID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    ip_mask: Optional[str] = field(
        default=None,
        metadata={
            "name": "ipMask",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    ip_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ipName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    ip_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "ipPriority",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    ip_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "ipType",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    ip_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "ipValue",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    is_config_change: Optional[int] = field(
        default=None,
        metadata={
            "name": "isConfigChange",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    is_dynamic: Optional[int] = field(
        default=None,
        metadata={
            "name": "isDynamic",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    is_integration_enabled: Optional[str] = field(
        default=None,
        metadata={
            "name": "isIntegrationEnabled",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    is_lookup_skipped: Optional[str] = field(
        default=None,
        metadata={
            "name": "isLookupSkipped",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    is_parent: Optional[int] = field(
        default=None,
        metadata={
            "name": "isParent",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    is_policy_scope: Optional[int] = field(
        default=None,
        metadata={
            "name": "isPolicyScope",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    is_using_ssl: Optional[str] = field(
        default=None,
        metadata={
            "name": "isUsingSsl",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    last_access_attempt_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastAccessAttemptDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    last_access_attempt_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastAccessAttemptStatus",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    last_access_success_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastAccessSuccessDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    last_config_change_user_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "lastConfigChangeUserID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    last_config_policy_checked_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastConfigPolicyCheckedDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    last_duplex_data_update: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastDuplexDataUpdate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    last_import_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastImportDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    last_login_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastLoginDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    last_modified_access_log_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "lastModifiedAccessLogID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    last_modified_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastModifiedDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    last_modified_user_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "lastModifiedUserID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    last_modify_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastModifyDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    last_modify_user_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "lastModifyUserID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    last_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    last_record_modified_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastRecordModifiedDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    last_seen: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastSeen",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    last_snapshot_attempt_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastSnapshotAttemptDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    last_snapshot_attempt_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastSnapshotAttemptStatus",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    last_snapshot_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastSnapshotDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    last_snapshot_success_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastSnapshotSuccessDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    last_topology_data_update: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastTopologyDataUpdate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    last_updated: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastUpdated",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    last_used_authentication_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "lastUsedAuthenticationID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    latest_software_history_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "latestSoftwareHistoryID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    latest_startup_running_differ: Optional[int] = field(
        default=None,
        metadata={
            "name": "latestStartupRunningDiffer",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    limit_searchby_device_group: Optional[str] = field(
        default=None,
        metadata={
            "name": "limitSearchbyDeviceGroup",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    limit_searchby_partition: Optional[str] = field(
        default=None,
        metadata={
            "name": "limitSearchbyPartition",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_create_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "mCreateDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_custom_service_types: Optional[str] = field(
        default=None,
        metadata={
            "name": "mCustomServiceTypes",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_device_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "mDeviceID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_device_property_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "mDevicePropertyID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_last_modified_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "mLastModifiedDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_service_types: Optional[str] = field(
        default=None,
        metadata={
            "name": "mServiceTypes",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_applies_to: Optional[int] = field(
        default=None,
        metadata={
            "name": "m_appliesTo",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_build_num: Optional[str] = field(
        default=None,
        metadata={
            "name": "m_buildNum",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_comments: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_core_hostname: Optional[str] = field(
        default=None,
        metadata={
            "name": "m_coreHostname",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_core_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "m_coreID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_core_rmiport: Optional[int] = field(
        default=None,
        metadata={
            "name": "m_coreRMIPort",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_database_hostname: Optional[str] = field(
        default=None,
        metadata={
            "name": "m_databaseHostname",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_database_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "m_databaseIdentifier",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_database_port: Optional[int] = field(
        default=None,
        metadata={
            "name": "m_databasePort",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_default_device_group_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "m_defaultDeviceGroupID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_device_group_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "m_deviceGroupID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_enabled: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_is_master_def: Optional[int] = field(
        default=None,
        metadata={
            "name": "m_isMasterDef",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    microfocus_com_nas_2020_08_m_last_modified_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "m_lastModifiedDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_managing_core_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "m_managingCoreID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_owning_core_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "m_owningCoreID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_realm_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "m_realmName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_replication_admin_user: Optional[str] = field(
        default=None,
        metadata={
            "name": "m_replicationAdminUser",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_replication_password: Optional[str] = field(
        default=None,
        metadata={
            "name": "m_replicationPassword",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_site_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "m_siteID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_timezone_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "m_timezoneOffset",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_user_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "m_userName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_view_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "m_viewID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    m_view_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "m_viewName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    mac_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "macAddress",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    management_status: Optional[int] = field(
        default=None,
        metadata={
            "name": "managementStatus",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    manager_user_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "managerUserID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    managing_core_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "managingCoreID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    masked_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "maskedSize",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    max_vlannumber: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxVLANNumber",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    max_wait_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxWaitTime",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    max_wait_time_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxWaitTimeType",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    md5_digest: Optional[str] = field(
        default=None,
        metadata={
            "name": "md5Digest",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    memory: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    message_to: Optional[str] = field(
        default=None,
        metadata={
            "name": "messageTo",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    metadata_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "metadataID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    metadata_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "metadataName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    model: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    model_data_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "modelDataName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    model_required: Optional[str] = field(
        default=None,
        metadata={
            "name": "modelRequired",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    modem_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "modemNumber",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    modifiable: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    module_custom1: Optional[str] = field(
        default=None,
        metadata={
            "name": "moduleCustom1",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    module_custom2: Optional[str] = field(
        default=None,
        metadata={
            "name": "moduleCustom2",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    module_custom3: Optional[str] = field(
        default=None,
        metadata={
            "name": "moduleCustom3",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    module_custom4: Optional[str] = field(
        default=None,
        metadata={
            "name": "moduleCustom4",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    module_custom5: Optional[str] = field(
        default=None,
        metadata={
            "name": "moduleCustom5",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    module_custom6: Optional[str] = field(
        default=None,
        metadata={
            "name": "moduleCustom6",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    module_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "moduleDescription",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    module_model: Optional[str] = field(
        default=None,
        metadata={
            "name": "moduleModel",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    module_os: Optional[str] = field(
        default=None,
        metadata={
            "name": "moduleOS",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    most_recent: Optional[int] = field(
        default=None,
        metadata={
            "name": "mostRecent",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    most_recent_config_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "mostRecentConfigID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    mtu: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    n_atipaddress: Optional[str] = field(
        default=None,
        metadata={
            "name": "nATIPAddress",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    n_atrealm_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "nATRealmName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    na_integration_user: Optional[str] = field(
        default=None,
        metadata={
            "name": "naIntegrationUser",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    native_vlan: Optional[int] = field(
        default=None,
        metadata={
            "name": "nativeVlan",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    negotiated_duplex: Optional[str] = field(
        default=None,
        metadata={
            "name": "negotiatedDuplex",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    negotiated_speed: Optional[str] = field(
        default=None,
        metadata={
            "name": "negotiatedSpeed",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    network_address_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "networkAddressStart",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    nnmi_host_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "nnmiHostName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    nnmi_integration_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "nnmiIntegrationID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    nnmi_node_uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "nnmiNodeUUID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    nnmi_password: Optional[str] = field(
        default=None,
        metadata={
            "name": "nnmiPassword",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    nnmi_port: Optional[int] = field(
        default=None,
        metadata={
            "name": "nnmiPort",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    nnmi_system_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "nnmiSystemID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    nnmi_user: Optional[str] = field(
        default=None,
        metadata={
            "name": "nnmiUser",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    no_prune: Optional[int] = field(
        default=None,
        metadata={
            "name": "noPrune",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    operand: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    operating_mode: Optional[str] = field(
        default=None,
        metadata={
            "name": "operatingMode",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    operator_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "operatorName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    originating_device_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "originatingDeviceID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    padded_ip: Optional[str] = field(
        default=None,
        metadata={
            "name": "paddedIp",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    parameters: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    parent_device_group_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "parentDeviceGroupID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    parent_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "parentIdentifier",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    parent_module_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "parentModuleID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    parent_task_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "parentTaskID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    partition_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "partitionCount",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    partitions: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    password: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    password_last_modified_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "passwordLastModifiedDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    password_option: Optional[int] = field(
        default=None,
        metadata={
            "name": "passwordOption",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    pattern: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    pending_child_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "pendingChildCount",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    perform_aclparsing: Optional[int] = field(
        default=None,
        metadata={
            "name": "performACLParsing",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    policy_importance: Optional[int] = field(
        default=None,
        metadata={
            "name": "policyImportance",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    policy_in_compliance: Optional[int] = field(
        default=None,
        metadata={
            "name": "policyInCompliance",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    port_allows: Optional[str] = field(
        default=None,
        metadata={
            "name": "portAllows",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    port_channel_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "portChannelID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    port_channel_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "portChannelName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    port_custom1: Optional[str] = field(
        default=None,
        metadata={
            "name": "portCustom1",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    port_custom2: Optional[str] = field(
        default=None,
        metadata={
            "name": "portCustom2",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    port_custom3: Optional[str] = field(
        default=None,
        metadata={
            "name": "portCustom3",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    port_custom4: Optional[str] = field(
        default=None,
        metadata={
            "name": "portCustom4",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    port_custom5: Optional[str] = field(
        default=None,
        metadata={
            "name": "portCustom5",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    port_custom6: Optional[str] = field(
        default=None,
        metadata={
            "name": "portCustom6",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    port_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "portName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    port_state: Optional[str] = field(
        default=None,
        metadata={
            "name": "portState",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    port_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "portStatus",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    port_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "portType",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    post_check_expression: Optional[str] = field(
        default=None,
        metadata={
            "name": "postCheckExpression",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    power_script_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "powerScriptID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    pre_check_expression: Optional[str] = field(
        default=None,
        metadata={
            "name": "preCheckExpression",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    primary_fqdn: Optional[str] = field(
        default=None,
        metadata={
            "name": "primaryFQDN",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    primary_ipaddress: Optional[str] = field(
        default=None,
        metadata={
            "name": "primaryIPAddress",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    priority: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    privilege_level: Optional[int] = field(
        default=None,
        metadata={
            "name": "privilegeLevel",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    processor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    pruning_mode: Optional[str] = field(
        default=None,
        metadata={
            "name": "pruningMode",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    put_in_service_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "putInServiceDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    r_omversion: Optional[str] = field(
        default=None,
        metadata={
            "name": "rOMVersion",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    realm_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "realmName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    redirect_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "redirectLocation",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    refresh_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "refreshToken",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    refresh_token_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "refreshTokenID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    relationship_type_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "relationshipTypeID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    relationship_type_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "relationshipTypeName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    remote_device_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "remoteDeviceID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    remote_device_port_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "remoteDevicePortID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    remote_sas_server_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "remoteSasServerID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    remote_sas_server_interface_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "remoteSasServerInterfaceID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    repeat_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "repeatCount",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    repeat_end_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "repeatEndDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    repeat_interval: Optional[int] = field(
        default=None,
        metadata={
            "name": "repeatInterval",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    repeat_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "repeatType",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    repeat_weekday: Optional[int] = field(
        default=None,
        metadata={
            "name": "repeatWeekday",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    required: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    required_user: Optional[int] = field(
        default=None,
        metadata={
            "name": "requiredUser",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    requires_reference_update: Optional[str] = field(
        default=None,
        metadata={
            "name": "requiresReferenceUpdate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    requires_update: Optional[str] = field(
        default=None,
        metadata={
            "name": "requiresUpdate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    reservation_end_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "reservationEndDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    reserved_duration: Optional[int] = field(
        default=None,
        metadata={
            "name": "reservedDuration",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    reserved_duration_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "reservedDurationType",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    resource_identity_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "resourceIdentityID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    resource_identity_pool_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "resourceIdentityPoolID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    result: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    result_config_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "resultConfigID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    retry_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "retryCount",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    retry_interval: Optional[int] = field(
        default=None,
        metadata={
            "name": "retryInterval",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    role_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "roleID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    role_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "roleName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    role_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "roleType",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    roll_back_script_vo: Optional[str] = field(
        default=None,
        metadata={
            "name": "rollBackScriptVO",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    rule_condition_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ruleConditionID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    rule_condition_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "ruleConditionOrder",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    rule_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ruleName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    rule_pattern: Optional[str] = field(
        default=None,
        metadata={
            "name": "rulePattern",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    rule_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "rulePriority",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    rule_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "ruleType",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    run_asap: Optional[int] = field(
        default=None,
        metadata={
            "name": "runASAP",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    run_roll_back: Optional[int] = field(
        default=None,
        metadata={
            "name": "runRollBack",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    run_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "runType",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    running_child_task_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "runningChildTaskId",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    salt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    saltmode: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    save_favorite_link: Optional[str] = field(
        default=None,
        metadata={
            "name": "saveFavoriteLink",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    save_task: Optional[str] = field(
        default=None,
        metadata={
            "name": "saveTask",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    save_template: Optional[str] = field(
        default=None,
        metadata={
            "name": "saveTemplate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    schedule_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "scheduleDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    schedule_task_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "scheduleTaskID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    scope: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    script: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    script_mode: Optional[str] = field(
        default=None,
        metadata={
            "name": "scriptMode",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    script_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "scriptName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    script_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "scriptType",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    script_vo: Optional[str] = field(
        default=None,
        metadata={
            "name": "scriptVO",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    scripts: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    serial_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "serialNumber",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    session_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "sessionData",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    session_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "sessionType",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    shared: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    site_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "siteID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    site_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "siteName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    slot: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    slot_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "slotNumber",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    slot_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "slotType",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    software_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "softwareVersion",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    solution: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    source_device_data_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "sourceDeviceDataID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    start_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "startDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    start_range: Optional[str] = field(
        default=None,
        metadata={
            "name": "startRange",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    status: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    stop_on_fail: Optional[int] = field(
        default=None,
        metadata={
            "name": "stopOnFail",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    sub_task: Optional[int] = field(
        default=None,
        metadata={
            "name": "subTask",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    sub_tasks: Optional[str] = field(
        default=None,
        metadata={
            "name": "subTasks",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    subnet_bit_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "subnetBitCount",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    succeeded_child_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "succeededChildCount",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    system_task: Optional[int] = field(
        default=None,
        metadata={
            "name": "systemTask",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    t_ftpserver_ipaddress: Optional[str] = field(
        default=None,
        metadata={
            "name": "tFTPServerIPAddress",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    table_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "tableName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    tag: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    task_custom1: Optional[str] = field(
        default=None,
        metadata={
            "name": "taskCustom1",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    task_custom2: Optional[str] = field(
        default=None,
        metadata={
            "name": "taskCustom2",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    task_custom3: Optional[str] = field(
        default=None,
        metadata={
            "name": "taskCustom3",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    task_custom4: Optional[str] = field(
        default=None,
        metadata={
            "name": "taskCustom4",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    task_custom5: Optional[str] = field(
        default=None,
        metadata={
            "name": "taskCustom5",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    task_custom6: Optional[str] = field(
        default=None,
        metadata={
            "name": "taskCustom6",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    task_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "taskData",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    task_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "taskName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    task_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "taskType",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    task_user_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "taskUserID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    temporary_vlan_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "temporaryVlanName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    ticket_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ticketNumber",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    time_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "timeZone",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    topology_data_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "topologyDataType",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    total_ports: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalPorts",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    treat_null_as_empty: Optional[str] = field(
        default=None,
        metadata={
            "name": "treatNullAsEmpty",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    unmanaged_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "unmanagedDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    uptime: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    uptime_stored_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "uptimeStoredDate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    use_aaa_login_for_proxy: Optional[int] = field(
        default=None,
        metadata={
            "name": "useAaaLoginForProxy",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    use_latest: Optional[int] = field(
        default=None,
        metadata={
            "name": "useLatest",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    use_regex: Optional[int] = field(
        default=None,
        metadata={
            "name": "useRegex",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    use_regexp: Optional[str] = field(
        default=None,
        metadata={
            "name": "useRegexp",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    used_to_access: Optional[int] = field(
        default=None,
        metadata={
            "name": "usedToAccess",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    user_custom1: Optional[str] = field(
        default=None,
        metadata={
            "name": "userCustom1",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    user_custom2: Optional[str] = field(
        default=None,
        metadata={
            "name": "userCustom2",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    user_custom3: Optional[str] = field(
        default=None,
        metadata={
            "name": "userCustom3",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    user_custom4: Optional[str] = field(
        default=None,
        metadata={
            "name": "userCustom4",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    user_custom5: Optional[str] = field(
        default=None,
        metadata={
            "name": "userCustom5",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    user_custom6: Optional[str] = field(
        default=None,
        metadata={
            "name": "userCustom6",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    user_generated_change: Optional[str] = field(
        default=None,
        metadata={
            "name": "userGeneratedChange",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    user_groups: Optional[str] = field(
        default=None,
        metadata={
            "name": "userGroups",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    user_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "userID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    user_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "userName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    user_password: Optional[str] = field(
        default=None,
        metadata={
            "name": "userPassword",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    user_password_unhashed: Optional[str] = field(
        default=None,
        metadata={
            "name": "userPasswordUnhashed",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    variable_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "variableData",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    variables: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    vendor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    vendor_advisory_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "vendorAdvisoryURL",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    vendor_solution_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "vendorSolutionURL",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    vlan_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "vlanID",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    vlan_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlanName",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    vlan_port_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlanPortType",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    vlan_private: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlanPrivate",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    vlan_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlanStatus",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    vlan_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "vlanType",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    volatile_ramrequired: Optional[int] = field(
        default=None,
        metadata={
            "name": "volatileRAMRequired",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    vtp_traps_generation: Optional[str] = field(
        default=None,
        metadata={
            "name": "vtpTrapsGeneration",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    vtp_v2_mode: Optional[str] = field(
        default=None,
        metadata={
            "name": "vtpV2Mode",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
    vtp_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "vtpVersion",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
            "nillable": True,
        }
    )
