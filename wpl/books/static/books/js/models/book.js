var app = app || {};

app.Book = Backbone.Model.extend({
    defaults: {
        coverImage: 'books/cover_images/placeholder.png',
        title: 'No title',
        author: 'Unknown',
        releaseDate: '',
        keywords: 'None'
    }

});