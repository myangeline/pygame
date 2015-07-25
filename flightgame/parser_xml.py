# _*_ coding:utf-8 _*_
import json

__author__ = 'Administrator'
from xml.dom import minidom


def xml_to_json(xmlstr):
    dom = minidom.parseString(xmlstr)
    # print(dom.toxml())
    root = dom.lastChild
    childs = root.childNodes
    pos = {}
    for child in childs:
        if child.nodeType == child.TEXT_NODE:
            pass
        else:
            name = child.getAttribute('name')
            width = child.getAttribute('width')
            height = child.getAttribute('height')
            x = child.getAttribute('x')
            y = child.getAttribute('y')
            pos[name] = [width, height, x, y]
    return pos


def doxml(xml_path):
    with open(xml_path, 'r') as f:
        xmlstr = f.read()
    return xml_to_json(xmlstr)