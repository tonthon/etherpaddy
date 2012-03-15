<%inherit file="base.mako"></%inherit>
<%block name='content'>
<table class="table table-striped">
% for i, pad in enumerate(pads):
    <tr><td>i</td>
     <td>${pad.get_name()}</td>
     <td>
     <a class="btn" href="${request.route_path('pad', padid=pad.get_name())}">Edit it</a>
     </td>
     </tr
% endfor
</table>
<div id='container'></div>
</%block>
