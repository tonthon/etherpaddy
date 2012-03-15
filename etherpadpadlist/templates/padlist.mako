<%inherit file="base.mako"></%inherit>
<%block name='content'>
% for pad in pads:
    ${pad.key} : ${pad.value}
% endfor
</%block>
