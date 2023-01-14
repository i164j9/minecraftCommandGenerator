from tunnel import Tunnel
# This file is for demonstration purposes
# I created this because I enjoy creating things in creative mode in Minecraft.
# It works, but on my laptop when performance begins to lag from the system
# getting hot, commands are sometimes missed or not completed, this can be compensated
# for by adjusting the time delay between entry of commands (delay = 5)and adjusting
# the typeWrite interval (pyautogui.typewrite(newCmds[i],interval=0.01)) in tunnel.py.
# I have not tested with Minecraft for windows only the java edition.
# eventually I plan on adding GUI functionality.
# all commands are written out to a text file, however with every
# generation of commands the file is overwritten. if you want to keep the generated
# commands you will need to cut or copy the file(commands.txt) to an alternate location

# To use this as it sits, you simply need to fill in your own
# start and ending coordinate values using the list provided below.
# in the constructor Tunnel() you need to provide two commands,
# the list of coordinate values, the two block you will be using and
# the direction of travel. The reason for two commands is maybe your second
# command may be a 'replace' command versus the 'fill' command.
# and finally the direction of travel.

# simply run main.py and the switch to your minecraft instance and wait.
# it will begin entering commands and executing them.

# I know it's inconvient but at this time it starts you at the greatest distance
# not your point of origin. unless your going negative like north or west.

# Without any changes below this will generate a 'lined' tunnel using glass.
# It takes your entered coordinate values and expands them by 1, then generates
# the coordinates in 100 block increments then generates 'fill' commands.
# The next step it generates new coordinates using the original values,
# and once again generates new 'fill' commands to hollow out the tunnel.
# then it generates 'teleport' commands.

# keep in mind that the maximum volume that can be cleared at one time is 32768
# I am not checking for volume limitation yet but it is calculated and displayed to you.
# what is displayed currently, is the total volume of blocks to be cleared.

# example:
# volumetric displacement: 237666 blocks to be replaced

# example:
# teleport @p -26400 45 10
# fill -26400 51 11 -26500 44 -1 glass
# fill -26400 50 10 -26500 45 0 air
# teleport @p -26500 45 10
# fill -26500 51 11 -26600 44 -1 glass
# fill -26500 50 10 -26600 45 0 air
# teleport @p -26600 45 10
# fill -26600 51 11 -26700 44 -1 glass
# fill -26600 50 10 -26700 45 0 air
# teleport @p -26700 45 10
# fill -26700 51 11 -26800 44 -1 glass
# fill -26700 50 10 -26800 45 0 air

#                x   y    z     x   y    z
#mycoordinates=[5318,113,-3326,5323,118,-3872]
#mycoordinates=[5260,50,0, 5255,45,-30000]#north
#mycoordinates=[5242, 45, 0, 5252, 50, 31000]#south
#mycoordinates=[5253, 45, 0, 30000, 50, 10]#east
mycoordinates=[-26400, 45, 0, -30000, 50, 10]#west
t = Tunnel('fill','fill', mycoordinates,'air','glass','w')

