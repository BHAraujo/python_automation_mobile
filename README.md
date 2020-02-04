### Environment Configuration ###

### Install ###

 **Python**
   - url: https://www.python.org/downloads/

 **Pip**   
   - url: https://pip.pypa.io/en/stable/installing/

**Allure Report**
  - url: https://docs.qameta.io/allure/#_installing_a_commandline

 **Android Studio**  
   - url: https://developer.android.com/studio


### Configuration Project ###

## Created environment variable

**Android Studio**
  **Include variable in ~/.bash_profile** <br>
  - export ANDROID_HOME=/Users/<userprofilehere>/Library/Android/sdk
  - export PATH=$PATH:"$PWD":"$ANDROID_HOME/build-tools/29.0.2"
  - export PATH=$PATH:"$PWD":"$ANDROID_HOME/platform-tools"
  - export PATH=$PATH:/Library/Java/JavaVirtualMachines/jdk1.8.0_231.jdk/Contents/Home
  - export PATH=$PATH:"$PWD":"$ANDROID_HOME/emulator"
  - export PATH=$PATH:"$PWD":"$ANDROID_HOME/tools/bin"

**Project** <br>
   **behave.yml** <br>
     - "environment": Environment want to execute test (dev, hml, prod)<br>
     - "os": Operation System Mobile (Android or iOS)<br>

    *service > capabilities*
     -  "android":
            "platformName": "Operation System Mobile"
            "platformVersion": "Version Operation System Mobile"
            "udid": "Id device real"
              - Command Line: adb devices
                  List of devices attached
                    0049195854	device
            "automationName": "uiautomator2"
            "deviceName": "Define name for device"
            "app": "Name apk or ipa, located in folder service > binary"


## Install Dependency ##
   **Command Line:** <br>
      - pip3 install -r requirements.txt

    **Create Emulator**
       - Open Android Studio
       - Click Device Virtual Android(AVD)
       - Create Virtual Device
       - Select anyone device
       - Download image, example: Nougat 9
       - Next
       - Finish


## Execution Project ##
    **Allure Report**
      - All Scenarios:
          - `behave -f allure_behave.formatter:AllureFormatter -o reports/allure_report *.feature`

      - By Tag:
          - `behave -f allure_behave.formatter:AllureFormatter -o reports/allure_report -t @nametag`
