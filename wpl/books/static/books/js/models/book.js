var app = app || {};

app.Book = Backbone.Model.extend({
    defaults: {
        coverImage: 'http://127.0.0.1:8000/static/books/img/placeholder.png',
        title: 'No title',
        author: 'Unknown',
        releaseDate: '',
        keywords: 'None'
    },
    parse: function( response ) {
        response.id = response._id;
        console.log(response);
        return response;
    }
});