'use strict';

/* Controllers */

function PostListCtrl($scope, $http) {
  $http.get('/blog/posts/').success(function(data) {
    $scope.posts = data;
  });

  $scope.orderProp = 'age';
}

//PhoneListCtrl.$inject = ['$scope', '$http'];


function PostDetailCtrl($scope, $routeParams, $http) {
    $http.get('/blog/posts/' + $routeParams.postId).success(function(data) {
        $scope.post = data;
    });
    $scope.postId = $routeParams.postId;
    $scope.orderProp = 'age';
}

//PhoneDetailCtrl.$inject = ['$scope', '$routeParams'];
