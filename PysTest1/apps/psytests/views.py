from django.forms import model_to_dict
from django.shortcuts import render
from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.http import HttpResponse, HttpResponseNotFound, HttpRequest, JsonResponse, HttpResponseRedirect
from .models import MentalEvaluation, UserEvaluation, UserReviewForEvaluation, EvalQuestion, UserEvalQuestionInfo, Options
from users.models import UserProfile
from .forms import ReviewForm

from operations.models import UserEvaluation

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
        eval_dict = {"status": HttpResponse.status_code, "msg": "success",
                     "data": evals}  # json.dumps(evals) unicode error
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    print(eval_dict)
    return JsonResponse(eval_dict)


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
    eval_dict = json.dumps(eval_dict)
    return HttpResponse(eval_dict, mimetype="application/json")


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
    type_name = request.POST.get("eval_type")
    for item in data:
        if type_name in item["eval_type"]:
            type_list.append({"title": item["title"], "price": item["price"], "nums_eval": item["nums_eval"]})
    type_dict = {"status": HttpResponse.status_code, "msg": "success", "data": type_list}
    type_dict = json.dumps(type_dict)
    return HttpResponse(type_dict, content_type="application/json")


def get_eval_type_detail_time(request):
    data = MentalEvaluation.objects.order_by("-created_on").values()
    type_list = []
    type_name = request.POST.get("eval_type")
    for item in data:
        if type_name in item["eval_type"]:
            type_list.append({"title": item["title"], "price": item["price"], "nums_eval": item["nums_eval"],
                              "created_on": item["created_on"]})
    type_dict = {"status": HttpResponse.status_code, "msg": "success", "data": type_list}
    type_dict = json.dumps(type_dict)
    return HttpResponse(type_dict, content_type="application/json")


def delete_eval(request):
    # get id from front
    item = MentalEvaluation.objects.get(eval_id='1')
    item.delete()
    return redirect('http://127.0.0.1:8000')


def add_eval(request):
    new_eval = MentalEvaluation(title='test', eval_id='1')
    new_eval.save()
    return redirect('http://127.0.0.1:8000/')


def edit_eval(request):
    item = MentalEvaluation.objects.get(eval_id='1')
    # item.title = request.POST.get('title')
    item.title = "testtttt"
    item.save()
    return redirect('http://127.0.0.1:8000')



def get_user_eval_list(request):
    user_id = request.POST.get("eval_user_id")

    user_info = UserEvaluation.objects.get(user_id=user_id)
    info = []
    for item in user_info:
        mental_info = MentalEvaluation.objects.get(eval_id=item["eval_id"])
        info.append({"title": mental_info["title"], "price": mental_info["price"],
                     "discount_price": mental_info["discount_price"]})
    user_eval = {"status": HttpResponse.status_code, "msg": "success", "data": info}
    user_eval = json.dumps(user_eval)
    return HttpResponse(user_eval, content_type="application/json")

def get_user_review_list(request):
    user_id = request.POST.get("user_id")
    user_re = UserReviewForEvaluation.objects.get(user_id=user_id)
    data = []
    for item in user_re:
        mental_info = MentalEvaluation.objects.get(eval_id=item["eval_id"])
        data.append({"title": mental_info["title"], "created_on": item["created_on"]})

    user_review = {"status": HttpResponse.status_code, "msg": "success",  "data": [{"title": "xxx", "created_on": "10"}]}
    user_review = json.dumps(user_review)
    return HttpResponse(user_review, content_type="application/json")

def get_user_favourite(request):
    user_id = request.POST.get("user_id")
    user_re = UserReviewForEvaluation.objects.get(user_id=user_id)
    data = []
    for item in user_re:
        mental_info = MentalEvaluation.objects.get(eval_id=item["eval_id"])
        data.append({"title": mental_info["title"], "price": mental_info["price"], "discount_price": mental_info["discount_price"],
                     "nums_eval": mental_info["nums_eval"]})

    user_fv = {"status": HttpResponse.status_code, "msg": "success", "data": [{"title": "xxx", "created_on": "10"}]}
    user_fv = json.dumps(user_fv)
    return HttpResponse(user_fv, content_type="application/json")

