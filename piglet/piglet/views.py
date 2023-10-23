from django.shortcuts import render
from django.http import JsonResponse

def main(request):
    return render(request, "main.html")

def login(request):
    return render(request, "login.html")

def missinglist(request):
    return render(request, "missinglist.html")

def missinglistdetail(request):
    return render(request, "missinglistdetail.html")

def reportmissing(request):
    return render(request, "reportmissing.html")

def eventpage1(request):
    return render(request, "eventpage1.html")

def eventpage2(request):
    if request.method == 'POST':
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        uploaded_image = request.FILES['picture']

        # 업로드된 이미지를 저장할 경로
        image_path = "uploads/" + uploaded_image.name

        # 이미지를 저장
        with open(image_path, 'wb') as destination:
            for chunk in uploaded_image.chunks():
                destination.write(chunk)

    return render(request, "eventpage2.html")

def eventpage3(request):
    return render(request, "eventpage3.html")

def dashboard(request):
    return render(request, "dashboard.html")

# 랜딩페이지 사진, 성별, 나이 입력후 백엔드 프로세스
def process_upload(request):
    if request.method == "POST":
        # 데이터 받아오기
        image = request.FILES.get("picture")
        # age = request.POST.get("age")
        gender = request.POST.get("gender")

        # GAN 모델 추가하기

        # 데이터 응답하기
        response_data = {"message": "데이터 성공"}
        return JsonResponse(response_data)

    return JsonResponse({"message": "데이터 실패"})
