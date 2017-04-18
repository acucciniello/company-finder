import tornado.ioloop
import tornado.web
import json
from tornado.httpclient import AsyncHTTPClient


class MainHandler(tornado.web.RequestHandler):

  def handle_response(self, response):
    if response.error:
      print('Error: %s' % response.error)
    else:
      stringOutput = response.body.decode('utf-8')
      output = json.loads(stringOutput)
      print(output['response']['employers'])

  # Maybe what I need to do here is check how many pages there are and from there
  # We can make a second request to pull the last page's worth of data


  def get(self):
    print('We are here')
    http_client = AsyncHTTPClient()
    http_client.fetch('http://api.glassdoor.com/api/api.htm?t.p=142069&t.k=dsrY9os4nMQ&userip=0.0.0.0&useragent=&format=json&v=1&action=employers', self.handle_response)


def make_app():
  return tornado.web.Application([
    (r'/', MainHandler)
  ])

if __name__ == "__main__":
  app = make_app()
  app.listen(8888)
  tornado.ioloop.IOLoop.current().start()
