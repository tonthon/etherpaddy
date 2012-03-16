<%inherit file="base.mako"></%inherit>
<%block name='submenu'>
<div class="subnav subnav-fixed">
<ul class="nav nav-pills">
<li>
<a href="${request.route_path('genpadname')}" title="Generate a random name for your new pad" >Generate random pad name</a>
</li>
</ul>
</div>
</%block>
<%block name='content'>
<form onsubmit="gotopad($('#padname').val());return false;">
<input id='padname' type='text' name='padname'></input><br />
<button type='submit'>Create new pad</button>
</form>
</%block>
