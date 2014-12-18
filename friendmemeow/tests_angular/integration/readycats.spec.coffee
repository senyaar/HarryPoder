describe 'friendmemeow homepage', ->

  beforeEach ->
    browser.get('http://127.0.0.1:8000/')


  it 'should have the correct header', ->
    expect(browser.getTitle()).toEqual('Friend Me Meow')

  it 'should have 4 cats', ->
    cats = element.all(protractor.By.css('.content h1'))
    expect(cats.count()).toEqual(4)