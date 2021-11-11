## simple script for converting .trs files to .srt

Transcriptions from services like [Transcriber](http://trans.sourceforge.net/en/presentation.php) can sometimes be produced in an XML format called TRS (`.trs`)

Timestamped transcriptions contained in formats such as `.trs` can be paired with their media in a video player as subtitles, yet need to be in a valid subtitle format such as `.vtt` or `.srt`.

Services which perform the conversion between `.trs` and `.srt` are hard to find. This script does that.

### instructions

Simply download the script and, from the command line and inside the directory in which the script was downloaded, enter your python interpreter command, followed by the script name and then the file you want to convert (`python convert.py 'transcription_1.trs'`). Make sure the file you want to convert is in this directory.

The output `.srt` file can then be found in the same directory.
