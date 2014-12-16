(function() {
  var app;

  app = angular.module('catBrowser', ['CatAPI']).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

  app.controller('BrowserController', [
    '$scope', 'Cat', function($scope, Cat) {
      $scope.cats = Cat.query();
      return $scope.cats;
    }
  ]);

}).call(this);

(function() {
  var app;

  app = angular.module('CatAPI', ['ngResource']);

  app.factory('Cat', [
    '$resource', function($resource) {
      return $resource('/api/kitty/:id', {
        id: '@id'
      }, {'query': {method: 'GET', isArray: false}});
    }
  ]);

}).call(this);
