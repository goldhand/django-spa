'use strict';

/* Services */

angular.module('postsServices', ['ngResource']).
    factory('Post', function($resource){
  return $resource('/api/blog/posts/:postId/', {}, {
    query: {method:'GET', params:{postId:''}, isArray:true}
  });
});