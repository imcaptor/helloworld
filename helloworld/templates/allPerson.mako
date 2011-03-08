<%inherit file="/base.mako" />
<%def name="head_tags()"><title>你好，世界</title></%def>
Hello World, the environ variable looks like。 <br/>

%for person in c.persons:
	${person.name}<br/>
%endfor