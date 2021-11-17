# Appium Basics Repo

## Appium installation
- JDK 1.8 must be installed ( 1.8.0_251 works fine);
- Nodejs 
- Appium GUI
- Android Studio (install sdk package)

Put the following content in `.zprofile`

```
export JAVA_HOME=$(/usr/libexec/java_home -v 1.8.0_251)
export PATH=$PATH:$JAVA_HOME/bin

export ANDROID_HOME=/Users/$(whoami)/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

### Check of Appium installation
To verify appium installation, `appium-doctor` is used. Installed via npm. See for detailed info:
https://github.com/appium/appium-doctor

Just simply run `appium-doctor` in cmd and verify output.
### Install Appium via npm
`npm install -g appium`

Usually appium from npm is installed with *separated installed* chromedriver.
To ge the latest one, run:

`npm install -g appium --chromedriver_version="<desired_version_num>"`

Or you can simply specify to download chromedirver automatically:

```appium --allow-insecure chromedriver_autodownload```

All chromedrivers of appium npm will be found:

```/usr/local/lib/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac```

After that appium will be available via command line.
You can start appium like(in example port is specified):

```appium -p 4274```

### Start Appium
- Via Appium Server Gui - need only click btn "Start Server...";
- Via npm - see section above;
- Programmatically - see `test_appium_starts_itself.py` for details

### Stop Appium
`lsof -P | grep ':<port-num>' | awk '{print $2}' | xargs kill -9`


## Connect real device
- Enable developer mode. 
- Allow debugging on USB connection. 
- Connect to computer and select `Transfer files`
- Run `adb devices` - you see message like:
```➜  ~ adb devices
List of devices attached
9WV4C19221015777	device
```
- Start Appium Server
- Run your tests

### Error, when device is unauthorized
If you see the following:
```➜  ~ adb devices
List of devices attached
9WV4C19221015777	unauthorized
```
1. Detach device
2. Click on phone `Revoke USB debugging authorizations`
3. Run `adb kill-server`
4. Run `adb start-server`


## Debug Mobile Chrome On Computer  
*NB*: for tests in Chrome chromedriver is required.

How to open app in chrome devtools:

`chrome://inspect/#devices`

Then find connected device and click on `Inspect`

## Running emulator
You need to create emulator in Android Studio, ideally with PlayMarket by default 

To get emulator name, please run:
```
emulator -list-avds
```
After that you need to run the following:
```
/Users/$(whoami)/Library/Android/sdk/emulator/emulator -avd  Pixel_2_API_30 -netdelay none -netspeed full -dns-server 8.8.8.8 -verbose
```

### Possible Problems (Mac OS issues)

- if there's no internet connection - create DNS in WI-FI Sections with ip 8.8.8.8
For more info see: https://stackoverflow.com/questions/44535500/internet-stopped-working-on-android-emulator-mac-os
- if emulator is extremely slow, try to reinstall HAXM, see: 
https://github.com/intel/haxm
- increase memory, try different Boost options (quick/slow)
- run device from cmd, not from Android Studio

### Test native App
- connect real device;
- launch desired apk;
- run `adb shell`;
- in shell run `dumpsys window windows | grep -E 'mCurrentFocus'`
or `dumpsys window windows | grep -E 'mTopActivityComponent'` 
- From output:
```  
mCurrentFocus=Window{99846e8 u0 com.android.contacts/com.android.contacts.activities.DialtactsActivity}
```
before slash is package name and after slash is package activity. Add them in desired_caps instead of browser:
```
    desired_caps = dict(
    deviceName='Android',
    platformName='Android',
    appPackage='com.android.contacts',
    appActivity='com.android.contacts.activities.DialtactsActivity'
)
```
### Run Appium Inspector
To get locators, XPaths, etc. 
#### Installation
https://github.com/appium/appium-inspector/
#### Running
1. Start Appium Server
2. Connect Device
3. Open App for debug
4. Open Appium Inspector
5. In Appium Inspector add Capabilities, like:
```
{
  "appium:deviceName": "Android",
  "platformName": "Android",
  "appium:appPackage": "com.android.contacts",
  "appium:appActivity": "com.android.contacts.activities.DialtactsActivity"
}
```
6. Add Remote Path value `/wd/hub`
7. Start the Session

### uiautomatorviewer
- Open app, which locators are needed.
- Run in terminal:
```uiautomatorviewer```
- Make snapshot 
- If no errors occurred, you see app with locators
- If it doesn't work, verify JDK version

### APK installation on device
``` 
adb -s  <device_id> install <path_to_apk_file>
```
To uninstall package
```
adb uninstall <package_name>
```
package_name can be found via `dumpsys` command (see above)

#### How to pull APK from device
```
adb shell pm list packages
```
Then run to get package path on device
```adb shell pm path <package-name>```

Finally, pull apk:
```
adb pull <path-to-apk-on-device> <path-local-to-save>
```