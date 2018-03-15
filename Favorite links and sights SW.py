import pyautogui as pg
import webbrowser

videos = ["https://www.youtube.com/watch?v=IdQCi48gI80","https://www.youtube.com/watch?v=qnydFmqHuVo"]

music = ["https://www.youtube.com/watch?v=3M_5oYU-IsU","https://www.youtube.com/watch?v=WDZJPJV__bQ"]

answer = pg.prompt(
"""
which would you rather do??
a) watch videos
b) Liten to music

"""
    )


if answer == "a":
    for i in videos:
        webbrowser.open (i)
elif answer == "b":
    for i in music:
        webbrowser.open (i)
