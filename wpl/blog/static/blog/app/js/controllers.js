'use strict';

/* Controllers */

function PostListCtrl($scope, Post) {
  $scope.posts = Post.query(function(posts) {
      $scope.postDetail = posts[0];
  });
  $scope.viewDetail = function(postContent) {
      $scope.postDetail = postContent;
  }

  $scope.orderProp = 'age';
}

//PhoneListCtrl.$inject = ['$scope', '$http'];


function PostDetailCtrl($scope, $routeParams, Post) {
    $scope.post = Post.get({postId: $routeParams.postId});
    $scope.orderProp = 'age';
}

//PhoneDetailCtrl.$inject = ['$scope', '$routeParams'];
