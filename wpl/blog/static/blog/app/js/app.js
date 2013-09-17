'use strict';

/* App Module */

//noinspection JSValidateTypes
angular.module('posts', ['postsServices', 'ngRoute', 'ngAnimate']).

  config(['$routeProvider', function($routeProvider) {
  $routeProvider.
      when('/posts', {templateUrl: '/api/blog/angular/partials/post-list/'}).
      when('/posts/:postId', {templateUrl: '/api/blog/angular/partials/post-detail/'}).
      otherwise({redirectTo: '/posts'});
    }])
;


