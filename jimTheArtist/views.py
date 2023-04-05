from django.shortcuts import render
import random

def home(request):
    return render(request, 'home.html')

def gallery(request):
    paintings = [
        {'url': '/gallery/atlanticMoonrise', 'image': '/static/imgs/paintings/atlanticMoonrise.JPG' },
        {'url': '/gallery/atlanticMorning', 'image': '/static/imgs/paintings/atlanticMorning.JPG' },
        {'url': '/gallery/currents', 'image': '/static/imgs/paintings/currents.JPG' },
        {'url': '/gallery/deepInThePines', 'image': '/static/imgs/paintings/deepInThePines.JPG' },
        {'url': '/gallery/fosterTownRoad', 'image': '/static/imgs/paintings/fosterTownRoad.JPG' },
        {'url': '/gallery/habitiant', 'image': '/static/imgs/paintings/habitiant.JPG' },
        {'url': '/gallery/medfordScene', 'image': '/static/imgs/paintings/medfordScene.JPG' },
        {'url': '/gallery/morningShoreline', 'image': '/static/imgs/paintings/morningShoreline.JPG' },
        {'url': '/gallery/openOcean', 'image': '/static/imgs/paintings/openOcean.JPG' },
        {'url': '/gallery/oxidized', 'image': '/static/imgs/paintings/oxidized.JPG' },
        {'url': '/gallery/pastelTreeStudy', 'image': '/static/imgs/paintings/pastelTreeStudy.JPG' },
        {'url': '/gallery/pineBarrensHike', 'image': '/static/imgs/paintings/pineBarrensHike.JPG' },
        {'url': '/gallery/pineBarrensScene', 'image': '/static/imgs/paintings/pineBarrensScene.JPG' },
        {'url': '/gallery/pondView', 'image': '/static/imgs/paintings/pondView.JPG' },
        {'url': '/gallery/route206', 'image': '/static/imgs/paintings/route206.JPG' },
        {'url': '/gallery/sentient', 'image': '/static/imgs/paintings/sentient.JPG' },
        {'url': '/gallery/springTree', 'image': '/static/imgs/paintings/springTree.JPG' },
        {'url': '/gallery/sunsetFreedomPark', 'image': '/static/imgs/paintings/sunsetFreedomPark.JPG' },
        {'url': '/gallery/thePoint', 'image': '/static/imgs/paintings/thePoint.JPG' },
        {'url': '/gallery/thePoint2', 'image': '/static/imgs/paintings/thePoint2.JPG' },
        {'url': '/gallery/thirtySevenThousand', 'image': '/static/imgs/paintings/thirtySevenThousand.JPG' },
        {'url': '/gallery/tidalEnergy', 'image': '/static/imgs/paintings/tidalEnergy.JPG' },
        {'url': '/gallery/underTheSurface', 'image': '/static/imgs/paintings/underTheSurface.JPG' },
        {'url': '/gallery/winterBeach', 'image': '/static/imgs/paintings/winterBeach.JPG' },
        {'url': '/gallery/winterNocturne', 'image': '/static/imgs/paintings/winterNocturne.JPG' },
        {'url': '/gallery/winterThaw1', 'image': '/static/imgs/paintings/winterThaw1.JPG' },
        {'url': '/gallery/winterThaw2', 'image': '/static/imgs/paintings/winterThaw2.JPG' }
    ]
    #randomize order of paintings
    shuffled_paintings = paintings.copy()
    random.shuffle(shuffled_paintings)

    return render(request, 'gallery.html', {'paintings': shuffled_paintings})