### Appium Basics Repo

### Appium installation
- JDK 1.8 must be installed;
- Nodejs 
- Appium GUI
- Android Studio (install sdk package)

Put the following content in `.zprofile`

```
export JAVA_HOME=$(/usr/libexec/java_home -v 1.8.0_311)
export PATH=$PATH:$JAVA_HOME/bin

export ANDROID_HOME=/Users/$(whoami)/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

### Connect real device
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

#### Error, when device is unauthorized
If you see the following:
```➜  ~ adb devices
List of devices attached
9WV4C19221015777	unauthorized
```
1. Detach device
2. Click on phone `Revoke USB debugging authorizations`
3. Run `adb kill-server`
4. Run `adb start-server`


### Debug Mobile Chrome On Computer  
*NB*: for tests in Chrome chromedriver is required.

How to open app in chrome devtools:

`chrome://inspect/#devices`

Then find connected device and click on `Inspect`

### Running emulator
You need to create emulator in Android Studio, ideally with PlayMarket by default 

```
/Users/$(whoami)/Library/Android/sdk/emulator/emulator -avd  Pixel_2_API_30 -netdelay none -netspeed full -dns-server 8.8.8.8 -verbose
```

#### Possible Problems (Mac OS issues)

- if there's no internet connection - create DNS in WI-FI Sections with ip 8.8.8.8
For more info see: https://stackoverflow.com/questions/44535500/internet-stopped-working-on-android-emulator-mac-os
- if emulator is extremely slow, try to reinstall HAXM, see: 
https://github.com/intel/haxm
- increase memory, try different Boost options (quick/slow)
- run device from cmd, not from Android Studio