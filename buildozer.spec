[app]

# (str) Title of your application
title = Dice Roller

# (str) Package name
package.name = diceroller

# (str) Package domain (reverse DNS)
package.domain = org.example

# (str) Source code where main.py is located
source.dir = .

# (list) Extensions to include
source.include_exts = py,png,kv,wav

# (str) Main .py file
source.main = main.py

# (str) Application versioning
version = 1.0

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Icon of the application
# icon.filename = %(source.dir)s/icon.png

# (str) Supported platforms
osx.kivy_version = 2.2.0

# (list) Permissions
android.permissions = INTERNET

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme
android.theme = @android:style/Theme.NoTitleBar

# (str) Android requirements (dependencies)
requirements = python3,kivy

# (bool) Include source in apk
android.include_src = false

# (bool) Hide logcat on start
log_level = 2

# (bool) Copy library instead of linking
android.copy_libs = 1

# (str) Package format for release
# Supported formats: aar, apk, aab
android.package_format = apk

# (bool) Enable Android X support
android.enable_androidx = 1

# (bool) Android NDK (leave blank for default)
# android.ndk = 

# (str) Android SDK API to build with
android.api = 31

# (str) NDK API
android.ndk_api = 21

# (list) Presplash screen
# presplash.filename = %(source.dir)s/data/presplash.png

# (list) Additional Java .jars to add
# android.add_jars = 

# (str) Architectures to build for
# For most phones, arm64-v8a is preferred
android.archs = arm64-v8a, armeabi-v7a

# (bool) Use SDL2 instead of pygame
use.sdl2 = True

# (bool) Enable/disable keyboard
android.keyboard_mode = system

# (str) Entry point for your app (.py file name)
# Already defined above with source.main = main.py

# (list) Patterns to exclude from the app package
exclude_patterns = *.zip,*.pyc,*.swp,*.git,*.hg,*.svn

# (str) Path to your key.properties for release signing
# android.release_key.properties = 

# (str) Keystore to sign app (optional for debug)
# android.keystore = 

# (str) Minimum API level
android.minapi = 21

# (str) Target API level
android.target = 31