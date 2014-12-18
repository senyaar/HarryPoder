module.exports = (config) ->
  config.set
    basePath: ''
    frameworks: ['jasmine']
    files: [
      '../../static/bower_components/underscore/underscore.js'
      '../../static/bower_components/angular/angular.js'
      '../../static/bower_components/angular-resource/angular-resource.js'
      './readycats.unittest.coffee'
      '../../static/js/script.js'
    ]
    exclude: []
    preprocessors: {
      './*.coffee': ['coffee']
    }
    coffeePreProcessor: {
      base: false
      sourceMap: true
    }
    browsers: ['Chrome']
    port: 9876
    autoWatch: true
    singleRun: true


