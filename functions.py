import app
if app.DEBUG:
    def f():
        print("f")
else:
    def f():
        print("other f")

f()