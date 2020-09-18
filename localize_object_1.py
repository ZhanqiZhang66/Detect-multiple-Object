# cd Onedrive google cloud platform
##.\gcp\Scripts\activate  

## 
class boundary:
    def __init__(self, object_name, object_score, vertices):
        self.object_name = object_name
        self.object_score = object_score
        self.vertices = vertices
    def list_vertices (self):
        print('\n name of the object: {} {} '.format(self.object_name ,self.vertices))

class object_vertex:
    def __init__(self, x,y):
        self.x = x
        self.y = y


def localize_objects(path):
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations

    bounds = []
    

    print('Number of objects found: {}'.format(len(objects)))
    for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        vertices = []
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))
            vertex_tmp = object_vertex(vertex.x, vertex.y)
            vertices.append(vertex_tmp)
        bound_tmp = boundary(object_.name, object_.score, vertices)
        bounds.append(bound_tmp)
    return bounds

def draw_boxes(image, bounds, color):
    import numpy as np
    """Draw a border around the image using the hints in the vector list."""
    draw = ImageDraw.Draw(image)
    h, w = np.size(image,0), np.size(image,1)
    #for object in objects
    for bound in bounds:

        #bound.list_vertices()
        draw.text((w*bound.vertices[0].x , h*bound.vertices[0].y), bound.object_name)
        draw.polygon([
            (w*bound.vertices[0].x), (h*bound.vertices[0].y),
            (w*bound.vertices[1].x), (h*bound.vertices[1].y),
            (w*bound.vertices[2].x), (h*bound.vertices[2].y),
            (w*bound.vertices[3].x), (h*bound.vertices[3].y)], None, color)
    return image


def render_doc_text(filein, fileout):
    image = Image.open(filein)
    bounds = localize_objects(filein)
    draw_boxes(image, bounds, 'blue')
    if fileout != 0:
        image.save(fileout)
    else:
        image.show()
    return bounds

import argparse
from enum import Enum
import io

from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw
# [END vision_document_text_tutorial_imports]

import io
import os
import csv
import numpy as np
read_directory = 'your path'
with open('labels.csv', 'w', newline='') as csv_file:
    wr = csv.writer(csv_file, delimiter=',')
    for filename in os.listdir(read_directory):
        if filename.endswith('.jpg'):
            wr.writerow([filename])
            file_name = os.path.abspath(filename)
            image = Image.open(file_name)
            h, w = np.size(image,0), np.size(image,1)
            file_save_name =  filename[:-4] + '_labeled.jpg'
            #bounds = localize_objects(file_name)
            bounds = render_doc_text(file_name, file_save_name)
            for bound in bounds:
                print(type(bound.object_name))
                wr.writerow([[bound.object_name], [bound.object_score], 
                    [w*bound.vertices[0].x], [h*bound.vertices[0].y],
                    [w*bound.vertices[1].x], [h*bound.vertices[1].y],
                    [w*bound.vertices[2].x], [h*bound.vertices[2].y],
                    [w*bound.vertices[3].x], [h*bound.vertices[3].y]])
