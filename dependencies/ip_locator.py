import asyncio
import aiohttp
import socket
import os
from colorama import init, Fore

init(autoreset=True)


async def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


async def get_ip_info(ip):
    url = f"https://ipinfo.io/{ip}/json"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data
    return None


async def get_continent(country):
    continent_mapping = {
        "US": "Amérique du Nord",
        "CA": "Amérique du Nord",
        "MX": "Amérique du Nord",
        "SA": "Amérique du Sud",
        "FR": "Europe",
        "DE": "Europe",
        "AS": "Asie",
        "AF": "Afrique",
        "OC": "Océanie",
        "AN": "Antarctique",
    }
    return continent_mapping.get(country, "N/A")


async def get_zip_code(ip):
    url = f"https://ipinfo.io/{ip}/postal"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return (await response.text()).strip()
    return "N/A"


async def is_vpn(ip):
    url = f"http://ip-api.com/json/{ip}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data.get('proxy', False)
    return False


def set_console_title(title):
    if os.name == 'nt':
        os.system(f'title {title}')


set_console_title("Tool Master-Protocol Version 1.0.0 - Made By Directeur")

init(autoreset=True)


async def main():
    red_text = Fore.RED
    violet_text = Fore.MAGENTA 
    green_text = Fore.GREEN  
    light_blue_text = Fore.LIGHTBLUE_EX  

    while True:
        ip = input(f" -> Enter an IP Address : ")

        if await is_valid_ip(ip):
            ip_info_task = asyncio.create_task(get_ip_info(ip))
            zip_code_task = asyncio.create_task(get_zip_code(ip))
            is_vpn_ip_task = asyncio.create_task(is_vpn(ip))

            ip_data = await ip_info_task
            zip_code = await zip_code_task
            is_vpn_ip = await is_vpn_ip_task

            if ip_data:
                print("")
                print(f"{red_text} X IP Address information :", ip)
                print("")
                print(f"{red_text} Continent :", await get_continent(ip_data.get('country', 'N/A')))
                print(f"{red_text} Country :", ip_data.get('country', 'N/A'))
                print(f"{red_text} Region :", ip_data.get('region', 'N/A'))
                print(f"{red_text} Postal Code :", zip_code)
                print(f"{red_text} City :", ip_data.get('city', 'N/A'))
                print(f"{red_text} Latitude :", ip_data.get('loc', 'N/A').split(',')[0])
                print(f"{red_text} Longitude :", ip_data.get('loc', 'N/A').split(',')[1])
                print(f"{red_text} Organization :", ip_data.get('org', 'N/A'))
                print(f"{red_text} VPN/Proxy :", "Yes" if is_vpn_ip else "No")
                print("")
            else:
                print("")
                print(f"{red_text} X Information not available for this IP Address.")
                print("")
        else:
            print("")
            print(f"{red_text} X Invalid IP Address. Please enter a valid IP Address.")
            print("")

banner = f"""{Fore.RED}
     _                      _______                      _
  _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
 dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
 V      ~"Mb          dOOOOOOOOOOOOOOOOOb          dM"~      V
          `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'
           `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'
      __     `YMMM| OP'~"YOOOOOOOOOOOP"~`YO |MMMP'     __
    ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.
 _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._

             `YMMMM\`OOOo     OOO     oOOO'/MMMMP'
     ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.
   ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
  ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
  MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
  YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP
   `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'
     `'                  `OObNNNNNdOO'                   `'
                           `~OOOOO~'   \n"""

print(banner)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
