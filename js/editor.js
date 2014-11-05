// From http://danielnill.com/adding-a-wysiwyg-editor-to-django/

tinyMCE.init({
    mode : "textareas",
    language_url : '/static/js/pl.js',
    plugins: [
         "advlist autolink link image lists charmap print preview hr anchor pagebreak spellchecker",
         "searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking",
         "save table contextmenu directionality emoticons template paste textcolor"
   ]
});
