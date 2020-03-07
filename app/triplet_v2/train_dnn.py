﻿# -*- coding: utf-8 -*-
"""
Данный модуль тренирует нейронную сеть для классификации
и отбираем наилучшую с учетом валидационной ошибки.
Основные функции преобразования реализованы в модуле main_function.py
Задача тренировки нейронной сети обучиться так, чтобы на валидационном наборе
давать как можно более точный результат при этом не используя данные этого 
набора для обучения. Только для проверки. Это необходимо, чтобы
избежать overfitting.
Чем меньше исходный learning rate и больше максимальное число итераций -
тем точнее будет решение (однако не факт, что оно будет единствено верным).

"""

import main_functions as mf

mf.train_dnn()
