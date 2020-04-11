#!/usr/bin/env python3
#Magic API
#Print the meta info of picture.
import exif
import argparse

def print_image_meta(filename):
    with open(filename,'rb') as file:
        imagefile=exif.Image(file)
        attrlist = dir(imagefile)
        length=len(attrlist)

        for i in range(length):
            try:
                print("{} : {}".format(attrlist[i],imagefile[attrlist[i]]))
            except (Exception, NotImplementedError):
                i+=i
                pass

def print_simple(filename):
    with open(filename,'rb') as file:
        imagefile=exif.Image(file)
        print(dir(imagefile))

def main():
    parse = argparse.ArgumentParser(usage='%(prog)s <image filename>', description=\
                                    "print the metadata of image")
    parse.add_argument('fname',metavar='filename or file path',type=str)
    args=parse.parse_args()
    try:
        filename=args.fname
        print('list of tags for the instance:')
        print('-'*100)
        print_simple(filename)
        print('-'*100)
        print("Meta data details for image: {} >>>".format(filename))
        print_image_meta(filename)

    except Exception as e:
        print(e)
        exit(0)
if __name__=='__main__':
    main()