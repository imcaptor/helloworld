# -*- coding: utf-8 -*-
import logging,uuid

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from sqlalchemy.sql import select

from helloworld.lib.base import BaseController, render

from helloworld.model.__init__ import Person,Bill
from helloworld.model import meta
from datetime import datetime

log = logging.getLogger(__name__)

class HelloController(BaseController):

    def index(self):
        c.name = 'test'  #这个参数可以传递到模版
        c.person = meta.Session.query(Person).filter(Person.name == 'Mr Jones').first()                
        #result = conn.execute(s)        
        # Return a rendered template
        return render('/hello.mako')
        # or, return a string         
    
    def test(self):
        return "test"
    
    def createData(self):
        ##创建一条数据
        mr_jones = Person()
        mr_jones.name = 'Mr Jones'
        mr_jones.id = 1
        mr_jones.email = 'test@gmail.com'
        meta.Session.add(mr_jones)
        meta.Session.commit()
        ##创建一条数据
        return 'success'
    
    def onePerson(self):
        c.person = meta.Session.query(Person).filter(Person.name == 'Mr Jones').first()                
        return render('/onePerson.mako')
    
    def allPerson(self):
        c.persons = meta.Session.query(Person)[0:2]
        
        return render('/allPerson.mako')
    
    def createBill(self):
        bill = Bill()
        bill.id = str(uuid.uuid1());        
        print bill.id
        bill.addedOn = datetime.now()
        bill.count = 100
        meta.Session.add(bill)
        meta.Session.commit()        
        return 'success'
