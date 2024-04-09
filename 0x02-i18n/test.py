app = (__import__("1-app").app)
print(app.config["BABEL_DEFAULT_TIMEZONE"])
# for names in app.config:
#     print(names)