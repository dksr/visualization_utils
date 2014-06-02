#!/usr/bin/env python

"""image_player.py: Shows a bunch of images as a movie."""

__author__      = "Krishna Dubba"

import sys

def image_player(argv=None):
    import os
    import time
    from optparse import OptionParser
    
    import pygame
    from pygame.locals import KEYUP, KEYDOWN, K_SPACE, K_LEFT, K_RIGHT
    
    if len(sys.argv) == 1:
        sys.argv.append('-help')
    
    parser = OptionParser("usage: %prog [options]")
    parser.add_option("-i", "--im_dir",   dest="im_dir",   default="",  help="images directory")
    parser.add_option("-d", "--delay",    dest="delay",    default="0", help="Delay in showing frames")
    parser.add_option("-e", "--im_ext",   dest="im_ext",   default="jpg",    help="image extension (jpg by default)")
    parser.add_option("-s", "--size",     dest="img_size", default="640:420",help="image size (640:384)")
    parser.add_option("-t", "--delta",    dest="delta",    default="50",     help="Num of frames to jump")
    
    # Process command line and config file options
    (options, args) = parser.parse_args(sys.argv)
    
    im_dir = options.im_dir
    im_ext = options.im_ext
    delay  = int(options.delay)
    delta  = int(options.delta)    
    size   = options.img_size.split(':')
    
    # Start the show!
    pygame.init()
    display_width  = int(size[0])
    display_height = int(size[1])
    screen = pygame.display.set_mode( (display_width, display_height) )
            
    def display_frame(frame, frame_number):
        fr = pygame.image.load(fname)
        loaded_img_w, loaded_img_h = fr.get_size()
        if loaded_img_w != display_width or loaded_img_h != display_height:
            print 'Error: Loaded image size not same as display size, use option "s" to set correct size'
            print loaded_img_w, loaded_img_h
            sys.exit()
        screen.blit( fr, (0,0) )
        
        frame_font = pygame.font.Font(None, 30)
        text = frame_font.render("%s" % (frame_number), 0, (255, 255, 255), (0, 0, 0))
        textpos = pygame.Rect(display_width-80, 30, 10, 10)
        screen.blit(text, textpos)
        
        pygame.display.update()
        
    play  = True
    
    LEFT = 1                
    
    old_x, old_y = 0, 0
    frames = os.listdir(im_dir)
    print 'sorting files ...'
    frames.sort()
    print 'sorted'
    frame_count = 0
    frame_map = {}
    for frame in frames:
        frame_map[frame_count] = frame
        frame_count += 1
    max_frames = frame_count
    frame_id = 0
    while frame_id < max_frames:
        for event in pygame.event.get():
            if (event.type == KEYDOWN):
                if (event.key == K_SPACE):
                    if play == False:
                        play = True
                    else:
                        play = False
                elif (event.key == K_RIGHT):
                    if play == True:
                        play = False
                    frame_id = frame_id + delta
                    if frame_id > max_frames:
                        break
                    fname = os.path.join(im_dir, frame_map[frame_id])
                    display_frame(fname, int(frame_map[frame_id].split('.')[0]))
                elif (event.key == K_LEFT):
                    if play == True:
                        play = False
                    frame_id = frame_id - delta
                    if frame_id < 0:
                        break
                    fname = os.path.join(im_dir, frame_map[frame_id])
                    display_frame(fname, int(frame_map[frame_id].split('.')[0]))
                                             
        if play == False:                            
            continue
        
        fname = os.path.join(im_dir, frame_map[frame_id])
        if frame_map[frame_id].split('.')[-1] == im_ext:
            display_frame(fname, int(frame_map[frame_id].split('.')[0]))
            time.sleep(delay)
        frame_id += 1
    
if __name__ == '__main__':
    import sys
    sys.exit(image_player())
    