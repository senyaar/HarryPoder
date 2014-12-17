describe 'friendmemeow homepage', ->

  it 'should have the correct header', ->
    browser.get('http://127.0.0.1:8000/')
    expect(browser.getTitle()).toEqual('Friend Me Meow')