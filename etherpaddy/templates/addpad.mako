<%inherit file="base.mako"></%inherit>
<%block name='submenu'>
<div class="subnav subnav-fixed">
<ul class="nav nav-pills">
<li>
<a href='#del' onclick="window.alert('We should generate a random pad name');return false;">Generate random pad name</a>
</li>
</ul>
</div>
</%block>
<%block name='content'>
<script>
function gotopad(){
    var padname = $('#padname').val();
    var url = "${request.route_path('pads')}" + "/" + padname;
    window.location = url;
    return false;
}
</script>
<form onsubmit='gotopad(); return false;'>
<input id='padname' type='text' name='padname'></input><br />
<button type='submit' onclick='gotopad()'>Create new pad</button>
</form>
</%block>

