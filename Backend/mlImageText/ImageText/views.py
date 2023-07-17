from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import createImage, createText, saveImage, saveText, getTextList, getImageList


@api_view(['GET'])
def getRoutes(request):

    routes = [{'Endpoint': '/image/', 'method': 'GET', 'body': None, 'description': 'Returns an array of image'},
              {'Endpoint': '/image/id', 'method': 'GET', 'body': None,
                  'description': 'Returns a single Image object'},
              {'Endpoint': '/image/create/', 'method': 'POST', 'body': {'body': ""},
                  'description': 'Creates new Image with data sent in post request'},
              {'Endpoint': '/image/id/update/', 'method': 'PUT', 'body': {'body': ""},
               'description': 'Creates an existing Image with data sent in post request'},
              {'Endpoint': '/image/id/delete/', 'method': 'DELETE',
                  'body': None, 'description': 'Deletes and exiting Image'},
              {'Endpoint': '/text/', 'method': 'GET', 'body': None,
                  'description': 'Returns an array of text'},
              {'Endpoint': '/text/id', 'method': 'GET', 'body': None,
                  'description': 'Returns a single Text object'},
              {'Endpoint': '/text/create/', 'method': 'POST', 'body': {'body': ""},
                  'description': 'Creates new Text with data sent in post request'},
              {'Endpoint': '/text/id/update/', 'method': 'PUT', 'body': {'body': ""},
               'description': 'Creates an existing Text with data sent in post request'},
              {'Endpoint': '/text/id/delete/', 'method': 'DELETE', 'body': None, 'description': 'Deletes and exiting Text'}]
    return Response(routes)


@api_view(['GET', 'POST'])
def getImages(request):
    if request.method == 'GET':
        return createImage(request)
    if request.method == 'POST':
        return saveImage(request)


@api_view(['GET', 'POST'])
def getTexts(request):
    if request.method == 'GET':
        return createText(request)
    if request.method == 'POST':
        return saveText(request)


@api_view(['GET', 'PUT', 'DELETE'])
def getImage(request, pk):
    if request.method == 'GET':
        return getImageList(request, pk)


@api_view(['GET', 'PUT', 'DELETE'])
def getText(request, pk):
    if request.method == 'GET':
        return getTextList(request, pk)
