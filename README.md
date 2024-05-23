QDN is Qbittorrent Discord (webhook) Notifier

Just edit the message in the code and put your webhook url in it.
Use the declared variables above in the message as you wish.
You will need pyinstaller and requests to compile this script.
After compilation, move the .exe into a safe place (so you won't delete it by accident) and then put the following into the qbittorrent space for the script:
<code> yourpathhere\notification.exe "%N" "%L" "%G" "%F" "%R" "%D" "%C" "%Z" "%T" "%I" "%J" "%K" </code>
