# audio_converter

a pyton script to convert audio files

## Alternatively ftransc can be used via the command line like so:

1. brew install ffmpeg lame
3. pip install ftransc
3. Run a test after installation, run `ftransc -f mp3 filename.wma`
4. Then run against a whole directory run `ftransc -f wma --directory /path/to/folder_name`

## Supported files ftransc

tag	         m4a	mp3	ogg	flac	wma	mpc	wav	wv
title	        Y	   Y	 Y	  Y	   Y	 Y	 N	Y
artist        Y	   Y	 Y	  Y	   Y	 Y	 N	Y
album	        Y	   Y	 Y	  Y	   Y	 Y	 N	Y
genre	        Y	   Y	 Y	  Y	   Y	 Y	 N	Y
date	        Y	   Y	 Y	  Y	   Y	 Y	 N	Y
tracknumber	  Y	   Y	 Y	  Y	   Y	 Y	 N	Y
composer	    Y	   Y	 Y	  Y	   Y	 Y	 N	N
publisher	    N	   Y	 N	  N	   Y	 N	 N	N
lyrics	      Y	   Y	 N	  N	   Y	 N	 N	N
album art	    Y	   Y	 N	  Y	   N	 N	 N	N
album artist	N	   N	 N	  N	   N	 N	 N	N
comment	      N	   N	 N	  N	   N	 N	 N	N

## ftransc Library

https://pypi.org/project/ftransc/