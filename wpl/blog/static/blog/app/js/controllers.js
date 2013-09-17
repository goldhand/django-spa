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

  $scope.updateUrl = function(postId) {
      $location.path('posts/'+postId);
    };

  $scope.orderProp = 'created';
}

//PhoneListCtrl.$inject = ['$scope', '$http'];


function PostDetailCtrl($scope, $routeParams, $sce, Post) {
    $scope.post = Post.get({postId: $routeParams.postId}, function (post) {
        $scope.postContent = function() {
            return $sce.trustAsHtml(post.content);
        };
    });
    $scope.orderProp = 'created';
}

//PhoneDetailCtrl.$inject = ['$scope', '$routeParams'];



