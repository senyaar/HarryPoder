describe 'do not break', ->
  it 'should not break', ->
    expect(true).toEqual(true)

describe 'BrowserController', ->
  $httpBackend = undefined
  scope = undefined

  beforeEach ->
    angular.mock.module 'catBrowser'

  beforeEach ->
    angular.mock.inject ($rootScope, $controller, _$httpBackend_) ->
      $httpBackend = _$httpBackend_
      $httpBackend.when('GET', '/api/kitty').respond(\
      {"count": 4,\
      "next": null,\
      "previous": null,\
      "results": [\
      {"id": 17, "name": "Marcus", "gender": "M", "age": 1, "breed": "Unknown/Mixed", "weight": 5, "about": "test 1", "photo": "./mixed-breed-cat.jpg", "location": {"name": "Brent Pod", "address1": "9191 Towne Center Drive", "address2": "", "city": "San Diego", "state": "CA", "zip_code": 92122, "phone": "6618058152", "email": "brent@brightscope.com"}},\
      {"id": 18, "name": "Michelle", "gender": "F", "age": 1, "breed": "Egyptian Mau", "weight": 5, "about": "test 2", "photo": "./egyptianMau_3EPH7s3.jpg", "location": {"name": "Marcus Pod", "address1": "9191 Towne Center Drive", "address2": "", "city": "San Diego", "state": "CA", "zip_code": 92122, "phone": "1234567890", "email": "marcus.planta@brightscope.com"}},\
      {"id": 19, "name": "Andrew", "gender": "M", "age": 2, "breed": "Exotic", "weight": 5, "about": "test 3", "photo": "./exotic_BsCG7sh.jpg", "location": {"name": "David's \"Fur-Real\" Felines", "address1": "2723 Durant Ave", "address2": "", "city": "Berkeley", "state": "CA", "zip_code": 94704, "phone": "8001234567", "email": "david.lorenz@brightscope.com"}},\
      {"id": 20, "name": "Aileen", "gender": "F", "age": 3, "breed": "Devon Rex", "weight": 5, "about": "a", "photo": "./Devon_rex_W9rGuda.jpg", "location": {"name": "Garrett's Girls", "address1": "2800 Buena Vista Rd", "address2": "", "city": "Bakersfield", "state": "CA", "zip_code": 93311, "phone": "8005555555", "email": "garrett@brightscope.com"}}\
      ]})
      scope = $rootScope.$new()
      $controller('BrowserController', {$scope: scope})

  it 'should have text', ->
    expect(scope.text).toBe('Hello Karma!')

  it 'should fetch cats', ->
    expect(scope.cats).toBeDefined()

  it 'should have 4 cats', ->
    $httpBackend.flush()
    expect(scope.cats.results.length).toBe(4)

  it 'marcus is marcus', ->
    $httpBackend.flush()
    expect(scope.cats.results[0].name).toBe('Marcus')
