# /usr/local/bin/python3.10
import httpx
from onvif import ONVIFCamera
from onvif.client import ONVIFService
import asyncio
from methods.get.device_service import FromDevice
from methods.set.device_service import ToDevice


class OmnyBase(FromDevice, ToDevice):
    """Omny autoconfig"""

    def __init__(self, ip_address: str, login: str, password: str) -> None:
        self.ip_address = ip_address
        self.login = login
        self.password = password
        self.devicemgmt_service: ONVIFService
        self.media_service: ONVIFService

    async def init_cam(self):
        mycam = ONVIFCamera(self.ip_address, 80, self.login,
                            self.password, "/etc/onvif/wsdl/")
        await mycam.update_xaddrs()
        self.devicemgmt_service = mycam.create_devicemgmt_service()
        self.media_service = mycam.create_media_service()

    async def main(self):
        await self.init_cam()



if __name__ == "__main__":
    app = OmnyBase("192.168.0.28", "admin", "password")
    asyncio.run(app.main())
