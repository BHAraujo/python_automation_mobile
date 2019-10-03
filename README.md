# python_automation_mobile
Automation APK with Python, Appium, Selenium, Pyhamcrest and Behave


### Configuration Environment ###

## Java ##

*1 - Download Java*<br>
  **URL:** https://www.java.com/pt_BR/download/

*2 - Variable Environment*<br>  

  - JAVA_HOME /usr/lib/jvm/java-8-oracle    


## Android Studio ##

*1 - Downlaod Android Studio*<br>
   **Url:** https://developer.android.com/studio

*2 - Variable Environment*<br>
    **Terminal Command:**<br>
      
      - export ANDROID_HOME=/home/<profileuser>/Android/Sdk

      - export uiautomatorviewer=/home/<profileuser>/Android/Sdk/tools/bin/uiautomatorviewer

      - export adb=/home/<profileuser>/Android/Sdk/platform-tools/adb

      - export emulator=/home/<profileuser>/Android/Sdk/tools/emulator

*3 - Create Emulator*
   - Open Android Studio
   - Click Device Virtual Android(AVD)
   - Create Virtual Device
   - Select anyone device
   - Download image, example: Nougat 7.1
   - Next
   - Finish  


## Project ##

*1 - Download project*<br>
    **Url:** https://github.com/BHAraujo/python_automation_mobile

*2 - Install Python > 3.5*<br>
    Url: https://www.python.org/downloads/

*3 - Install Client Appium*<br>
   **Url:** http://appium.io/docs/en/about-appium/getting-started/ <br>
    Obs: To install client Appium you must get installed Node.js

*4 - Install libs*<br>
   **Terminal Command:**<br>
      - pip3 install -r requirements.txt


# Run project #<br>

*1 - Appium*<br>
    appium

*2 - Emulator* <br>
    - emulator --list-avds <br>
    - emulator @<nameemulator>

*3 - Run BDD*<br>
    - behave



Developer: Bruno Henrique Araujo<br>
E-mail: lbruno.araujo@hotmail.com<br>
Github: BHAraujo    
