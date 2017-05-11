import math

x=0;z=0;
for i in range(1, 11):
	print('''
	<div id="slide%i" class="step slide transleft" data-x="%i" data-rotate-y="%i" data-z="-%i">
	    Hello Dude
	</div>
	''' % (i, x, (i*36), z))
	x += math.cos(math.radians(i*36)) * 900
	z += math.sin(math.radians(i*36)) * 900