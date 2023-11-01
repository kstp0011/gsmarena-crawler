import yaml
import pandas as pd
import os
import requests
from bs4 import BeautifulSoup
import time
from crawlBranch import convertTime


# get html from url
def getPageContent(url):
    r = requests.get(url)
    return BeautifulSoup(r.text, 'html.parser')

# parse data from html to get phone specs


def parseDeviceData(soup) -> list:
    # get image url
    try:
        imgUrl = soup.find('div', class_='specs-photo-main').find('img')['src']
    except:
        imgUrl = None

    # get name
    try:
        Name = soup.find('h1', class_='specs-phone-name-title').text
    except:
        Name = None

    # NETWORK section
    # get technology
    try:
        NETWORK_Technology = soup.find(
            'a', attrs={'data-spec': 'nettech'}).text
    except:
        NETWORK_Technology = None

    # get 2G bands
    try:
        NETWORK_2G_bands = soup.find('td', attrs={'data-spec': 'net2g'}).text
    except:
        NETWORK_2G_bands = None

    # get 3G bands
    try:
        NETWORK_3G_bands = soup.find('td', attrs={'data-spec': 'net3g'}).text
    except:
        NETWORK_3G_bands = None

    # get 4G bands
    try:
        NETWORK_4G_bands = soup.find('td', attrs={'data-spec': 'net4g'}).text
    except:
        NETWORK_4G_bands = None

    # get 5G bands
    try:
        NETWORK_5G_bands = soup.find('td', attrs={'data-spec': 'net5g'}).text
    except:
        NETWORK_5G_bands = None

    # get GPRS
    try:
        NETWORK_GPRS = soup.find('td', attrs={'data-spec': 'gprstext'}).text
    except:
        NETWORK_GPRS = None

    # get EDGE
    try:
        NETWORK_EDGE = soup.find('td', attrs={'data-spec': 'edge'}).text
    except:
        NETWORK_EDGE = None

    # get Speed
    try:
        NETWORK_Speed = soup.find('td', attrs={'data-spec': 'speed'}).text
    except:
        NETWORK_Speed = None

    # LAUNCH section
    # get Announced
    try:
        LAUNCH_Announced = soup.find('td', attrs={'data-spec': 'year'}).text
    except:
        LAUNCH_Announced = None

    # get Status
    try:
        LAUNCH_Status = soup.find('td', attrs={'data-spec': 'status'}).text
    except:
        LAUNCH_Status = None

    # BODY section
    # get Dimensions
    try:
        BODY_Dimensions = soup.find(
            'td', attrs={'data-spec': 'dimensions'}).text
    except:
        BODY_Dimensions = None

    # get Weight
    try:
        BODY_Weight = soup.find('td', attrs={'data-spec': 'weight'}).text
    except:
        BODY_Weight = None

    # get Build
    try:
        BODY_Build = soup.find('td', attrs={'data-spec': 'build'}).text
    except:
        BODY_Build = None

    # get SIM
    try:
        BODY_SIM = soup.find('td', attrs={'data-spec': 'sim'}).text
    except:
        BODY_SIM = None

    # DISPLAY section
    # get Type
    try:
        DISPLAY_Type = soup.find('td', attrs={'data-spec': 'displaytype'}).text
    except:
        DISPLAY_Type = None

    # get Size
    try:
        DISPLAY_Size = soup.find('td', attrs={'data-spec': 'displaysize'}).text
    except:
        DISPLAY_Size = None

    # get Resolution
    try:
        DISPLAY_Resolution = soup.find(
            'td', attrs={'data-spec': 'displayresolution'}).text
    except:
        DISPLAY_Resolution = None

    # get Protection
    try:
        DISPLAY_Protection = soup.find(
            'td', attrs={'data-spec': 'displayprotection'}).text
    except:
        DISPLAY_Protection = None

    # PLATFORM section
    # get OS
    try:
        PLATFORM_OS = soup.find('td', attrs={'data-spec': 'os'}).text
    except:
        PLATFORM_OS = None

    # get Chipset
    try:
        PLATFORM_Chipset = soup.find('td', attrs={'data-spec': 'chipset'}).text
    except:
        PLATFORM_Chipset = None

    # get CPU
    try:
        PLATFORM_CPU = soup.find('td', attrs={'data-spec': 'cpu'}).text
    except:
        PLATFORM_CPU = None

    # get GPU
    try:
        PLATFORM_GPU = soup.find('td', attrs={'data-spec': 'gpu'}).text
    except:
        PLATFORM_GPU = None

    # MEMORY section
    # get Card slot
    try:
        MEMORY_Card_slot = soup.find(
            'td', attrs={'data-spec': 'memoryslot'}).text
    except:
        MEMORY_Card_slot = None

    # get Internal
    try:
        MEMORY_Internal = soup.find(
            'td', attrs={'data-spec': 'internalmemory'}).text
    except:
        MEMORY_Internal = None

    # MAIN CAMERA section
    # get cam 1 module type
    try:
        MAIN_CAM_1_Module = str(
            soup.find('td', attrs={'data-spec': 'cam1modules'}))
        if len(MAIN_CAM_1_Module) > 47:
            MAIN_CAM_1_Module = len(MAIN_CAM_1_Module.split('<br>'))
        else:
            MAIN_CAM_1_Module = 0
    except:
        MAIN_CAM_1_Module = None

    # get cam 1 features
    try:
        MAIN_CAM_1_Features = soup.find(
            'td', attrs={'data-spec': 'cam1features'}).text
    except:
        MAIN_CAM_1_Features = None

    # get cam 1 video
    try:
        MAIN_CAM_1_Video = soup.find(
            'td', attrs={'data-spec': 'cam1video'}).text
    except:
        MAIN_CAM_1_Video = None

    # SELFIE CAMERA section
    # get cam 2 module type
    try:
        SELFIE_CAM_2_Module = str(
            soup.find('td', attrs={'data-spec': 'cam2modules'}))
        if len(SELFIE_CAM_2_Module) > 47:
            SELFIE_CAM_2_Module = len(SELFIE_CAM_2_Module.split('<br>'))
        else:
            SELFIE_CAM_2_Module = 0
    except:
        SELFIE_CAM_2_Module = None

    # get cam 2 features
    try:
        SELFIE_CAM_2_Features = soup.find(
            'td', attrs={'data-spec': 'cam2features'}).text
    except:
        SELFIE_CAM_2_Features = None

    # get cam 2 video
    try:
        SELFIE_CAM_2_Video = soup.find(
            'td', attrs={'data-spec': 'cam2video'}).text
    except:
        SELFIE_CAM_2_Video = None

    # SOUND section
    # get Loudspeaker
    try:
        SOUND_Loudspeaker = soup.find('a', attrs={'href': 'glossary.php3?term=loudspeaker'}).find_parent(
            'tr').find('td', class_='nfo').text
    except:
        SOUND_Loudspeaker = None

    # get 3.5mm jack
    try:
        SOUND_35mm_jack = soup.find('a', attrs={
                                    'href': 'glossary.php3?term=audio-jack'}).find_parent('tr').find('td', class_='nfo').text
    except:
        SOUND_35mm_jack = None

    # COMMS section
    # get WLAN
    try:
        COMMS_WLAN = soup.find('td', attrs={'data-spec': 'wlan'}).text
    except:
        COMMS_WLAN = None

    # get Bluetooth
    try:
        COMMS_Bluetooth = soup.find(
            'td', attrs={'data-spec': 'bluetooth'}).text
    except:
        COMMS_Bluetooth = None

    # get GPS
    try:
        COMMS_GPS = soup.find('td', attrs={'data-spec': 'gps'}).text
    except:
        COMMS_GPS = None

    # get NFC
    try:
        COMMS_NFC = soup.find('td', attrs={'data-spec': 'nfc'}).text
    except:
        COMMS_NFC = None

    # get Radio
    try:
        COMMS_Radio = soup.find('td', attrs={'data-spec': 'radio'}).text
    except:
        COMMS_Radio = None

    # get USB
    try:
        COMMS_USB = soup.find('td', attrs={'data-spec': 'usb'}).text
    except:
        COMMS_USB = None

    # FEATURES section
    # get Sensors
    try:
        FEATURES_Sensors = soup.find('td', attrs={'data-spec': 'sensors'}).text
    except:
        FEATURES_Sensors = None

    # BATTERY section
    # get Type
    try:
        BATTERY_Type = soup.find(
            'td', attrs={'data-spec': 'batdescription1'}).text
    except:
        BATTERY_Type = None

    # get Stand by
    try:
        BATTERY_Stand_by = soup.find(
            'td', attrs={'data-spec': 'batstandby1'}).text
    except:
        BATTERY_Stand_by = None

    # get Talk time
    try:
        BATTERY_Talk_time = soup.find(
            'td', attrs={'data-spec': 'battalktime1'}).text
    except:
        BATTERY_Talk_time = None

    # get Music play
    try:
        BATTERY_Music_play = soup.find(
            'td', attrs={'data-spec': 'batmusicplayback1'}).text
    except:
        BATTERY_Music_play = None

    # MISC section
    # get Colors
    try:
        MISC_Colors = soup.find('td', attrs={'data-spec': 'colors'}).text
    except:
        MISC_Colors = None

    # get SAR
    try:
        MISC_SAR = soup.find('td', attrs={'data-spec': 'sar-us'}).text
    except:
        MISC_SAR = None

    # get SAR EU
    try:
        MISC_SAR_EU = soup.find('td', attrs={'data-spec': 'sar-eu'}).text
    except:
        MISC_SAR_EU = None

    # get Models
    try:
        MISC_Models = soup.find('td', attrs={'data-spec': 'models'}).text
    except:
        MISC_Models = None

    # get Price
    try:
        MISC_Price = soup.find('td', attrs={'data-spec': 'price'}).text
    except:
        MISC_Price = None

    return [imgUrl,
            Name,
            NETWORK_Technology,
            NETWORK_2G_bands,
            NETWORK_3G_bands,
            NETWORK_4G_bands,
            NETWORK_5G_bands,
            NETWORK_GPRS,
            NETWORK_EDGE,
            NETWORK_Speed,
            LAUNCH_Announced,
            LAUNCH_Status,
            BODY_Dimensions,
            BODY_Weight,
            BODY_Build,
            BODY_SIM,
            DISPLAY_Type,
            DISPLAY_Size,
            DISPLAY_Resolution,
            DISPLAY_Protection,
            PLATFORM_OS,
            PLATFORM_Chipset,
            PLATFORM_CPU,
            PLATFORM_GPU,
            MEMORY_Card_slot,
            MEMORY_Internal,
            MAIN_CAM_1_Module,
            MAIN_CAM_1_Features,
            MAIN_CAM_1_Video,
            SELFIE_CAM_2_Module,
            SELFIE_CAM_2_Features,
            SELFIE_CAM_2_Video,
            SOUND_Loudspeaker,
            SOUND_35mm_jack,
            COMMS_WLAN,
            COMMS_Bluetooth,
            COMMS_GPS,
            COMMS_NFC,
            COMMS_Radio,
            COMMS_USB,
            FEATURES_Sensors,
            BATTERY_Type,
            BATTERY_Stand_by,
            BATTERY_Talk_time,
            BATTERY_Music_play,
            MISC_Colors,
            MISC_SAR,
            MISC_SAR_EU,
            MISC_Models,
            MISC_Price]


