class FromDevice:
    async def get_profiles(self):
        profiles: list = await self.media_service.GetProfiles()
        if profiles:
            profiles = profiles[0]
            params = {
                "Name": profiles.Name,
                "VideoSourceConfiguration": {
                    "Name": profiles.VideoSourceConfiguration.Name,
                    "SourceToken": profiles.VideoSourceConfiguration.SourceToken,
                    "token": profiles.VideoSourceConfiguration.token
                }
            }

    async def get_device_info(self):
        """:returns serialNo, firmware_ver"""
        return await self.devicemgmt_service.GetDeviceInformation()

    async def get_storage_configurations(self):
        return await self.devicemgmt_service.GetStorageConfigurations()

    async def get_datetime_config(self):
        """:returns timezone, utc_dt, local_dt"""
        return await self.devicemgmt_service.GetSystemDateAndTime()

    async def get_network_interfaces(self):
        """:returns ip_address, mac_address, interface_name"""
        return await self.devicemgmt_service.GetNetworkInterfaces()

    async def get_users(self):
        """:returns list[dict]{username, userlevel}"""
        return await self.devicemgmt_service.GetUsers()

    async def get_ntp(self):
        return await self.devicemgmt_service.GetNTP()

    async def get_capabillities(self):
        return await self.devicemgmt_service.GetCapabilities()

    async def get_dns(self):
        return await self.devicemgmt_service.GetDNS()
