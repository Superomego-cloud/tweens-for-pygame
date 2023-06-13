# tweens-for-pygame

Thanks for downloading this module!

Info:

EasingFunction: Can be any function you want so long as f(0)=0 and f(t)=t. f(f(t)) still follows this condition but makes the easing effect faster  
t: time the tween takes to run.  
d: the distance the tween travels (please note this is a scalar and not a vector)  
obj: The object that will be tweened (will be changed to take *pygame.Rect* as argument)  
dirList: This is the vector your tween is supposed to follow (calculate the trajectory with d x dirList)  
reverse: Optionnal argument, set to *True* if you want your tween to reverse
