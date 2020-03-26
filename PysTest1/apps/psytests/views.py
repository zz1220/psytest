
from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpRequest, JsonResponse
from .models import MentalEvaluation, UserEvaluation
from django.shortcuts import redirect
from django.template import loader
import sys
import json
from django.core.serializers.json import DjangoJSONEncoder
sys.getfilesystemencoding()
# Create your views here.
# encoding=utf-8


def eval_index(request):
    evals = MentalEvaluation.objects.all().values()
    evals = list(evals)
    request.content_type = 'application/json'
    if request.method == "GET":
        print(HttpResponse.reason_phrase)
        print(HttpResponse.content)
        print(HttpResponse.charset)
        eval_dict = {"status": HttpResponse.status_code, "msg": "success", "data": evals}     # json.dumps(evals) unicode error
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    print(eval_dict)
    return render(request, 'eval_index.html', eval_dict)


def eval_list_time_order(request):
    evals = MentalEvaluation.objects.all().values().order_by("-created_on")
    evals = list(evals)
    request.content_type = 'application/json'
    if request.method == "GET":
        print(HttpResponse.reason_phrase)
        print(HttpResponse.content)
        print(HttpResponse.charset)
        eval_dict = {"status": HttpResponse.status_code, "msg": "success",
                     "data": evals}  # json.dumps(evals) unicode error
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    print(eval_dict)
    return JsonResponse(eval_dict)


def get_eval_types(request):
    EVAL_TYPE_CHOICE = (
        ("1", "分类1"),
        ("2", "分类2"),
        ("3", "分类3")
    )
    classify = []
    for e in EVAL_TYPE_CHOICE:
        classify.append({"id": e[0], "name": e[1]})

    classify_dict = {"status": 200, "msg": "success", "data": classify}
    return JsonResponse(classify_dict)


def get_eval_type_detail(request):
    data = MentalEvaluation.objects.all().values()
    type_list = []
    type_name = "2"     # input eval type, request.POST.get()
    for item in data:
        if type_name in item["eval_type"]:
            type_list.append({"title": item["title"], "price": item["price"], "nums_eval": item["nums_eval"]})
    type_dict = {"status": HttpResponse.status_code, "msg": "success", "data": type_list}
    print(type_dict)
    return JsonResponse(type_dict)


def get_eval_type_detail_time(request):
    data = MentalEvaluation.objects.all().values().order_by("-created_on")
    type_list = []
    type_name = "2"     # input eval type, request.POST.get()
    for item in data:
        if type_name in item["eval_type"]:
            type_list.append({"title": item["title"], "price": item["price"], "nums_eval": item["nums_eval"], "created_on": item["created_on"]})
    type_dict = {"status": HttpResponse.status_code, "msg": "success", "data": type_list}
    print(type_dict)
    return JsonResponse(type_dict)

def delete_eval(request):
    #get id from front
    item = MentalEvaluation.objects.get(eval_id='1')
    item.delete()
    return redirect('http://127.0.0.1:8000')

def add_eval(request):
    new_eval = MentalEvaluation(title='test', eval_id='1')
    new_eval.save()
    return redirect('http://127.0.0.1:8000/')

def edit_eval(request):
    item = MentalEvaluation.objects.get(eval_id='1')
    #item.title = request.POST.get('title')
    item.title = "testtttt"
    item.save()
    return redirect('http://127.0.0.1:8000')


def get_user_eval_list(request):
    user_id = "111"   # request.POST.get()
    user_info = UserEvaluation.objects.get(user_id=user_id)
    info = []
    for item in user_info:
        mental_info = MentalEvaluation.objects.get(eval_id=item["eval_id"])
        info.append({"title": mental_info["title"], "price": mental_info["price"], "discount_price": mental_info["discount_price"]})
    user_eval = {"status": HttpResponse.status_code, "msg": "success", "data": info}
    return JsonResponse(user_eval)


def test(request):

    return HttpResponse("hellllll")


def test1(request):
    #foo_instance = MentalEvaluation.objects.create('')
    return HttpResponse("hi")


