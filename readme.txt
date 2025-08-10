install Java JDK
Appium needs Java for Android automation.

Set Environment Variables:

JAVA_HOME → C:\Program Files\Java\jdk-xx.x.x

Add to Path → %JAVA_HOME%\bin

Install Node.js
Appium server runs on Node.js.

Download from: https://nodejs.org/ (LTS version recommended)
Install (default location fine)
node -v
npm -v

Install Appium Server
Using npm:
npm install -g appium
appium --version

Install Appium Drivers
Install necessary drivers for Android/iOS:

appium driver install uiautomator2   # Android

Go to https://inspector.appiumpro.com/

Install Android SDK Platform
Install Android SDK Tools

Set Environment Variables:

ANDROID_HOME → C:\Users\<YourUser>\AppData\Local\Android\Sdk
Add to Path:
%ANDROID_HOME%\tools
%ANDROID_HOME%\tools\bin
%ANDROID_HOME%\platform-tools

adb version
Checks if everything is set up correctly:
npm install -g appium-doctor
appium-doctor --android

Start appium server:
appium --allow-cors

Connect device:
enable developer option in device
Enable usb debugging from developer option
connect device with USB

[Execution]

to execute all test and generate report run below command:
cd tests
pytest -s -v --html=./report/report.html

To group test cases and run test use below command
cd tests
pytest -s -v -m login --html=./report/report.html
