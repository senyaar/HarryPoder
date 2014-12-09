(function() {
  var app;

  app = angular.module('catBrowser', ['CatAPI']).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

  app.controller('BrowserController', [
    '$scope', 'Cat', function($scope, Cat) {
      return $scope.cats = Cat.query();
    }
  ]);

}).call(this);

(function() {
  var app;

  app = angular.module('CatAPI', ['ngResource']);

  app.factory('Cat', [
    '$resource', function($resource) {
      return $resource('/api/kitty/:name', {
        name: '@name'
      }, {'query': {method: 'GET', isArray: false}});
    }
  ]);

}).call(this);
