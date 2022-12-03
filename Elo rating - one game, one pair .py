'''
5 kyu
Name: Elo rating - one game, one pair
https://www.codewars.com/kata/55633765da97b266e3000067
Task: Рассчитайте новый рейтинг Эло шахматиста, используя его предыдущие рейтинги (experience),
рейтинг его противника (opponent), результат новой партии (score) и функцию фактора k (k).
'''


def default_k(experience):
    return 25 if len(experience)<30 else 15 if max(experience)<2400 else 10

def elo(experience, opponent, score, k=default_k):
    player_rating=1000 if not experience else experience[-1]
    expectation=1.0/(1+10**((opponent-player_rating)/400.0))
    new_player_rating=int(round(player_rating+k(experience)*(score-expectation)))
    return new_player_rating