import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
         self.response.headers["Content-Type"] = "text/html"
         self.response.write("""
          <html>
            <head><title>Enter your name...</title></head>
            <body>
              <form action="/welcome" method="post">
                <input type="text" name="my_name"><br>
                <input type="submit" value="Sign In">
              </form>
            </body>
            </html>""")

routes = [('/', MainPage)]

app = webapp2.WSGIApplication(routes, debug=True)