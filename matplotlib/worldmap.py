#!/usr/bin/env python
# coding=utf-8

from pygal.maps.world import World

wm = World()
wm.title = 'North,Central,and South America'

wm.add('North America',{'ca':341900,'mx':232323,'us':232323232})
wm.add('Central America',['bz','cr','gt','hn','ni','pa','sv'])
wm.add('South America',['ar','bo','br','cl','co','ec','gf',
                       'gy','pe','py','sr','uy','ve'])

wm.render_to_file('worldmap.svg')


