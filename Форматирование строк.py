# Входные данные
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

# 1. Количество участников первой команды
print("В команде Мастера кода участников: %d !" % team1_num)

# 2. Количество участников в обеих командах
print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))

# 3. Количество задач решённых командой 2
print("Команда Волшебники данных решила задач: {} !".format(score_2))

# 4. Время, за которое команда 2 решила задачи
print("Волшебники данных решили задачи за {:.1f} с !".format(team2_time))

# 5. Количество решённых задач по командам
print(f"Команды решили {score_1} и {score_2} задач.")

# 6. Исход соревнования
print(f"Результат битвы: {challenge_result}")

# 7. Количество задач и среднее время решения
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунд на задачу!.")
