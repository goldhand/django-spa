var app = app || {};

$(function() {
    $( '#releaseDate' ).datepicker();
    new app.LibraryView();
});
(function() {
  var _sync = Backbone.sync;
  Backbone.sync = function(method, model, options){
    options.beforeSend = function(xhr){
      var token = $('input[name=csrfmiddlewaretoken]').val();
          //$('meta[name="csrf-token"]').attr('content');
      xhr.setRequestHeader('X-CSRFToken', token);
    };
      console.log('added csrf');
    return _sync(method, model, options);
  };
})();