from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .utils import generate_password_dict, brute_force_authenticate, create_zip

@csrf_exempt  
def execute_submission(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Only GET allowed'}, status=405)

    try:
        generate_password_dict()
        temp_url = brute_force_authenticate()
        if temp_url:
            create_zip(temp_url)
            return JsonResponse({"status": "Success"})
        return JsonResponse({"status": "Failed"}, status=400)
    except Exception as e:
        print("❌ Exception occurred:", e)
        return JsonResponse({"status": "Error", "message": str(e)}, status=500)
