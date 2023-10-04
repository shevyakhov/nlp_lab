# -*- coding: utf-8 -*-
"""lab 3 shevyakhov.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kSeO0e_mgj2WMBMWIPZSJ45-xsR03QMJ

Текст 1 лабораторной
"""

import nltk
from nltk.tokenize import word_tokenize,sent_tokenize

nltk.download('punkt')

text = "Студенты колледжей и университетов, которые регулярно посещают занятия и хорошо спят, с большей вероятностью получат хорошие оценки в конце семестра. Присутствие на парах важно для налаживания взаимодействия между студентом и преподавателем и прохождения ключевых моментов учебного курса, а хороший сон необходим для оптимизации процессов запоминания и обучения. Однако в большинстве учебных заведений первые пары начинаются рано утром, из-за чего студенты нередко опаздывают или вовсе пропускают их, стремясь заполучить лишние часы для сна. Учитывая, что подростки и молодые люди часто ложатся спать поздно (причины не только социальные, но и биологические), первые пары вынуждают их недосыпать, а это не может не сказаться на общей успеваемости. Возможно, составителям расписаний занятий в вузах следует отказаться от утренних пар и перенести начало занятий на более позднее время, считают исследователи. Это позволит обучающимся получать достаточное количество часов сна и без дополнительных усилий повысить собственную успеваемость."

lab_1_res = ["студент колледж",
"колледж университет",
"университет который",
"конец семестр",
"студент преподаватель",
"учебный курс",
"курс хороший",
"хороший сон",
"сон необходимый",
"запоминание обучение",
"обучение большинство",
"сон подросток",
"социальный биологический",
"биологический первый",
"расписание занятие",
"вуз утренний",
"начало занятие",
"сон дополнительный"]

"""Текст 3 лабораторной"""

!pip install rnnmorph

from rnnmorph.predictor import RNNMorphPredictor

predictor = RNNMorphPredictor(language="ru")

tokens = word_tokenize(text)
res = predictor.predict(tokens)

def extract_variables(word):
    variables = {
        'Case': None,
        'Degree': None,
        'Gender': None,
        'Number': None
    }
    key_value_pairs = word.split('|')
    for pair in key_value_pairs:
      key, value = pair.split('=')
      variables[key] = value
    return variables

lemmas = []
parts = ['NOUN','ADJ']

for token in res:
  nform = token.normal_form
  if token.pos in parts:
      lemmas.append((nform,token.tag))

matching_pairs = []
for i in range(len(lemmas) - 1):
  word1 = lemmas[i][0]
  tag1 = lemmas[i][1]

  word2 = lemmas[i + 1][0]
  tag2 = lemmas[i+1][1]

  t1 = extract_variables(tag1)
  t2 = extract_variables(tag2)

  if (t1['Case'] == t2['Case'] and
      t1['Number'] == t2['Number'] and
      t1['Gender'] == t2['Gender']):
      matching_pairs.append((word1, word2))

for pair in matching_pairs:
      print(" ".join(pair))

for line in lab_1_res:
  print(line)

"""Что мы видим? Лишь некоторые пары совпадают. На самом деле некоторые данные он не смог определить, например, пол, у некоторых слов, следовательно и результат будет разниться. Стоит отметить, что обработка токенов, также повлияла на результат"""