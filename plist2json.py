#coding=utf-8

import os
import sys
import click
from mtool import utils
import importlib

import xmltodict

@click.command()
@click.option('-i', '--input-path', required = True, help='plist文件读取路径')
def run(**options):
    '''plist转为json, 需要配置plist读取路径'''
    print(options)
    plist_to_json(options)

def load_json(xml_path):
    #获取xml文件
    xml_file = open(xml_path, 'r')
    #读取xml文件内容
    xml_str = xml_file.read()
    #将读取的xml内容转为json
    json = xmltodict.parse(xml_str)
    return json

@click.command()
@click.option('-i', '--input-path', required = True, help='plist文件读取路径')
def plist_to_json(options):
    print(options)

    all_plist_file_name = []
    utils.get_all_file_list( options["input_path"], all_plist_file_name, 'plist')

    for plistFilePath in all_plist_file_name:
        if os.path.exists(plistFilePath):
            print(plistFilePath)
            result = load_json(plistFilePath)
            jsonFilePath = plistFilePath.replace("plist","json")
            outputfile = open(jsonFilePath, 'w', encoding='UTF-8')
            outputfile.write(str(result))
            outputfile.close()


if __name__ == '__main__':
    
    # args = {
    #     "input_path" : "/data/work/svn/Vega/frontend/Assets/anim/flash",
    # }
    # plist_to_json(args)
    run()
    print("---done!---");
