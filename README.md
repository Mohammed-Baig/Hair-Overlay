# Hair-Overlay
Application that lets you try on various styles, such as glasses, hair, facial hair, combinations(custom and premade), etc. Users have the option of adding their own
styles, or using already existing ones. App is regularly updated with new styles as models become available online. Uses live image detection based off of an
XML model used to detect faces to make landmarks and overlay tracking possible. If a certain style doesn't fit on your face, you can always try moving 
your face back and fourth or left and right. If that still doesnt work you can go into the load() function call to adjust the x and y location parameters, as well as
the height and width size parameters. Positive X and Y params move the image left and upwards respectively, and in cases where you don't want to change the size, the 
load_no_resize() function can also be called. In the event that the image is perfectly overlayed in its default position, calling the aformentioned function with a 1 for
X location and 1 for Y location will keep it in its default location. 

EDIT: Finished mix and matching. Updated custom styling. Added randomizing feature

Coming soon: GUI update. Additional styles such as necklaces and wrist watches
