from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .services import get_districts, get_taluks, get_hobli, save_data, get_save_data


def home(request):
    return render(request, 'api/index.html')


@api_view(['GET'])
def districts(request):
    districts = get_districts()
    return Response({
        'status': True,
        'districts': districts
    })


@api_view(['GET'])
def taluks(request, district_id):
    taluks = get_taluks(district_id)
    return Response({
        'status': True,
        'taluks': taluks
    })


@api_view(['GET'])
def hoblis(request, taluk_id):
    hoblis = get_hobli(taluk_id)
    return Response({
        'status': True,
        'hoblis': hoblis
    })


@api_view(['POST'])
def save_form_data(request):
    name = request.data.get('name')
    address = request.data.get('address')
    district_id = request.data.get('district_id')
    taluk_id = request.data.get('taluk_id')
    hobli_id = request.data.get('hobli_id')

    if not name:
        return Response({
            'status': False,
            'message': "Name is required"
        }, status=400)

    if not address:
        return Response({
            'status': False,
            'message': 'Address is required'
        }, status=400)

    if not district_id:
        return Response({
            'status': False,
            'message': 'District_id is required'
        }, status=400)

    if not taluk_id:
        return Response({
            'status': False,
            'message': 'Taluk_id is required'
        }, status=400)

    if not hobli_id:
        return Response({
            'status': False,
            'message': 'Hobli_id is required'
        }, status=400)

    result = save_data(
        name,
        address,
        district_id,
        taluk_id,
        hobli_id
    )

    return Response(result)



@api_view(['GET'])
def get_form_data(request, id):
    result = get_save_data(id)

    if result['status']:
        return Response(result)

    return Response(
        result, 
        status=404
    )