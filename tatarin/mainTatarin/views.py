from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from .models import *
import json
import requests

@csrf_exempt
def user_registration(request):
    if request.method == "POST":
        body = request.body.decode("utf-8")
        body = json.loads(body)
        wallet = body["wallet"]
        contract = body["contract"]
        character = body["character"]
        user = User()
        user.wallet = wallet
        user.contract = contract
        user.character = Character.objects.get(name=character)
        levels = Level.objects.all()
        currentSublevel = 1 if character == "Пока котёнок" else 2
        for obj in levels:
            if obj.sublevel == currentSublevel and obj.number == 1:
                user.level = obj
        try:
            user.save()
            return HttpResponse("History successfully written!")
        except Exception as e:
            return HttpResponse(status=500, reason=e)
    elif request.method == "GET":
        return HttpResponse(status=500, reason="Only for post request")

@csrf_exempt
def get_theory(request):
    data = tuple({"topic": theory.topic, "content": theory.content, "bonus": theory.bonus} for theory in Theory.objects.all())
    return HttpResponse(data)

@csrf_exempt
def get_level(request):
    body = request.body.decode("utf-8")
    body = json.loads(body)
    sublevel = body["sublevel"]
    levels = Level.objects.all()
    data = [{"number": level.number,
             "sublevel": level.sublevel,
             "topic": level.topic,
             "task": level.task,
             } for level in [level for level in levels if level.sublevel == int(sublevel)]]
    return HttpResponse(data)

@csrf_exempt
def check_answer(request):
    if request.method == "POST":
        body = request.body.decode("utf-8")
        body = json.loads(body)
        answer = str(body["answer"]).strip().lower()
        wallet = str(body["wallet"])
        level = str(body["id"])
    elif request.method == "GET":
        return HttpResponse(status=500, reason="Only for post request")



@csrf_exempt
def user_authorization(request):
    if request.method == "POST":
        body = request.body.decode('utf-8')
        body = json.loads(body)
        try:
            user = User.objects.get(wallet=body["wallet"])
            return HttpResponse({"contract": user.contract,
                                 "name": user.character.name,
                                 "image": user.character.image,
                                 "number": user.level.number})
        except ObjectDoesNotExist:
            return HttpResponse(status=500, reason="Person doesn't exist")
    elif request.method == "GET":
        return HttpResponse(status=500, reason="Only for post request")


def post_for_authorization(request):
    url = "http://127.0.0.1:8000/login/"
    wallet = {"wallet": input("Enter your wallet: ")}
    res = requests.post(url, json=wallet)
    if res.status_code == 200:
        return HttpResponse(f"<h4>Данные успешно отправлены {wallet}<h4>")
    else:
        return HttpResponse(f"<h4>Данные не отправлены с кодом {res.status_code}<h4>")


def post_for_registration(request):
    url = "http://127.0.0.1:8000/register/"
    data = {"wallet": "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
            "contract": "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
            "character": "Уже серьёзный кот",
            }
    res = requests.post(url, json=data)
    if res.status_code == 200:
        return HttpResponse(f"<h4>Данные успешно отправлены {data}<h4>")
    else:
        return HttpResponse(f"<h4>Данные не отправлены с кодом {res.status_code}<h4>")


def post_for_level(request):
    url = "http://127.0.0.1:8000/get-level/"
    data = {"sublevel": "1"}
    res = requests.post(url, json=data)
    if res.status_code == 200:
        return HttpResponse(f"<h4>Данные успешно отправлены {data}<h4>")
    else:
        return HttpResponse(f"<h4>Данные успешно отправлены {res.status_code}<h4>")


def home_page(request):
    return HttpResponse("<h4>Основная страница. Ничего лишнего<h4>"
                        "<p4>Я сразу смазал карту будня,<p4>"
                        "<p>плеснувши краску из стакана;<p>"
                        "<p>я показал на блюде студня<p> "
                        "<p>косые скулы океана.<p> "
                        "<p>На чешуе жестяной рыбы<p>"
                        "<p> прочёл я зовы новых губ.<p>"
                        "<p>А вы ноктюрн сыграть могли бы"
                        "<p> на флейте водосточных труб?<p>")