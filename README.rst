Example for an internationalized Kivy Application
=================================================

NOTE: If you have a Windows operating system, your life will be a lot harder.  Luckily, you can follow these directions to be able to automatically generate .po and .mo files!
 1. View the stuff in the "Cygwin info and setup" folder and follow the instructions.
 2. Go to https://poedit.net/ to download Poedit.  This free program allows you to edit .po files. (Poedit is not Poeditor.  Poeditor is an other software that really expensive...)
 3. Whenever you make a change to lang.kv to add more labels/text/buttons/etc., just run the Cygwin terminal and do the command:

Run this command in the Cygwin Terminal::

    cd C:/Users/username/Desktop/....../kivy-change-app--language-en-fr-zh-example-master
    make

Obviously, change the path to whatever folder contains the MakeFile file.

Remember, Ctrl+V doesn't work in Cygwin; instead, you can right-click to paste.



Mac Users Only:
=================================================

Note: _() dynamic changes works only in kv right now.

How to extract _() message and update the po::

    make po

How to generate the locales::

    make mo


I modified the MakeFile to work on Windows.  If this is broken for Macs or Linuxes, woopsiedaisy~~~!  Check out the old fork down below.


Forked Update
==================================================
Forked from https://github.com/jtownley/kivy-gettext-example which was forked from https://github.com/tito/kivy-gettext-example.
All works subject to same copyright as original author
On March 6th 2020 (早晨!)

Goals:
 - A richer interface that demonstrates more text in different widgets
 - Show updating techniques for non kv lang code.

Changes:
 - Removed the Klingon language because that's for nerds
 - Added the Chinese language to demonstrate font switching.
 - Added an in-depth guide on how to do all this .po .mo stuff in Windows with Cygwin.

Completed Goals:
 - The previous fork wanted "Support International characters."  Done!!!!!! :D
 - The previous fork wanted "Add a third language as a learning exercise." Yay!!!!! xD
