/*global Backbone */
var app = app || {};
var lib;

(function () {
	'use strict';

	// Todo Router
	// ----------
	var BookRouter = Backbone.Router.extend({
		routes: {
			':id': 'getBook'
		},

		getBook: function (id) {
            lib = new app.BookDetailView(id);
            console.log("You are trying to reach todo " + id);
            console.log(lib);
		}
	});

	app.BookRouter = new BookRouter();
	Backbone.history.start();
})();
