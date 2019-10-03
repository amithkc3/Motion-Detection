Works on Raspberry Pi PiCamera.

To run:
python3 motion.py 

with preview:
python3 motion.py preview

parameters:
The parameters are optional.But if entered shoult be entered in the same order.
	Note : Also if you want to specify the values of one parameter, you should specify the value of all preceding parameters.
		Example : 1) If you want length_of_recording as 10
		        	"python3 motion.py clip.h264 preview 320x240 10"
			  2) If you want preview set
		        	"python3 motion.py clip.h264 preview"
			  3) If you want specify all 
		        	"python3 motion.py clip.h264 preview 320x240 10 45 28"

ALL COMMAND LINE PARAMETERS (followed by python3 motion.py) in the very same order:
FORMAT :< parameter_name(data_type) : default_value >

1. <preview(str) : preview >		Possible values: "preview" or "no"
					Default: "no"

2. <videoclip_name: *.h264 >		The file type should be .h264 only
					ex: a.h264, b.h264
					Default path: "clips/default_clip.h264"
	
3. <resolution(axb): 320x240>		recommended resolutions:  [160x128, 320x240, 640x480] 
					Note: Higher the resolution lower the efficiency
					Default: "320x240"

4. <length_of_recording(seconds):10>	Possible values: [1,2,3,4,5 ... ] seconds
					Default value: 10 seconds

5. <number_of_pixels_moved(int): 45>

6. <threshold_for_difference_in_pixel_intensity(int) : 28>




NOTE:
The video clips captured are of format h264.
To convert to mp4 "ffmpeg" is needed.
To install "sudo apt install ffmpeg".
To convert the files to mp4 use command:
	ffmpeg -i <input file pathname of format .h264> -c copy <output file pathname>
Example :
	ffmpeg -i myfile.h264 -c copy converted.mp4