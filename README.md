# text2pic
A simple Flask app that converts text into images

Usage:
Send a JSON object via POST to /text2pic 

JSON example
```
data = {
	'text': 'The (plain) text to put into images',
	'width': 800,
	'height': 600,
	'margin-width': 100,
	'margin-height': 50,
	'font': 'arial.ttf',
	'font-size': 32
}
```

Width and height represent the size (in pixels) of the output images.
The margin attributes tell the algorithm to leave a margin (in pixels) and 
print text only in the inner box. 

text, width and height parameters are mandatory.
The others are optionals with the following default values:
	'margin-width': 0,
	'margin-height': 0,
	'font': 'arial.ttf',
	'font-size': 32


```
<br>
<p>
  <----------------- WIDTH -----------------------><br>
  <-m_w->                                   <-m_w-><br>
^^                                                 ^^<br>
||                                                 ||<br>
|m                                                 m|<br>
|h                                                 h|<br>
||                                                 ||<br>
|v       ___________________________________       v|<br>
|        |AAAAAAAA AAAAAAAAAAAA AAAAAAAAA  A|       |<br>
H        |AAA BBBBBBB BBBBBBBBBBBBBBB bbb b |       |<br>
E        |AAAAA AAAAAAAAA AAAAAAAAA a BBBBBB|       |<br>
I        |C CCCCCCC CCC...                  |       |<br>
G        |                                  |       |<br>
H        |                                  |       |<br>
T        |                                  |       |<br>
|        |__________________________________|       |<br>
|^                                                 ^|<br>
||                                                 ||<br>
|m                                                 m|<br>
|h                                                 h|<br>
||                                                 ||<br>
vv                                                 vv<br>
  <----------------- WIDTH -----------------------><br>
  <-m_w->                                   <-m_w-><br>
<br>
</p>
```

The algorithm will try to split the text in lines that will fit
in the inner box between margins and then put each line into 
the image. If all the lines don´t fit into a single image it 
will create more images as needed.

The text will be white over a black background.

TODO: add text color and background color as JSON input parameters