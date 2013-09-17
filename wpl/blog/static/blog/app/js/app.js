'use strict';

/* App Module */

//noinspection JSValidateTypes
angular.module('posts', ['postsServices', 'ngRoute', 'ngAnimate']).

  config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
  $routeProvider.
      //when('/posts', {templateUrl: '/api/blog/angular/partials/post-list/'}).
      when('/posts/:postId', {templateUrl: '/api/blog/angular/partials/post-list/'}).
      otherwise({redirectTo: '/posts'});
    }])


;


