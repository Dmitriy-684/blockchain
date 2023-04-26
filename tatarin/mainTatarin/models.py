
from django.db import models


class Theory(models.Model):
    topic = models.CharField(max_length=32, verbose_name="Тема")
    content = models.TextField(verbose_name="Содержание")
    bonus = models.BooleanField(default=False, verbose_name="Бонусная теория")


class Reward(models.Model):
    caption = models.CharField(max_length=32, verbose_name="Название NFT")
    hash = models.CharField(max_length=46, verbose_name="Хэш NFT в IPFS")
    theory = models.ForeignKey("Theory", on_delete=models.DO_NOTHING, related_name="TheoryOf", default="")


class Level(models.Model):
    topic = models.CharField(max_length=32, verbose_name="Тема вопроса")
    task = models.TextField(verbose_name="Вопрос для пользователя")
    answer = models.CharField(max_length=64, verbose_name="Ответ на вопрос")
    reward = models.ForeignKey("Reward", on_delete=models.DO_NOTHING, related_name="RewardOf")
    sublevel = models.IntegerField(default=1, verbose_name="Уровень сложности")
    number = models.IntegerField(default=1, verbose_name="Номер уровня в зависимости от сложности")


class Character(models.Model):
    name = models.CharField(max_length=32, verbose_name="Имя персонажа")
    image = models.TextField(verbose_name="Модель персонажа")


class User(models.Model):
    wallet = models.CharField(max_length=42, unique=True, verbose_name="Адрес кошелька пользователя")
    contract = models.CharField(max_length=42, verbose_name="Контракт пользователя")
    character = models.ForeignKey("Character", on_delete=models.DO_NOTHING, related_name="CharacterOf")
    level = models.ForeignKey("Level", on_delete=models.DO_NOTHING, related_name="LevelOf")
