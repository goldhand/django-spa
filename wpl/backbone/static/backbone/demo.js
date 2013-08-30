// BACKBONE MODELS
var Todo = Backbone.Model.extend({
// Default todo attribute values
	defaults: {
	title: '',
	content: '',
	language: '',
	owner: '',
	completed: false
	},
	initialize: function() {
		console.log('INITIALIZED');
		this.on('change', function(){
			console.log('CHANGED');
			});
	}
});

// Instantiate the Todo Model with a title, allowing completed attribute
// to default to false
var myTodo = new Todo({
	title: 'Check attributes property of the logged models in the console.'
});
var myTodo0 = new Todo({
	title: 'SET TITLE'
});

console.log(JSON.stringify(myTodo));
console.log(JSON.stringify(myTodo.toJSON()));
myTodo.set('title', 'SET TITLE');
console.log(JSON.stringify(myTodo));




// BACKBONE VIEWS

var ul = $('<input id="todo_complete" type="checkbox" checked="checked">');
var ul0 = $('<input id="todo_complete0" type="checkbox" checked="checked">');

var TodosView = Backbone.View.extend({
	tagName: 'ul',
	className: 'container',
	
});

var todosView = new TodosView({el: ul});
var todosView0 = new TodosView({el: ul0});
todosView.render();


console.log(todosView.el);


var TodoView = Backbone.View.extend({

	tagName:  'li',
	// Cache the template function for a single item.
	todoTpl: _.template( $('#item-template').html() ),

	events: {
		'dblclick label': 'edit',
		'keypress .edit': 'updateOnEnter',
		'blur .edit':   'close'
	},

	// Called when the view is first created
	initialize: function() {
		this.$el = $('#todo');
		// Later we'll look at:
		// this.listenTo(someCollection, 'all', this.render);
		// but you can actually run this example right now by
		// calling TodoView.render();
	},

	// Re-render the titles of the todo item.
	render: function() {
		this.$el.html( this.todoTpl( this.model.toJSON() ) );
		// $el here is a reference to the jQuery element 
		// associated with the view, todoTpl is a reference
		// to an Underscore template and toJSON() returns an 
		// object containing the model's attributes
		// Altogether, the statement is replacing the HTML of
		// a DOM element with the result of instantiating a 
		// template with the model's attributes.
		this.input = this.$('.edit');
		return this;
	},

	edit: function() {
	// executed when todo label is double clicked
	},

	close: function() {
	// executed when todo loses focus
	},

	updateOnEnter: function( e ) {
	// executed on each keypress when in todo edit mode, 
	// but we'll wait for enter to get in action
	}
});

// create a view for a todo
var todoView = new TodoView({model: myTodo});
var todoView0 = new TodoView({model: myTodo0});
var todoView1 = new TodoView({model: myTodo});
console.log(todoView.el);
console.log(todoView0.el);
todoView.render();
todoView0.render();

var TodosCollection = Backbone.Collection.extend({
  model: Todo,
  url: '/blog/posts/1/'
});
var TodosCollection2 = Backbone.Collection.extend({
  model: Todo,
  url: '/blog/posts/2/'
});

var todos = new TodosCollection();
todos.fetch(); // sends HTTP GET to /todos
console.log(JSON.stringify(todos.toJSON()));
for (var i = 0; todos.length; i ++) {
	var newTodoItem = todos[i];
	var newtodoView = new TodoView({model: newTodoItem});
	newtodoView.render({el: '#todo' + i});
}

var todo2Object = todos.toJSON();
var todo2 = todos.get('c10');
console.log(todo2);
	
	
		
	
