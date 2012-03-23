/*
 * File Name : etherpaddy.js
 *
 * Copyright (C) 2012 Gaston TJEBBES g.t@majerti.fr
 * Company : Majerti ( http://www.majerti.fr )
 *
 * This software is distributed under GPLV3
 * License: http://www.gnu.org/licenses/gpl-3.0.txt
 *
 */
function getPadUrl(padId){
  /*
   * Return a pad's url
   */
  return PADURL + "/" + padId;
}
function gotopad(padId){
  /*
   * returns the user to the padname edit page
   */
  var url = getPadUrl(padId);
  window.location = url;
  return false;
}
function delPad(padId){
  /*
   * Call the delpad method
   */
  if (window.confirm("Are you sure you want to delete this pad ?")){
    var delurl = getPadUrl(padId);
    jQuery.ajax({url:delurl, type:'DELETE',
                 success:function(data){
                  if (data['code'] === 0){
                    alert("The pad " + padId + " has been deleted");
                    window.location.href = PADURL;
                  }else{
                    alert(data['message']);
                  }
                },
                error:function(e){
                  alert(e);
                }
              });
  }
}
