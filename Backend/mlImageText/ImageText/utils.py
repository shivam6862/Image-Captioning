from rest_framework.response import Response
from django.core.files.storage import default_storage


# D:\WEB - D\....Mern Development\Django And React App For ML\Backend\mlImageText>
# env\Scripts\activate.bat      {Open the local django}
# python manage.py runserver    {Run the sever}
# env\Scripts\deactivate.bat    {Close the local django}


def createImage(request):
    return Response("helo, every one createImage")


def createText(request):
    return Response("Hello, every one createText")


def saveImage(request):
    image_file = request.FILES['file']
    filename = default_storage.save('photos/' + image_file.name, image_file)
    return Response({'message': 'Image uploaded successfully.'})


def saveText(request):
    return Response("Hello, every one saveText")


def getImageList(request, pk):
    return Response("Hello, every one getImageList " + pk)


def getTextList(request, pk):
    return Response("Hello, every one getTextList "+pk)
