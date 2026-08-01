from fa_commands import get_server_setting


def test_get_server_setting_uses_default_for_missing_values():
    server_settings = {"prefix": "-"}

    assert get_server_setting(server_settings, "threeyearrule", "off") == "off"
    assert get_server_setting(server_settings, "options", "off") == "off"
    assert get_server_setting(server_settings, "holdout", "0") == "0"
