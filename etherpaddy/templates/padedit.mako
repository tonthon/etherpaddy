<%inherit file="base.mako"></%inherit>
<%block name='submenu'>
<div class="subnav subnav-fixed">
<ul class="nav nav-pills">
<li>
<a href='#del' onclick="delPad('${padid}');return false;">Delete this pad</a>
</li>
<li>
<a href='/etherpad/p/${padid}'>Go Fullscreen</a>
</li>
</ul>
</div>
</%block>
<%block name='content'>
<iframe src="${request.route_path('etherpad')}/p/${padid}" id='padframe' scrolling='no'></iframe>
</%block>
