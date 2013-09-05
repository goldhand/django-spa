/**
 * by: wpl
 * Date: 9/3/13
 * Time: 7:36 PM
 */

var app = app || {};

app.Library = Backbone.Collection.extend({
    model: app.Book,
    url: '/books/',
    emulateJSON: true
});