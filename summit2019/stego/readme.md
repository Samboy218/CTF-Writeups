## 1% Power
relevant files:
* 1_power.jpg

ezpz, just do `strings 1_power.jpg | grep flag`


## 15% Power
relevant files:
* 15_power.jpg
* extracted_at_0xd110.jpg

use cyberchef `extract files`, there is another jpg hidden in the jpg
the extracted file has the image

## 30% Power
relevant files:
* 30_power.jpeg
* 30_power-extracted.jpg

this one had me for a long time. the hint was "RRRRRAAAAAAAWWWWWWRRRR!!!!!", and I thought it had
something to do with the channels the data was hidden in. I slammed my head against stegsolve for multiple
hours before I really thought about it:

RRRRAAAAWWWWRRR

RAWR

RAR

.rar

just run unrar on the image

## 60% Power
relevant files:
* 60_power.png
* 60_power2.png

this one is pretty cool. I tried the standard stego things to no avail, and then I decided to just look
at the hexdump. At first glance it looks all normal, so I looked into the PNG format for clues.
every PNG has chunks of metadata in the beginning of the file, and all of them need an IHDR chunk which
determines things like the width and height of the image. I noticed that this file has 2 IHDR chunks, which
is not right. Then you can see that there is a string "MEME.PNG", which I thought was just filename metadata, but
the PNG in that string is in the right place to be magic bytes for the second IHDR chunk. I removed all of the data
before the second PNG and voila, there be a flag.

## Final Form
relevant files:
* final_form.png

the hint for this one gave it all away, "you are not the least bit significant against my power. you'll be seeing red by the end of this"
least bit significant, red. Red channel LSB. I used stegsolve to extract this data but at first it didn't work. I examined the red 0 channel
and noticed a weird pattern along the left side of the image, so I extracted the data by column instead of by row and there it was.
