def record_scores(new_score: float, score_history: list = []) -> tuple:
    score_history.append(new_score)
    avg = sum(score_history) / len(score_history)
    return score_history, avg

print(record_scores(23.0, [20.5, 22.0, 24.0]))

