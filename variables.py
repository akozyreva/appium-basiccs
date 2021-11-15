from pathlib import Path

desired_caps_real_device = dict(
    deviceName="HUAWEI P20 Lite",
    udid="9WV4C19221015777",
    platformName="Android",
    platformVersion="9",
)
desired_caps_emulator = dict(
    deviceName='Android',
    platformName='Android',
)
desired_caps_chrome = dict(
    browserName='Chrome',
    locale='GB',
    language='en'
)
desired_caps_real_device_chrome = {**desired_caps_real_device, **desired_caps_chrome}
desired_caps_emulator_chrome = {**desired_caps_emulator, **desired_caps_chrome}

PROJECT_DIR = Path(__file__).absolute().parent