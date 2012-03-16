/*
 * File Name : pad.js
 *
 * Copyright (C) 2012 Gaston TJEBBES g.t@majerti.fr
 * Company : Majerti ( http://www.majerti.fr )
 *
 * This software is distributed under GPLV3
 * License: http://www.gnu.org/licenses/gpl-3.0.txt
 *
 */
function goToPadList(){
  /*
   * Launched on menu item click, redirect the user to the padlist
   */
  if (window.confirm("Go to padlist and leave the document ?")){
    window.location = '/pads';
  }
  return false;
}
function getCustomMenuItems(){
  /*
   * Return the custom menu Item
   */
  return "<li onclick=\"goToPadList();return false;\" \
  title='Go to the pads list'> \
  <a class='buttonicon buttonicon-insertunorderedlist'></a> \
    </li>";

}

function customStart()
{
  /*
   * Etherpad-lite built-in function to hack pad's startup
   * add a custom button
   */
  var right_menu = $('#menu_right');
  right_menu.prepend(getCustomMenuItems);
}
