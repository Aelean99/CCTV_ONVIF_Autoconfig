class ToDevice:
    async def set_ntp(self, ssh: bool = False):
        """{ 'IPv4Address', 'IPv6Address', 'DNSname'}"""
        """{ 'IPv4', 'IPv6', 'DNS' }"""
        if ssh:
            params = {
                "FromDHCP": False,
                "NTPManual": [
                    {
                        "Type": "DNSname",
                        "DNS": "time.windows.com"
                    },
                ]
            }
        else:
            params = {
                "FromDHCP": False,
                "NTPManual": [
                    {
                        "Type": "IPv4",
                        "IPv4Address": "217.24.176.232"
                    },
                ]
            }
        await self.devicemgmt_service.SetDNS(params)

    async def set_datetime_config(self, tz):
        """{ 'Manual', 'NTP' }"""
        params = {
            "DateTimeType": "NTP",
            "DaylightSavings": False,
            "TimeZone": {
                "TZ": tz
            }
        }
        await self.devicemgmt_service.SetSystemDateAndTime(params)

    async def set_system_factory_default(self, mode: str):
        """
        - Hard: Indicates that a hard factory default is requested.
        - Soft: Indicates that a soft factory default is requested.
        """
        params = {
            "FactoryDefault": mode
        }
        await self.devicemgmt_service.SetSystemFactoryDefault(params)

    async def set_user(self, username, password, userlevel):
        """
        userlevel - enum { 'Administrator', 'Operator', 'User', 'Anonymous' }
        """
        params = {
            "Username": username,
            "Password": password,
            "UserLevel": userlevel
        }
        await self.devicemgmt_service.SetUser(params)

    async def start_firmware_upgrade(self, file):
        await self.devicemgmt_service.StartFirmwareUpgrade()

    async def upgrade_system_firmware(self, file):
        with open(file, "rb") as f:
            params = {
                "Firmware": {
                    "contentType": "multipart/form-data",
                    "Include": f
                }
            }
        await self.devicemgmt_service.UpgradeSystemFirmware(params)

    async def create_users(self, user, password, userlevel):
        """
        userlevel - enum { 'Administrator', 'Operator', 'User', 'Anonymous' }
        """
        params = {
            "User": {
                "Username": user,
                "Password": password,
                "UserLevel": userlevel
            }
        }
        await self.devicemgmt_service.CreateUsers(params)

    async def set_dns(self, ssh: bool = False):
        if ssh:
            params = {
                "FromDHCP": True
            }
        else:
            params = {
                "FromDHCP": False,
                "DNSManual": [
                    {
                        "Type": "IPv4",
                        "IPv4Address": "217.24.176.230"
                    },
                    {
                        "Type": "IPv4",
                        "IPv4Address": "217.24.177.2"
                    },
                ]
            }
        await self.devicemgmt_service.SetDNS(params)
