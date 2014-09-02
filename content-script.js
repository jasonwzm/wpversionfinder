/*
Copyright (c) 2013-2014 by White Fir Design

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, only version 2 of the License is applicable.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

//Check for indicators of WordPress use
if (/<meta name="generator" content="WordPress [0-9\.]+/i.test(document.getElementsByTagName('head')[0].innerHTML))
	chrome.extension.sendMessage({'tooltip' : document.getElementsByTagName('head')[0].innerHTML.match(/<meta name="generator" content="WordPress ([0-9\.]+)/i)[1]}, function(response) {});
else if ( (/<link rel=["']stylesheet["'].*href=["'][a-z0-9\:\\\\\/\-_.~]*\/wp-content\//i.test(document.getElementsByTagName('head')[0].innerHTML)) && (!/<meta name="generator" content="WordPress\.com"/i.test(document.getElementsByTagName('head')[0].innerHTML)) )
	chrome.extension.sendMessage({'tooltip' : 'Unknown'}, function(response) {});

//Returns WordPress version in use
chrome.extension.onMessage.addListener(
  function(request, sender, sendResponse) {
    if (request.check == "version") {
		if (/<meta name="generator" content="WordPress [0-9\.]+/i.test(document.getElementsByTagName('head')[0].innerHTML))
			chrome.extension.sendMessage({'popup' : document.getElementsByTagName('head')[0].innerHTML.match(/<meta name="generator" content="WordPress ([0-9\.]+)/i)[1]}, function(response) {});
		else {
			if (/<link rel=["']stylesheet["'].*href="(https?:\/\/[a-z0-9\-_.~]+\/|\/)[a-z0-9\-_.~\/]+wp-content\//i.test(document.getElementsByTagName('head')[0].innerHTML))
				var directory = "/"+document.getElementsByTagName('head')[0].innerHTML.match(/<link rel=["']stylesheet["'].*href="(https?:\/\/[a-z0-9\-_.~]+\/|\/)([a-z0-9\-_.~\/]+)wp-content\//i)[2];
			else
				var directory = "/";
			
			xmlhttp=new XMLHttpRequest();
			xmlhttp.open("GET",directory+"readme.html",true);
			xmlhttp.setRequestHeader("Cache-Control", "max-age=0");
			xmlhttp.onreadystatechange = function (oEvent) {
				if (xmlhttp.readyState === 4) {
					if (xmlhttp.status === 200) {
				
						if (/Version ([0-9.]+)/.test(xmlhttp.responseText)) {
							var version = xmlhttp.responseText.match(/Version ([0-9.]+)/)[1];
							chrome.extension.sendMessage({'popup' : version}, function(response) {});
						}
						else {
							i = 0;
							checkFiles(directory);
						}
					}
					else {
						i = 0;
						checkFiles(directory);
					}
				}
			};
			xmlhttp.send();
		}
	}
});

//WordPress file version matches
var file_versions = [
{
    "version": "3.9.1-3.9.2",
    "file": "wp-includes/css/editor-rtl.css",
    "match": "listbox span"
},
{
    "version": "3.9",
    "file": "wp-includes/css/admin-bar-rtl.css",
    "match": "webkit\-border\-radius: 0"
},
{
    "version": "3.8.1-3.8.4",
    "file": "wp-includes/css/admin-bar-rtl.css",
    "match": "f464"
},
{
    "version": "3.8",
    "file": "wp-includes/js/jquery/suggest.js",
    "match": "input.trigger"
},
{
    "version": "3.7.1-3.7.4",
    "file": "wp-includes/js/tinymce/plugins/wpeditimage/editor_plugin.js",
    "match": "'\\+f\\+'px"
},
{
    "version": "3.7",
    "file": "wp-includes/js/imgareaselect/jquery.imgareaselect.js",
    "match": "navigator.userAgent"
},
{
    "version": "3.6.1",
    "file": "wp-includes/js/tinymce/plugins/wordpress/editor_plugin_src.js",
    "match": "tinymce.isIOS5"
},
{
    "version": "3.6",
    "file": "wp-includes/css/admin-bar.css",
    "match": "-webkit-transition:"
},
{
    "version": "3.5.2",
    "file": "wp-includes/js/plupload/handlers.js",
    "match": "jQuery\\('<div class=\"media-item\">'\\)"
},
{
    "version": "3.5.1",
    "file": "wp-includes/css/editor.css",
    "match": "\.rtl \.wp-dialog \.ui-dialog-titlebar-close"
},
{
    "version": "3.5",
    "file": "wp-includes/css/admin-bar-rtl.min.css",
    "match": "#wpadminbar"
},
{
    "version": "3.4.x",
    "file": "wp-includes/css/editor.css",
    "match": "\.wp_themeSkin"
},
{
    "version": "3.3.x",
    "file": "wp-includes/css/editor-buttons.css",
    "match": "\.wp_themeSkin"
},
{
    "version": "3.2.x",
    "file": "wp-includes/js/tinymce/plugins/wpdialogs/js/wpdialog.dev.js",
    "match": "\\(function\\(\\$\\)\\{"
},
{
    "version": "3.1.x",
    "file": "wp-includes/css/admin-bar-rtl.css",
    "match": "#wpadminbar"
},
{
    "version": "3.0.x",
    "file": "wp-includes/js/wp-list-revisions.dev.js",
    "match": "\\(function\\(w\\)"
},
{
    "version": "2.9.x",
    "file": "wp-includes/js/json2.dev.js",
    "match": "http:\/\/www\.JSON\.org"
},
{
    "version": "2.8.x",
    "file": "wp-includes/js/autosave.dev.js",
    "match": "var autosave"
},
{
    "version": "2.7.x",
    "file": "wp-includes/js/comment-reply.js",
    "match": "addComment"
},
{
    "version": "2.6.x",
    "file": "wp-includes/js/jquery/ui.core.js",
    "match": "eval\\(function\\("
},
{
    "version": "2.5.x",
    "file": "wp-includes/js/wp-ajax-response.js",
    "match": "wpAjax = jQuery"
},
{
    "version": "Below 2.5.x",
    "file": "wp-includes/js/colorpicker.js",
    "match": "Matt Kruse"
},
{
    "version": "Hidden",
    "file": "",
    "match": ""
}
];

//Check for existence of files
var i = 0;
function checkFiles(directory) {
	if (file_versions[i].version!="Hidden") {
		var xmlhttp=new XMLHttpRequest();
		xmlhttp.open("GET",directory+file_versions[i].file,true);
		xmlhttp.setRequestHeader("Cache-Control", "max-age=0");
		xmlhttp.onreadystatechange = function (oEvent) {
			if (xmlhttp.readyState === 4) {
				if (xmlhttp.status === 200) {
					var match2 = new RegExp(file_versions[i].match);
							
					if (match2.test(xmlhttp.responseText))
						chrome.extension.sendMessage({'popup' : file_versions[i].version}, function(response) {});
					else {
						i++;
						checkFiles(directory);
					}
				}
				else {
					i++;
					checkFiles(directory);
				}
			}
		};
		xmlhttp.send();
	}
	else
		chrome.extension.sendMessage({'popup' : "Hidden"}, function(response) {});
}