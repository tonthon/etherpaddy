<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<%block name="header">
<title>${title}</title>
<link rel="shortcut icon" href="" type="image/x-icon" />
<meta name="description" comment="">
<meta name="KEYWORDS" CONTENT="">
<meta NAME="ROBOTS" CONTENT="INDEX,FOLLOW,ALL">
</%block>
<link href="${request.static_url('etherpad-padlist:static/css/default.css')}" rel="stylesheet"  type="text/css" />
<link href="${request.static_url('etherpad-padlist:static/css/main.css')}" rel="stylesheet"  type="text/css" />
<%block name="headjs" />
<%block name="css" />
</head>
<body>
    <h1>${title}</h1>
    <%block name='content' />
</body>
</html>