def get_user_info(request):
    user_id = request.POST.get("user_id")
    user_info = UserProfile.objects.get(user_id=user_id)
    data = [{"gender": user_info["wsex"], "age": user_info["age"]}]
    info = {"status": HttpResponse.status_code, "msg": "success", "data": data}
    return JsonResponse(info)

def get_eval_detail(request):
    eval_id = request.POST.get("eval_id")
    mental_info = MentalEvaluation.objects.get(eval_id=eval_id)
    data = [{"title": mental_info["title"], "intro": mental_info["intro"], "ques_num": mental_info["ques_num"],
             "report": mental_info["report"], "nums_eval": mental_info["nums_eval"], "price": mental_info["price"],
             "discount_price": mental_info["discount_price"], "eval_id": eval_id}]
    eval_info = {"status": HttpResponse.status_code, "msg": "success", "data": data}
    eval_info = json.dumps(eval_info)
    return HttpResponse(eval_info, content_type="application/json")

def get_eval_reviews(request):
    eval_id = request.POST.get("eval_id")
    rev_info = UserReviewForEvaluation.objects.get(eval_id=eval_id)
    user_id = rev_info["user_id"]
    user_info = UserProfile.objects.get(user_id=user_id)
    data = [{"username": user_info["username"], "is_vip": user_info["is_vip"], "review": rev_info["review"], "created_on": rev_info["created_on"]}]
    data = json.dumps(data)
    return HttpResponse(data, content_type="application/json")

def get_eval_result(request, user_id):
    user_id = request.POST.get("user_id")
    eval_id = request.POST.get("eval_id")
    eval_info = MentalEvaluation.objects.get(eval_id=eval_id)
    eval_q = EvalQuestion.objects.get(eval_id=eval_id)
    data = [{"dimension": eval_q["eval_dimension"], "title": eval_info["title"], "intro": eval_info["intro"]}]
    res = {"status": HttpResponse.status_code, "msg": "success", "data": data}
    res = json.dumps(res)
    return HttpResponse(res, content_type="application/json")

def get_evalq(request, eval_id):
    eval_id = request.POST.get("eval_id")
    q_info = EvalQuestion.objects.get(eval_id=eval_id)
    eval_info = MentalEvaluation.objects.get(eval_id=eval_id)
    data = []
    for items in q_info:
        each_q = {"ques_num": eval_info["ques_num"], "q_id": items["q_id"], "q_desc": items["q_desc"]}
        choices = Options.objects.get(q_id=items["q_id"])

        for c in choices:
            each_q["choice"] = {}
            each_q["choice"]["o_id"] = c["o_id"]
            each_q["choice"]["o_desc"] = c["o_desc"]
            data.append(each_q)

    qes = {"status": HttpResponse.status_code, "msg": "success", "data": data}
    qes = json.dumps(qes)
    return HttpResponse(qes, content_type="application/json")

def get_related_eval(request, eval_id):
    eval_id = request.POST.get("eval_id")
    eval_info = MentalEvaluation.objects.get(eval_id=eval_id)
    data = [{"title": eval_info["title"], "price": eval_info["price"], "discount_price": eval_info["discount_price"],
             "nums_eval": eval_info["nums_eval"], "eval_id": eval_id}]
    res = {"status": HttpResponse.status_code, "msg": "success", "data": data}
    res = json.dumps(res)
    return HttpResponse(res, content_type="application/json")

def submit_review(request, eval_id):
    eval_id = request.POST.get("eval_id")
    user_id = request.POST.get("user_id")
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            review = data['review']
            usr_review = UserReviewForEvaluation(eval_id=eval_id, user_id=user_id, review=review)
            usr_review.save()
            return HttpResponse("Success")

    else:
        form = ReviewForm()
    return JsonResponse({"status": 404, "msg": "Fail to submit"})



























