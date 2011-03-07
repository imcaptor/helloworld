# -*- coding: utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from helloworld.lib.base import BaseController, render

log = logging.getLogger(__name__)

class HelloController(BaseController):

    def index(self):
        c.name = '王红宝'
        # Return a rendered template
        return render('/hello.mako')
        # or, return a string         
    
    def test(self):
        return "test"