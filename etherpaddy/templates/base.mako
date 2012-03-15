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
    <link href="${request.static_url('etherpaddy:static/css/default.css')}" rel="stylesheet"  type="text/css" />
    <link href="${request.static_url('etherpaddy:static/css/main.css')}" rel="stylesheet"  type="text/css" />
    <link href="${request.static_url('etherpaddy:static/css/bootstrap.min.css')}" rel="stylesheet"  type="text/css" />
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>
    <script src="${request.static_url('etherpaddy:static/js/etherpad.js')}"></script>
    <script src="${request.static_url('etherpaddy:static/js/bootstrap.min.js')}"></script>
    <%block name="headjs" />
    <%block name="css" />
  </head>
  <body>
    <div class="navbar">
      <div class="navbar-inner">
        <div class="container">
          <div class="nav-collapse">
            <ul class='nav'><li class=''><a href='${request.route_path("padnew")}'>Add a pad</a></li><li class=''><a href='${request.route_path("pads")}'>List all pads</a></li></ul>
          </div>
        </div>
      </div>
    </div>
    <%block name='submenu' />
    % if title:
    <h1>${title}</h1>
    % endif
    <%block name='content' />
  </body>
</html>
