'use strict';

/* Services */

angular.module('postsServices', ['ngResource']).
    factory('Post', function($resource){
  return $resource('/blog/posts/:postId/', {}, {
    query: {method:'GET', params:{postId:''}, isArray:true}
  });
});