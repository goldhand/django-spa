'use strict';

/* App Module */

//noinspection JSValidateTypes
angular.module('posts', ['postsServices']).
  config(['$routeProvider', function($routeProvider) {
  $routeProvider.
      when('/posts', {templateUrl: '/blog/angular/partials/post-list.html',   controller: PostListCtrl}).
      when('/posts/:postId', {templateUrl: '/blog/angular/partials/post-detail.html', controller: PostDetailCtrl}).
      otherwise({redirectTo: '/posts'});
}]);
