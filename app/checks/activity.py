from app.collector.activity import collect_stat_activity


def count_active_sessions(sessions):
    count = 0

    for session in sessions:
        if session[3] == "active":
            count += 1

    return count
