By = protractor.By

class ReadyCats
  constructor: (url) ->
    @url = browser.baseUrl + url

  get: ->
    browser.get(@url)

  getTitle: ->
    browser.getTitle()

  getPageUrl: ->
    browser.getCurrentUrl()

  getPage: (url) ->
    browser.driver.get(url)

  getElementByCss: (css) ->
    element(By.css(css))

  getElementByModel: (model) ->
    element(By.model(model))

  getElementByBinding: (binding) ->
    element(By.binding(binding))

  getElementsByCss: (css) ->
    element.all(By.css(css))

  getElementsByModel: (model) ->
    element.all(By.model(model))

  getElementsByBinding: (binding) ->
    element.all(By.model(binding))

    constructor: ->
    @page_url = '/#/'
    @header = @getElementByCss('.page-header h3')
    @login = @getElementByCss('#login')
    @logout = @getElementByCss('[ng-controller=LoginCtrl]')
    super(@page_url)

  getHeaderText: ->
    @header.getText()

  clickLogin: ->
    @login.click()

module.exports.Page = ReadyCats