# Main function
# get all phone specs
def crawlAllPhoneSpecs(config):
    # load all device url
    DeviceUrls = pd.read_csv(os.path.join(
        config['SavePath'], config['AllDevicesUrlsFileName'] + ".csv"))

    phoneSpecs = []
    print("Start crawling phone specs")
    startTime = time.time()

    # get all phone specs
    for i in range(len(DeviceUrls)):
        url = DeviceUrls['DeviceUrl'][i]
        soup = getPageContent(url)
        phoneSpecs.append(parseDeviceData(soup))
        time.sleep(0.15)

        if i % 100 == 0:
            print(i, "devices crawled")

    print("Total devices crawled:", len(DeviceUrls))
    print("Total time:", convertTime(time.time() - startTime))

    savePhoneSpecs(config, phoneSpecs)


# Util function
def savePhoneSpecs(config, phoneSpecs):
    columns = ['imgUrl', 'Name', 'NETWORK_Technology', 'NETWORK_2G_bands', 'NETWORK_3G_bands', 'NETWORK_4G_bands', 'NETWORK_5G_bands', 'NETWORK_GPRS', 'NETWORK_EDGE', 'NETWORK_Speed', 'LAUNCH_Announced', 'LAUNCH_Status', 'BODY_Dimensions', 'BODY_Weight', 'BODY_Build', 'BODY_SIM', 'DISPLAY_Type', 'DISPLAY_Size', 'DISPLAY_Resolution', 'DISPLAY_Protection', 'PLATFORM_OS', 'PLATFORM_Chipset', 'PLATFORM_CPU', 'PLATFORM_GPU', 'MEMORY_Card_slot',
               'MEMORY_Internal', 'MAIN_CAM_1_Module', 'MAIN_CAM_1_Features', 'MAIN_CAM_1_Video', 'SELFIE_CAM_2_Module', 'SELFIE_CAM_2_Features', 'SELFIE_CAM_2_Video', 'SOUND_Loudspeaker', 'SOUND_35mm_jack', 'COMMS_WLAN', 'COMMS_Bluetooth', 'COMMS_GPS', 'COMMS_NFC', 'COMMS_Radio', 'COMMS_USB', 'FEATURES_Sensors', 'BATTERY_Type', 'BATTERY_Stand_by', 'BATTERY_Talk_time', 'BATTERY_Music_play', 'MISC_Colors', 'MISC_SAR', 'MISC_SAR_EU', 'MISC_Models', 'MISC_Price']
    df = pd.DataFrame(phoneSpecs, columns=columns)
    df.to_csv(os.path.join(
        config['SavePath'], config['DevicesSpecsFileName'] + ".csv"), index=False)


if __name__ == "__main__":
    # load config
    with open('crawler\config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    crawlAllPhoneSpecs(config)
