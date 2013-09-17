'use strict';

/* Controllers */

function PostListCtrl($scope, $routeParams, $location, Post) {
  $scope.posts = Post.query(function(posts) {
      if ($routeParams.postId) {
          $scope.post = Post.get({postId: $routeParams.postId});
      } else {
          $scope.post = posts[0];
      }

  });
  $scope.viewDetail = function(postContent) {
      $scope.post = postContent;
  };

  $scope.updateUrl = function(postId) {
      $location.path('posts/'+postId);
    };

  $scope.orderProp = 'created';
}

//PhoneListCtrl.$inject = ['$scope', '$http'];


function PostDetailCtrl($scope, $routeParams, Post) {
    $scope.post = Post.get({postId: $routeParams.postId});
    $scope.orderProp = 'age';
}

//PhoneDetailCtrl.$inject = ['$scope', '$routeParams'];



