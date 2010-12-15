#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

class MainHandler(webapp.RequestHandler):
    def get(self):
        # TODO use a template to tidy this indented mess up!
        self.response.out.write("""<!DOCTYPE html>
<html>
  <head>
    <title>Dump My Request!</title>
    <link rel="stylesheet" type="text/css" href="/css/main.css" />
  </head>
  <body>
    <div>
      <dl id="headers">
""")
        for k,v in self.request.headers.iteritems():
            self.response.out.write("""        <dt>%s</dt>
        <dd>%s</dd>
""" % (k, v))
        self.response.out.write("""      </dl>
    </div>
  </body>
</html>""")


def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
