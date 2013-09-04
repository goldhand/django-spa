Backbone.on('event', function() {console.log('Handled Backbone event');});
Backbone.trigger('event'); // logs: Handled Backbone event

// BACKBONE MODELS
var Post = Backbone.Model.extend({
	defaults: {
        id: '',
        created: '',
        owner: '',
        title: '',
        language: '',
        content: ''
	},
	initialize: function() {
		console.log('INITIALIZED');
		this.on('change', function(){
			console.log('CHANGED');
			});
	}
});


var PostsCollection = Backbone.Collection.extend({
  model: Post,
  url: '/blog/posts/:results'
});

var posts = new PostsCollection();
posts.fetch();
console.log(posts);

var post1 = posts.get(1);

console.log(post1);

var JqPosts = $.getJSON(url='/snippets/', function(data) {return data;});
console.log(JqPosts.responseJSON.results);
