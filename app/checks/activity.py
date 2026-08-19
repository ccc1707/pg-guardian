from datetime import datetime


def count_active_sessions(sessions):
    count = 0

    for session in sessions:
        if session[3] == "active":
            count += 1

    return count


def get_active_sessions(sessions):
    active_sessions = []

    for session in sessions:
        if session[3] == "active":
            active_sessions.append(session)

    return active_sessions


def get_long_running_sessions(sessions, threshold):
    long_running_sessions = []

    for session in sessions:
        if session[3] == "active":
            running_time = datetime.now(session[4].tzinfo) - session[4]

            if running_time.total_seconds() >= threshold:
                long_running_sessions.append(session)

    return long_running_sessions
