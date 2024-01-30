# SettingParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Alias for setting name |
**name** | **str** | Setting unique name |
**full_name** | **str** | Setting full user readable name |
**category** | **str** | The category of setting |
**category_name** | **str** | The human readable name of settings category |
**settings_type** | **str** | Value type, that the setting accepts |
**description** | **str** | Describes the purpose of the setting |
**default** | **str** | Default value for the setting |
**value** | **str** | Setting current value. If this setting is encypted, the value will not be returned |
**readonly** | **bool** | Is this setting readonly? |
**encrypted** | **bool** | Is this setting encrypted? |
**config_file** | **str** | If this setting needs to be changed in file, it will have the file path. |
**select_values** | **list[str]** | If this setting has list of possible values, this includes the list of the values. |
**updated_at** | **str** | Last updated. NOTE: this will be reset to application install time, when setting is reset to default value. |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
