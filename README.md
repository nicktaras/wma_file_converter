# audio_converter

a pyton script to convert audio files

![alt text](https://raw.githubusercontent.com/nicktaras/audio_converter/master/Screenshot%202020-03-02%20at%2022.39.23.png?raw=true)

## Alternatively ftransc can be used via the command line like so:

1. brew install ffmpeg lame
3. pip install ftransc
3. Run a test after installation, run `ftransc -f mp3 filename.wma`
4. Then run against a whole directory run `ftransc -f wma --directory /path/to/folder_name`

## Supported files ftransc

| tag	        | m4a | mp3 | ogg	| flac | wma | mpc | wav | wv | 
| ----------- |:---:|:---:|:---:|:----:|:---:|:---:|:---:|:--:|
| title	      |  Y	|  Y	|  Y	| Y	   | Y   |	Y	 |  N	 | Y  |
| artist      |  Y	|  Y	|  Y	| Y	   | Y   |	Y	 |  N	 | Y  |
| album	      |  Y	|  Y	|  Y	| Y	   | Y   |	Y	 |  N	 | Y  |
| genre	      |  Y	|  Y	|  Y	| Y	   | Y   |	Y	 |  N	 | Y  |
| date	      |  Y	|  Y	|  Y	| Y	   | Y   |	Y	 |  N	 | Y  |
| tracknumber	|  Y	|  Y	|  Y	| Y	   | Y   |	Y	 |  N	 | Y  |
| composer	  |  Y	|  Y	|  Y	| Y	   | Y   |	Y	 |  N	 | N  |
| publisher	  |  N	|  Y	|  N	| N	   | Y   |	N	 |  N	 | N  |
| lyrics	    |  Y	|  Y	|  N	| N	   | Y   |	N	 |  N	 | N  |
| album art	  |  Y	|  Y	|  N	| Y	   | N   |	N	 |  N	 | N  |
| album artist|	 N  |  N	|  N	| N	   | N   |	N	 |  N	 | N  |
| comment	    |  N	|  N	|  N	| N	   | N   |	N	 |  N	 | N  |

## ftransc Library

https://pypi.org/project/ftransc/

## reading

https://docs.python.org/3/library/tk.html

https://www.tutorialspoint.com/python3/python_files_io.htm

https://data-flair.training/blogs/python-best-practices/

## util

https://github.com/navdeep-G/samplemod

https://www.python-boilerplate.com/py3+executable+gitignore+unittest

## Application development steps:

1. Create a dialog UI that will house all of the components.
2. Include a browse button to select the source folder.
3. Store the source folder value.
4. Include drop down to select the conversion type e.g. wma > mp3
5. Store the type value.
6. Include button to start the process.
7. Notify the end user when the conversion is complete.


