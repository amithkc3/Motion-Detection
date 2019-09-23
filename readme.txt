Works on Raspberry Pi PiCamera

To run:
python3 motion.py 320x240 preview

parameters:
	< parameter_name(data_type) : default_value >
	The parameters are optional.But if entered shoult be entered in the same order.
	Note : Also if you want to specify the values of one parameter, you should specify the value of all preceding parameters.
		Example : 1) If you want length_of_recording as 10
		        	"python3 motion.py clip.h264 preview 320x240 10"
			  2) If you want preview set
		        	"python3 motion.py clip.h264 preview"
			  3) If you want specify all 
		        	"python3 motion.py clip.h264 preview 320x240 10 45 28"

ALL COMMAND LINE PARAMETERS (followed by python3 motion.py):
<videoclip_name: *.h264 >		The file type should be .h264 only
					ex: a.h264, b.h264
					Default path: "clips/default_clip.h264"

<preview(str) : preview >		Possible values: "preview" or "no"
					Default: "no"
	
<resolution(axb): 320x240>		recommended resolutions:  [160x128, 320x240, 640x480] 
					Note: Higher the resolution lower the efficiency
					Default: "320x240"

<length_of_recording(seconds):10>	Possible values: [1,2,3,4,5 ... ] seconds
					Default value: 10 seconds

<number_of_pixels_moved(int): 45>

<threshold_for_difference_in_pixel_intensity(int) : 28>